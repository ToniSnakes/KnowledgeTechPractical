questions = {
    #1.
    "variance known":
        {
            "question": "Is the population variance known?",
            "answers": { "Yes": { "variance known": "true" }, "No": { "variance known": "false" } },
            "info": """Possibly, known from prior experiments."""
        },
    #2.
    "sample size":
    {
        "question": "How large is the sample size?",
        "answers": { "Large (>50)": { "sample size": "large" } , "Small (<=50)": { "sample size": "small"}},
        "info": """The number of observations in a sample. R: length(.)"""
    },
    #3.
    "situation":
    {
        "question": "How many samples (or groups) and measurements were taken?",
        "answers": { "One sample, one measurement": { "situation": "one sample, one measurement" }, "One sample, two measurements": { "situation": "one sample, two measurements" } , "Two samples / groups, one measurement" : {"situation": "two samples / groups, one measurement"}, "More than two samples (or groups), one measurement": { "situation": "more than two samples (or groups), one measurement" }, "One sample, more than two measurements": { "situation": "one sample, more than two measurements" } },
        "info": """The number of samples is the number of times a subset of subjects/observations is drawn from the population. With multiple measurements, the same subjects/observations are measured multiple times, e.g. before and after a treatment. multiple measurements are usually dependent."""
    },
    #4.
    "goal":
    {
        "question": "What's your goal?",
        "answers": { "Test for a relationship": {"goal": "test for a relationship"}, "Compare against a hypothesized value / distribution": {"goal": "compare against hypothesized value / distribution"}, "Compare statistics (e.g. means, variances) between samples / groups": { "goal": "compare statistics (e.g. means, variances) between samples / groups"}},
        "info": """Testing for a relationship includes determining the strength of a correlation, tests for independence, and tests for the effects of variables on each other.
        Comparing against a hypothesized value / distribution includes, for example, testing whether a mean is different from a hypothesized theoretical mean.
        Comparing statistics (e.g. means, variances) between samples / groups includes, for example, testing for a difference in means between two samples."""
    },
    #5.
    "dv normally distributed":
    {
        "question": "How is the dependent variable distributed?",
        "answers":  { "Normally": {"dv normally distributed": "true"}, "Not normally": {"dv normally distributed": "false"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        information on how to test for normality:
        http://www.sthda.com/english/wiki/normality-test-in-r"""
    },
    #6.
    "iv type":
    {
        "question": "Of what type is your independent variable?",
        "answers": {"Categorical (nominal/ordinal)": {"iv type": "categorical (nominal/ordinal)"}, "Numerical (continuous/discrete)": {"iv type": "numerical (continuous/discrete)"}},
        "info": """In your setting, the independent variable is likely a variable that has an effect on a dependent variable.
        Examples of numerical data: height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color."""
    },
    #7.
    "iv type-update":
    {
        "question": "Is your independent variable continuous or discrete?",
        "answers":  {"Continuous": {"iv type-update": "continuous (ratio or interval)"}, "Discrete": {"iv type-update": "discrete"}},
        "info": """In your setting, the independent variable is likely a variable that has an effect on a dependent variable.
        Examples of continuous data: height in meters, age in years.
        Examples of discrete data: number of points in a game, the test-score as a count of correct answers."""
    },
    #8.
    "statistics goal":
    {
        "question": "Which statistics would you like to compare?",
        "answers":  {"Medians": {"statistics goal": "median"}, "Means": {"statistics goal": "mean"}, "Variances":{ "statistics goal": "variance"}},
        "info": """Both median and mean are measures of spread. The median (r: median(.)) is the value separating the upper half from lower half of the values in the sample. The mean (r: mean(.)) is the arithmetic average of all values in the sample.
        The variance (r: var(.)) is a measure of how spread out the values are in the sample. It is the squared standard deviation"""
    },
    #9
    "equal variances":
    {
        "question": "Are the variances between the samples/groups equal?",
        "answers":  {"Equal variances": {"equal variances": "true"}, "Unequal variances": {"equal variances": "false"}},
        "info": """The variance (r: var(.)) is a measure of how spread out the values are in the sample. If unsure about equal variances, perform an f-test or use the rule of thumb: if the ratio between the larger and smaller variance is less than 4, they may be considered equal"""
    },
    #10.
    "equal sample sizes":
    {
        "question": "Are the sizes of the samples/groups equal?",
        "answers":  {"Equal sample sizes": {"equal sample sizes": "true"}, "Unequal sample sizes": {"equal sample sizes": "false"}},
        "info": """r: length(.)"""
    },
    #11.
    "iv types":
    {
        "question": "What are the types of the independent variables (ivs)?",
        "answers":  {"One categorical iv": {"iv types": "one categorical iv"}, "One categorical and one numerical iv": { "iv types": "one categorical and one numerical iv"}, "Multiple categorical ivs": {"iv types": "multiple categorical ivs"}, "Other": {"iv types": "other"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable.
        Examples of numerical data: height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color"""
    },
    #12.
    "number of ivs":
    {
        "question": "How many independent variables are there?",
        "answers": { "One": {"number of ivs": "one"}, "More than one": {"number of ivs": "more than one"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable"""
    },
    #14.
    "include all ivs":
    {
        "question": "Should all independent variables have coefficients in the model?",
        "answers":  { "Yes": { "include all ivs": "true"}, "No": {"include all ivs": "false"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable.
        Do you wish to include all independent variables in the model?", if you are unsure that all independent variables are important or if you already know that some independent variables are unimportant, choose 'no'."""
    },
    #15.
    "dv type":
    {
        "question": "Of what type is your dependent variable?",
        "answers":  {"Categorical (nominal/ordinal)": {"dv type": "categorical"}, "Numerical (continuous/discrete)": {"dv type": "numerical"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of numerical data: height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color"""
    },
    #16.
    "dv type-update":
    {
        "question": "Is your dependent variable continuous or discrete?",
        "answers":  { "Continuous": {"dv type-update": "continuous (ratio or interval)"}, "Discrete": {"dv type-update": "discrete"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of continuous data: height in meters, age in years.
        Examples of discrete data: number of points in a game, the test-score as a count of correct answers"""
    },
    #17.
    "goal-update":
    {
        "question": "What about the relationship are you looking for?",
        "answers":  {"Test for an effect or model the relationship": {"goal-update": "test for an effect / find a model of the relationship"}, "Test for correlation": {"goal-update": "test for correlation"}, "Test for independence": {"goal-update": "test for independence"}},
        "info": """Test for an effect includes tests that show if one variable affects the other.
        A model of the relationship returns the strengths (coefficients) of these effects.
        A test for correlation tests whether or how strong the values of variables move in coordination with each other"""
    },
    #18.
    "linear relationship":
    {
        "question": "How is the relationship between the variables?",
        "answers":  {"Linear relationship": {"linear relationship": "true"}, "Non-linear relationship": {"linear relationship": "false"}},
        "info": """When you plot one variable in function of the other, do the datapoints roughly form a line?"""
    },
    #19.
    "variable types":
    {
        "question": "Of what type are the variables?",
        "answers":  {"All categorical": {"variable types": "all categorical"}, "All continuous": {"variable types": "all continuous"}, "Other or mixed": {"variable types": "other or mixed"}},
        "info": """Examples of continuous data: height in meters, age in years.
            Examples of discrete data: number of points in a game, the test-score as a count of correct answers"""
    }
}


rules = [
    {
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect / find a model of the relationship"
		},
		"conclusion": {
			"goal": "test for effect or model"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for correlation"
		},
		"conclusion": {
			"goal": "test for correlation"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for independence"
		},
		"conclusion": {
			"goal": "test for independence"
		}
	},
	{
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for correlation"
		},
		"conclusion": {
			"goal": "test for correlation"
		}
	},
	{
		"premises": {
			"dv type": "numerical (continuous/discrete)",
			"dv type-update": "continuous (ratio or interval)"
		},
		"conclusion": {
			"dv type": "continuous"
		}
	},
	{
		"premises": {
			"dv type": "numerical (continuous/discrete)",
			"dv type-update": "discrete"
		},
		"conclusion": {
			"dv type": "discrete"
		}
	},
	{
		"premises": {
			"iv type": "numerical (continuous/discrete)",
			"iv type-update": "continuous (ratio or interval)"
		},
		"conclusion": {
			"iv type": "continuous"
		}
	},
	{
		"premises": {
			"iv type": "numerical (continuous/discrete)",
			"iv type-update": "discrete"
		},
		"conclusion": {
			"iv type": "discrete"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value / distribution",
			"dv type": "categorical"
		},
		"conclusion": {
			"test": "chi-square goodness of fit test"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "categorical"
		},
		"conclusion": {
			"test": "logistic regression"
		}
	},
	{
		"premises": {
			"goal": "test for independence",
			"variable types": "all categorical"
		},
		"conclusion": {
			"test": "chi-square test for independence"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test",
			"variance known": "false",
			"sample size": "small"
		},
		"conclusion": {
			"test": "t-test (one-sample)"
		}
	},
	{
		"premises": {
			"test class": "z- or t-test",
			"variance known": "true",
			"sample size": "large"
		},
		"conclusion": {
			"test": "z-test"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value / distribution",
			"dv type": "continuous",
			"dv normally distributed": "true",
			"situation": "situation: one sample, one measurement"
		},
		"conclusion": {
			"test class": "z- or t-test"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value / distribution",
			"dv type": "continuous",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test": "difference of two means (paired)"
		}
	},
	{
		"premises": {
			"goal": "compare against hypothesized value / distribution",
			"dv type": "continuous",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"test": "levene's test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"situation": "one sample, one measurement",
			"dv type": "continuous",
			"dv normally distributed": "false",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "wilcoxon signed rank test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"dv normally distributed": "false",
			"situation": "one sample, two measurements",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "wilcoxon matched-pairs signed rank test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"situation": "more than two samples (or groups), one measurement",
			"dv type": "continuous",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "moods median"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "true",
			"equal sample sizes": "true"
		},
		"conclusion": {
			"test": "student's t-test"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal variances": "false"
		},
		"conclusion": {
			"test": "welsh's t-test"
		}
	},
	{
		"premises": {
			"test class": "t-test (unpaired two sample)",
			"equal sample sizes": "false"
		},
		"conclusion": {
			"test": "welsh's t-test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
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
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "one sample, one measurement",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"test": "mann whitney u test (wilcoxon rank sum test)"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "one sample, two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test": "t-test (paired sample)"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test": "one-way anova"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical iv",
			"dv normally distributed": "false"
		},
		"conclusion": {
			"test": "kruskal-wallis test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "one categorical and one numerical iv"
		},
		"conclusion": {
			"test": "ancova"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "more than two samples (or groups), one measurement",
			"iv types": "multiple categorical ivs"
		},
		"conclusion": {
			"test": "n-way anova (factorial anova)"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "one sample, more than two measurements",
			"dv normally distributed": "true"
		},
		"conclusion": {
			"test": "repeated measures anova"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"dv normally distributed": "false",
			"situation": "one sample, more than two measurements"
		},
		"conclusion": {
			"test": "friedman"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"dv normally distributed": "true",
			"situation": "two samples / groups, one measurement"
		},
		"conclusion": {
			"test": "f-test"
		}
	},
	{
		"premises": {
			"goal": "compare statistics (e.g. means, variances) between samples / groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"dv normally distributed": "true",
			"situation": "more than two samples (or groups), one measurement"
		},
		"conclusion": {
			"test": "bartlett's test"
		}
	},
	{
		"premises": {
			"goal": "test for correlation",
			"dv type": "continuous",
			"variable types": "all continuous",
			"linear relationship": "true"
		},
		"conclusion": {
			"test": "pearson correlation"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"number of ivs": "one"
		},
		"conclusion": {
			"test": "simple linear regression"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"number of ivs": "more than one",
			"include all ivs": "true"
		},
		"conclusion": {
			"test": "multiple regression"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"number of ivs": "more than one",
			"include all ivs": "false"
		},
		"conclusion": {
			"test": "lasso regression"
		}
	},
	{
		"premises": {
			"goal": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "false"
		},
		"conclusion": {
			"test": "spearman correlation"
		}
	}
]

recommendations = {
    "chi-square goodness of fit test": """
    Chi-square goodness of fit test
    When to use it?
    The Chi-square goodness of fit test is a statistical hypothesis test used to determine whether a variable is likely to come from a specified distribution or not. It is often used to evaluate whether sample data is representative of the full population.
    dv type categorical
    goal: Compare against hypothesized value / distribution (q4)
    Assumption(s):
    R-command(s):
    chisq.test(.)
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html
    """,
    "logistic regression":
    """
    Logistic regression
    When to use it?
    Use it when you want to know the probability of the dependent variable given an input.
    dv type categorical
    iv type continuous
    goal: Test for a relationship (q4)
    Assumptions: Observations independent, little multicollinearity of indep vars. Big sample size. (big defined depending on # of indep vars) Errors independent.
    R-command(s):
    glm(., family=binomial)
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
    """,
    "chi-square test for independence":
    """
    Chi-square Test for independence
    When to use it?
    dv type categorical
    iv type categorical (nominal/ordinal) (q6)
    goal: Test for a relationship (q4)
    Assumption(s): 
    R-command(s):
    chisq.test
    More information under:
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html
    """,
    "t-test (one-sample)":
    """
    t-test (one-sample)
    When to use it?
    variance known: false (q1), sample size: small (q2), dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: true (q5), situation: one sample, one measurement (q3)
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
    """,
    "z-test":
    """
    z-test
    When to use it?
    variance known: true (q1), sample size: large (q2), dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: true (q5), situation: one sample, one measurement (q3)
    Assumption(s):
    R-command(s):
    No built-in function
    """,
    "difference of two means (paired)":
    """
    Difference of two means (paired)
    When to use it?
    dv type continuous, goal: Compare against hypothesized value / distribution (q4), situation: one sample, two measurements (q3), DV Normally distributed: true (q5)
    Assumption(s):
    R-command(s):
    """,
    "levene's test":
    """
    Levene's Test
    When to use it?
    dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: false (q5)
    - Test for Variance
    - Multiple samples / groups
    Assumption(s):
    R-command(s):
    https://search.r-project.org/CRAN/refmans/car/html/leveneTest.html
    """,
    "wilcoxon signed rank test":
    """
    Wilcoxon signed rank test
    When to use it?
    dv type continuous, DV Normally distributed: false (q5),  goal: compare statistics (e.g. means, variances) between samples / groups (q4), situation: one sample, one measurement (q3), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
    """,
    "wilcoxon matched-pairs signed rank test":
    """
    Wilcoxon matched-pairs signed rank test
    When to use it?
    dv type continuous, DV Normally distributed: false (q5), situation: One sample, two measurement (q3), goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
    """,
    "moods median":
    """
    Moods Median
    When to use it?
    dv type continuous, situation: More than two groups (q3), goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    """,
    "student's t-test":
    """
    Student's t-test
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: true (q5), equal variances (q9), equal sample sizes (q10)
    Assumption(s):
    - variance of the 2 populations is equal
    - sample sizes are equal
    R-command(s):
    """,
    "welsh's t-test":
    """
    Welsh's t-test
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: true (q5), Unequal variances (q9), Unequal sample sizes (q10)
    Assumption(s):
    R-command(s):
    """,
    "mann whitney u test (wilcoxon rank sum test)":
    """
    Mann Whitney U Test (Wilcoxon Rank Sum Test)
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: false (q5)
    Assumption(s):
    R-command(s):
    """,
    "t-test (paired sample)":
    """
    T-test (paired sample)
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, two measurements (q3), DV Normally distributed: true (q5)
    When to use it?
    Assumption(s):
    R-command(s):

    """,
    "one-way anova":
    """
    One-way ANOVA
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: One categorical IV (q11), DV Normally distributed: true (q5)
    Assumption(s):
    R-command(s):
    """,
    "kruskal-wallis test":
    """
    Kruskal-Wallis Test
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: One categorical IV (q11), DV Normally distributed: false (q5)
    Assumption(s):
    R-command(s):
    """,
    "ancova":
    """
    ANCOVA
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: A categorical and a numerical IV (q11)
    Assumption(s):
    R-command(s):
    """,
    "n-way anova (factorial anova)":
    """
    n-way ANOVA (Factorial ANOVA)
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: Multiple categorical IVs (q11)
    Assumption(s):
    R-command(s):
    """,
    "repeated measures anova":
    """
    Repeated measures ANOVA
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: One sample, more than two measurements (q3), DV Normally distributed: true (q5)
    Assumption(s):
    R-command(s):
    """,
    "friedman":
    """
    Friedman
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: One sample, more than two measurements (q3), DV Normally distributed: false (q5)
    Assumption(s):
    R-command(s):
    """,
    "f-test":
    """
    F-test
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), DV Normally distributed: true (q5), situation: Two samples, one measurement (q3)
    Assumption(s):
    R-command(s):
    """,
    "bartlett's test":
    """Bartlett's Test
    When to use it?
    dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), DV Normally distributed: true (q5), situation: More than two samples, one measurement (q3)
    Assumption(s):
    R-command(s):
    """,
    "pearson correlation":
    """Pearson Correlation
    When to use it?
    dv type continuous, goal: Test for a relationship (q4), number of ivs: more than one (q12), Relationship goal: the degree of correlation (q13)
    - Multiple independent variables, all to be included in the test
    - Ranked dependent variable
    - some IVs are important, but unkown which
    - Find the degree of correlation
    Assumption(s):
    R-command(s):
    """,
    "simple linear regression":
    """Simple Linear Regression
    When to use it?
    dv type continuous, goal: Test for a relationship (q4), number of ivs: one (q12), Relationship goal: model or effect (q13)
    - One independent variable
    - Continuous DV and IV (Ratio or Interval)
    - Test for a relationship between the variables or find a a model of the relationship
    Assumption(s):
    - Homoscedasticity
    R-command(s):
    """,
    "multiple regression":
    """Multiple Regression
    When to use it? 
    dv type continuous, goal: Test for a relationship (q4), number of ivs: more than one (q12), include all ivs: true (q13)
    - Multiple independent variables, all to be included in the test
    - Ranked dependent variable
    - Test for a relationship
    - Test for a relationship between the variables, and find a model of the relationship
    Assumption(s):
    - Homoscedasticity, 
    R-command(s):
    """,
    "lasso regression":
    """Lasso Regression
    When to use it?
    dv type continuous, goal: Test for a relationship (q4),  number of ivs: more than one (q12), include all ivs: false (q13)
    - Multiple independent variables, some of which are important, but unknown which
    - Continuous DV (Ratio or Interval)
    - Test for a relationship between the variables, and find a model of the relationship
    Assumption(s):
    - Homoscedasticity
    R-command(s):
    """,
    "spearman correlation":
    """Spearman Correlation
    When to use it?
    dv type discrete, goal: Test for a relationship (q4), number of ivs: one (q12)
    - One independent variable
    - Ranked (positive and discrete) dependent variable
    - Test for a relationship
    Assumptions:
    R-command(s):
    """
}
