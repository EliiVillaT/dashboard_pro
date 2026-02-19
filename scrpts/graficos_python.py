# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:50:33 2024

@author: info
"""

import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
data = pd.read_csv('ligapro2020.csv', delimiter=';')

# Histograma de edades
plt.figure(figsize=(10, 6))
plt.hist(data['edadjugador'], bins=10, color='blue', alpha=0.7)
plt.title('Histograma de Edades de los Jugadores')
plt.xlabel('Edad')
plt.ylabel('Número de Jugadores')
plt.grid(True)
plt.show()

# Gráfico de barras del número de jugadores por equipo
jugadores_por_equipo = data['nombreequipo'].value_counts()
plt.figure(figsize=(12, 8))
jugadores_por_equipo.plot(kind='bar', color='green')
plt.title('Número de Jugadores por Equipo')
plt.xlabel('Equipo')
plt.ylabel('Número de Jugadores')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
