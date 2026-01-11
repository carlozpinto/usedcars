import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Cargar csv
df = pd.read_csv('vehicles_us.csv')

# Pasos de limpieza
df['model_year'] = df['model_year'].fillna(
    df['model_year'].median()).astype(int)
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].median()).astype(int)
df['odometer'] = df['odometer'].fillna(df['odometer'].median()).astype(int)
df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)


# Título de la página
st.header('Cuadro de mando de anuncios de venta de coches')

# --- SECCIÓN DE HISTOGRAMA ---
st.write('### Distribución del Kilometraje')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Usando graph_objects
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE GRÁFICO DE DISPERSIÓN ---
st.write('### Relación entre Kilometraje y Precio')
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el kilometraje (odómetro) y el precio')
    # Usando graph_objects
    fig_scatter = go.Figure(data=[go.Scatter(
        x=df['odometer'],
        y=df['price'],
        mode='markers'
    )])
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)
