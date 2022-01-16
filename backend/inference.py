from rules import *

def forward_chaining(state, trace):
  '''
  Infers as many new rules as possible using forward chaining.
  '''
  while True: # repeat until no more added facts
    new = {}
    newRules = []
    for rule in rules:
      add = True
      for premise, value in rule["premises"].items(): # check if all premisses are satisfied
        if (premise not in state or value != state[premise]) and (premise not in new or value != new[premise]):
          add = False
          break
      if add == True:
        print(rule)
        ruleIsNew = True  # Check if the rule hasn't been added to the trace, otherwise
        for ruleSet in trace["rules"]: # we can assume it's relevant for this step
          if rule in ruleSet:
            ruleIsNew = False
            break
        if ruleIsNew:
          newRules.append(rule.copy())
        for conclusion, value in rule["conclusion"].items(): # add every conclusion
          if conclusion not in state:
            new[conclusion] = value
    if not bool(new): # stop if we did not infer any new facts
      print("STATE:")
      print(state)
      break
    print("NEW:")
    print(new)
    trace["facts"].append(new.copy())
    trace["rules"].append(newRules.copy())
    for key, value in new.items(): # update our state with new facts
      state[key] = value
    print("STATE:")
    print(state)
