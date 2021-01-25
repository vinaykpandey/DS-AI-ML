from matplotlib import pyplot as plt

test = (1, 2, 3, 4, 5)
marks_of_1 = [67, 55, 77, 80, 78]
marks_of_2 = [60, 59, 74, 83, 71]
plt.plot(test, marks_of_1, label="Vin")
plt.plot(test, marks_of_2, label="Dev")
plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Test Score")
plt.legend()
plt.show()
