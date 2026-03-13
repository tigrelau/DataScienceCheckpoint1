import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('applications.csv')

print("Preço Lançamento x Desconto")
df_par1 = df.dropna(subset=['mat_initial_price', 'mat_discount_percent'])
x1 = df_par1['mat_initial_price']
y1 = df_par1['mat_discount_percent']


corr1 = x1.corr(y1)
print("Correlação de Pearson (Par 1):", corr1)

plt.scatter(x1, y1, alpha=0.5)
plt.title("Scatterplot: Preço Lançamento vs Desconto")
plt.xlabel("Preço inicial")
plt.ylabel("% Desconto")
plt.show()
plt.show()


print("Crítica x Recomendações")
df_par2 = df.dropna(subset=['metacritic_score', 'recommendations_total'])
x2 = df_par2['metacritic_score']
y2 = df_par2['recommendations_total']

corr2 = x2.corr(y2)
print("Correlação de Pearson (Par 2):", corr2)

plt.scatter(x2, y2, alpha=0.5)
plt.title("Scatterplot: Crítica vs Recomendações")
plt.xlabel("Crítica")
plt.ylabel("Recomendações")
plt.show()