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
			"goal": "compare against hypothesized value or distribution"
		},
		"conclusion": {
			"goal hypothesis": "true"
		}
	},
	{
		"premises": {
			"goal hypothesis": "true",
			"dv type": "categorical"
		},
		"conclusion": {
			"chi-square goodness of fit test": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for an effect or find a model of the relationship"
		},
		"conclusion": {
			"goal relationship": "test for effect"
		}
	},
	{
		"premises": {
			"goal relationship": "test for effect",
			"dv type": "categorical"
		},
		"conclusion": {
			"logistic regression": "true"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"relationship goal-update": "test for independence"
		},
		"conclusion": {
			"goal relationship": "test for independence"
		}
	},
	{
		"premises": {
			"goal relationship": "test for independence",
			"variable types": "all categorical"
		},
		"conclusion": {
			"chi-square test for independence": "true"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test (one-sample)",
			"variance known": "false",
			"sample size": "small"
		},
		"conclusion": {
			"t-test (one-sample)": "true"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test (one-sample)",
			"variance known": "true"
		},
		"conclusion": {
			"z-test": "true"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test (one-sample)",
			"sample size": "large"
		},
		"conclusion": {
			"z-test": "true"
		}
	},
	{
		"premises": {
			"dv type": "numerical",
			"dv type-update": "continuous"
		},
		"conclusion": {
			"dv numerical type": "continuous"
		}
	},
	{
		"premises": {
			"goal hypothesis": "true",
			"dv numerical type": "continuous",
			"dv normally distributed": "true",
			"situation": "one sample, one measurement"
		},
		"conclusion": {
			"test class": "z- or t-test (one-sample)"
		}
	},
	{
		"premises": {
			"goal hypothesis": "true",
			"dv numerical type": "continuous",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"difference of two means (paired)": "true"
		}
	},
	{
		"premises": {
			"goal hypothesis": "true",
			"dv type": "numerical",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"levene's test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"statistics goal-update": "median"
		},
		"conclusion": {
			"goal statistics": "median"
		}
	},
	{
		"premises": {
			"goal statistics": "median",
			"situation": "two samples (or groups), one measurement",
			"dv type": "numerical"
		},
		"conclusion": {
			"wilcoxon signed rank test": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "median",
			"situation": "one sample, two measurements",
			"dv type": "numerical"
		},
		"conclusion": {
			"wilcoxon matched-pairs signed rank test": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "median",
			"situation": "more than two samples (or groups), one measurement",
			"dv type": "numerical"
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
			"welch's t-test": "true"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples or groups",
			"statistics goal-update": "mean"
		},
		"conclusion": {
			"goal statistics": "mean"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv numerical type": "continuous",
			"situation": "two samples (or groups), one measurement",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test class": "t-test (unpaired two sample)"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv type": "numerical",
			"situation": "two samples (or groups), one measurement",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"mann whitney u test (wilcoxon rank sum test)": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv numerical type": "continuous",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"t-test (paired sample)": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv numerical type": "continuous",
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
			"goal statistics": "mean",
			"dv type": "numerical",
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
			"goal statistics": "mean",
			"dv type": "numerical",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical and one numerical iv"
		},
		"conclusion": {
			"ancova": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv type": "numerical",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "multiple categorical ivs"
		},
		"conclusion": {
			"n-way anova (factorial anova)": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv type": "numerical",
			"situation": "one sample, more than two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"repeated measures anova": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "mean",
			"dv numerical type": "continuous",
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
			"statistics goal-update": "variance"
		},
		"conclusion": {
			"goal statistics": "variance"
		}
	},
	{
		"premises": {
			"goal statistics": "variance",
			"dv numerical type": "continuous",
			"dv normally distributed": "true",
			"situation": "two samples (or groups), one measurement"
		},
		"conclusion": {
			"f-test": "true"
		}
	},
	{
		"premises": {
			"goal statistics": "variance",
			"dv numerical type": "continuous",
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
			"relationship goal-update": "test for correlation"
		},
		"conclusion": {
			"goal relationship": "test for correlation"
		}
	},
	{
		"premises": {
			"goal relationship": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "true"
		},
		"conclusion": {
			"pearson correlation": "true"
		}
	},
	{
		"premises": {
			"goal relationship": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "false"
		},
		"conclusion": {
			"spearman correlation": "true"
		}
	},
	{
		"premises": {
			"goal relationship": "test for effect",
			"dv numerical type": "continuous",
			"number of ivs": "one"
		},
		"conclusion": {
			"simple linear regression": "true"
		}
	},
	{
		"premises": {
			"goal relationship": "test for effect",
			"dv type": "numerical",
			"number of ivs": "more than one",
			"include all ivs": "true"
		},
		"conclusion": {
			"multiple linear regression": "true"
		}
	},
	{
		"premises": {
			"goal relationship": "test for effect",
			"dv type": "numerical",
			"number of ivs": "more than one",
			"include all ivs": "false"
		},
		"conclusion": {
			"lasso regression": "true"
		}
	}
]
