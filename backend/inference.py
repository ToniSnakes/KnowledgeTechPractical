# List of rules
rules = [
          { "premises": { "homoskedastic": "true", "independent observations": "true" },
            "conclusion": { "regression": "true", "output continuity": "unknown" } },
          { "premises": { "regression": "true", "output continuity": "false" },
            "conclusion": { "logistic regression": "true" } },
          { "premises": { "regression": "true", "output continuity": "true" },
            "conclusion": { "not logistic": "true", "linear relationship": "unknown", "output normally distributed": "unknown" } },
          { "premises": { "not logistic": "true", "output continuity": "true", "linear relationship": "true", "output normally distributed": "true" },
            "conclusion": { "linear or lasso": "true", "all predictors important": "unknown" } },
          { "premises": { "linear or lasso": "true", "all predictors important": "true" },
            "conclusion": { "linear regression": "true" } },
          { "premises": { "linear or lasso": "true", "all predictors important": "false" },
            "conclusion": { "lasso regression": "true" } }
]

def forward_chaining(state):
  '''
  Infers as many new rules as possible using forward chaining.
  '''
  while True: # repeat until no more added facts
    new = {}
    for rule in rules:
      add = True
      for premise, value in rule["premises"].items(): # check if all premisses are satisfied
        if (premise not in state or value != state[premise]) and (premise not in new or value != new[premise]):
          add = False
          break
      if add == True:
        print(rule)
        for conclusion, value in rule["conclusion"].items(): # add every conclusion
          if conclusion not in state:
            new[conclusion] = value
    if not bool(new): # stop if we did not infer any new facts
      print("STATE:")
      print(state)
      break
    print("NEW:")
    print(new)
    for key, value in new.items(): # update our state with new facts
      state[key] = value
    print("STATE:")
    print(state)
