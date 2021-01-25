from matplotlib import pyplot as plt

from functools import reduce


def avg(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


days = (1, 2, 3, 4, 5, 6, 7)
sleep = [7.5, 8.2, 8.1, 7.2, 7.6, 6.50, 8.2]
study = [5, 4, 3, 5, 4, 5, 3]
phone = [4, 3, 4, 5, 2, 3, 4]
workout = [1, 2, 2, 1, 2, 1, 1]
other = [3, 4, 3, 2, 4, 3, 2]
hrs = [avg(sleep), avg(study), avg(phone), avg(workout), avg(other)]
lbs = ("Sleep", "Study", "phone", "workout", "other")
plt.pie(hrs, labels=lbs, explode=(0, .1, 0, 0, .1), autopct="%2.1f%%")
plt.xlabel("Days")
plt.ylabel("Activity")
plt.title("Day wise Activity")
# plt.legend()
plt.show()
