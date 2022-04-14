from matplotlib import pyplot as plt

year = list(range(2011, 2020))
res = [128, 119, 229, 308, 270, 300, 382, 193, 264]

plt.bar(year, res)
plt.xlabel(year)
plt.show()
