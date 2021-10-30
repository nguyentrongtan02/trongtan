import matplotlib.pyplot as plt
import numpy as np
divisions = ["Python","PHP","CSS","JAVA","C++"]
divisions_average_marks = [92,76,9,67,51]
plt.bar(divisions, divisions_average_marks,color='pink')
plt.title("Bar Graph")
plt.xlabel("ngôn ngữ lập trình")
plt.ylabel("tỷ lệ")
plt.show()