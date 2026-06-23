import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("world_population.csv - Copy - Copy.csv")
top_10 = df.sort_values(by="2022 Population", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10["Country/Territory"], top_10["2022 Population"])

plt.title("Top 10 Most Populous Countries in 2022")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()