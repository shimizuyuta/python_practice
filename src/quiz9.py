from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('./data/平均気温.csv')
df.plot(x="月", y="平均気温",marker='o')
plt.grid()
plt.ylabel('度',rotation=0)
plt.title('2021年の平均気温')
plt.show()
plt.savefig('グラフ.png')