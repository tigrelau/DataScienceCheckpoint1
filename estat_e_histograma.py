import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('applications.csv')

print(df.head())
df.info()

percentual_nulos = (df.isnull().sum() / len(df)) * 100
print(percentual_nulos)

df_clean = df.dropna(subset=['mat_initial_price', 'name', 'mat_discount_percent'])

print("variável 1 - preço inicial")
s = df_clean['mat_initial_price']

media = s.mean()
mediana = s.median()
moda = s.mode().tolist()
var_amostral = s.var(ddof=1)
dp_amostral = s.std(ddof=1)

print("Média:", media)
print("Mediana:", mediana)
print("Moda(s):", moda)
print("Variância amostral:", var_amostral)
print("DP amostral:", dp_amostral)


plt.hist(s[s < 10000], bins="auto", edgecolor='black')
plt.title("Histograma: Preço inicial")
plt.xlabel("% Desconto")
plt.xlabel("Preço inicial")
plt.ylabel("Frequência")
plt.show()

print("variável 2 - percentual de desconto")
s = df_clean['mat_discount_percent']

media = s.mean()
mediana = s.median()
moda = s.mode().tolist()
var_amostral = s.var(ddof=1)
dp_amostral = s.std(ddof=1)

print("Média:", media)
print("Mediana:", mediana)
print("Moda(s):", moda)
print("Variância amostral:", var_amostral)
print("DP amostral:", dp_amostral)


plt.hist(s[s > 0], bins="auto", edgecolor='black')
plt.title("Histograma: Apenas jogos em promoção")
plt.xlabel("% Desconto")
plt.ylabel("Frequência")
plt.show()