from matplotlib import pyplot as plt
import csv
tests = []
marks = []
with open("pt_data.csv", "r") as fp:
    plots = csv.reader(fp, delimiter=",")
    for row in plots:
        tests.append(int(row[0]))
        marks.append(int(row[1]))

plt.plot(tests, marks)
plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Test Score")
plt.show()
