# Using statsmodels for Linear Regression
import statsmodels.api as sm

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Add constant term for intercept
X = sm.add_constant(x)

# Fit Ordinary Least Squares (OLS) regression
model = sm.OLS(y, X).fit()

# Print the regression summary
print(model.summary())
