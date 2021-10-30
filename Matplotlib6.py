import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.title("chiều cao")
plt.xlabel("cân nặng")
plt.ylabel("tỷ lệ suy dinh dưỡng")
plt.hist(x,10)
plt.show()