# Using SciPy for Scientific Computation
from scipy import stats
import numpy as np

# Sample data
data = [10, 20, 30, 30, 40, 50]

# Mean
print("Mean:", np.mean(data))

# Median
print("Median:", np.median(data))

# Mode (SciPy mode function returns a ModeResult object)
mode_result = stats.mode(data, keepdims=True)  # keepdims=True ensures compatibility
print("Mode:", mode_result.mode.item())        # Convert to scalar using .item()
