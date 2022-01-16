# The starting state
# Unknown demarks the fields the engine attempts to determine next
start = {
  "homoskedastic": "unknown",
  "independent observations": "unknown"
  }
emptyTrace = {
    "rules": [],
    "facts": [start.copy()]
  }
