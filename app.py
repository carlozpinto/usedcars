import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Paso 4: Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de mando de anuncios de venta de coches')

# --- SECCIÓN DE HISTOGRAMA ---
# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Lógica al hacer clic
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear histograma con graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE GRÁFICO DE DISPERSIÓN ---
# Agregar otro botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre el kilometraje (odómetro) y el precio')

    # Crear scatter plot con graph_objects
    fig_scatter = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                             y=car_data['price'],
                                             mode='markers')])
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
