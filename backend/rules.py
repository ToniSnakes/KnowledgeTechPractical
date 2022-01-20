# List of rules
find_unknowns_rule = {
    "premisses": {
        "no goals found": "true",
    },
    "conclusion": {
        "add new unknowns": "true"
    }
}

rules = [
	{
		"premisses": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "categorical"
		},
		"conclusion": {
			"chi-square goodness of fit test": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for an effect or find a model of the relationship",
			"dv type": "categorical"
		},
		"conclusion": {
			"logistic regression": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for independence",
			"variable types": "all categorical"
		},
		"conclusion": {
			"chi-square test for independence": "true"
		}
	},
	{
		"premisses": {
			"test class": "z- or t-test (one-sample)",
			"variance known": "false",
			"sample size": "small"
		},
		"conclusion": {
			"t-test (one-sample)": "true"
		}
	},
	{
		"premisses": {
			"test class": "z- or t-test (one-sample)",
			"variance known": "true",
			"sample size": "large"
		},
		"conclusion": {
			"z-test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"dv normally distributed": "true",
			"situation": "one sample, one measurement"
		},
		"conclusion": {
			"test class": "z- or t-test (one-sample)"
		}
	},
	{
		"premisses": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"difference of two means (paired)": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare against hypothesized value or distribution",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"levene's test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"situation": "one sample, one measurement",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"dv normally distributed": "false",
			"statistics goal-update": "median"
		},
		"conclusion": {
			"wilcoxon signed rank test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"dv normally distributed": "false",
			"situation": "one sample, two measurements",
			"statistics goal-update": "median"
		},
		"conclusion": {
			"wilcoxon matched-pairs signed rank test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"situation": "more than two samples (or groups), one measurement",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "median"
		},
		"conclusion": {
			"moods median": "true"
		}
	},
	{
		"premisses": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "true",
			"equal sample sizes": "true"
		},
		"conclusion": {
			"student's t-test": "true"
		}
	},
	{
		"premisses": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "false"
		},
		"conclusion": {
			"welsh's t-test": "true"
		}
	},
	{
		"premisses": {
			"test class": "t-test (unpaired two sample)",
			"equal sample sizes": "false"
		},
		"conclusion": {
			"welsh's t-test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "two samples (or groups), one measurement",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test class": "t-test (unpaired two sample)"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"statistics goal-update": "mean",
			"situation": "two samples (or groups), one measurement",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"mann whitney u test (wilcoxon rank sum test)": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"t-test (paired sample)": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"one-way anova": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"kruskal-wallis test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical and one numerical iv"
		},
		"conclusion": {
			"ancova": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "multiple categorical ivs"
		},
		"conclusion": {
			"n-way anova (factorial anova)": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"situation": "one sample, more than two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"repeated measures anova": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "mean",
			"dv normally distributed": "false",
			"situation": "one sample, more than two measurements"
		},
		"conclusion": {
			"friedman": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "variance",
			"dv normally distributed": "true",
			"situation": "two samples (or groups), one measurement"
		},
		"conclusion": {
			"f-test": "true"
		}
	},
	{
		"premisses": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"statistics goal-update": "variances",
			"dv normally distributed": "true",
			"situation": "more than two samples (or groups), one measurement"
		},
		"conclusion": {
			"bartlett's test": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "true"
		},
		"conclusion": {
			"pearson correlation": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "false"
		},
		"conclusion": {
			"spearman correlation": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"number of ivs": "one"
		},
		"conclusion": {
			"simple linear regression": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"number of ivs": "more than one",
			"include all ivs": "true"
		},
		"conclusion": {
			"multiple linear regression": "true"
		}
	},
	{
		"premisses": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for an effect or find a model of the relationship",
			"dv type": "numerical",
			"dv type-update": "continuous",
			"number of ivs": "more than one",
			"include all ivs": "false"
		},
		"conclusion": {
			"lasso regression": "true"
		}
	}
]

rules2 = [
          { "premisses": { "homoskedastic": "true", "independent observations": "true" },
            "conclusion": { "regression": "true" } },
          { "premisses": { "regression": "true", "output continuity": "false" },
            "conclusion": { "logistic regression": "true" } },
          { "premisses": { "regression": "true", "output continuity": "true" },
            "conclusion": { "not logistic": "true" } },
          { "premisses": { "not logistic": "true", "output continuity": "true", "linear relationship": "true", "output normally distributed": "true" },
            "conclusion": { "linear or lasso": "true" } },
          { "premisses": { "linear or lasso": "true", "all predictors important": "true" },
            "conclusion": { "linear regression": "true" } },
          { "premisses": { "linear or lasso": "true", "all predictors important": "false" },
            "conclusion": { "lasso regression": "true" } }
]
