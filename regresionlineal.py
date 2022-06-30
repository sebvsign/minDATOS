import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

estados = {'Albury':'Nueva Gales del Sur', 'BadgerysCreek':'Nueva Gales del Sur', 'Canberra':'Nueva Gales del Sur', 'Cobar':'Nueva Gales del Sur', 'CoffsHarbour':'Nueva Gales del Sur', 'Moree':'Nueva Gales del Sur', 'MountGinini':'Nueva Gales del Sur', 'Newcastle':'Nueva Gales del Sur', 'NorahHead':'Nueva Gales del Sur', 'Penrith':'Nueva Gales del Sur', 'Sydney':'Nueva Gales del Sur', 'SydneyAirport':'Nueva Gales del Sur', 'WaggaWagga':'Nueva Gales del Sur', 'Wollongong':'Nueva Gales del Sur', 'Tuggeranong':'Nueva Gales del Sur'
            ,'Albany':'Australia Occidental', 'Perth':'Australia Occidental', 'PearceRAAF':'Australia Occidental', 'PerthAirport':'Australia Occidental', 'SalmonGums':'Australia Occidental', 'Walpole':'Australia Occidental', 'Witchcliffe':'Australia Occidental'
            ,'Adelaide':'Australia Meridional', 'MountGambier':'Australia Meridional', 'Nuriootpa':'Australia Meridional', 'Williamtown':'Australia Meridional', 'Woomera':'Australia Meridional'
            ,'AliceSprings':'Territorio del Norte', 'Darwin':'Territorio del Norte', 'Katherine':'Territorio del Norte', 'Uluru':'Territorio del Norte'
            ,'Ballarat':'Victoria', 'Bendigo':'Victoria', 'Dartmoor':'Victoria', 'Melbourne':'Victoria', 'MelbourneAirport':'Victoria', 'Mildura':'Victoria', 'Portland':'Victoria', 'Richmond':'Victoria', 'Sale':'Victoria', 'Watsonia':'Victoria'
            ,'Brisbane':'Queensland', 'Cairns':'Queensland', 'GoldCoast':'Queensland', 'Townsville':'Queensland'
            ,'Hobart':'Tasmania', 'Launceston':'Tasmania'
            ,'NorfolkIsland':'Sin Estado'}

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

def listar_years(years_list):
    contador = 0
    years = []
    print("\n\t\tYears Aviables")
    for year in years_list:
        contador += 1
        years.append(year)
        print(str(contador) + ") " + str(year))
    return years

            
df = pd.read_csv(r'weatherAUS.csv')

#Eliminando datos nulos
df = df.dropna(subset=['Pressure9am'])
df = df.dropna(subset=['Pressure3pm'])


df['Estado'] = df['Location'].map(estados)
group_location_size = df.groupby("Estado").size()
group_estado_column = pd.unique(df['Estado'])          
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

while True:          
    estados = listar_estados(group_estado_column)
    opcion = input('Estado: ') 
    if(opcion == "0"):
        break
    df_estado_selected = df[df['Estado'] == estados[int(opcion) - 1]]
    est = df_estado_selected.iloc[24]['Estado']
    df_rain = df_estado_selected[df_estado_selected['Rainfall'].notna()]
    df_rain = df_rain.dropna()
    df4 = df_estado_selected.groupby(['Year'])['Rainfall'].mean().reset_index(name='Prom_precipitacion')
    
    #Separo la columna con la informacion
    X = np.array(df_rain.drop(['Year','Date','Rainfall','Date','Location','Sunshine','WindDir9am','WindDir3pm','WindGustDir','RainToday','RainTomorrow','Estado'], axis=1).values)
    
    y = np.array(df_rain['Rainfall'].values)
    y = y.astype('int')
    print(X.shape, y.shape)
    #Separo los datos de "train" en entrenamiento y prueba para grabar los algoritmos 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)


    ##Regresión logística
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    Y_pred = logreg.predict(X_test)


    s = np.array(df4['Year'])
    d = np.array(df4['Prom_precipitacion'])

    n = len(s)

    sumx = sum(s)
    sumy = sum(d)
    sumx2 = sum(s*s)
    sumy2 = sum(d*d)
    sumxy = sum(s*d)
    promx = sumx/n
    promy = sumy/n
        # correlacion de regresión lineal

    varx2 = ( sumx2 / n ) - (promx ** 2)
    vary2 = ( sumy2 / n ) - (promy ** 2)

    raizx2 = math.sqrt(varx2) 
    raizy2 = math.sqrt(vary2)

    raizxy = raizx2*raizy2

    coev = ( sumxy / n) - ( promx * promy )
    
    corr = coev / raizxy

    m = (sumx*sumy - n * sumxy) / (sumx ** 2 - n*sumx2)

    b = promy - m*promx

    lx = list()
    ly = list()

    for i in df4['Year']:
        lx.append(i)
    for c in df4['Prom_precipitacion']:
        ly.append(c)

    anios = [2018, 2019]

    for i in anios:
        if i not in lx:
            pred = float((m*i)+b)
            lx.append(i)
            ly.append(pred)
        else:
            print('Item ya agregado')

    lx = np.array(lx)
    ly = np.array(ly)

    a = np.array(2018)
    a = a.reshape(1,-1)
    print('****\t')
    print('Precisión Regresión logística: ')
    print(logreg.score(X_train, y_train))

    print('****\t')
    print('el valor de m es: '+str(m))
    print('el valor de b es: '+str(b))
    print('Coeficiente de correlación: '+str(corr))
    print("Predicción para el año 2018 y 2019 ↓")
    print("2018: "+logreg.predict(a))
    #print("2019: "+logreg.predict(lx[12]).reshape(1,-1) )

