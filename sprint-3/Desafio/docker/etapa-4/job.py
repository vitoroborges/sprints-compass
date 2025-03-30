
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('input/csv_limpo.csv')

# Questão 1

appear_most_and_most_total_gross = df.loc[(df['Artist'].value_counts().max()) & (df['Actual gross'].max())]
q1 = pd.DataFrame({
    "Métrica": ["Artista mais frequente", "Maior Bilheteria"],
    "Valor": [appear_most_and_most_total_gross['Artist'], appear_most_and_most_total_gross['Actual gross']]
})

print(q1)

#Questão 2

single_year_turne = df.loc[(df['Start Year'] == df['End Year'])]

max_average_gross_tour_by_year = single_year_turne.loc[single_year_turne['Average gross'].idxmax()]

q2 = pd.DataFrame({
    "Métrica": ["Artista", "Nome do Tour", "Lucro Médio"],
    "Valores": [max_average_gross_tour_by_year['Artist'], max_average_gross_tour_by_year['Tour title'], max_average_gross_tour_by_year['Average gross']]
})
print(q2)

# Questão 3

df['Adjusted average per show'] = df['Adjustedgross (in 2022 dollars)'] / df['Shows']

top_3_most_profitable_per_show = df.sort_values('Adjusted average per show', ascending=False).head(3)

q3 = top_3_most_profitable_per_show[['Artist', 'Tour title', 'Start Year', 'Adjusted average per show']]

print(q3)

# Escrita das respostas

with open('output/respostas.txt', 'w') as file:
    file.writelines(f'Q1:\n\n{q1.to_string(index=False)}\n\nQ2:\n\n{q2.to_string(index=False)}\n\nQ3:\n\n{q3.to_string(index=False)}')


# Questão 4

taylor_swift = df.loc[df['Artist'] == 'Taylor Swift'].copy()

yearly_gross = taylor_swift.groupby('Start Year')['Actual gross'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(yearly_gross['Start Year'], yearly_gross['Actual gross'], marker='o', color='#1DA1F2', linewidth=2.5, markersize=8, markerfacecolor='red')
plt.title('Evolução do Faturamento das Turnês da Taylor Swift', fontsize=14, pad=20)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Faturamento Bruto (USD)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.gca().yaxis.set_major_formatter('${x:,.0f}')

for x,y in zip(yearly_gross['Start Year'], yearly_gross['Actual gross']):
    plt.text(x, y, f'${y/1e6:.0f}M', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('output/Q4.png')
plt.show()
plt.close()

# Questão 5

top_5_artists_with_most_shows = df.groupby('Artist')['Shows'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,5))
bars = plt.bar(top_5_artists_with_most_shows.index, top_5_artists_with_most_shows.values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

plt.title('Top 5 Artistas com Mais Shows', fontsize=16, pad=20)
plt.xlabel('Artista', fontsize=12)
plt.ylabel('Número Total de Shows', fontsize=12)
plt.xticks(fontsize=10)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('output/Q5.png')
plt.show()
plt.close()
