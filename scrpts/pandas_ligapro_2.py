# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:12:51 2024

@author: info
"""

import pandas as pd

# Cargar los datos
data = pd.read_csv('ligapro2020.csv', delimiter=';')

# Mostrar las primeras 10 filas
print(data.head(10))

#Entender el archivo con shape, dtypes, info
data.info()

# Convertir 'nacimientojugador' a datetime
data['nacimientojugador'] = pd.to_datetime(data['nacimientojugador'])

# Convertir 'edadjugador' a entero
data['edadjugador'] = data['edadjugador'].astype(int)

#Cambio el tipo de dato ID a caracter
data["idJugador"] = data["idJugador"].astype("str")
data["idequipo"] = data["idequipo"].astype("str")

#Algo de limpieza de datos
data['nacimientojugador']

data.iloc[35,0]

data.head(40)

data[data['nacimientojugador'] == "[Table]"]

data_fecha = data[data['nacimientojugador'] != "[Table]"]

# Convertir 'nacimientojugador' a datetime
data_fecha['nacimientojugador'] = pd.to_datetime(data_fecha['nacimientojugador'])

# Convertir 'edadjugador' a entero
data_fecha['edadjugador'] = data_fecha['edadjugador'].astype(int)

data_fecha.info()

#Edad promedio
promedio_edad = data_fecha["edadjugador"].mean()

print("La edad promedio de los jugadores de la LigaPro 2020 es:", round(promedio_edad,2))

# Altura y peso promedio
altura_promedio = data['alturajugador'].mean()
peso_promedio = data['pesojugador'].mean()
print(f"Altura promedio: {altura_promedio:.2f} cm, Peso promedio: {peso_promedio:.2f} kg")

################################ LO NUEVO ################################################
# Equipos únicos
equipos_unicos = data['nombreequipo'].unique()
print(f"Equipos únicos: {list(equipos_unicos)}")

# Or rename the existing DataFrame (rather than creating a copy)
data['nombreequipo'] = data['nombreequipo'].replace('Delf?n', 'Delfín')

#reemplazar Macará - Técnico Universitario - U.Católica 


# Rol más común
rol_comun = data['roljugador'].mode()[0]
print(f"Rol más común: {rol_comun}")


# Filtrar jugadores con peso mayor a 80 kg
jugadores_pesados = data[data['pesojugador'] > 80]

#Filtrar los jugadores con peso mayor al promedio


# Seleccionar columnas específicas
resultado = jugadores_pesados[['nombreequipo', 'roljugador', 'paisjugador']]
print(resultado)

# Agrupar por 'roljugador' y calcular la altura media
altura_media_por_rol = data.groupby('roljugador')['alturajugador'].mean()
print(altura_media_por_rol)

# Agrupar por 'nombreequipo' y encontrar el peso máximo y mínimo
peso_stats_por_equipo = data.groupby('nombreequipo')['pesojugador'].agg(['max', 'min'])
print(peso_stats_por_equipo)

# Identificar columnas con datos faltantes
print(data.isnull().sum())

# Rellenar datos faltantes
data['pesojugador'].fillna(altura_promedio, inplace=True)
data['alturajugador'].fillna(peso_promedio, inplace=True)

# Crear nueva columna basada en condiciones
data['paisjugador'].value_counts()

data['origen_jugador'] = data['paisjugador'].apply(lambda x: 'Ecuador' if x == 'Ecuador' else 'Otro país')
print(data[['paisjugador', 'origen_jugador']].head())

#Sacar el promedio de altura por equipo, por posición y que sean extranjeros

extranjero = data[data["origen_jugador"]=="Otro país"].groupby(["nombreequipo","roljugador"])["alturajugador"].mean()
extranjero.columns
type(extranjero)
extranjero

extranjero = data[data["origen_jugador"]=="Otro país"].groupby(["nombreequipo","roljugador"])["alturajugador"].mean().reset_index()
extranjero.columns
type(extranjero)
extranjero

#Sacar el promedio de altura por equipo, por posición y que sean de Ecuador y elaborar un informe


file_name = "extranjero.xlsx"
extranjero.to_excel(file_name)

