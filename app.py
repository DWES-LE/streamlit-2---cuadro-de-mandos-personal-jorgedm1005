import pandas as pd
import streamlit as st

# Load data

df = pd.read_csv("f1.csv")

#Título de la página

st.title("Campeonato de Fórmula 1")

# Mostramos los datos de la tabla
if st.checkbox('Mostrar todos los datos'):
    st.subheader('Todos los datos:')
    st.write(df)

# Definimos la interfaz de usuario usando Streamlit para recoger el nombre del circuito
st.title("INFO SOBRE EL CIRCUITO")
st.write("Selecciona un circuito para saber de él:")

# Creamos un widget de selección de menú desplegable para el nombre del circuito
circuit = st.selectbox('Circuito seleccionado', df['name'].unique())

# Filtramos los datos para mostrar solo los datos del circuito seleccionado
filtered_data = df[df['name'] == circuit]

# Mostramos los datos del circuito seleccionado
st.write(filtered_data)

# Hacemos que el usuario pueda filtrar los campeonatos por año

st.subheader("Filtro por año")

# Crear widget de entrada de texto para el año
year = st.text_input('Introduzca el año para filtrar: ')

# Verificar que el valor de entrada no está vacío
if year != '':
    # Filtrar datos por año
    filtered_data = df[df['year'] == int(year)]

    # Mostrar datos filtrados
    st.write(filtered_data)
else:
    # Si el valor de entrada está vacío, mostrar un mensaje de error
    st.write('Introduce un valor válido')

# Hago un gráfico de barras para saber los campeonatos celebrados en cada circuito

st.subheader("Cantidad de campeonatos por circuito")

datos=(df.groupby("name").count()["year"].sort_values(ascending=False))

st.bar_chart(datos)
