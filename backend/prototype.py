from flask import Flask
from flask_cors import CORS
from markupsafe import escape
from data import *
from inference import *

app = Flask(__name__)
CORS(app)

# create a copy to fall back to the start if needed
state = start.copy()
trace = {}
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
  step["trace"] = trace.copy()
  print("==========   NEXT STACK    ==========")
  stack.append(step)
  stack_print(stack)
  print("==========    END ADD      ==========")

add_step(state, trace)

def findQ():
  '''
  :return: the next question to ask or "solved" otherwise.
  '''
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
  trace = step["trace"].copy()
  add_step(state, trace) # Inefficient 2/2: re-add the last element
                         # Kept inefficiency since copies cannot be avoided anyway

def resetState():
  '''
  Resets the interaction by copying the original starting state into the current state.
  '''
  global state, trace, stack
  state = start.copy()
  trace = {}
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
              "description": descriptions[recommend] }
  question_text = questions[nextQ]["question"]
  present_keywords = findKeywords(question_text)
  return { "name": nextQ, "question": question_text,
    "answers": list(questions[nextQ]["answers"].keys()),
    "keywords": present_keywords} # return the next question

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
      break
  forward_chaining(state)
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
