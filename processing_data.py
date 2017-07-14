
# coding: utf-8

# In[1]:

####!/usr/bin/python



# In[2]:

#Import required libraries

import numpy as np
import pandas as pd
import psycopg2, psycopg2.extras
import psycopg2.extensions
import sys
import os
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) 
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[3]:

def funcion(ccaa,mun,dist): 
    
    #Connect Database
    conn = psycopg2.connect(database='cityData', host='localhost',user = 'postgres', password="DS17")
    cur = conn.cursor() 
    
    #Select Data
    ccaa = str(ccaa)
    mun = str(mun)
    dist = str(dist)
    a=(' and seccdetail.idccaa='+ ccaa +' and seccdetail.codmun = '+ mun +' and seccdetail.iddist = '+ dist +';')
    q = """SELECT * FROM seccdetail,seccresults,barrio where  seccdetail.idsecc = seccresults.idsecc ?"""
    def check_sql_string(q, a):
        q = q.replace("?",a)
        return q
    cur.execute(check_sql_string(q, a))
    ver = cur.fetchall()
    df = pd.DataFrame(ver)
    #return df
    #Sort results
    df1 = pd.DataFrame(df.groupby([8]).size().reset_index().rename(columns={0:'count'}))
    df1.columns = ['secc', 'count']
    df1 = df1.set_index('secc')
    df1 = df1.sort_values(df1.columns[0],ascending=False)
    #return df1
    r1 = str(df1.index[0])
    
    #r3 = str(df1.index[2])

    #Prepare SQL string
    
    #First Result
    def check_sql_string1(q1, a1):
        q1 = q1.replace("?",a1)
        return q1
    a1=('seccdetail.idsecc ='+ r1 +' and barrio.idbarrio =seccdetail.idbarrio ;')
    q1 = """SELECT seccdetail.idsecc,barrioname,seccdetail.idbarrio  FROM seccdetail,barrio where ?""" #+rw 
    cur.execute(check_sql_string1(q1, a1))
    ver1 = cur.fetchall()
    dfr = pd.DataFrame(ver1)
    #return dfr
    #Second Result
    r2 = None
    
    def check_sql_string1(q1, b):
        q1 = q1.replace("?",b)
        return q1
    
    try: 
        r2 = str(df1.index[1])
        b=('seccdetail.idsecc ='+ r2 +' and barrio.idbarrio =seccdetail.idbarrio ;')
        cur.execute(check_sql_string1(q1,b))
        ver2 = cur.fetchall()
        dfr = dfr.append(ver2)
    except :
        pass
    
    
    #Third Result
    r3= None
    try:
        r3 = str(df1.index[2])
        c=('seccdetail.idsecc ='+ r3 +' and barrio.idbarrio =seccdetail.idbarrio ;')
        cur.execute(check_sql_string1(q1,c))
        ver3 = cur.fetchall()
        dfr = dfr.append(ver3)
    except :
        pass
    
    #Select barrio names
    #dfr = dfr[1]
 
    return dfr


# In[1]:

def recommender():
    return gresult()

