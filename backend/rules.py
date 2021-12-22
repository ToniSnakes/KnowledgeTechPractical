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
