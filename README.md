# ProyectoFinalAREP Fraud-Detector


## Authors

* [David Pérez](https://github.com/DavidPZ666)
* [Juan Espinosa](https://github.com/Juancode-Espi)
* [Nicolas Camacho](https://github.com/haatom)
* [Daniel Porras](https://github.com/Daniel19902)
* Jhonatan Pulido
## Introduccion y contexto 

Nuestro proyecto se basa en la detección de fraude documentario utilizando un  procesamiento automatizado de transacciones en un conjunto de datos de
ejemplo o en su propio conjunto de datos. además de posible detección de actividad fraudulenta. Vamos a crear una arquitectura que detecta fraudes o actividad sospechosamente fraudulenta en documentos bancarios.

Para esto nos vamos basar en una arquitectura recomendada por aws 

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/hybrid.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/Arquitectura.png)

Nosotros vamos a simplificar esta arquitectura basándonos en nuestro proyecto y las limitaciones tanto de costo como de tiempo para implementar una arquitectura que nos permita detectar fraude o actividad sospechosa principalmente en temas de documentos bancarios véase como tarjetas debito o credito.


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

### Creacion S3 Bucket
El primer paso es crear un Bucket S3
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-1.png)

Seleccionamos un nombre y un servidor en este caso y por lo general seleccionamos US-EAST

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-2.png)
Creamos el bucket

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-3.png)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-5.PNG)

En esta parte vamos a seleccionar el archivo que vamos a usar para entrenar nuestro fraud detector en este caso es el archivo .csv que esta en este git este cuenta con 20k registros que nos permitira tener una buena precision.

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-6.png)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-7.PNG)


![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-8.png)

A pesar de ser un archivo no excesivamente grande (4.2MB) es un buen tamaño para nuestra pequeña arquitectura aunque para una arquitectura más grande es necesario un numero muchisimo más grande que este.

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/2-8%20%232.PNG)

### Creacion del evento para el modelo del AWS Fraud detector

Creamos un event type en este caso creamos el event type "customer"


![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-2.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-3.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-3%20%232.PNG)

**Creamos un label**

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-4.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-5.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-6.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-6%20%232.PNG)


**Creamos el evento**
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-7.png)

Seleccionamos el event type recien creado

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-8.png)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/3-11.PNG)




### Entrenar y desplegar 

En la pestaña de AWS fraud detector asignandole sus propiedades
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-2.png)

Asignamos el IAM que creamos anteriormente y el archivo de entreno el guardado en nuestro S3 bucket
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-3.PNG)

 En la página Configurar el entrenamiento seleccionamos las caracteristicas que sirven para entrenar que estaban en el archivo csv en la parte de labels seleccionamos en la parte de fraude el label "fraud" y en la parte de legitimo el label creado "legit"

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-4.PNG)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-5.PNG)

*Esta parte es donde ponemos a entrenar nuestro fraud detector este proceso con la cantidad de datos que tenemos para entrenar duro 1:20 horas*

Despues que estuvo entrenando nuestro fraud detector esta listo para desplegarse

Y estas fueron las estadisticas que nos muestra despues de desplegado fueron las siguientes:
**Score distribution:**
Esta estadistica despues del entrenamiento nos afirma que lograra atrapar el 94.3% de los eventos fraudulentos y se acepta un riesgo de que el 13.2% de los eventos legitimos se etiqueten como un "falso fraude"
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-6%20%231.PNG)

**Confusion matrix:**
la matriz de confusión representa el resultado esperado dados 100000 eventos de la muestra 
nos muestra 94% y 13% fraude, la tabla tambien se puede leer que realmente no tiene muchos fallos en sus resultados.
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-6%20%232.PNG)


**Model variable importance**

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-6%20%233.PNG)

En esta ultima grafica nos muestra alguno porcentajes como el porcentaje de "positivos falsos",
"Positivos verdaderos", "precision", "model threshold".

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-6%20%234.PNG)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/4-7.PNG)

### Crear y publicar el fraud detector

Vamos a definir y crear nuestras reglas en este caso siguiendo las recomendaciones de AWS.
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-3.PNG)

Definimos los detalles del detector

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-5.png)

Añadimos el modelo previamente creado

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-7.png)
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-8.png)

Luego modificamos las reglas dependiendo del puntaje obtenido que clasifique la prediccion en un riesgo alto, medio o bajo
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-9%20%231.PNG)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-9%20%232.PNG)

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-9%20%233.PNG)

Antes de crear revisamos 

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-12.png)

### Lanzamos la aplicacion y ahora vamos a probar algunos casos de prueba

En este caso nos vota un riesgo bajo 

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-13%20%231.PNG)

En este caso nos vota un riesgo alto

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/5-13%20%232.PNG)

## Creamos una function lambda para poder correr el api que nos genera el fraud detector
![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/LambdaFunction.PNG)

APIFraud

```
import boto3, uuid, json
client = boto3.client('frauddetector', region_name='us-east-1')
response = client.get_event_prediction(
    detectorId="detector-getting-started",
    eventId=str(uuid.uuid4()),
    eventTypeName="registration",
    eventTimestamp="2019-08-10T20:44:00Z",
    entities=[{"entityType": "customer", "entityId": str(uuid.uuid4())},],
    eventVariables={
        "billing_address": "78253 Centro Comercial Calima.",
        "billing_postal": "39854",
        "billing_state": "NC",
        "email_address": "ncamacho@gmail.com",
        "ip_address": "122.136.132.150",
        "phone_number": "(555) 332 - 9271",
        "user_agent": "Mozilla/5.0 (iPad CPU iPad OS 10_3_3 like Mac OS X) AppleWebKit/532.2 (KHTML, like Gecko) CriOS/34.0.827.0 Mobile/13K063 Safari/532.2"
    }
    print('The predicted outcome is :' +json.dumps(response['ruleResults'][0]['outcomes']))
)
```
Corremos nuestra api en una funcion lambda

![](https://github.com/DavidPZ666/ProyectoFinalAREP--Fraud-Detector-/blob/master/img/LambdaCodigo.PNG)



## Conclusiones

Despues de la creacion de nuestro amazon fraud detector podemos ver que este es una herramienta muy poderosa que aprovecha muy bien el machine learning para mostrar resultados muy buenos , que a pesar que nuestro prototipo se basa en la deteccion de fraude en documentos bancarios este se puede extrapolar a otro tipo de documentos como documentos de identificacion , inclusive para documentos que cuenten con  algun tipo de imagen como una foto o algun tipo de codigo qr entre otros, este prototipo puede ser usado por cualquier empresa o compañia que maneje temas de validacion de cualquier tipo de documentos, sumado a algun otro tipo de verificacion puede evitar cualquier tipo de incoveniente con el fraude documentario.
