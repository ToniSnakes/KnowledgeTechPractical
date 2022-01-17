# Recommendations when the dialogue ends

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

recommendations2 = {
  "logistic regression": "Logistic Regression",
  "linear regression": "Linear Regression",
  "lasso regression": "Lasso Regression",
  "none": "This is not in our database"
  }
