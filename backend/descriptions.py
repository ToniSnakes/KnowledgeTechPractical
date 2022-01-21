# Recommendations when the dialogue ends
descriptions = {
"chi-square goodness of fit test": """When to use it?
The Chi-square goodness of fit test is a statistical hypothesis test used to determine whether a variable is likely to come from a specified distribution or not. It is often used to evaluate whether sample data is representative of the full population.
Assumption(s):
- Sample data is a random selection of population data. 
- There are a sufficient number of observations for each category. 
R-command(s):""",
"logistic regression":
"""When to use it?
Use it when you want to know the probability of the dependent variable given an input.
Assumptions:
- Observations independent
- little multicollinearity of independent variables
- large sample size (in function of the number of indep vars)
- Errors independent
R-command(s):""",
"chi-square test for independence":
"""Use this test to determine whether or not two categorical variables are related.
Assumption(s):
- Data should be frequencies or counts. 
- Categories are mutually exclusive, meaning an observation cannot belong to multiple categories. 
R-command(s):""",
"t-test (one-sample)":
"""When to use it?
Use it to determine if a single unknown population mean is statistically different from a specific numerical value.
Assumption(s):
- Data is independent, continuous, and randomly sampled from the target population
R-command(s):""",
"z-test":
"""When to use it?
Use it to determine if the mean of the population is different from a value (one-sample) or different from a second sample. 
Assumption(s):
- Underlying data is normally distributed
- There are a big number of datapoints to evaluate (> 30)
R-command(s):""",
"difference of two means (paired)":
"""When to use it?
Use it to test whether the difference of the means of two populations differ, or differ in a specific manner.
Assumption(s):
- Observations between subjects are independent. 
- Measurements are paired
- Sensitive to outliers
- Normality
R-command(s):""",
"levene's test":
"""When to use it?
Us it to test if at least two of many samples come from populations with unequal variances. It can be used to verify the assumption of equal variances for other statistical tests. It does not assume normality of the populations.
Assumption(s):
- Independent observations
R-command(s):""",
"wilcoxon signed rank test":
"""When to use it?
Use this to test if the medians from two indpendent samples are equal to a given value.
Assumption(s):
- Data needs to be ranked
R-command(s):""",
"wilcoxon matched-pairs signed rank test":
"""When to use it?
Use it to test if the median from from two paired samples are equal to a given value.
Assumption(s):
- none, since non-parametric
R-command(s):""",
"moods median":
"""When to use it?
Use it to test for a difference in medians of two or more independent samples.
Assumption(s):
- Samples are independent
- Sensitive to sample size. Should be used on smaller samples.
R-command(s):""",
"student's t-test":
"""When to use it?
Use the Student's t-test to test the means of two populations.
Assumption(s):
- normality of the populations
- variance of the 2 populations is equal
- sample sizes are equal
R-command(s):""",
"welch's t-test":
"""When to use it?
Use to compare the means when the variance is unknown.
Assumption(s):
- normality of the data
R-command(s):""",
"mann whitney u test (wilcoxon rank sum test)":
"""When to use it?
Use it to compare the mean of a sample.
Assumption(s):
- Independence of observations
- Independent variable has two independent, categorical groups. 
- The observation groups need to follow the same basic shape (e.g., skewed right)
- Dependent variable should be ordinal or continuous
R-command(s):""",
"t-test (paired sample)":
"""When to use it?
Use it to test whether the means of paired data differ. 
Assumption(s):
- Normally distributed
- Paired sample data
R-command(s):""",
"one-way anova":
"""When to use it?
Use it to compare the means of three or more samples, and there is one independent variable.
Assumption(s):
- Normality of population
- Variance is equal 
- Samples are independent
R-command(s):""",
"kruskal-wallis test":
"""When to use it?
Use this non-parametric test to determine whether three or more samples have the same mean.
Assumption(s):
- Variance is equal 
- Samples are independent
R-command(s):
""",
"ancova":
"""When to use it?
Use it to compare the means of the dependent variable over different levels of the categorical independent variables. 
dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: More than two samples, one measurement (q3), iv types: A categorical and a numerical IV (q11)
Assumption(s):
- A linear relationship between dependent variable and covariates.
R-command(s):
""",
"n-way anova (factorial anova)":
"""When to use it?
Use it to test the means when your dependent variable has more than one dependent variable and two or more independent variables. Similar to one-way ANOVA, the n-way ANOVA test includes multiple independent variables and their interaction terms.
Assumption(s):
- No multicolinearity (variables are not linear combinations of each other)
- Dependent variable is interval data
- Normally distributed dependent variable
- Homoscedasticity
R-command(s):""",
"repeated measures anova":
"""When to use it?
dv type continuous, goal: compare statistics (e.g. means, variances) between samples / groups (q4), statistics goal: mean (q8), situation: One sample, more than two measurements (q3), DV Normally distributed: true (q5)
Assumption(s):
R-command(s):
""",
"friedman":
"""When to use it?
Use it to compare means of one sample measured three or more times. 
Assumption(s):
- Three or more measurements of data, so the data is “matched”
R-command(s):
""",
"f-test":
"""When to use it?
Compare the means of two samples. It is can be more powerful that the t-test when the variance is known.
Assumption(s):
- Normally distributed dependent variable
R-command(s):""",
"bartlett's test":
"""When to use it?
Use it to test if any two of multiple samples come from a population with different variances. This can be used to test the assumption of equal variances in other statistical tests.
Assumption(s):
- Samples are from populations that are normally distributed
R-command(s):""",
"pearson correlation":
"""When to use it?
Use it to test the correlation between two independent variables.
Assumption(s):
- Each variable should be continuous 
- Observations should be paired and not-missing 
- Linearity of the variables, checkable by scatterplot
- Absence of outliers
R-command(s):""",
"simple linear regression":
"""When to use it?
Use it to quantify the relationship between a single independent variable and a dependent variable.
Assumption(s):
- Homoscedasticity (the variance of the residuals are constant)
- DV is normally distributed and continuous. Observations are independent
R-command(s):""",
"multiple linear regression":
"""When to use it? 
Use it if your DV is continuous and the range is -inf to inf. It is often used as a baseline regression for when you have a more complicated model, to compare results.
Assumption(s):
- Homoscedasticity (the variance of the residuals are constant)
- DV is normally distributed and continuous. Observations are independent
- The independent variables are not linear combinations of each other
R-command(s):""",
"lasso regression":
"""When to use it?
Use it to quantify a relationship between multiple independent variables. It is similar to linear regression, however, it is used when it is suspected that not all independent variables are necessary in a model. It uses shrinkage to reduce the coefficients to zero, in that case. 
Assumption(s):
- Homoscedasticity
- Linear relationship between independent variables
- Sensitive to outliers.
R-command(s):""",
"spearman correlation":
"""When to use it?
Spearman correlation is used to test if there is a monotonic relationship between ranked variables. For example, it can be used to test a relationship in a contingency table of whether education level (high school, university, graduate degree) is related to income (low, medium, high). 
Assumptions:
- Ranked (positive and discrete) dependent variable
R-command(s):""",
"none": """Sorry, this scenario currently not supported. Possibly, the appropriate test hasn't yet been invented. Consider making some additional assumptions about your data."""
}

