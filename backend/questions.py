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