def gresult ():   
    #Get input data
    try:
        ccaa = raw_input("introduzca la ccaa")
        mun = raw_input("introduzca el municipio")
        dist = raw_input("introduzca el distrito")
    except:
        print ('Selecciona algún dato de los ejemplos')
    #Fix no values
    result = pd.DataFrame(funcion(ccaa,mun,dist))
    #Connect to database
    conn = psycopg2.connect(database='cityData', host='localhost',user = 'postgres', password="DS17")
    cur = conn.cursor() 
    barrioname1 = result[1].iloc[0]
    barrioname2 = result[1].iloc[1]
    #barrioname3 = result[1].iloc[2]
    idbarrio = str(result[2].iloc[0])
    a = ("SELECT * FROM secc,seccdetail  where  seccdetail.idsecc=secc.idsecc and seccdetail.idccaa = 13 and seccdetail.codmun = 79 and seccdetail.idbarrio ="+ idbarrio+ "" "")
    cur.execute(a)

    #cur.execute("SELECT * FROM secc,seccdetail  where  seccdetail.idsecc=secc.idsecc and seccdetail.idccaa = 13 and seccdetail.codmun = 79 and seccdetail.idbarrio = 79012")
    ver =  cur.fetchall()
    indexed_df_secc_mad = pd.DataFrame(ver)#.set_index([0])
    df =indexed_df_secc_mad.set_index([0])
    df = df.iloc[:,:145]
    df.head(10)
    total_pob = df[1].sum()
    total_pob_hombres= df[2].sum()
    total_pob_mujeres= df[3].sum()
    t_viv=df[110].sum()
    t_viv_prin=df[111].sum()
    t_viv_sec=df[112].sum()
    t_viv_vac=df[113].sum()
    t_viv_propiedad_pag=df[114].sum()
    t_viv_propiedad_pend=df[115].sum()
    t_viv_propiedad_her=df[116].sum()
    t_viv_alquiler=df[117].sum()
    t_viv_cedidas_gratis=df[118].sum()
    t_viv_otro_tipo=df[119].sum()
    t_h_menos_16=df[33].sum()
    t_h_16_64=df[34].sum()
    t_h_mas_64=df[35].sum()
    t_m_menos_16=df[36].sum()
    t_m_16_64=df[37].sum()
    t_m_mas_64=df[38].sum()
    t_h_1=df[140].sum()
    t_h_2=df[141].sum()
    t_h_3=df[142].sum()
    t_h_4=df[143].sum()
    t_h_5=df[144].sum()
    t_h_6=df[145].sum()
    
    t_solt=df[140].sum()
    t_cas=df[141].sum()
    t_sep=df[142].sum()
    t_divo=df[143].sum()
    t_viu=df[144].sum()
    
    #Grafico por uso de vivienda
    print " "
    print "Nuestra recomendación es : " 
    print ('\x1b[1;31m'+ barrioname1 +'\x1b[0m')
    print
    print ('Segunda Opcion')
    print (barrioname2)
    #print barrioname3
    #plt.pie(X,labels=Y)
    #plt.show()
    print ('\x1b[1;31m'+ ' Datos de ' + barrioname1 +'\x1b[0m')
    
    #Data for Plots
    P=[total_pob_hombres,total_pob_mujeres]
    lP=['Hombres','Mujeres']
    Ph=[t_h_menos_16,t_h_16_64,t_h_mas_64]
    lPh=['<16', '16 -64','>64']
    Pm=[t_m_menos_16,t_m_16_64,t_m_mas_64]
    lPm=[]
    X=[t_viv_prin,t_viv_sec,t_viv_vac]
    Y=['Viviendas Principales','Viviendas Secundarias','Viviendas Vacias']
    X1=[t_viv_propiedad_pag,t_viv_propiedad_pend,t_viv_propiedad_her,t_viv_alquiler,t_viv_cedidas_gratis,t_viv_otro_tipo]
    Y1 = ['Pagada','Deuda Pendiente','Heredada', 'Alquiler','Cedidas Gratis','Otros']
    H=[t_h_1,t_h_2,t_h_3,t_h_4,t_h_5,t_h_6]
    lH=['1','2','3','4','5','6+',]
    E=[t_solt,t_cas,t_sep,t_divo,t_viu]
    lE=['soltero','casado','Separado','Divorciado','Viudo']
    
    # plot with various axes scales
    plt.figure(1)

    # By Sex
    plt.subplot(231)
    plt.pie(P,labels=lP)
    plt.title('Poblacion por sexo')
    plt.grid(True)


    # Age Man
    plt.subplot(232)
    plt.bar(range(len(Ph)),Ph)
    plt.xticks(np.arange(len(Ph))+.5,lPh)
    plt.title('Hombres por Edad')

    # Age Woman
    plt.subplot(233)
    plt.bar(range(len(Pm)),Pm)
    plt.xticks(np.arange(len(Pm))+.5,lPh)
    plt.title('Mujeres por Edad')

    
     # Civil status
    plt.subplot(224)
    plt.pie(E,labels=lE)
    plt.title('Estado Civil')
    plt.grid(True)
    
    # House Person
    plt.subplot(223)
    plt.bar(range(len(H)),H)
    plt.xticks(np.arange(len(H))+.5,lH)
    plt.title('Hogares por numero de personas')
    plt.grid(True)
    plt.subplots_adjust(top=2., bottom=0.08, left=1.510, right=3.5, hspace=0.25,
                        wspace=0.5)

    plt.show()
    
    print ('\x1b[1;31m'+ 'Vivienda' +'\x1b[0m')
    
    # plot with various axes scales
    plt.figure(1)

     # House Uses
    plt.subplot(223)
    plt.pie(X,labels=Y)
    plt.title('Viviendas por uso')
    plt.grid(True)
    
    # House Owner
    plt.subplot(224)
    plt.bar(range(len(X1)),X1)
    plt.xticks(np.arange(len(X1))+.5,Y1)
    plt.title('Viviendas por propiedad')
    plt.grid(True)
    plt.subplots_adjust(top=2., bottom=0.08, left=1.510, right=3.5, hspace=0.25,
                        wspace=0.7)

    plt.show()
    
    #Resume Data
    total_viv = t_viv_prin+t_viv_sec+t_viv_vac
    print ("El número total de viviendas es: %d"%total_viv)
    print ("Viviendas Principales: %d"%t_viv_prin)
    print ("Viviendas Secundarias: %d"%t_viv_sec)
    print ("Viviendas Vacias: %d"%t_viv_vac)
    
    return 'Vuelve a Ejecutar la Celda'


# In[ ]:



