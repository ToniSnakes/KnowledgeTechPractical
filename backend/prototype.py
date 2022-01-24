import copy
from flask import Flask
from flask_cors import CORS
from markupsafe import escape
from data import *
from inference import *

app = Flask(__name__)
CORS(app)

# create a copy to fall back to the start if needed
state = start.copy()
trace = copy.deepcopy(emptyTrace)
stack = []

def add_step(state, trace):
  global stack
  step = {}
  step["state"] = state.copy()
  step["trace"] = copy.deepcopy(trace)
  stack.append(step)

goals = list(recommendations.keys())
goals.pop() # remove the extra "none" state
depth_tree = {}
newTraceFacts = {}

def findConclusion(goal):
  for rule in rules:
    for conclusion, value in rule["conclusion"].items():
      if conclusion == goal:
        return rule # Otherwise return None

def findConclusionValue(goal, desired):
  for rule in rules:
    for conclusion, value in rule["conclusion"].items():
      if conclusion == goal and value == desired:
        return rule # Otherwise return None

def getDepth(goal, rule, initial, goals):
  if goal in depth_tree.keys():
    return depth_tree[goal]
  max_depth = 0
  for premise in rule["premises"].keys():
    if premise in depth_tree.keys():
      if depth_tree[premise] > max_depth:
        max_depth = depth_tree[premise]
      continue
    depth = 0
    #new_rule = findConclusion(premise)
    new_rule = findConclusionValue(premise, rule["premises"][premise])
    if premise in state.keys() and state[premise] != rule["premises"][premise]:
      depth = HIGH_NUMBER # high number
    elif new_rule:
      if premise not in state.keys():
        depth = getDepth(premise, new_rule, initial, goals)
    if depth > max_depth:
      max_depth = depth
  depth_tree[goal] = max_depth + 1
  return depth_tree[goal]

def buildDepth(goals):
  global depth_tree, newTraceFacts
  depth_tree = {}
  newTraceFacts = {}
  for goal in goals:
    rule = findConclusion(goal)
    getDepth(goal, rule, goal, goals)

def setUnknown(goal):
  (goal)
  rule = findConclusion(goal)
  (depth_tree[goal])
  for premise in rule["premises"].keys():
    if depth_tree[goal] == 1:
      if premise in questions.keys() and premise not in state.keys():  # or in state
        ("TO ADD")
        (premise)
        newTraceFacts[premise] = "unknown"
        state[premise] = "unknown"
        return True
    elif premise in depth_tree.keys():
      if (setUnknown(premise)):
        return True
  return False

def findUnknown():
  buildDepth(goals)
  lowest_goal = ""
  global depth_tree, newTraceFacts
  depth_tree = dict(sorted(depth_tree.items(), key=lambda item: item[1]))
  trace["facts"].append(newTraceFacts)
  newRules = []
  newRules.append(find_unknowns_rule)
  trace["rules"].append(newRules)
  for goal in depth_tree.keys():
    if goal in goals:
      lowest_goal = goal
      break
  setUnknown(lowest_goal)
  stack.pop()
  add_step(state, trace)
  (depth_tree)

add_step(state, trace)

findUnknown()

def findQ():
  '''
  :return: the next question to ask or "solved" otherwise.
  '''
  for key in state:
    if state[key] == "unknown":
      return key
  if solve() == "none":
    findUnknown()
    for key in state:
      if state[key] == "unknown":
        return key
  return "solved"

def solve():
  '''
  Checks if the problem was solved
  '''
  sol = "none"
  for solution in solutions:
    if solution in state and state[solution] == "true":
      sol = solution

  return sol

def undoState():
  '''
  Undoes the last interaction by popping the state from the stack
  '''
  global state, trace, stack
  if len(stack) == 1:
    return
  step = stack.pop() # Remove the last commit
  step = stack.pop() # get the last element
  state = step["state"].copy()
  trace = copy.deepcopy(step["trace"])
  add_step(state, trace) # re-add the last element

def resetState():
  '''
  Resets the interaction by copying the original starting state into the current state.
  '''
  global state, trace, stack
  state = start.copy()
  trace = copy.deepcopy(emptyTrace)
  stack = []
  add_step(state, trace)
  findUnknown()

def traceUpdate(key, value):
  global trace
  for traceStep in trace["facts"]:
    if key in traceStep:
      traceStep[key] = value


@app.route("/") # reroute default request to be handled by next question
@app.route("/nextQuestion")
def nextQuestion():
  '''
  Decides what to do next and returns required callback.
  
  :return: json with next question or final recommendation
  '''
  nextQ = findQ()
  if nextQ == "solved": # return final recommendation
    recommend = solve()
    return { "name": nextQ, "question": recommendations[recommend],
              "description": descriptions[recommend],
              "r": r[recommend],
              "trace": trace }
  question_text = questions[nextQ]["question"]
  return { "name": nextQ, "question": question_text,
    "answers": list(questions[nextQ]["answers"].keys()),
    "info": questions[nextQ]["info"],
    "trace": trace } # return the next question

@app.route("/answer/<question>/<inp>", methods=['POST'])
def processAnswer(question, inp):
  '''
  Processes the user's answer to a question.
  
  :param question: question that was asked
  :param inp: the user's answer
  :return: next question callback
  '''
  (question)
  (inp)
  answers = questions[question]["answers"]
  for answer, values in answers.items():
    if inp == answer:
      for key, value in values.items():
        state[key] = value
        traceUpdate(key, value)
      break
  forward_chaining(state, trace)
  add_step(state, trace)
  return nextQuestion()

@app.route("/undo", methods=['POST'])
def undo():
  '''
  Undoes the last answer by popping it from the stack

  :return: next question callback
  '''
  undoState()
  return nextQuestion()

@app.route("/reset", methods=['POST'])
def reset():
  '''
  Resets the system and restarts the interaction.

  :return: next question callback
  '''
  resetState()
  return nextQuestion()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8888)