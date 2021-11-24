import sys 

state = { "short": "unknown", "medium": "unknown", "long": "unknown" }
solutions = { "short":
                { "short": "true", "medium": "false", "long": "false" },
              "medium":
                { "short": "false", "medium": "true", "long": "false" },
              "long":
                { "short": "false", "medium": "false", "long": "true" } }

rules = { "short":
            { "question": "Is the route short?: ", "answers": { "yes": { "short": "true", "medium": "false", "long": "false" }, "no": { "short": "false" } } },
          "medium":
            { "question": "Is the route medium?: ", "answers": { "yes": { "medium": "true", "long": "false"}, "no": { "medium": "false"} } },
          "long":
            { "question": "Is the route long?: ", "answers": { "yes": { "long": "true" }, "no": { "long": "false" } } } }

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
      

while (True):
  nextQ = findQ()
  if nextQ == "solved":
    print(solve())
    break

#  if nextQ == "short":
#    inp = input("Is the route short?: ")
#    if inp == "yes":
#      state["short"] = "true"
#      state["medium"] = "false"
#      state["long"] = "false"
#    else:
#      state["short"] = "false"

#  if nextQ == "medium":
#    inp = input("Is the route medium?: ")
#    if inp == "yes":
#      state["medium"] = "true"
#      state["long"] = "false"
#    else:
#      state["medium"] = "false"

#  if nextQ == "long":
#    inp = input("Is the route long?: ")
#    if inp == "yes":
#      state["long"] = "true"
#    else:
#      state["long"] = "false"

  for question in rules:
    if nextQ == question:
      inp = input(rules[question]["question"])
      answers = rules[question]["answers"]
      for answer, values in answers.items():
        if inp == answer:
          for key, value in values.items():
            state[key] = value
          break
    
      

    
    
