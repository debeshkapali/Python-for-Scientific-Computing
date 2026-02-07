"""
Simple data analysis practice
Learning basic Python for scientific computing
"""

# Basic statistics function
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Some sample data - test scores
scores = [85, 92, 78, 90, 88, 76, 95, 82]

print("Test Scores:", scores)
print("Number of tests:", len(scores))

# Calculate average
average = calculate_average(scores)
print(f"Average score: {average:.2f}")

# Find high and low scores using loops and conditionals
high_scores = []
low_scores = []

for score in scores:
    if score >= 85:
        high_scores.append(score)
    else:
        low_scores.append(score)

print(f"\nHigh scores (>=85): {high_scores}")
print(f"Low scores (<85): {low_scores}")

# Write results to a file
with open('results.txt', 'w') as f:
    f.write("Test Score Analysis\n")
    f.write(f"Average: {average:.2f}\n")
    f.write(f"Highest: {max(scores)}\n")
    f.write(f"Lowest: {min(scores)}\n")

print("\nResults saved to results.txt")
