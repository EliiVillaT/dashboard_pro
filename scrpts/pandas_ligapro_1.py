# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:09:53 2024

@author: info
"""

import pandas as pd

# Cargar los datos
data = pd.read_csv('ligapro2020.csv', delimiter=';')

# Mostrar las primeras 10 filas
print(data.head(10))

print(data.columns)

#Entender el archivo con shape, dtypes, info
data.shape
data.dtypes

data.info()

# Convertir 'nacimientojugador' a datetime
data['nacimientojugador'] = pd.to_datetime(data['nacimientojugador'])


#Algo de limpieza de datos
data['nacimientojugador']

data.iloc[35,0]

data.head(40)

data[data['nacimientojugador'] == "[Table]"]

data_fecha = data[data['nacimientojugador'] != "[Table]"]

# Convertir 'nacimientojugador' a datetime
data_fecha['nacimientojugador'] = pd.to_datetime(data_fecha['nacimientojugador'])

data_fecha.dtypes

# Convertir 'edadjugador' a entero
data_fecha['edadjugador'] = data_fecha['edadjugador'].astype(int)

data_fecha.dtypes

#Edad promedio
promedio_edad = data_fecha["edadjugador"].mean()

print("La edad promedio de los jugadores de la LigaPro 2020 es:",round(promedio_edad,0))

# Altura y peso promedio
altura_promedio = data['alturajugador'].mean()
peso_promedio = data['pesojugador'].mean()
print(f"Altura promedio: {altura_promedio:.2f} cm, Peso promedio: {peso_promedio:.2f} kg")

# Equipos únicos
print(data)
equipos_unicos = data['nombreequipo'].unique()
print(f"Equipos únicos: {list(equipos_unicos)}")

numero_equipos_unicos = data['nombreequipo'].nunique()
print(f"Equipos únicos: {(numero_equipos_unicos)}")

# Or rename the existing DataFrame (rather than creating a copy)
data['nombreequipo'] = data['nombreequipo'].replace('Delf?n', 'Delfín')
data['nombreequipo'].unique()

#reemplazar Macará - Técnico Universitario - U.Católica 
data['nombreequipo'] = data['nombreequipo'].replace('Macar?','Macará')
data['nombreequipo'].unique()

data['nombreequipo'] = data['nombreequipo'].replace('T?cnicoUniversitario','TécnicoUniversitario')
data['nombreequipo'].unique()

data['nombreequipo'] = data['nombreequipo'].replace('U.Cat?lica(E)', 'U.Católica')
data['nombreequipo'].unique()


# Rol más común
rol_comun = data['roljugador'].mode()[0]
print(f"Rol más común: {rol_comun}")

