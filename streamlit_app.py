import streamlit as st

st.title("🎈 Mi aplicacion")
st.write(
    "Esto es una aplicacion de prueba")

st.header("Esto es una cabecera")

cantidad = st.slider("Elija un valor")

print(f'El identificador de cantidad es {id(cantidad)}')

for i in range(cantidad):
    st.button(f'boton {i}')
    st.checkbox(f'Opcion {i}')
    