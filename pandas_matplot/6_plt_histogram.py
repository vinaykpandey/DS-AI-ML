from matplotlib import pyplot as plt

test = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
marks_of_1 = [64, 55, 77, 80, 58, 61, 68, 74, 77, 70]

# grouping of ranged data  bar is Histogram
bins = [0, 30, 60, 75, 100]
plt.hist(marks_of_1, bins, histtype="bar", rwidth=1, color="cyan")
plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Test Score")
plt.show()
