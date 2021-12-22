from flask import Flask
from flask_cors import CORS
from markupsafe import escape
from data import *
from inference import *

app = Flask(__name__)
CORS(app)

# create a copy to fall back to the start if needed
state = start.copy()

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

def resetState():
  '''
  Resets the interaction by copying the original starting state into the current state.
  '''
  global state
  state = start.copy()

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
    return { "name": nextQ, "question": recommendations[recommend] }
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
  return nextQuestion()

@app.route("/reset", methods=['POST'])
def reset():
  '''
  Resets the system and restarts the interaction.

  :return: next question callback
  '''
  resetState()
  return nextQuestion()
