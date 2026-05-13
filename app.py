import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Flavia Valencia")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión1")
  st.image ("Python_logo.png")

