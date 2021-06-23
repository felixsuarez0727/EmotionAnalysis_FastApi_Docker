# Emotion Analysis en Docker

## **Introducción**
Emotion Analysis es un API que corre sobre Docker, este API es la implementación de PySentimiento y FastAPI. Este API utiliza la tecnología BERT (Representación de Codificador Bidireccional de Transformadores), una tecnología de red neural desarrollada por Google para el procesamiento de lenguaje natural (NLP). 
Esta API determina el Sentimiento con el que se escriben frases, por tanto ofrece una poderosa herramienta para el análisis de las emociones de un grupo de estudio.
Es importante destacar que el análisis de las frases de esta implementación es posible en el Idioma Español.

En el presente proyecto, la implentación es capaz de analizar la emoción de frases para categorizarlas como:

1. Positivas
2. Neutrales
3. Negativas

## **Instalación**
Emotion Analysis requiere de los siguientes pasos para ser desplegado:
1. Instalar Docker (https://docs.docker.com/docker-for-windows/install/)
2. Descargar este repositorio.
3. Descomprimir el archivo ZIP.
4. Ejecutar Docker, emplear la CLI (Command Line Interface) de Docker para navegar hasta la ruta raiz del paquete.
5. Ejecutar las siguientes instrucciones en la CLI:
    ```Bash
    # To build the image.
        docker build -t test.
    # To run the image.
        docker run -d -p 8080:8080 --env=GOOGLE_APPLICATION_CREDENTIALS=./auth/gcp-key.json --env=BERT_MODEL=bert-base-cased --env=PRE_TRAINED_MODEL=model.h5 --name test test
    ```
## **Ejecución**
1. Recomendable instalar Postman para realizar la prueba del API.
2. Para probar el API:
    1. Se debe ejecutar la herramienta Postman.
    2. Crear una nueva solicitud HTTP, seleccionar el método HTTP POST.
    3. Por URL se emplea http://localhost:8080/predict
    4. Por Cuerpo de Request se emplea el siguiente JSON
        ```JSON
        {
            
        }
        ```
    El Resultado es un JSON con los siguientes datos:
     ```JSON
     {
                
     }
     ```
    5. Se puede saber el estado de API haciendo una solicitud HTTP GET a la siguiente URL 'http://localhost:8080/healthcheck'
    
## **Referencias**    



Emotion Analysis en Docker en Docker - 2021
