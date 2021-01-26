def miFuncion(ArchivoXlsb):
    print ('Comienza el proceso')
    
    import pandas as pd
    import re
    import pyxlsb
    #import xlsxwriter
    #ArchivoXlsb ='c:\\Users\\WILDER\\Desktop\\WilderPython\\servicios1\\Plantilla2.xlsb'
    #ArchivoXlsb = "Plantilla2.xlsb" 
    print ("ruta en funcion "+ArchivoXlsb)
    CamposPaTrabajar = ['TIPO_TARJETA','MES','BS','LUGAR_TRANSACION','RUBRO','NOMBRE_COMERCIO']
    Naturalezas = 'Naturalezas.xlsx'
    PalabrasClave = 'PalabrasClave.xlsx'

    ##Seleccionamos solo los campos que necitamos
    DatosBruto =pd.read_excel(ArchivoXlsb, engine='pyxlsb')
    dfDatosPaTrabajar = pd.DataFrame(DatosBruto, columns = CamposPaTrabajar)
    ## Seleccionamos los campos del diccionario Naturalezas que nos interesa
    dfNaturalezasP = pd.read_excel(Naturalezas)
    dfNaturalezas = pd.DataFrame(dfNaturalezasP, columns=['RUBRO','Naturaleza'])
    valorPorDefecto= "Por identificar"
    ## Juntamos nuestro Dataframe con Naturalezas tipo BuscarV
    resultadoMerge=dfDatosPaTrabajar.merge(dfNaturalezas, on='RUBRO', how='left').fillna(valorPorDefecto)
    ##print("resultado merge")
    ##print(resultadoMerge.shape)
    ##print(resultadoMerge.head())
    dfDatosPaTrabajar['Naturaleza']=resultadoMerge['Naturaleza']

    ## creamos una cadena separadas con | para que extraigamos
    dfPalabrasClave = pd.read_excel(PalabrasClave)
    listaPalabrasClave = dfPalabrasClave['Conceptos'].values.tolist()
    apachurrado=''
    for palabrita in listaPalabrasClave:
        apachurrado +='|'+palabrita 
    apachurrado=apachurrado[1:]

    #miDf2=miDf.set_index("LUGAR_TRANSACION","TIPO_TARJETA")
    #print (miDf2.loc['EXTERIOR'])
    #miDf3= miDf.groupby(['LUGAR_TRANSACION','EMISOR'])['BS'].sum()/6860000



    ##print("resultado de datos para trabajar")
    ##print(dfDatosPaTrabajar.shape)
    ##print(dfDatosPaTrabajar.shape)
    ##print ('pruebas con extract y regex')

    # Buscamos nuestras palabras clave y si no encuentra le decimos que llene con Naturalezas
    df3=dfDatosPaTrabajar["NOMBRE_COMERCIO"].str.extract(r'(%s)'%apachurrado,re.IGNORECASE)
    dfDatosPaTrabajar['Conceptos']=df3
    dfDatosPaTrabajar['Conceptos']=dfDatosPaTrabajar['Conceptos'].str.title()
    dfDatosPaTrabajar['Conceptos']=dfDatosPaTrabajar['Conceptos'].fillna(dfDatosPaTrabajar['Naturaleza'])
    #print(dfDatosPaTrabajar.shape)
    ############################ Creamos el campo de Grupos para el resumen final
    resultadoJunte=dfDatosPaTrabajar.merge(dfPalabrasClave, on='Conceptos',how='left')
    dfDatosPaTrabajar['Grupos']=resultadoJunte['Grupos']
    dfDatosPaTrabajar['Grupos']=resultadoJunte['Grupos'].fillna(dfDatosPaTrabajar['Conceptos'])
    ####print(dfDatosPaTrabajar[['Naturaleza','Grupos','Conceptos']].head(20))
    #creamos un nuevo campo de Millones de USD
    dfDatosPaTrabajar['Millones de USD']=dfDatosPaTrabajar['BS']/6960000

    #creamos el campo mes y gestion

    dfDatosPaTrabajar['Gestion']=dfDatosPaTrabajar['MES'].str.extract(r'(\d+)').astype(int)
    dfDatosPaTrabajar['Mes']=dfDatosPaTrabajar['MES'].str[:3]
    #Hacemos las tablas dinamicas
    resultadoResumen1=dfDatosPaTrabajar.groupby(['Gestion','Mes','Grupos','Conceptos'])['Millones de USD'].sum()
    resultadoResumen2=dfDatosPaTrabajar.groupby(['Gestion','Mes','Grupos'])['Millones de USD'].sum()
    #print (dfDatosPaTrabajar['Naturaleza'].unique())
    #print(resultadoResumen)
    #resultadoResumen.set_index("LUGAR_TRANSACION","TIPO_TARJETA")

    #escribidor = pd.ExcelWriter('ResumenOK.xlsx', engine='xlsxwriter')
    #resultadoResumen1.to_excel(escribidor,sheet_name="Resumen detallado")
    #resultadoResumen2.to_excel(escribidor,sheet_name="Resumen")
    #escribidor.save()
    #resultadoResumen1 =resultadoResumen1.append(resultadoResumen1.agg(['sum']))
    #resultadoResumen2 =resultadoResumen2.append(resultadoResumen2.agg(['sum']))
    resultadoResumen1.loc['Total']= resultadoResumen1.sum(axis=0)
    resultadoResumen2.loc['Total']= resultadoResumen2.sum(axis=0)
    #df.loc[:,'Row_Total'] = df.sum(numeric_only=True, axis=1)
    with pd.ExcelWriter('ResumenOK.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
        resultadoResumen1.to_excel(writer, sheet_name='Resumen detallado')
        resultadoResumen2.to_excel(writer, sheet_name='Resumen')
    print ('termina el procesin')
#miFuncion('c:\\Users\\WILDER\\Desktop\\WilderPython\\servicios1\\Plantilla2.xlsb')
#miFuncion('c:/Users/WILDER/Desktop/WilderPython/servicios1/Plantilla2.xlsb')