import numpy as np
import matplotlib.pyplot as plt

index = np.array([1, 2, 3, 4, 5])
means_men = np.array([20, 35, 30, 35, 27])
means_women = np.array([25, 32, 34, 20, 25])
bar_width = 0.35

plt.bar(index, means_men, bar_width, color="b", label="Men")
plt.bar(index + bar_width, means_women, bar_width, color="r", label="Women")

plt.xticks([1, 2, 3, 4, 5],["A", "B", "C", "D", "E"])
plt.legend()

plt.savefig("Barchart.png")
plt.show()
