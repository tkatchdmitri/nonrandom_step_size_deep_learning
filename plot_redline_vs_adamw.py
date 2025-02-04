redline = []
adamw = []
# Open the file in read mode
with open('redline.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Strip leading/trailing whitespace (optional)
        line = line.strip()
        # Do something with the line
        # print(line)
        if 'val loss' in line:
            redline.append(float(line.split(' ')[-1]))
# Open the file in read mode
with open('adamw.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Strip leading/trailing whitespace (optional)
        line = line.strip()
        # Do something with the line
        # print(line)
        if 'val loss' in line:
            adamw.append(float(line.split(' ')[-1]))
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

print([x for x in range(0, 5001, 250)])

# Create a plot
plt.plot([x for x in range(0, 5001, 250)], adamw, marker='o')

plt.plot([x for x in range(0, 5001, 250)], redline, marker='x', color='red')

# Add title and labels
plt.title('Redline Versus Adamw')
plt.xlabel('Optimization Step')
plt.ylabel('Loss')

# Show the plot
plt.savefig('redline_vs_adamw.png')