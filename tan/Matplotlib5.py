import matplotlib.pyplot as plt
import numpy as np
firms = ["HTML/CSS","JAVA","PYTHON","RUBY","Khác"]
market_share = [25,20,15,10,5]
Explode = [0,0.1,0,0,0]
plt.pie(market_share,explode=Explode,labels=firms,shadow=True,startangle=45)
plt.axis('equal')
plt.legend(title="tỷ lệ việc làm ở Việt Nam")
plt.show()