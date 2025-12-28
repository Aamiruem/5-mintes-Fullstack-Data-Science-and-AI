# Here is your 4️⃣ Temperature Line Chart program using Matplotlib
# (uses Line Plot, Markers, Grid, Pyplot exactly as asked) 📈

# 🧑‍💻 Python Code
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [28, 30, 29, 31, 32, 33, 34]

# Plot
plt.plot(days, temperatures, marker='o', linewidth=2)

# Title and labels
plt.title("Weekly Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Grid
plt.grid(True)

# Show graph
plt.show()

# 🧠 Concepts Used
# Requirement	Implemented
# Line Plot	plt.plot()
# Circular Markers	marker='o'
# Line Width	linewidth=2
# Title	plt.title()
# X & Y Labels	plt.xlabel(), plt.ylabel()
# Grid	plt.grid(True)
# Pyplot	import matplotlib.pyplot as plt
# 🧪 What the graph shows

# A clear rising temperature trend from 28°C → 34°C over 7 days with visible circular points and grid lines.
