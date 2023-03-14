# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:32:32 2021


Gráficos da base de dados da BU:
    MP10, Temperatura, Umidade no mesmo gráfico
    - Titulo, cores, legenda, nome dos eixos, valores nos eixos,


@author: Gabriel Ratão
"""


#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% lendo o arquivo da BU e já tirando as linhas nulas


df_bu = pd.read_excel(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\MP10_BU.xlsx')

df_bu = df_bu.dropna()

#%%

for coluna in df_bu.columns:
    print(coluna)
    
    
#%% definindo as medias de Temperatura, Umidade, MP10 para plotar diretamente
#por numpy
 
#criando uma matriz numpy com os valores de MP10
mp10 = np.array(df_bu['MP10'])

#vamos criar uma matriz com n linhas onde n é o numero total de dados que tem MP10
# e cada linha vai ter o valor de sua media
media_MP10 = [np.mean(mp10)] * len(mp10)  

    
temperatura = np.array(df_bu['TEMPERATURE'])
media_temperatura = [np.mean(temperatura)] * len(temperatura)
    
umidade = np.array(df_bu['HUMIDITY'])
media_umidade = [np.mean(umidade)] * len(umidade)


#%% criando os gráficos

plt.subplot(3, 1, 1)


plt.plot(df_bu['TEMPERATURE'], label = 'Temperatura', color = 'red')
plt.plot(media_temperatura, color = 'black', label= 'Média') #adicionando a linha reta da media
plt.ylabel('°C      ', rotation = 0)

plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df_bu['HUMIDITY'], label = 'Umidade', color = 'blue')
plt.plot(media_umidade, color = 'black', label= 'Média')
plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.ylabel('%', rotation = 0)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df_bu['MP10'], label = 'MP10', color = 'green')
plt.plot(media_MP10, color = 'black', label= 'Média')
plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.ylabel('ug/m³        ', rotation = 0)
plt.legend(loc='lower left')

plt.suptitle('Análise Temperatura, Umidade, MP10 na BU \n 2014-2019')
plt.show()


