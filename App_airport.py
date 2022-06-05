#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json
from PIL import Image

# Настройка заголовка и текста
st.title("Система анализа данных о сотрудниках аэропорта для разработки стратегии удержания персонала ")

# Настройка боковой панели
st.sidebar.title("О системе")


# Создадим функцию для загрузки данных
def load_data(data):
    df = pd.read_csv(data, delimiter=',')
    return df

data = 'data/res_data.csv'

df = load_data(data)

# Показ описаний
show_describe = st.sidebar.checkbox("Показать данные")
if show_describe:
    st.markdown("### Данные о сотрудниках")
    st.write(df)

df_ex = df[df.Работает == 0]    
dfs = (
    df_ex.groupby("Причина")[["Возраст"]].count())
dfs.rename(columns = {'Возраст' : 'Количество'}, inplace = True) 

    
# функция для построения графика
def draw_schedule1(i):
    fig = px.bar(dfs, x=dfs.index, y=dfs.Количество, color=dfs.index,color_discrete_sequence=px.colors.qualitative.Set2)

    fig.update_layout(title="Количество уволенных сотрудников",
                      xaxis_title="Причина",
                      yaxis_title="Количество",
                      legend_title_text='Причина',
                      plot_bgcolor='rgb(232, 246, 255)')
    
    return fig


st.plotly_chart(draw_schedule1(df), use_container_width=True)

dfm = (
    df.groupby("Группа")
    .mean())

# функция для построения графика
def draw_schedule2(i):
    fig = px.bar(dfm, x=dfm.index, y=dfm.Зарплата, color=dfm.index ,color_discrete_sequence=px.colors.qualitative.Dark24)

    fig.update_layout(title="Средняя заработная плата в зависимости от тестирования",
                      xaxis_title="Оценка за тесты",
                      yaxis_title="Средняя з/п",
                      legend_title_text='Оценка за тесты',
                      plot_bgcolor='rgb(232, 246, 255)')

    return fig


st.plotly_chart(draw_schedule2(df), use_container_width=True)

# функция для построения графика
def draw_schedule3(i):
    fig = px.bar(dfm, x=dfm.index, y=dfm.Средний_штраф_в_месяц, color=dfm.index ,color_discrete_sequence=px.colors.qualitative.Pastel1)

    fig.update_layout(title="Средний размер штрафа в зависимости от тестирования ",
                  xaxis_title="Оценка за тесты",
                  yaxis_title="Средний штраф",
                  legend_title_text='Оценка за тесты',
                  plot_bgcolor='rgb(232, 246, 255)')

    return fig


st.plotly_chart(draw_schedule3(df), use_container_width=True)

# функция для построения графика
def draw_schedule4(i):
    fig = px.bar(dfm, x=dfm.index, y=dfm.Средняя_премия_в_месяц, color=dfm.index ,color_discrete_sequence=px.colors.qualitative.Pastel)

    fig.update_layout(title="Средний размер премии в зависимости от тестирования ",
                      xaxis_title="Оценка за тесты",
                      yaxis_title="Средняя премия",
                      legend_title_text='Оценка за тесты',
                      plot_bgcolor='rgb(232, 246, 255)')

    return fig


st.plotly_chart(draw_schedule4(df), use_container_width=True)

