# Question list:
# { determined field : { "question": question content , "answers": {field: value, ...} }, ... }
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
        "answers": { "One sample, one measurement": { "situation": "one sample, one measurement" }, "One sample, two measurements": { "situation": "one sample, two measurements" } , "Two samples or groups, one measurement" : {"situation": "two samples or groups, one measurement"}, "More than two samples (or groups), one measurement": { "situation": "more than two samples (or groups), one measurement" }, "One sample, more than two measurements": { "situation": "one sample, more than two measurements" } },
        "info": """The number of samples is the number of times a subset of subjects or observations is drawn from the population. With multiple measurements, the same subjects or observations are measured multiple times, e.g. before and after a treatment. multiple measurements are usually dependent."""
    },
    #4.
    "goal":
    {
        "question": "What's your goal?",
        "answers": { "Test for a relationship": {"goal": "test for a relationship"}, "Compare against a hypothesized value or distribution": {"goal": "compare against hypothesized value or distribution"}, "Compare statistics (e.g. means, variances) between samples or groups": { "goal": "compare statistics (e.g. means, variances) between samples or groups"}},
        "info": """Testing for a relationship includes determining the strength of a correlation, tests for independence, and tests for the effects of variables on each other.
        Comparing against a hypothesized value or distribution includes, for example, testing whether a mean is different from a hypothesized theoretical mean.
        Comparing statistics (e.g. means, variances) between samples or groups includes, for example, testing for a difference in means between two samples."""
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
        "answers": {"Categorical (nominal or ordinal)": {"iv type": "categorical (nominal or ordinal)"}, "Numerical (continuous or discrete)": {"iv type": "numerical"}},
        "info": """In your setting, the independent variable is likely a variable that has an effect on a dependent variable.
        Examples of numerical data: height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color."""
    },
    #7.
    "iv type-update":
    {
        "question": "Is your independent variable continuous or discrete?",
        "answers":  {"Continuous": {"iv type-update": "continuous"}, "Discrete": {"iv type-update": "discrete"}},
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
        "question": "Are the variances between the samples or groups equal?",
        "answers":  {"Equal variances": {"equal variances": "true"}, "Unequal variances": {"equal variances": "false"}},
        "info": """The variance (r: var(.)) is a measure of how spread out the values are in the sample. If unsure about equal variances, perform an f-test or use the rule of thumb: if the ratio between the larger and smaller variance is less than 4, they may be considered equal"""
    },
    #10.
    "equal sample sizes":
    {
        "question": "Are the sizes of the samples or groups equal?",
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
        "answers":  {"Categorical (nominal or ordinal)": {"dv type": "categorical"}, "Numerical (continuous or discrete)": {"dv type": "numerical"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of numerical data: height in meters, age in years, and income in euros.
        Examples of categorical data: country of origin, hair color"""
    },
    #16.
    "dv type-update":
    {
        "question": "Is your dependent variable continuous or discrete?",
        "answers":  { "Continuous": {"dv type-update": "continuous"}, "Discrete": {"dv type-update": "discrete"}},
        "info": """The dependent variable is a variable whose value depends on that of at least another (independent variable).
        Examples of continuous data: height in meters, age in years.
        Examples of discrete data: number of points in a game, the test-score as a count of correct answers"""
    },
    #17.
    "goal-update":
    {
        "question": "What about the relationship are you looking for?",
        "answers":  {"Test for an effect or model the relationship": {"goal-update": "test for an effect or find a model of the relationship"}, "Test for correlation": {"goal-update": "test for correlation"}, "Test for independence": {"goal-update": "test for independence"}},
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

questions2 = {
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
