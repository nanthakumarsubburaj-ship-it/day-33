import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Plot line chart with circle markers and solid line
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Chart")

# Adding grid for better readability
plt.grid(True)

# Show the chart
plt.show()




