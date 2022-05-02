
from operator import index
from os import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'weatherAUS.csv')
#cantidad de datos filas x columns
#print(df.size)

#transformando el campo fecha a un desgloce de los datos como son año, mes y dia
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#canidad de valores nulos x columnas
#print(df.isnull().sum())
#print(df.info())

#borrando filas en null
#df = df.dropna(subset=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine' ])
#print(df.isnull().sum())

# viendo si haa llovido según ubicacion y año
#locationYes = df.loc[df["RainToday"] == 'Yes', ["Location", "Year"]]
#locationNo = df.loc[df["RainToday"] == 'No', ["Location", "Year"]]

lluviaYes = df[df['RainToday'] == 'Yes' ]
lluviaNO = df[df['RainToday'] == 'No']
lNO = lluviaNO.groupby(['Year', 'RainToday'])['RainToday'].count()
lou = lluviaYes['RainToday']
#print(lou)


#cantidad de lluvia por año según ciudad

df3 = lluviaYes.groupby(['Year','Location'])['RainToday'].count().reset_index(name='LLuviaCOUNT')
#print(df3)

#array ciudades
citys = list()
indices = list()
#ciudades
ciudadess = df.groupby(by = "Location").sum()

count = 0
for i in ciudadess.index:
    count = count + 1
    citys.append(str(i))
    indices.append(count)


localidades = { 'indice': indices, 'citys' : citys}
df02 = pd.DataFrame(data = localidades)
df02.rename(columns={'indice': 'id', 'citys': 'ciudad'})
cxd = np.array(df02, dtype=object)
cdsID = np.array(df02['indice'])
cds = np.array(df02['citys'])
print (""" \t DataFrame
ID\t Ciudad""")
print(cxd)
busqueda = int(input("Ingrese id a buscar: "))
if busqueda in cdsID:
    found = str(cds[busqueda-1])
    local = df[df['Location'] == found]
    print ('Ciudad: '+found)
    df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad')#.sort_values(by='Cantidad', ascending=False)
    print(df4)
else:
    print("Digitalice el id correspondiente, estos pueden ser\n"+str(cxd))
    print (""" \t TIPO
ID\t Ciudad""")
        

#for i in range(cds)

# ciudad adelaide
local = df[df['Location'] == 'Adelaide']

# cantidad de veces y las que no ha llovido en adelaide según groupby de años y lluvia (yes or no)
#df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad')#.sort_values(by='Cantidad', ascending=False)


#print('Datos 2017 si ha llovido o no en adelaide')

#anoNO = 0
#anoYES = 0
#anius = int(input('Ingrese el año: '))
#for i in local.index:
    #v2017 = v2017
#    if local['Year'][i] == anius:
        
#        if local['RainToday'][i] == 'No':
#            anoNO = anoNO+1
#        else:
#            if local['RainToday'][i] == 'Yes':
#                anoYES = anoYES+1
#    else:
#        print('ingrese un valor valido')
#        break
            #print('Año: '+str(local['Year'][i])+' '+'lluvio: '+ str(local['RainToday'][i]))


#print('Cantidad de veces que no lluvio en Adelaide: '+ str(anoNO))
#print('Cantidad de veces que lluvio en Adelaide: '+ str(anoYES))


#print('Datos anuales si ha llovido o no en adelaide')
#print(df4)
#cantidad de veces que lluvio o no lluvio según ciudad
#local = df[df['Location'] == 'Canberra']
#df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count()

    

    
#→ DataFrame de frecuencia
#for cate in a:
#    frecuency = df[cate].value_counts()
#    df_frequency = pd.DataFrame({
#        cate: frecuency.index.tolist(), 
#        'Cantidad': frecuency.tolist()
#    })
#    sns.barplot(x=cate, y='Cantidad', data=df_frequency)
#    plt.show()

#df['Date'] = pd.to_datetime(df['Date'])
#df['Year'] = df['Date'].dt.year
#df['Month'] = df['Date'].dt.month
#df['Day'] = df['Date'].dt.day


#descripcion = df.describe()
#print(descripcion)

#estadistica cualitativa
categorical_var = ['Location','RainToday','RainTomorrow','Year', 'Month','WindGustDir']
categorical_hours_var = ['WindDir9am','WindDir3pm']
#estadistica cuantitativa
numerical_clima_var = ['MinTemp','MaxTemp', 'Evaporation', 'RISK_MM','Evaporation','Sunshine','WindGustSpeed']
numerical_clima_hours_var = ['WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm']
#lluviano = df[df['RainToday'] == 'Yes']
#
#locationYes = df.loc[df["RainToday"] == 'Yes', ["Location", "Year"]]
#locationNo = df.loc[df["RainToday"] == 'No', ["Location", "Year"]]
#location = df[['Location','Year', 'RainToday']]
