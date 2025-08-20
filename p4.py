# Mini Project 4: Using Seaborn for Statistical Visualization

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {"Age": [22, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)

# Plot a histogram with KDE (Kernel Density Estimate)
sns.histplot(df["Age"], bins=5, kde=True, color="skyblue")

# Add labels and title
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Ages with KDE")

# Show the plot
plt.show()

