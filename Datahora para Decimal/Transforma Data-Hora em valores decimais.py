# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

#this data is the same in the excel file. (without header)
data = [
    ["A", "1/25/2024 9:35"],
    ["A", "1/25/2024 17:35"],
    ["B", "1/25/2024 10:05"],
    ["B", "1/25/2024 16:15"],
    ["C", "1/25/2024 8:02"],
    ["C", "1/25/2024 13:58"],
    ["C", "1/25/2024 7:25"],
    ["D", "1/25/2024 11:22"],
    ["D", "1/25/2024 18:08"],
    ["A", "1/26/2024 9:35"],
    ["A", "1/26/2024 22:23"],
    ["B", "1/26/2024 14:53"],
    ["B", "1/26/2024 21:03"],
    ["C", "1/26/2024 12:50"],
    ["C", "1/26/2024 18:46"],
    ["C", "1/26/2024 12:13"],
    ["D", "1/26/2024 16:10"],
    ["D", "1/26/2024 22:56"]
]


df = pd.read_excel("Caminhoes.xlsx")
df['Data-Hora'] = df['Data-Hora'].astype(str)

#split date and time in two columns
df[['date', 'time']] = df['Data-Hora'].str.split(' ', expand=True)
#change time to datetime
df['time'] = pd.to_datetime(df['time'])

# Extrair horas, minutos e segundos
df['hour'] = df['time'].dt.hour
df['minute'] = df['time'].dt.minute
df['second'] = df['time'].dt.second

# Calcular a hora decimal
df['hour_decimal'] = df['hour'] + df['minute'] / 60 + df['second'] / 3600