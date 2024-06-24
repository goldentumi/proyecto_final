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

