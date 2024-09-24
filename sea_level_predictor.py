import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Carregar os dados do arquivo CSV
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Criar gráfico de dispersao
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', marker='o', label='Dados')

    # Primeira linha de regressão (usando todos os dados)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    print(f"A inclinação é {slope}") #inclinacao da linha de regressao
    
    # Criando valores previstos para a linha de regressão até 2050
    years_extended = np.arange(df['Year'].min(), 2051)
    #Calculando os valores previstos utilizando a formula da linha de regressao
    sea_level_pred = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_pred, color='red', label='Linha de Ajuste 1')

    # Segunda linha de regressão (a partir do ano 2000)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = np.arange(2000, 2051)
    sea_level_pred_2000 = slope_2000 * years_extended_2000 + intercept_2000
    plt.plot(years_extended_2000, sea_level_pred_2000, color='green', label='Linha de Ajuste 2 (a partir de 2000)')

    # Adicionar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Salvar e exibir o gráfico
    plt.savefig('sea_level_plot.png')
    plt.show()
    
    return plt.gca()

# Chamar a função para desenhar o gráfico
draw_plot()