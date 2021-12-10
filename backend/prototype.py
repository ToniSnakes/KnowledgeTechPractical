from flask import Flask
from flask_cors import CORS
from markupsafe import escape
from inference import *

app = Flask(__name__)
CORS(app)

# The starting state
# Unknown demarks the fields the engine attempts to determine next
start = {
  "homoskedastic": "unknown",
  "independent observations": "unknown"
  }

# create a copy to fall back to the start if needed
state = start.copy()

# Question list:
# { determined field : { "question": question content , "answers": {field: value, ...} }, ... }
questions = {
  "homoskedastic":
    { "question": "Is the data homoskedastic?", "answers": { "yes": { "homoskedastic": "true" }, "no": { "homoskedastic": "false" } } },
  "independent observations":
    { "question": "Are the observations independent of one another?", "answers": { "yes": { "independent observations": "true" }, "no": { "independent observations": "false" } } },
  "output continuity":
    { "question": "Is the output continuous or binary?", "answers": { "continuous": { "output continuity": "true" }, "binary": { "output continuity": "false" } } }, # change to actual values continuous/binary
  "linear relationship":
    { "question": "Is the relationship between the predictors linear?", "answers": { "yes": { "linear relationship": "true" }, "no": { "linear relationship": "false" } } },
  "output normally distributed":
    { "question": "Is the output normally distributed?", "answers": { "yes": { "output normally distributed": "true" }, "no": { "output normally distributed": "false" } } },
  "all predictors important":
    { "question": "Are all predictors important?", "answers": { "yes": { "all predictors important": "true" }, "no": { "all predictors important": "false" } } },
  }

# State fields considered solutions
solutions = [ "logistic regression", "linear regression", "lasso regression" ]

# Recommendations when the dialogue ends
recommendations = {
  "logistic regression": "Logistic Regression",
  "linear regression": "Linear Regression",
  "lasso regression": "Lasso Regression",
  "none": "This is not in our database"
  }

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
  return { "name": nextQ, "question": questions[nextQ]["question"],
    "answers": list(questions[nextQ]["answers"].keys()) } # return the next question

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
