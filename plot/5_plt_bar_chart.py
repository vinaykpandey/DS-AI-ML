from matplotlib import pyplot as plt

test = (1, 2, 3, 4, 5)
marks_of_1 = [64, 55, 77, 80, 78]
marks_of_2 = [60, 59, 74, 83, 71]
# plt.bar(test, marks_of_1, label="Vin")
# plt.bar(test, marks_of_2, label="Dev")
plt.bar([i + 0.1 for i in test], marks_of_1, width=0.2, label="Dev")
plt.bar([i - 0.1 for i in test], marks_of_2, width=0.2, label="Dev")

# plt.plot(test, marks_of_1)
# plt.plot(test, marks_of_2)

plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Test Score")
plt.legend()
plt.show()
