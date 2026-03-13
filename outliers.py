import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('applications.csv')

df_valid = df.dropna(subset=['mat_initial_price'])
s = df_valid['mat_initial_price']


plt.figure(figsize=(6, 4))
plt.boxplot(s, vert=True, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
plt.ylabel("Preço Inicial")
plt.title("Boxplot ANTES da remoção: Preço Inicial")
plt.tight_layout()
plt.show()

q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1

low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr

mask = (s < low) | (s > high)
s_sem_outliers = s[~mask]

print("Limite Inferior (Tukey):", low)
print("Limite Superior (Tukey):", high)
print("Total de outliers encontrados:", mask.sum())

plt.figure(figsize=(6, 4))
plt.boxplot(s_sem_outliers, vert=True, patch_artist=True, boxprops=dict(facecolor='lightyellow'))
plt.ylabel("Preço Inicial")
plt.title("Boxplot DEPOIS da remoção (IQR): Preço Inicial")
plt.tight_layout()
plt.show()