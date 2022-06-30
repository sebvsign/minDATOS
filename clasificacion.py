import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

estados = {'Albury':'Nueva Gales del Sur', 'BadgerysCreek':'Nueva Gales del Sur', 'Canberra':'Nueva Gales del Sur', 'Cobar':'Nueva Gales del Sur', 'CoffsHarbour':'Nueva Gales del Sur', 'Moree':'Nueva Gales del Sur', 'MountGinini':'Nueva Gales del Sur', 'Newcastle':'Nueva Gales del Sur', 'NorahHead':'Nueva Gales del Sur', 'Penrith':'Nueva Gales del Sur', 'Sydney':'Nueva Gales del Sur', 'SydneyAirport':'Nueva Gales del Sur', 'WaggaWagga':'Nueva Gales del Sur', 'Wollongong':'Nueva Gales del Sur', 'Tuggeranong':'Nueva Gales del Sur'
            ,'Albany':'Australia Occidental', 'Perth':'Australia Occidental', 'PearceRAAF':'Australia Occidental', 'PerthAirport':'Australia Occidental', 'SalmonGums':'Australia Occidental', 'Walpole':'Australia Occidental', 'Witchcliffe':'Australia Occidental'
            ,'Adelaide':'Australia Meridional', 'MountGambier':'Australia Meridional', 'Nuriootpa':'Australia Meridional', 'Williamtown':'Australia Meridional', 'Woomera':'Australia Meridional'
            ,'AliceSprings':'Territorio del Norte', 'Darwin':'Territorio del Norte', 'Katherine':'Territorio del Norte', 'Uluru':'Territorio del Norte'
            ,'Ballarat':'Victoria', 'Bendigo':'Victoria', 'Dartmoor':'Victoria', 'Melbourne':'Victoria', 'MelbourneAirport':'Victoria', 'Mildura':'Victoria', 'Portland':'Victoria', 'Richmond':'Victoria', 'Sale':'Victoria', 'Watsonia':'Victoria'
            ,'Brisbane':'Queensland', 'Cairns':'Queensland', 'GoldCoast':'Queensland', 'Townsville':'Queensland'
            ,'Hobart':'Tasmania', 'Launceston':'Tasmania'
            ,'NorfolkIsland':'Sin Estado'}

trimestres ={1: 1, 2: 1,3: 1
            ,4:2 ,5:2,6:2
            ,7:3,8:3,9:3
            ,10:4, 11:4,12:4}

def listar_estados(estados):
    contador = 0
    estados_list = []
    print("\n\t\tEstado Aviables")
    for column in estados:
        if pd.isna(column):
            continue
        contador += 1
        estados_list.append(str(column))
        print(str(contador) + ") " + str(column))
    print("0) Salir")
    return estados_list

def lista_order(list):
    contador = 0
    lista = []
    for data in list:
        contador += 1
        lista.append(data)
    return lista.sort()
            
df = pd.read_csv(r'weatherAUS.csv')


df['Estado'] = df['Location'].map(estados)
group_location_size = df.groupby("Estado").size()
group_estado_column = pd.unique(df['Estado'])          
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Trimestre'] = df['Month'].map(trimestres)
group_trimestre_size = df.groupby("Trimestre").size()
group_trimestre_column = np.sort(pd.unique(df['Trimestre'])) 

df = df.dropna()
df.to_csv(r'wAUS.csv')

#while True:          
    #estados = listar_estados(group_estado_column)
    #opcion = input('Estado: ') 
    #if(opcion == "0"):
    #    break
    #df_estado_selected = df[df['Estado'] == estados[int(opcion) - 1]]
    
    #est = df_estado_selected.iloc[24]['Estado']
    #print(df_estado_selected)
