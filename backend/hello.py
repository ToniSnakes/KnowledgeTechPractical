import sys 
from flask import Flask
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)

state = { "short": "unknown", "medium": "unknown", "long": "unknown" }
solutions = { "short":
                { "short": "true", "medium": "false", "long": "false" },
              "medium":
                { "short": "false", "medium": "true", "long": "false" },
              "long":
                { "short": "false", "medium": "false", "long": "true" } }

rules = { "short":
            { "question": "Is the route short?", "answers": { "yes": { "short": "true", "medium": "false", "long": "false" }, "no": { "short": "false" } } },
          "medium":
            { "question": "Is the route medium?", "answers": { "yes": { "medium": "true", "long": "false"}, "no": { "medium": "false"} } },
          "long":
            { "question": "Is the route long?", "answers": { "yes": { "long": "true" }, "no": { "long": "false" } } } }

recommendations = { "short": "You took the short route!",
                    "medium": "You took the medium route! Whoo!",
                    "long": "Wow, you took the long route!",
                    "none": "This is not in our database =[[" }

def findQ():
  for key in state:
    if state[key] == "unknown":
      return key
  return "solved"

def solve():
  sol = "none"
  for solName, solution in solutions.items():
    ok = True
    for key in state:
      if state[key] != solution[key]:
        ok = False
        break
    if ok:
      sol = solName
      break

  return sol

def resetState():
  for key in state:
    state[key] = "unknown"


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
  return f"Hello, {escape(name)}!"
      
@app.route("/nextQuestion")
def nextQuestion():
  nextQ = findQ()
  if nextQ == "solved":
    recommend = solve()
    return { "name": nextQ, "question": recommendations[recommend] }
  return { "name": nextQ, "question": rules[nextQ]["question"] }

@app.route("/answer/<question>/<inp>", methods=['POST'])
def processAnswer(question, inp):
  answers = rules[question]["answers"]
  for answer, values in answers.items():
    if inp == answer:
      for key, value in values.items():
        state[key] = value
      break
  return nextQuestion()

@app.route("/reset", methods=['POST'])
def reset():
  resetState()
  return nextQuestion()


## Below you have how the inference looks in normal code

#while (True):
#  nextQ = findQ()
#  if nextQ == "solved":
#    print(solve())
#    break

#  for question in rules:
#    if nextQ == question:
#      inp = input(rules[question]["question"])
#      answers = rules[question]["answers"]
#      for answer, values in answers.items():
#        if inp == answer:
#          for key, value in values.items():
#            state[key] = value
#          break
