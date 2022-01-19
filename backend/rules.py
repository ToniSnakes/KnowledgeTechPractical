# List of rules
find_unknowns_rule = {
    "premises": {
        "no goals found": "true",
    },
    "conclusion": {
        "add new unknowns": "true"
    }
}

rules = [
	{
		"premises": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "categorical"
		},
		"conclusion": {
			"chi-square goodness of fit test": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect or find a model of the relationship",
			"dv type": "categorical"
		},
		"conclusion": {
			"logistic regression": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for independence",
			"variable types": "all categorical"
		},
		"conclusion": {
			"chi-square test for independence": "true"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test",
			"variance known": "false",
			"sample size": "small"
		},
		"conclusion": {
			"t-test (one-sample)": "true"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test",
			"variance known": "true",
			"sample size": "large"
		},
		"conclusion": {
			"z-test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"dv normally distributed": "true",
			"situation": "situation: one sample, one measurement"
		},
		"conclusion": {
			"test class": "z- or t-test"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"difference of two means (paired)": "true"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"levene's test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"situation": "one sample, one measurement",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"dv normally distributed": "false",
			"statistics goal": "median"
		},
		"conclusion": {
			"wilcoxon signed rank test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"dv normally distributed": "false",
			"situation": "one sample, two measurements",
			"statistics goal": "median"
		},
		"conclusion": {
			"wilcoxon matched-pairs signed rank test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"situation": "more than two samples (or groups), one measurement",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "median"
		},
		"conclusion": {
			"moods median": "true"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "true",
			"equal sample sizes": "true"
		},
		"conclusion": {
			"student's t-test": "true"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "false"
		},
		"conclusion": {
			"welsh's t-test": "true"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal sample sizes": "false"
		},
		"conclusion": {
			"welsh's t-test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "one sample, one measurement",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test class": "t-test (unpaired two sample)"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "one sample, one measurement",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"mann whitney u test (wilcoxon rank sum test)": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"t-test (paired sample)": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"one-way anova": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"kruskal-wallis test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical and one numerical iv"
		},
		"conclusion": {
			"ancova": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "multiple categorical ivs"
		},
		"conclusion": {
			"n-way anova (factorial anova)": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"situation": "one sample, more than two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"repeated measures anova": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"dv normally distributed": "false",
			"situation": "one sample, more than two measurements"
		},
		"conclusion": {
			"friedman": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"dv normally distributed": "true",
			"situation": "two samples or groups, one measurement"
		},
		"conclusion": {
			"f-test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"statistics goal": "mean",
			"dv normally distributed": "true",
			"situation": "more than two samples (or groups), one measurement"
		},
		"conclusion": {
			"bartlett's test": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for correlation",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"variable types": "all continuous",
			"linear relationship": "true"
		},
		"conclusion": {
			"pearson correlation": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"number of ivs": "one"
		},
		"conclusion": {
			"simple linear regression": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"number of ivs": "more than one",
			"include all ivs": "true"
		},
		"conclusion": {
			"multiple regression": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous (ratio or interval)",
			"number of ivs": "more than one",
			"include all ivs": "false"
		},
		"conclusion": {
			"lasso regression": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "false"
		},
		"conclusion": {
			"spearman correlation": "true"
		}
	}
]

rules2 = [
          { "premises": { "homoskedastic": "true", "independent observations": "true" },
            "conclusion": { "regression": "true" } },
          { "premises": { "regression": "true", "output continuity": "false" },
            "conclusion": { "logistic regression": "true" } },
          { "premises": { "regression": "true", "output continuity": "true" },
            "conclusion": { "not logistic": "true" } },
          { "premises": { "not logistic": "true", "output continuity": "true", "linear relationship": "true", "output normally distributed": "true" },
            "conclusion": { "linear or lasso": "true" } },
          { "premises": { "linear or lasso": "true", "all predictors important": "true" },
            "conclusion": { "linear regression": "true" } },
          { "premises": { "linear or lasso": "true", "all predictors important": "false" },
            "conclusion": { "lasso regression": "true" } }
]
