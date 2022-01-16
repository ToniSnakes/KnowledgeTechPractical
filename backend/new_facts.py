questions = {
    #1.
    "variance known":
        {
            "question": "Is the population variance known?",
            "answers": { "Yes" : { "variance known": "True" }, "No" : { "variance known" : "False" } },
            "info": """Possibly, known from prior experiments."""
        },
    #2.
    "sample size":
    {
        "question": "How large is the sample size?",
        "answers": { "Large (>50)": { "sample size" : "large" } , "Small (<=50)": { "sample size": "small"}},
        "info": """The number of observations in a sample. R: length(.)"""
    },
    #3.
    "situation":
    {
        "question": "How many samples and measurements were taken?",
        "answers": { "One sample, one measurement" : { "situation" : "one sample, one measurement" }, "One sample, two measurements": { "situation" : "one sample, two measurements" } , "More than two groups / samples, one measurement": { "situation": "more than two groups / samples, one measurement" }, "One sample, more than two measurements / groups" : { "situation" : "one sample, more than two measurements / groups" } },
        "info": """The number of samples is the number of times a subset of subjects/observations is drawn from the population. With multiple measurements, the same subjects/observations are measured multiple times, e.g. before and after a treatment. Multiple measurements are usually dependent."""
    },
    #4.
    "goal":
    {
        "question": "What's your goal?",
        "answers":  { "Test for a relationship": {"goal": "test for a relationship"}, "Compare against a hypothesized value / distribution": {"goal": "compare against hypothesized value / distribution"}, "Compare statistics (e.g. means, variances) between samples / groups": { "goal": "compare statistics (e.g. means, variances) between Samples / Groups"}},
        "info": """Testing for a relationship includes determining the strength of a correlation, tests for independence, and tests for the effects of variables on each other.
        Comparing against a hypothesized value / distribution includes, for example, testing whether a mean is different from a hypothesized theoretical mean.
        Comparing statistics (e.g. means, variances) between samples / groups includes, for example, testing for a difference in means between two samples."""
    },

    #5.
    "DV normally distributed":
    {
        "question": "How is the dependent variable distributed?",
        "answers":  { "Normally": {"DV normally distributed": "True"}, "Not normally": {"DV normally distributed": "False"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Information on how to test for normality:
        http://www.sthda.com/english/wiki/normality-test-in-r"""
    },

    #6.
    "iv type":
    {
        "question": "Of what type is your independent variable?",
        "answers": {"Categorical (nominal/ordinal)": {"iv type": "categorical (nominal/ordinal)"}, "Numerical (continuous/discrete)": {"iv type": "numerical (continuous/discrete)"}},
        "info": """In your setting, the independent variable is likely a variable that has an effect on a dependent variable.
        Examples of numerical data: Height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color."""
    },
    #7.
    "iv type-update":
    {
        "question": "Is your independent variable continuous or discrete?",
        "answers":  {"Continuous": {"iv type-update": "continuous (Ratio or Interval)"}, "Discrete": {"iv type-update": "discrete"}},
        "info": """In your setting, the independent variable is likely a variable that has an effect on a dependent variable.
        Examples of continuous data: height in meters, age in years.
        Examples of discrete data: number of points in a game, the test-score as a count of correct answers."""
    },
    #8.
    "Statistics goal":
    {
        "question": "Which statistics would you like to compare?",
        "answers":  {"Medians": {"Statistics goal": "median"}, "Means": {"Statistics goal": "mean"}, "Variances":{ "Statistics goal": "variance"}},
        "info": """Both median and mean are measures of spread. The median (R: median(.)) is the value separating the upper half from lower half of the values in the sample. The mean (R: mean(.)) is the arithmetic average of all values in the sample.
        The variance (R: var(.)) is a measure of how spread out the values are in the sample. It is the squared standard deviation"""
    },
    #9
    "Equal variances":
    {
        "question": "Are the variances between the samples/groups equal?",
        "answers":  {"Equal variances": {"Equal variances": "True"}, "Unequal variances": {"Equal variances": "False"}},
        "info": """The variance (R: var(.)) is a measure of how spread out the values are in the sample. If unsure about equal variances, perform an F-test or use the rule of thumb: If the ratio between the larger and smaller variance is less than 4, they may be considered equal"""
    },
    #10.
    "Equal sample sizes":
    {
        "question": "Are the sizes of the samples/groups equal?",
        "answers":  {"Equal sample sizes": {"Equal sample sizes": "True"}, "Unequal sample sizes": {"Equal sample sizes": "False"}},
        "info": """R: length(.)"""
    },
    #11.
    "iv types":
    {
        "question": "What are the types of the independent variables (IVs)?",
        "answers":  {"One categorical IV": {"iv types": "one categorical IV"}, "One categorical and one numerical IV": { "iv types": "one categorical and one numerical IV"}, "Multiple categorical IVs": {"iv types": "Multiple categorical IVs"}, "Other": {"iv types": "other"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable.
        Examples of numerical data: Height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color"""
    },
    #12.
    "Number of IVs":
    {
        "question": "How many independent variables are there?",
        "answers": { "One": {"Number of IVs": "one"}, "More than one": {"Number of IVs": "more than one"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable"""
    },
    "Include all IVs":
    {
        #14.
        "question": "Should all independent variables have coefficients in the model?",
        "answers":  { "Yes": { "Include all IVs" : "True"}, "No": {"Include all IVs": "False"}},
        "info": """In your setting, the independent variables are likely the variables that have an effect on a dependent variable
        Do you wish to include all independent variables in the model?", If you are unsure that all independent variables are important or if you already know that some independent variables are unimportant, choose 'no'."""
    },
    #15.
    "dv type":
    {
        "question": "Of what type is your dependent variable?",
        "answers":  {"Categorical (nominal/ordinal)": {"dv type": "categorical (nominal/ordinal)"}, "Numerical (continuous/discrete)": {"dv type": "numerical (continuous/discrete)"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of numerical data: Height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color"""
    },
    #16.
    "dv type-update":
    {
        "question": "Is your dependent variable continuous or discrete?",
        "answers":  { "Continuous": {"dv type-update": "continuous (Ratio or Interval)"}, "Discrete": {"dv type-update": "discrete"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of continuous data: height in meters, age in years.
        Examples of discrete data: number of points in a game, the test-score as a count of correct answers"""
    },
    #17.
    "goal-update":
    {
        "question": "What about the relationship are you looking for?",
        "answers":  {"Test for an effect or model the relationship": {"goal-update": "test for an effect / Find a model of the relationship"}, "Test for correlation": {"goal-update": "test for correlation"}, "Test for independence": {"goal-update": "test for independence"}},
        "info": """Test for an effect includes tests that show if one variable affects the other.
        A model of the relationship returns the strengths (coefficients) of these effects.
        A test for correlation tests whether or how strong the values of variables move in coordination with each other"""
    },
    "linear relationship":
    {
    #18.
        "question": "How is the relationship between the variables?",
        "answers":  {"Linear relationship": {"linear relationship": "True"}, "Non-linear relationship": {"linear relationship": "False"}},
        "info": """When you plot one variable in function of the other, do the datapoints roughly form a line?"""
    },
    #19.
    "variable types":
    {
        "question": "Of what type are the variables?",
        "answers":  {"All Categorical": {"variable types": "all Categorical"}, "All Continuous": {"variable types": "all Continuous"}, "Other or mixed": {"variable types": "other or mixed"}},
        "info": """Examples of continuous data: height in meters, age in years.
            Examples of discrete data: number of points in a game, the test-score as a count of correct answers"""
    }
}


rules = [
    {
		"premises": {
			"goal": "test for a relationship",
			"goal-update": "test for an effect / Find a model of the relationship"
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
			"dv type-update": "continuous (Ratio or Interval)"
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
			"iv type-update": "continuous (Ratio or Interval)"
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
			"goal": "Compare against hypothesized value / distribution",
			"dv type": "categorical"
		},
		"conclusion": {
			"test": "Chi-square goodness of fit test"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "categorical"
		},
		"conclusion": {
			"test": "Logistic regression"
		}
	},
	{
		"premises": {
			"goal": "test for independence",
			"variable types": "Categorical variables"
		},
		"conclusion": {
			"test": "Chi-square Test for independence"
		}
	},
	{
		"premises": {
			"test class": "Z- or T-test",
			"variance known": "False",
			"sample size": "small"
		},
		"conclusion": {
			"test": "t-test (one-sample)"
		}
	},
	{
		"premises": {
			"test class": "Z- or T-test",
			"variance known": "True",
			"sample size": "large"
		},
		"conclusion": {
			"test": "z-test"
		}
	},
	{
		"premises": {
			"goal": "Compare against hypothesized value / distribution",
			"dv type": "continuous",
			"DV Normally distributed": "True",
			"situation": "situation: one sample, one measurement"
		},
		"conclusion": {
			"test class": "Z- or T-test"
		}
	},
	{
		"premises": {
			"goal": "Compare against hypothesized value / distribution",
			"dv type": "continuous",
			"situation": "one sample, two measurements",
			"DV Normally distributed": "True"
		},
		"conclusion": {
			"test": "Difference of two means (paired)"
		}
	},
	{
		"premises": {
			"goal": "Compare against hypothesized value / distribution",
			"dv type": "continuous",
			"DV Normally distributed": "False"
		},
		"conclusion": {
			"test": "Levene's Test"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"situation": "One sample, one measurement",
			"dv type": "continuous",
			"DV Normally distributed": "False",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "Wilcoxon signed rank test"
		}
	},
	{
		"premises": {
			"goal": " Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"DV Normally distributed": "False",
			"situation": "One sample, two measurement",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "Wilcoxon matched-pairs signed rank test"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"situation": "More than two groups / samples, one measurement",
			"dv type": "continuous",
			"statistics goal": "median"
		},
		"conclusion": {
			"test": "Moods Median"
		}
	},
	{
		"premises": {
			"test class": "T-test (unpaired two sample)",
			"Equal variances": "True",
			"Equal sample sizes": "True"
		},
		"conclusion": {
			"test": " Student's t-test"
		}
	},
	{
		"premises": {
			"test class": "T-test (unpaired two sample)",
			"Equal variances": "False"
		},
		"conclusion": {
			"test": "Welsh's t-test"
		}
	},
	{
		"premises": {
			"test class": "T-test (unpaired two sample)",
			"Equal sample sizes": "False"
		},
		"conclusion": {
			"test": "Welsh's t-test"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"Statistics goal": "Mean",
			"situation": "one sample, one measurement",
			"DV Normally distributed": "True"
		},
		"conclusion": {
			"test class": "T-test (unpaired two sample)"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"Statistics goal": "Mean",
			"situation": "one sample, one measurement",
			"DV Normally distributed": "False",
			"": ""
		},
		"conclusion": {
			"test": "Mann Whitney U Test (Wilcoxon Rank Sum Test)"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "one sample, two measurements",
			"DV Normally distributed": "True"
		},
		"conclusion": {
			"test": " T-test (paired sample)"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "More than two samples / groups, one measurement",
			"iv types": "One categorical IV",
			"DV Normally distributed": "True"
		},
		"conclusion": {
			"test": "One-way ANOVA"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "More than two samples / groups, one measurement",
			"iv types": "One categorical IV",
			"DV Normally distributed": "False"
		},
		"conclusion": {
			"test": "Kruskal-Wallis Test"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "More than two samples / groups, one measurement",
			"iv types": "A categorical and a numerical IV"
		},
		"conclusion": {
			"test": "ANCOVA"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "More than two samples / groups, one measurement",
			"iv types": "Multiple categorical IVs"
		},
		"conclusion": {
			"test": "n-way ANOVA (Factorial ANOVA)"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "One sample, more than two measurements / groups",
			"DV Normally distributed": "True"
		},
		"conclusion": {
			"test": "Repeated measures ANOVA"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"situation": "One sample, more than two measurements / groups",
			" DV Normally distributed": "False"
		},
		"conclusion": {
			"test": "Friedman"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"DV Normally distributed": "True",
			"situation": "Two samples / groups, one measurement"
		},
		"conclusion": {
			"test": "F-test"
		}
	},
	{
		"premises": {
			"goal": "Compare statistics (e.g. means, variances) between Samples / Groups",
			"dv type": "continuous",
			"statistics goal": "mean",
			"DV Normally distributed": "True",
			"situation": "More than two samples / groups, one measurement"
		},
		"conclusion": {
			"test": "Barlett's"
		}
	},
	{
		"premises": {
			"goal": "test for correlation",
			"dv type": "continuous",
			"variable types": "Continuous variables",
			"linear relationship": "True"
		},
		"conclusion": {
			"test": "Pearson correlation"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"Number of IVs": "one",
			"": "",
			"": "",
			"": ""
		},
		"conclusion": {
			"test": "Simple Linear Regression"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"Number of IVs": "more than one",
			"Include all IVs": "True",
			"": ""
		},
		"conclusion": {
			"test": "Multiple Regression"
		}
	},
	{
		"premises": {
			"goal": "test for effect or model",
			"dv type": "continuous",
			"Number of IVs": "more than one",
			"Include all IVs": "False",
			"": "",
			"": ""
		},
		"conclusion": {
			"test": "Lasso Regression"
		}
	},
	{
		"premises": {
			"goal": "test for correlation",
			"variable types": "all continuous",
			"linear relationship": "False"
		},
		"conclusion": {
			"test": "Spearman Correlation"
		}
	}
]

recommendations = {
    "Chi-square goodness of fit test" : """
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
    "Logistic regression":
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
    "Chi-square Test for independence":
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
    variance known: False (q1), sample size: small (q2), dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: True (q5), situation: one sample, one measurement (q3)
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html

    """,
    "z-test":
    """
    z-test
    When to use it?
    variance known: True (q1), sample size: large (q2), dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: True (q5), situation: one sample, one measurement (q3)
    Assumption(s):
    R-command(s):
    No built-in function
    """,
    "Difference of two means (paired)":
    """
    Difference of two means (paired)
    When to use it?
    dv type continuous, goal: Compare against hypothesized value / distribution (q4), situation: one sample, two measurements (q3), DV Normally distributed: True (q5)

    Assumption(s):
    R-command(s):

    """,
    "Levene's Test":
    """
    Levene's Test
    When to use it?
    dv type continuous, goal: Compare against hypothesized value / distribution (q4), DV Normally distributed: False (q5)
    - Test for Variance
    - Multiple samples / groups
    Assumption(s):
    R-command(s):
    https://search.r-project.org/CRAN/refmans/car/html/leveneTest.html

    """,
    "Wilcoxon signed rank test":
    """
    Wilcoxon signed rank test
    When to use it?
    dv type continuous, DV Normally distributed: False (q5),  goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), situation: One sample, one measurement (q3), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
    """,
    "Wilcoxon matched-pairs signed rank test":
    """
    Wilcoxon matched-pairs signed rank test
    When to use it?
    dv type continuous, DV Normally distributed: False (q5), situation: One sample, two measurement (q3), goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
    """,
    "Moods Median":
    """
    Moods Median
    When to use it?
    dv type continuous, situation: More than two groups (q3), goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: median (q8)
    - non-parametric
    Assumption(s):
    R-command(s):
    """,
    "Student's t-test":
    """
    Student's t-test
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: True (q5), Equal variances (q9), Equal sample sizes (q10)
    Assumption(s):
    - variance of the 2 populations is equal
    - sample sizes are equal
    R-command(s):
    """,
    "Welsh's t-test":
    """
    Welsh's t-test
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: True (q5), Unequal variances (q9), Unequal sample sizes (q10)
    Assumption(s):
    R-command(s):
    """,
    "Mann Whitney U Test (Wilcoxon Rank Sum Test)":
    """
    Mann Whitney U Test (Wilcoxon Rank Sum Test)
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: False (q5)
    Assumption(s):
    R-command(s):
    """,
    "T-test (paired sample)":
    """
    T-test (paired sample)
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: one sample, two measurements (q3), DV Normally distributed: True (q5)
    When to use it?
    Assumption(s):
    R-command(s):

    """,
    "One-way ANOVA":
    """
    One-way ANOVA
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: One categorical IV (q11), DV Normally distributed: True (q5)
    Assumption(s):
    R-command(s):
    """,
    "Kruskal-Wallis Test":
    """
    Kruskal-Wallis Test
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: One categorical IV (q11), DV Normally distributed: False (q5)
    Assumption(s):
    R-command(s):
    """,
    "ANCOVA":
    """
    ANCOVA
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: A categorical and a numerical IV (q11)
    Assumption(s):
    R-command(s):
    """,
    "n-way ANOVA (Factorial ANOVA)":
    """
    n-way ANOVA (Factorial ANOVA)
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: Multiple categorical IVs (q11)
    Assumption(s):
    R-command(s):
    """,
    "Repeated measures ANOVA":
    """
    Repeated measures ANOVA
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: One sample, more than two measurements / groups (q3), DV Normally distributed: True (q5)
    Assumption(s):
    R-command(s):
    """,
    "Friedman":
    """
    Friedman
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), situation: One sample, more than two measurements / groups (q3), DV Normally distributed: False (q5)
    Assumption(s):
    R-command(s):
    """,
    "F-test":
    """
    F-test
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), DV Normally distributed: True (q5), situation: Two samples, one measurement (q3)
    Assumption(s):
    R-command(s):
    """,
    "Bartlett's Test":
    """Bartlett's Test
    When to use it?
    dv type continuous, goal: Compare statistics (e.g. means, variances) between Samples / Groups (q4), statistics goal: mean (q8), DV Normally distributed: True (q5), situation: More than two samples, one measurement (q3)
    Assumption(s):
    R-command(s):
    """,
    "Pearson Correlation":
    """Pearson Correlation
    When to use it?
    dv type continuous, goal: Test for a relationship (q4), Number of IVs: more than one (q12), Relationship goal: the degree of correlation (q13)
    - Multiple independent variables, all to be included in the test
    - Ranked dependent variable
    - some IVs are important, but unkown which
    - Find the degree of correlation
    Assumption(s):
    R-command(s):
    """,
    "Simple Linear Regression":
    """Simple Linear Regression
    When to use it?
    dv type continuous, goal: Test for a relationship (q4), Number of IVs: one (q12), Relationship goal: model or effect (q13)
    - One independent variable
    - Continuous DV and IV (Ratio or Interval)
    - Test for a relationship between the variables or find a a model of the relationship
    Assumption(s):
    - Homoscedasticity
    R-command(s):
    """,
    "Multiple Regression":
    """Multiple Regression
    When to use it? 
    dv type continuous, goal: Test for a relationship (q4), Number of IVs: more than one (q12), Include all IVs: True (q13)
    - Multiple independent variables, all to be included in the test
    - Ranked dependent variable
    - Test for a relationship
    - Test for a relationship between the variables, and find a model of the relationship
    Assumption(s):
    - Homoscedasticity, 
    R-command(s):
    """,
    "Lasso Regression":
    """Lasso Regression
    When to use it?
    dv type continuous, goal: Test for a relationship (q4),  Number of IVs: more than one (q12), Include all IVs: False (q13)
    - Multiple independent variables, some of which are important, but unknown which
    - Continuous DV (Ratio or Interval)
    - Test for a relationship between the variables, and find a model of the relationship
    Assumption(s):
    - Homoscedasticity
    R-command(s):
    """,
    "Spearman Correlation":
    """Spearman Correlation
    When to use it?
    dv type discrete, goal: Test for a relationship (q4), Number of IVs: one (q12)
    - One independent variable
    - Ranked (positive and discrete) dependent variable
    - Test for a relationship
    Assumptions:
    R-command(s):
    """
}
