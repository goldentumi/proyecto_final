# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:58:13 2024

@author: gaby-
"""

import pandas as pd
import streamlit as st

archivo = open('conjugaciones_quechua.xlsx')
esp = pd.read_excel('conjugaciones.xlsx')

st.title(':rainbow[Conjugador inverso]')

quechua = pd.ExcelFile('conjugaciones_quechua.xlsx')
df_conjugaciones = pd.read_excel('conjugaciones_quechua.xlsx')

#Abrir todas las hojas del excel
excel_file = pd.ExcelFile('conjugador.xlsx')
D = {}
for hoja in excel_file.sheet_names:
  df = pd.read_excel('conjugador.xlsx', sheet_name = hoja)
  c = df.columns
  df.set_index(c[0], inplace = True)
 

  d = df.to_dict()

  D[hoja] = d
# Dividir las columnas en listas
columnas = df_conjugaciones.columns
listas = {columna: df_conjugaciones[columna].tolist() for columna in columnas}
  
fr_input = st.selectbox(
    "Seleccione un verbo en español:",
    df[hoja])    
fr_quechua = st.selectbox(
    "Seleccione una conjugación en quechua:",
   df_conjugaciones['Conjugación'])