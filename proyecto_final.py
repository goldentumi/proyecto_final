# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:58:13 2024

@author: gaby-
"""

import pandas as pd
import streamlit as st

archivo = open('conjugaciones_quechua.xlsx')
quechua = pd.read_excel('conjugaciones_quechua.xlsx')

st.title(':rainbow[Conjugador inverso]')

df_conjugaciones = pd.ExcelFile('conjugaciones_quechua.xlsx')

# Dividir las columnas en listas
columnas = df_conjugaciones.columns
listas = {columna: df_conjugaciones[columna].tolist() for columna in columnas}

# Imprimir las listas para verificar
for columna, lista in listas.items():
    print(f"Columna: {columna}")
    print(lista)