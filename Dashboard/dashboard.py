
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np

# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================

st.set_page_config(page_title="LigaPro Dashboard", layout="wide")

sns.set_style("whitegrid")
plt.rcParams["figure.facecolor"] = "#F8F9FA"

st.title("⚽ LigaPro Ecuador – Dashboard Analítico")
st.markdown("Análisis estadístico de jugadores (Datos Limpios y Filtrados)")

# ==================================================
# CARGA Y LIMPIEZA DE DATOS
# ==================================================

df = pd.read_csv("ligapro2020.csv", sep=";")

# Convertir a numérico correctamente
df["edadjugador"] = pd.to_numeric(df["edadjugador"], errors="coerce")
df["alturajugador"] = pd.to_numeric(df["alturajugador"], errors="coerce")
df["pesojugador"] = pd.to_numeric(df["pesojugador"], errors="coerce")

# Eliminar valores inválidos
df = df.dropna(subset=["edadjugador", "alturajugador", "pesojugador"])

# Eliminar DT y alturas menores a 80 cm
df = df[
    (df["roljugador"].str.upper() != "DT") &
    (df["alturajugador"] >= 80)
]

# Calcular IMC
df["imc"] = df["pesojugador"] / ((df["alturajugador"] / 100) ** 2)

# ==================================================
# FILA 1
# ==================================================

col1, col2 = st.columns(2)

# 1️⃣ Barras - Jugadores por Equipo
with col1:
    st.subheader("1️⃣ Jugadores por Equipo")

    conteo = df["nombreequipo"].value_counts().sort_values(ascending=False)

    fig1, ax1 = plt.subplots(figsize=(10,5))
    bars = ax1.bar(conteo.index, conteo.values, color="#1f77b4")

    ax1.set_ylabel("Cantidad de Jugadores")
    ax1.set_xticklabels(conteo.index, rotation=90)
    ax1.set_title("Distribución de Plantillas")

    st.pyplot(fig1)

# 2️⃣ Histograma Edades
with col2:
    st.subheader("2️⃣ Distribución de Edades")

    fig2, ax2 = plt.subplots(figsize=(8,5))
    ax2.hist(df["edadjugador"], bins=12, color="#ff7f0e", edgecolor="black")

    ax2.set_xlabel("Edad")
    ax2.set_ylabel("Cantidad")
    ax2.set_title("Histograma de Edades")

    st.pyplot(fig2)

# ==================================================
# FILA 2
# ==================================================

col3, col4 = st.columns(2)

# 3️⃣ Boxplot Alturas por Rol
with col3:
    st.subheader("3️⃣ Altura por Rol")

    fig3, ax3 = plt.subplots(figsize=(8,5))
    sns.boxplot(
        data=df,
        x="roljugador",
        y="alturajugador",
        palette="Set2",
        ax=ax3
    )

    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    ax3.set_ylabel("Altura (cm)")

    st.pyplot(fig3)

# 4️⃣ Scatter Peso vs Altura
with col4:
    st.subheader("4️⃣ Peso vs Altura")

    fig4, ax4 = plt.subplots(figsize=(8,5))

    roles = df["roljugador"].unique()
    colores = sns.color_palette("husl", len(roles))

    for rol, color in zip(roles, colores):
        subset = df[df["roljugador"] == rol]

        ax4.scatter(
            subset["alturajugador"],
            subset["pesojugador"],
            s=(subset["edadjugador"] * 3),
            alpha=0.6,
            label=rol,
            color=color
        )

    ax4.set_xlabel("Altura (cm)")
    ax4.set_ylabel("Peso (kg)")
    ax4.legend()

    st.pyplot(fig4)

# ==================================================
# FILA 3
# ==================================================

col5, col6 = st.columns(2)

# 5️⃣ IMC por Rol
with col5:
    st.subheader("5️⃣ Distribución de IMC por Rol")

    fig5, ax5 = plt.subplots(figsize=(8,5))
    sns.boxplot(
        data=df,
        x="roljugador",
        y="imc",
        palette="coolwarm",
        ax=ax5
    )

    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45)
    ax5.set_ylabel("IMC")

    st.pyplot(fig5)

# 6️⃣ Heatmap Correlación
with col6:
    st.subheader("6️⃣ Matriz de Correlación")

    corr = df[["edadjugador", "pesojugador", "alturajugador", "imc"]].corr()

    fig6, ax6 = plt.subplots(figsize=(6,5))
    sns.heatmap(
        corr,
        annot=True,
        cmap="Blues",
        fmt=".2f",
        linewidths=0.5,
        ax=ax6
    )

    st.pyplot(fig6)
    # ==================================================
# FILA 4
# ==================================================

st.markdown("---")
st.subheader("7️⃣ Indicadores Generales LigaPro 2020")

# Cálculos KPI
edad_promedio = df["edadjugador"].mean()
edad_minima = df["edadjugador"].min()
edad_maxima = df["edadjugador"].max()

# IMC promedio por rol
imc_promedio_por_rol = df.groupby("roljugador")["imc"].mean()

rol_mayor_imc = imc_promedio_por_rol.idxmax()
valor_mayor_imc = imc_promedio_por_rol.max()

# Crear 4 columnas para los indicadores
k1, k2, k3, k4 = st.columns(4)

k1.metric("Edad Promedio", f"{edad_promedio:.1f} años")
k2.metric("Edad Mínima", f"{edad_minima:.0f} años")
k3.metric("Edad Máxima", f"{edad_maxima:.0f} años")
k4.metric(
    "Posición con Mayor IMC Promedio",
    rol_mayor_imc,
    f"IMC: {valor_mayor_imc:.2f}"
)