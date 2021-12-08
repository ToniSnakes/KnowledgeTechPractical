import sys 
from flask import Flask
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)

start = { "homoskedastic": "unknown", "independent observations": "unknown" }
state = start.copy()
solutions = [ "logistic regression", "linear regression", "lasso regression" ]

questions = { "homoskedastic":
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

rules = { "regression":
            { "premises": { "homoskedastic": "true", "independent observations": "true" }, "conclusion": { "regression": "true", "output continuity": "unknown" } },
          "logistic":
            { "premises": { "regression": "true", "output continuity": "false" }, "conclusion": { "logistic regression": "true" } },
          "not logistic":
            { "premises": { "regression": "true", "output continuity": "true" }, "conclusion": { "not logistic": "true", "linear relationship": "unknown", "output normally distributed": "unknown" } },
          "linear or lasso":
            { "premises": { "not logistic": "true", "output continuity": "true", "linear relationship": "true", "output normally distributed": "true" }, "conclusion": { "linear or lasso": "true", "all predictors important": "unknown" } },
          "linear":
            { "premises": { "linear or lasso": "true", "all predictors important": "true" }, "conclusion": { "linear regression": "true" } },
          "lasso":
            { "premises": { "linear or lasso": "true", "all predictors important": "false" }, "conclusion": { "lasso regression": "true" } }
            }


recommendations = { "logistic regression": "Logistic Regression",
                    "linear regression": "Linear Regression",
                    "lasso regression": "Lasso Regression",
                    "none": "This is not in our database" }

def findQ():
  for key in state:
    if state[key] == "unknown":
      return key
  return "solved"

def solve():
  sol = "none"
  for solution in solutions:
    if solution in state and state[solution] == "true":
      sol = solution

  return sol

def resetState():
  global state
  state = start.copy()


def infer():
  ok = True
  while ok:
    new = {}
    for rulename, rule in rules.items():
      add = True
      for premise, value in rule["premises"].items():
        if premise not in state or value != state[premise]:
          add = False
          break
      if add == True:
        print(rulename)
        print(rule)
        for conclusion, value in rule["conclusion"].items():
          if conclusion not in state:
            new[conclusion] = value
    if not bool(new):
      ok = False
    else:
      print("NEW:")
      print(new)
      for key, value in new.items():
        state[key] = value
    print("STATE:")
    print(state)



@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/nextQuestion")
def nextQuestion():
  nextQ = findQ()
  if nextQ == "solved":
    recommend = solve()
    return { "name": nextQ, "question": recommendations[recommend] }
  return { "name": nextQ, "question": questions[nextQ]["question"], "answers": list(questions[nextQ]["answers"].keys()) }

@app.route("/answer/<question>/<inp>", methods=['POST'])
def processAnswer(question, inp):
  answers = questions[question]["answers"]
  for answer, values in answers.items():
    if inp == answer:
      for key, value in values.items():
        state[key] = value
      break
  infer()
  return nextQuestion()

@app.route("/reset", methods=['POST'])
def reset():
  resetState()
  return nextQuestion()
