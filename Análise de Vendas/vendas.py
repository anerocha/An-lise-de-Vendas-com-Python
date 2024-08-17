import pandas as pd

# Carregar os dados
df = pd.read_csv('vendas.csv')

# Visualizar os primeiros dados
print(df.head())

# Calcular o total de vendas (Quantidade * Preço)
df['Total'] = df['Quantidade'] * df['Preco']

# Total de vendas
total_vendas = df['Total'].sum()
print(f"Total de vendas: R${total_vendas:.2f}")

# Produto mais vendido
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print(f"Produto mais vendido: {produto_mais_vendido}")

# Faturamento mensal (supondo que temos dados de diferentes meses)
df['Data'] = pd.to_datetime(df['Data'])
faturamento_mensal = df.groupby(df['Data'].dt.to_period('M'))['Total'].sum()
print("Faturamento mensal:")
print(faturamento_mensal)