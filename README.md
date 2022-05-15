# ProyectoFinalAREP Fraud-Detector


## Authors

## Introduccion y contexto 

Nuestro proyecto se basa en la deteccion de fraude documentario utilizando un  procesamiento automatizado de transacciones en un conjunto de datos de
ejemplo o en su propio conjunto de datos. además de posible detección de actividad fraudulenta. Vamos a crear una arquitectura que detecte fraudes o actividad sospechosamente fraudulenta en documentos bancarios.

Para esto nos vamos basar en una arquitectura recomendada por aws 
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/hybrid.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/Arquitectura.png)

Nosotros vamos a simplificar esta arquitectura basandonos en nuestro proyecto y las limitaciones tanto de costo como de tiempo para implementar una arquitectura que nos permita detectar fraude o actividad sospechosa principalmente en temas de documentos bancarios vease como tarjetas debito o credito.

## Arquitectura

Esta es la arquitectura simplificada y acoplada a nuestros intereses de nuestro proyecto

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/simple.png)

Para esta arquitectura vamos a utilizar algunos componentes que nos brida aws:

* **Amazon S3:** Es un servicio de almacenamiento de objetos que ofrece almacenamiento de objetos a traves de una interfaz de servicio web. Esto nos va permitir almacenar los datos para los datos del fraud detector que se vaya alimentando.
* **Amazon Fraud Detector:**  Amazon Fraud Detector es un servicio completamente administrado que permite a los clientes identificar las actividades potencialmente fraudulentas y detectar más fraudes en línea con mayor rapidez. A traves del machine learning que mientras más datos tenga para entrenar, con más precision dara las predicciones.
* **AWS Lambda:** Es un servicio informatico sin servidor y basado en eventos que le permite ejecutar codigo para practicamente cualquier tipo de aplicacion sin la necesidad de aprovisionar o administrar servidores.
* **Amazon API Gateway:** es un servicio completamente administrado que facilita a los desarrolladores la creación, la publicación, el mantenimiento, el monitoreo y la protección de API a cualquier escala.

*Entendiendo el Amazon fraud detector*
Un detector es un motor de categorización basado en reglas que predice resultados predefinidos basados en nuestras propias reglas.
Los modelos se pueden entrenar dentro del Detector de Fraude de Amazon utilizando datos de usuario personalizados o se puede acceder a ellos desde puntos finales precreados de Amazon Sagemaker.
El flujo de configuración de alto nivel se representa en el siguiente diagrama.


![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/Captura%20de%20pantalla%202022-05-14%20210551.jpg)

## Tutorial de creacion y utilización del prototipo

El primer paso es crear un Bucket S3
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-1.png)

Seleccionamos un nombre y un servidor en este caso y por lo general seleccionamos US-EAST

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-2.png)
Creamos el bucket

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-3.png)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-5.PNG)

En esta parte vamos a seleccionar el archivo que vamos a usar para entrenar nuestro fraud detector en este caso es el archivo .csv que esta en este git este cuenta con 20k registros que nos permitira tener una buena precision.

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-6.png)




## Conclusiones