# Recommendations when the dialogue ends
r = {
"chi-square goodness of fit test": """chisq.test(.)
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html""",
"logistic regression":
"""glm(., family=binomial)
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html""",
"chi-square test for independence":
"""chisq.test(.)
More information under:
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/chisq.test.html
""",
"t-test (one-sample)":
"""t.test(x, y=NULL, mu=value_of_interest) from the stats library
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html""",
"z-test":
"""z.test from the BSDA library
https://rdrr.io/cran/BSDA/man/z.test.html
Currently, no built-in function exists""",
"difference of two means (paired)":
"""t.test(x, y, paired = TRUE, alternative = "two.sided") 
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html""",
"levene's test":
"""leveneTest() from the car library 
https://search.r-project.org/CRAN/refmans/car/html/leveneTest.html""",
"wilcoxon signed rank test":
"""wilcox.test() from the stats library
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html""",
"wilcoxon matched-pairs signed rank test":
"""wilcox.test() from the stats library
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html""",
"moods median":
"""mood.medtest() from the RVAideMemoire library.
https://search.r-project.org/CRAN/refmans/RVAideMemoire/html/mood.medtest.html""",
"student's t-test":
"""t.test in the stats library. 
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html""",
"welch's t-test":
"""t.test from the stats package but var.equal has to be set to FALSE. 
t.test(x, y, paired = FALSE, var.equal=FALSE)
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html""",
"mann whitney u test (wilcoxon rank sum test)":
"""wilcox.test() in stats library 
arguments: paired = TRUE, alternative = “two.sided”""",
"t-test (paired sample)":
"""t.test() from the stats package with paired=TRUE
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html""",
"one-way anova":
"""aov() from the stats library.
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aov.html """,
"kruskal-wallis test":
"""kruskal.test() from the stats package 
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/kruskal.test.html""",
"ancova":
"""aov() followed by Anova() in the car library""",
"n-way anova (factorial anova)":
"""anova() from the stats library
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/anova.html""",
"repeated measures anova":
"""aov() followed by nova() from the car library""",
"friedman":
"""friedman.test() in the stats package
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/friedman.test.html""",
"f-test":
"""f-test for comparing variances of 2 samples: var.test() from the stats package
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/var.test.html """,
"bartlett's test":
"""bartletts.test() from the stats package
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/bartlett.test.html 
""",
"pearson correlation":
"""cor(x, y, method = c("pearson")) or cor.test(x, y, method = c("pearson"))
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/cor.html
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/cor.test.html""",
"simple linear regression":
"""lm()
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html""",
"multiple linear regression":
"""lm()
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html""",
"lasso regression":
"""glmnet() using family=gaussian and alpha=1 for lasso.
https://cran.r-project.org/web/packages/glmnet/glmnet.pdf""",
"spearman correlation":
"""cor.test with method = “spearman”
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/cor.test.html""",
"none": """"""
}
