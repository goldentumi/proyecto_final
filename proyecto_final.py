# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:58:13 2024

@author: gaby-
"""

import streamlit as st
import pandas as pd

# Cargar los archivos de datos
verbos = pd.read_excel('verbos.xlsx', sheet_name='Hoja 1')
quechua = pd.read_excel('quechua.xlsx')

# Cargar todas las hojas del archivo excel
excel_file = pd.ExcelFile('quechua.xlsx')
D = {}
for hoja in excel_file.sheet_names:
    df = pd.read_excel('quechua.xlsx', sheet_name=hoja)
    c = df.columns
    df.set_index(c[0], inplace=True)
    d = df.to_dict()
    D[hoja] = d

# Diccionario de pronombres
pronombre = pd.read_excel('quechua.xlsx', sheet_name='pronombres')
col = pronombre.columns
pronombre.set_index(col[0], inplace=True)
d_pronombre = pronombre.to_dict()

# Cargar conjugaciones de ejemplo
df_conjugaciones = pd.read_excel('conjugaciones_quechua.xlsx')

# Dividir las columnas en listas
columnas = df_conjugaciones.columns
listas = {columna: df_conjugaciones[columna].tolist() for columna in columnas}

def color_de_fondo():
    st.markdown(
        f'''
         <style>
         .stApp {{
             background-color: #FFE3E8;
             }}
         </style>
         ''',
         unsafe_allow_html=True
         )

color_de_fondo()

st.title(':rainbow[Conjugador de verbos en quechua y conjugador inverso]')
#st.image('head.jpg')

# Función para conjugar verbos
def conjugador(base, persona, numero, tiempo):
    return d_pronombre[numero][persona] + ' ' + base + D[tiempo][numero][persona]

# Función para descomponer una conjugación en sus partes
def descomponer_conjugacion(conjugacion):
    for base in verbos['quechua']:
       # if base.endswith('y'):
          #  base = base[:-1]
        for persona in ["primera inclusiva", "primera exclusiva", "segunda", "tercera"]:
            for numero in ["singular", "plural"]:
                for tiempo in D.keys():
                    if conjugador(base, persona, numero, tiempo) == conjugacion:
                        return base, persona, numero, tiempo
    return None, None, None, None

# Selección de verbo y conjugación
base = st.selectbox(":violet-background[Seleccione un verbo en quechua]", list(verbos['quechua']))
st.write("El verbo en español es:", dict(zip(verbos['quechua'], verbos['español']))[base])
if base.endswith("y"):
    base = base[:-1]

persona = st.selectbox("Seleccione una persona:", ["primera inclusiva", "primera exclusiva", "segunda", "tercera"])
numero = st.selectbox("Seleccione un número:", ["singular", "plural"])
tiempo = st.selectbox("Seleccione un tiempo:", ["presentesimple","presenteprogresivo", "presentehabitual", "pasadoexperimentadosimple", "pasadoexperimentadoprogresivo", "pasadoexperimentadohabitual", "pasadonoexperimentadosimple", "pasadonoexperimentadoprogresivo", "pasadonoexperimentadohabitual"])

st.write("Seleccionaste:", persona, numero, tiempo)
st.write("El verbo conjugado es:", conjugador(base, persona, numero, tiempo))

# Inverso: Elegir una conjugación
conjugacion_quechua = st.selectbox("Seleccione una conjugación en quechua:", df_conjugaciones['Conjugación'])
if conjugacion_quechua:
    base, persona, numero, tiempo = descomponer_conjugacion(conjugacion_quechua)
    if base and persona and numero and tiempo:
        st.write("Base del verbo:", base)
        st.write("Persona:", persona)
        st.write("Número:", numero)
        st.write("Tiempo:", tiempo)
    else:
        st.write("No se pudo descomponer la conjugación proporcionada.")

