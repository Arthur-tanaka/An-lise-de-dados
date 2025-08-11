import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gastos.csv')

#total gasto
total = df['Valor'].sum()
print(f'Total gasto: R$ {total:.2f}')

print('-='*15)

#total gasto por categoria

gasto_categoria = df.groupby('Categoria')['Valor'].sum()
print(gasto_categoria)

print('-='*15)

#Gráfico de barras

gasto_categoria.plot(kind='bar')
plt.title('Gasto por categoria')
plt.ylabel('Valor (R$)')
plt.show()