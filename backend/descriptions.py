# Recommendations when the dialogue ends
descriptions = {
  "chi-square goodness of fit test": """
  Chi-square goodness of fit test
  When to use it?
  The Chi-square goodness of fit test is a statistical hypothesis test used to determine whether a variable is likely to come from a specified distribution or not. It is often used to evaluate whether sample data is representative of the full population.
  Assumption(s):
  - Sample data is a random selection of population data. 
  - There are a sufficient number of observations for each category. 
  R-command(s):
  chisq.test(.)
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html
  """,
  "logistic regression":
  """
  Logistic regression
  When to use it?
  Use it when you want to know the probability of the dependent variable given an input.
  Assumptions:
  : Observations independent, little multicollinearity of indep vars. Big sample size. (big defined depending on # of indep vars) Errors independent.
  R-command(s):
  glm(., family=binomial)
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
  """,
  "chi-square test for independence":
  """
  Chi-square Test for independence
  Use this test to determine whether or not two categorical variables are related.
  Assumption(s):
  - Data should be frequencies or counts. 
  - Categories are mutually exclusive, meaning an observation cannot belong to multiple categories. 
  R-command(s):
  chisq.test
  More information under:
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html
  """,
  "t-test (one-sample)":
  """
  t-test (one-sample)
  When to use it?
  Use it to determine if a single unknown population mean is statistically different from a specific numerical value.
  Assumption(s):
  Data is independent, continuous, and randomly sampled from the target population.

  R-command(s):
  t.test(x, y=NULL, mu=value_of_interest) from the stats library
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
  """,
  "z-test":
  """
  z-test
  When to use it?
  Use it if the underlying data is normally distributed to determine if the mean of the population is different from a value (one-sample) or different from a second sample. 
  Assumption(s):
  Underlying data is normally distributed. There are a big number of datapoints to evaluate. (big > 30)
  R-command(s):
  z.test from the BSDA library
  https://rdrr.io/cran/BSDA/man/z.test.html
  No built-in function
  """,
  "difference of two means (paired)":
  """
  Difference of two means (paired)
  When to use it?
  Use it to test whether the difference of the means of two populations differ, or differ in a specific manner.
  Assumption(s):
  -Observations between subjects are independent. 
  -Measurements are paired
  -Sensitive to outliers
  -Normality
  R-command(s):
  t.test(x, y, paired = TRUE, alternative = "two.sided") 
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
  """,
  "levene's test":
  """
  Levene's Test
  When to use it?
  Us it to test if at least two of many samples come from populations with unequal variances. It can be used to verify the assumption of equal variances for other statistical tests. It does not assume normality of the populations.
  Assumption(s):
  -Independent observations
  R-command(s):
  https://search.r-project.org/CRAN/refmans/car/html/leveneTest.html
  """,
  "wilcoxon signed rank test":
  """
  Wilcoxon signed rank test
  When to use it?
  Use this to test if the medians from two indpendent samples are equal to a given value.
  Assumption(s):
  -Data needs to be able to be ranked
  R-command(s):
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
  """,
  "wilcoxon matched-pairs signed rank test":
  """
  Wilcoxon matched-pairs signed rank test
  When to use it?
  Use it to test if the median from from two paired samples are equal to a given value.
  Assumption(s):
  -non-parametric
  R-command(s):
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html
  """,
  "moods median":
  """
  Moods Median
  When to use it?
  Use it to test for a difference in medians of two or more independent samples.
  Assumption(s):
  -Samples are independent
  -Sensitive to sample size. Should be used on smaller samples.
  R-command(s):
  https://search.r-project.org/CRAN/refmans/RVAideMemoire/html/mood.medtest.html
  """,
  "student's t-test":
  """
  Student's t-test
  When to use it?
  Use the Student's t-test to test the means of two populations.
  Assumption(s):
  - normality of the populations
  - variance of the 2 populations is equal
  - sample sizes are equal
  R-command(s):
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
  """,
  "welch's t-test":
  """
  Welch's t-test
  When to use it?
  Use to compare the means when the variance is unknown. 
  Assumption(s):
  -normality of the data
  R-command(s):
  t.test from the stats package but var.equal has to be set to FALSE. 
  t.test(x, y, paired = FALSE, var.equal=FALSE)
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
  """,
  "mann whitney u test (wilcoxon rank sum test)":
  """
  Mann Whitney U Test (Wilcoxon Rank Sum Test)
  When to use it?
  dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, one measurement (q3), DV Normally distributed: false (q5)
  Assumption(s):
  R-command(s):
  wilcox.test() in stats library 
  arguments: paired = TRUE, alternative = “two.sided”

  """,
  "t-test (paired sample)":
  """
  T-test (paired sample)
  dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: one sample, two measurements (q3), DV Normally distributed: true (q5)
  When to use it?
  Assumption(s):
  R-command(s):
  Also uses t.test() from the stats package with paired=TRUE
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html
  """,
  "one-way anova":
  """
  One-way ANOVA
  When to use it?
  dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: One categorical IV (q11), DV Normally distributed: true (q5)
  Assumption(s):
  R-command(s):
  aov() from the stats library.
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aov.html 
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
  ANCOVA (ANalysis of COVAriance) 
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
  anova() from the stats library
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/anova.html
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
  f-test for comparing variances of 2 samples: var.test() from the stats package
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/var.test.html 
  """,
  "bartlett's test":
  """Bartlett's Test
  When to use it?
  Bartlett's Test is used to test if any two of multiple samples come from a population with different variances. This can be used to test the assumption of equal variances in other statistical tests.
  Assumption(s):
  - Samples are from populations that are normally distributed
  R-command(s):
  bartletts.test() from the stats package
  https://stat.ethz.ch/R-manual/R-devel/library/stats/html/bartlett.test.html 
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
  Specify pearson in the method for Pearson test. probably want cor.test because it returns confidence intervals)
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
  "multiple linear regression":
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
  """,
  "none": """Sorry, this scenario currently not supported. Possibly, the appropriate test hasn't yet been invented. Consider making some additional assumptions about your data."""
  }

descriptions2 = {
  "logistic regression": "It regresses logistically",
  "linear regression": "It regresses linearly",
  "lasso regression": "It regresses like a lasso",
  "none": "We apologize"
  }
