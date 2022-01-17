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

def stack_print(stack):
  for step in stack:
    print("")
    print(step)
  print("")

def add_step(state, trace):
  global stack
  print("========== ADDING TO STACK ==========")
  print("==========  CURRENT STACK  ==========")
  stack_print(stack)
  step = {}
  step["state"] = state.copy()
  step["trace"] = copy.deepcopy(trace)
  print("==========   NEXT STACK    ==========")
  stack.append(step)
  stack_print(stack)
  print("==========    END ADD      ==========")

goals = list(recommendations.keys())
goals.pop() # remove the extra "none" state
depth_tree = {}

def findConclusion(goal):
  for rule in rules:
    for conclusion, value in rule["conclusion"].items():
      if conclusion == goal:
        return rule # Otherwise return None

def getDepth(goal, rule):
  if goal in depth_tree.keys():
    return depth_tree[goal]
  #if goal == "logistic regression":
  #  print("DEBUGGING")
  #  print(state)
  max_depth = 0
  for premise in rule["premises"].keys():
    #if goal == "logistic regression":
    #  print(premise)
    if premise in depth_tree.keys():
      if depth_tree[premise] > max_depth:
        max_depth = depth_tree[premise]
      continue
    depth = 0
    new_rule = findConclusion(premise)
    #if new_rule and premise not in state.keys():
    #if premise in state.keys():
    #  print("Exists:")
    #  print(goal)
    #  print(premise)
    #  print(state[premise])
    #  print(rule["premises"][premise])
    if premise in state.keys() and state[premise] != rule["premises"][premise]:
      depth = HIGH_NUMBER # high number
    elif new_rule:
      if premise not in state.keys():
        #depth = getDepth(list(new_rule["premises"].keys()))
        depth = getDepth(premise, new_rule)
    if depth > max_depth:
      max_depth = depth
  depth_tree[goal] = max_depth + 1
  return depth_tree[goal]

def buildDepth(goals):
  global depth_tree
  depth_tree = {}
  for goal in goals:
    rule = findConclusion(goal)
    #if goal not in depth_tree.keys():
      #depth_tree["goal"] = getDepth(goal, rule) + 1
    getDepth(goal, rule)

def setUnknown(goal):
  print(goal)
  rule = findConclusion(goal)
  print(depth_tree[goal])
  for premise in rule["premises"].keys():
    #if depth_tree[rule] == 1 and premise not in depth_tree.keys():
    if depth_tree[goal] == 1:
      #if premise not in depth_tree.keys():  # or in state
      #if premise not in state.keys():  # or in state
      if premise in questions.keys() and premise not in state.keys():  # or in state
        print("TO ADD")
        print(premise)
        state[premise] = "unknown"
    elif premise in depth_tree.keys():
      setUnknown(premise)

def findUnknown():
  buildDepth(goals)
  lowest_goal = ""
  global depth_tree
  depth_tree = dict(sorted(depth_tree.items(), key=lambda item: item[1]))
  for goal in depth_tree.keys():
    if goal in goals:
      lowest_goal = goal
      break
  setUnknown(lowest_goal)
  print(depth_tree)

findUnknown()

add_step(state, trace)

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
  print("======== REMOVING FROM STACK ========")
  print("==========  CURRENT STACK  ==========")
  stack_print(stack)
  step = stack.pop() # Remove the last commit
  step = stack.pop() # Inefficient 1/2: get the last element
  print("==========   NEXT STACK    ==========")
  stack_print(stack)
  print("==========   END REMOVE    ==========")
  print("==========      STEP       ==========")
  print(step)
  state = step["state"].copy()
  trace = copy.deepcopy(step["trace"])
  add_step(state, trace) # Inefficient 2/2: re-add the last element
                         # Kept inefficiency since copies cannot be avoided anyway

def resetState():
  '''
  Resets the interaction by copying the original starting state into the current state.
  '''
  global state, trace, stack
  state = start.copy()
  trace = copy.deepcopy(emptyTrace)
  stack = []
  add_step(state, trace)

def findKeywords(text):
  to_find = list(keywords.keys())
  words = text.split()
  found = {}
  for word in words:
    for key in to_find:
      if word.lower() == key.lower() or word[:-1].lower() == key.lower():
        found[word] = keywords[key]
  return found

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
              "trace": trace }
  question_text = questions[nextQ]["question"]
  present_keywords = findKeywords(question_text)
  return { "name": nextQ, "question": question_text,
    "answers": list(questions[nextQ]["answers"].keys()),
    "keywords": present_keywords,
    "trace": trace } # return the next question

@app.route("/answer/<question>/<inp>", methods=['POST'])
def processAnswer(question, inp):
  '''
  Processes the user's answer to a question.
  
  :param question: question that was asked
  :param inp: the user's answer
  :return: next question callback
  '''
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
