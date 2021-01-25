from matplotlib import pyplot as plt

test = (1, 2, 3, 4, 5)
marks_of_1 = [64, 55, 77, 80, 78]
marks_of_2 = [60, 59, 74, 83, 71]
plt.scatter(test, marks_of_1, label="Vin", color="b", marker="*")
plt.scatter(test, marks_of_2, label="Dev", edgecolors="c", s=30)
plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Test Score")
plt.legend()
plt.show()
