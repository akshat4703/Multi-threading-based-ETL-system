import matplotlib.pyplot as plt

# Replace these values with actual execution times from your scripts
execution_times = {
    "One-by-One": 5.23,    # Example time in seconds
    "Import/Export": 2.89,
    "Multithreading": 1.34
}

# Extract keys (methods) and values (execution times)
methods = list(execution_times.keys())
times = list(execution_times.values())

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(methods, times, color=['red', 'blue', 'green'])

# Add labels and title
plt.xlabel("ETL Methods")
plt.ylabel("Execution Time (seconds)")
plt.title("Comparison of ETL Methods Execution Time")
plt.ylim(0, max(times) + 1)  # Adjust y-axis for better visibility
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show values on top of bars
for i, v in enumerate(times):
    plt.text(i, v + 0.1, str(v), ha='center', fontsize=12)

# Show the graph
plt.show()
