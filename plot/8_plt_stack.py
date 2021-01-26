from matplotlib import pyplot as plt

days = (1, 2, 3, 4, 5, 6, 7)
sleep = [7.5, 8.2, 8.1, 7.2, 7.6, 6.50, 8.2]
study = [5, 4, 3, 5, 4, 5, 3]
phone = [4, 3, 4, 5, 2, 3, 4]
workout = [1, 2, 2, 1, 2, 1, 1]
lbs = ("Sleep", "Study", "phone", "workout")
plt.stackplot(days, sleep, study, phone, workout, labels=lbs)
plt.xlabel("Days")
plt.ylabel("Activity")
plt.title("Day wise Activity")
plt.legend()
plt.show()
