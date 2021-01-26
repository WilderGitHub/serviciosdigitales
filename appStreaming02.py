def miFuncion(archivitos):
    #print ('Comienza el proceso')
    import pandas as pd
    import re
    import pyxlsb
     
    CamposPaTrabajar = ['TIPO_TARJETA','MES','BS','LUGAR_TRANSACION','RUBRO','NOMBRE_COMERCIO']
    Naturalezas = 'Naturalezas.xlsx'
    PalabrasClave = 'PalabrasClave.xlsx'
    #agarramos el parametro "archivitos" y les hacemos Dataframes y concatenamos
    bolaDeDataframes=[] 
    for archivito in archivitos:
        bruto =pd.read_excel(archivito, engine='pyxlsb')
        bolaDeDataframes.append(bruto)
    dataframeConcatenado = pd.concat(bolaDeDataframes,ignore_index=True)
    dfDatosPaTrabajar= pd.DataFrame(dataframeConcatenado, columns = CamposPaTrabajar)    
      
    ## Seleccionamos los campos del diccionario Naturalezas que nos interesa
    dfNaturalezasP = pd.read_excel(Naturalezas)
    dfNaturalezas = pd.DataFrame(dfNaturalezasP, columns=['RUBRO','Naturaleza'])
    valorPorDefecto= "Por identificar"
    ## Juntamos nuestro Dataframe con Naturalezas tipo BuscarV
    resultadoMerge=dfDatosPaTrabajar.merge(dfNaturalezas, on='RUBRO', how='left').fillna(valorPorDefecto)
    ##print("resultado merge")
    dfDatosPaTrabajar['Naturaleza']=resultadoMerge['Naturaleza']
    ## creamos una cadena separadas con | para que extraigamos
    dfPalabrasClave = pd.read_excel(PalabrasClave)
    listaPalabrasClave = dfPalabrasClave['Conceptos'].values.tolist()
    apachurrado=''
    for palabrita in listaPalabrasClave:
        apachurrado +='|'+palabrita 
    apachurrado=apachurrado[1:]
    # Buscamos nuestras palabras clave y si no encuentra le decimos que llene con Naturalezas
    df3=dfDatosPaTrabajar["NOMBRE_COMERCIO"].str.extract(r'(%s)'%apachurrado,re.IGNORECASE)
    dfDatosPaTrabajar['Conceptos']=df3
    dfDatosPaTrabajar['Conceptos']=dfDatosPaTrabajar['Conceptos'].str.title()
    dfDatosPaTrabajar['Conceptos']=dfDatosPaTrabajar['Conceptos'].fillna(dfDatosPaTrabajar['Naturaleza'])
    ############################ Creamos el campo de Grupos para el resumen final
    resultadoJunte=dfDatosPaTrabajar.merge(dfPalabrasClave, on='Conceptos',how='left')
    dfDatosPaTrabajar['Grupos']=resultadoJunte['Grupos']
    dfDatosPaTrabajar['Grupos']=resultadoJunte['Grupos'].fillna(dfDatosPaTrabajar['Conceptos'])
    #creamos un nuevo campo de Millones de USD
    dfDatosPaTrabajar['Millones de USD']=dfDatosPaTrabajar['BS']/6960000
    #creamos el campo mes y gestion
    dfDatosPaTrabajar['Gestion']=dfDatosPaTrabajar['MES'].str.extract(r'(\d+)').astype(int)
    dfDatosPaTrabajar['Mes']=dfDatosPaTrabajar['MES'].str[:3]
    #Hacemos las tablas dinamicas
    resultadoResumen1=dfDatosPaTrabajar.groupby(['Gestion','Mes','Grupos','Conceptos'])['Millones de USD'].sum()
    resultadoResumen2=dfDatosPaTrabajar.groupby(['Gestion','Mes','Grupos'])['Millones de USD'].sum()
    resultadoResumen1.loc['Total']= resultadoResumen1.sum(axis=0)
    resultadoResumen2.loc['Total']= resultadoResumen2.sum(axis=0)
    # exportamos a un archivo con sus pestanias
    with pd.ExcelWriter('ResumenOK.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
        resultadoResumen1.to_excel(writer, sheet_name='Resumen detallado')
        resultadoResumen2.to_excel(writer, sheet_name='Resumen')
    print ('termina el procesin')