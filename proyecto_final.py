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
         .stPopover {{
             background-color: violet;
             color: white;
             padding: 10px;
             border-radius: 10px;
         }}
         </style>
         ''',
         unsafe_allow_html=True
         )

color_de_fondo()

st.image('head.jpg')
st.title(':rainbow[**Conjugador de verbos en quechua**]')


# Función para conjugar verbos
def conjugador(base, persona, numero, tiempo):
    return d_pronombre[numero][persona] + ' ' + base + D[tiempo][numero][persona]

# Función para descomponer una conjugación en sus partes
def descomponer_conjugacion(conjugacion):
    for base in verbos['quechua']:
      original_base = base
      if base.endswith('y'):
          base = base[:-1]
          for persona in ["primera inclusiva", "primera exclusiva", "segunda", "tercera"]:
            for numero in ["singular", "plural"]:
                for tiempo in D.keys():
                    if conjugador(base, persona, numero, tiempo) == conjugacion:
                        return original_base, persona, numero, tiempo
    return None, None, None, None

# Selección de verbo y conjugación
st.subheader('**Base**', divider='rainbow')
base = st.selectbox(":violet-background[Seleccione un verbo en quechua]", list(verbos['quechua']))
st.write(":blue[**El verbo en español es:**]", dict(zip(verbos['quechua'], verbos['español']))[base])
if base.endswith("y"):
    base = base[:-1]
st.subheader('**Persona**', divider='rainbow')
persona = st.selectbox(":violet-background[Seleccione una persona:]", ["primera inclusiva", "primera exclusiva", "segunda", "tercera"])
st.subheader('**Número**', divider='rainbow')
numero = st.selectbox(":violet-background[Seleccione un número:]", ["singular", "plural"])
st.subheader('**Tiempo**', divider='rainbow')
tiempo = st.selectbox(":violet-background[Seleccione un tiempo:]", ["presentesimple","presenteprogresivo", "presentehabitual", "pasadoexperimentadosimple", "pasadoexperimentadoprogresivo", "pasadoexperimentadohabitual", "pasadonoexperimentadosimple", "pasadonoexperimentadoprogresivo", "pasadonoexperimentadohabitual"])
d_tiempo = {'presentesimple':'El **presente simple** es equivalente a las formas castellanas *yo como; tú bailas,* etc. En quechua, el presente simple es el tiempo no marcado, es decir que no hay una marca explícita que indique tal tiempo; por el contrario, para conjugar un verbo en presente simple solo es necesario añadir las marcas personales a la raíz verbal.','presenteprogresivo':'Llamamos **presente progresivo** a la forma del presente equivalente a las perífrasis verbales castellanas *estoy comiendo* o *estoy bailando*. Es decir que el presente progresivo se emplea cuando el **evento descrito por una oración está ocurriendo mientras dicha oración es pronunciada**. En otras palabras, el presente progresivo se emplea cuando el evento referido por la oración es simultáneo al acto de habla. Para conjugar verbos en presente progresivo solo es necesario anteponer el sufijo **-chka** a las marcas personales del presente simple.','presentehabitual': 'Llamamos **presente habitual** a la forma del presente equivalente a las perífrasis verbales castellanas *suelo caminar* o *suelo hablar*. Es decir que el presente habitual se emplea cuando el **evento descrito por una oración es cotidiano, natural y se da con cierta regularidad**. Para conjugar verbos en presente habitual es necesario hacer uso de una perífrasis verbal, en la que añadiremos el sufijo **–q** al verbo principal y emplearemos el verbo ser, **kay**, conjugado en presente simple, a manera de auxiliar. Como puedes apreciar, en el caso de la :blue[**tercera persona no se debe incluir el verbo ser, sino que es suficiente con el sufijo –mi**], tal como ocurría con el presente simple.','pasadoexperimentadosimple': 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo **pasado experimentado**, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** antes de la marca de persona.','pasadoexperimentadoprogresivo' : 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo pasado experimentado, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** después de la marca de progresivo y antes de la marca de persona.','pasadoexperimentadohabitual' : 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo pasado experimentado, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** en el verbo **kay**, antes de la marca de persona.','pasadonoexperimentadosimple': 'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**.','pasadonoexperimentadoprogresivo' :	'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**. Se conjuga agregando dicho sufijo después de la marca de progresivo y antes de la marca de persona.','pasadonoexperimentadohabitual':	'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**. Se conjuga agregando dicho sufijo al verbo **kay**, antes de la marca de persona.'}
with st.popover (":violet-background[:violet[💭 Da click aquí para conocer más sobre los tiempos.]]"):
   st.markdown(d_tiempo[tiempo])

st.write(":red[**Seleccionaste:**]", persona, numero, tiempo)
st.write(":green[**El verbo conjugado es:**]", conjugador(base, persona, numero, tiempo))


st.title(':rainbow[**Conjugador inverso**]')
# Selección de verbo en español
verbo_espanol = st.selectbox(":violet-background[Seleccione un verbo en español:]", list(verbos['español']))
verbo_quechua = dict(zip(verbos['español'], verbos['quechua']))[verbo_espanol]
st.write(":blue[**El verbo en quechua es:**]", verbo_quechua)

# Selección de conjugación en quechua filtrada por el verbo en español
conjugaciones_filtradas = df_conjugaciones[df_conjugaciones['Verbo base (español)'] == verbo_espanol]['Conjugación']
conjugacion_quechua = st.selectbox(":violet-background[Seleccione una conjugación en quechua:]", conjugaciones_filtradas)

# Inverso: Elegir una conjugación
#conjugacion_quechua = st.selectbox(":violet-background[Seleccione una conjugación en quechua:]", df_conjugaciones['Conjugación'])
if conjugacion_quechua:
    base, persona, numero, tiempo = descomponer_conjugacion(conjugacion_quechua)
    if base and persona and numero and tiempo:
        st.write(":rainbow[**Base del verbo:**]", base)
        st.write(":rainbow[**Persona:**]", persona)
        st.write(":rainbow[**Número:**]", numero)
        st.write(":rainbow[**Tiempo:**]", tiempo)
    else:
        st.write("No se pudo descomponer la conjugación proporcionada.")

