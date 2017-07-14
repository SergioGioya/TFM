
# TFM Sergio Gioya<br>
__El objetivo__ del proyecto es crear un  __recomendador de barrios de Madrid__ en donde introduciendo la comunidad autónoma, el municipio y el distrito el sistema nos devuelva el barrio más parecido en Madrid.<br>
El modelo elegido para realizarlo es Contend Based (ítem-item) utilizando Similitud Coseno para calcular las distancias entre los vectores eligiendo el que tenga  el valor más elevado.<br>

<br>
__La tecnología__ utilizada es  phyton 2.7, Python 3, postgresql, psycopg2, scikit-learn,pandas, numpy, matplotlib todo ello instalado y configurado en un servidor dedicado con Ubuntu 16.04 Server<br>
__Los datos__ utilizados para realizar la recomendación se han obtenido del INE del Censo de 2011 que se compone de más de 35.000 secciones censales y  145 variables que describen estas secciones. (Descripción de las mismas en datavariable.txt)<br>
Además he utilizado datos de Madrid Open Data con el fin de relacionar las secciones censales con los barrios de Madrid.<br>
<br>
El proyecto ha constado de las siguientes  __fases:__<br>
  -  Preparación del entorno de trabajo con la instalacion y configuración de todos los paquetes necesarios en un servidor dedicado.
(Anaconda 2.7,Python 3 , Posgresql,psycopg2,Spark, etc)<br>
  -  Extracción y preparación de los datos mediante Excel para su posterior tratamiento.<br>
  -  Construcción de base de datos y  subir todos los datos (utilizo Python 3 por problemas con Unicode para esta tarea el resto es Python 2.7)<br>
  -  Obtener los datos desde la base de datos para procesamiento<br>
  -  Procesar datos por medio de scikit-learn coseno similitud $$sim (A,B) = cos(\phi)= \frac{A \cdot B}{||A|| \cdot ||B||}$$
  -  Incorporar los resultados a la base de datos. 
  -  Desarrollar con python programa que devuelva los resultados
  Al no disponer de suficiente información de la correspondencia de mayoría de los municipios con sus distritos, barrios y secciones censales se ha agrupado la recomendación a nivel de distrito.<br>
El recomendador devuelve un barrio  con información relevante sobre el barrio recomendado


