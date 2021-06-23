# Emotion Analysis en Docker

## **Introducción**
Emotion Analysis es un API que corre en un contenedor de Docker, este API es la implementación de PySentimiento y FastAPI. El API utiliza la tecnología BERT (Representación de Codificador Bidireccional de Transformadores), una tecnología de red neural desarrollada por Google para el procesamiento de lenguaje natural (NLP). 
Esta API determina la emoción con el que se escriben frases, por tanto ofrece una poderosa herramienta para el análisis de las emociones de un grupo de estudio.
Es importante destacar que el análisis de las frases de esta implementación es posible en el Idioma Español e Inglés.

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
Mg. Augusto Cortez Vásquez, Mg. Hugo Vega Huerta, Lic. Jaime Pariona Quispe, Procesamiento de lenguaje natural. Revista de Ingeniería de Sistemas e Informática vol. 6, N.º 2, Julio - Diciembre 2009 https://core.ac.uk/download/pdf/304898423.pdf

Hohendahl, Andres. (2011). Procesamiento de Lenguaje Natural Robusto. 

Arbieu, Ugo & Helsper, Kathrin & Dadvar, Maral & Mueller, Thomas & Niamir, Aidin. (2021). Natural Language Processing as a tool to evaluate emotions in conservation conflicts. Biological Conservation. 256. 109030. 10.1016/j.biocon.2021.109030. 

A, Ashwitha & Gowda, Shruthi & R, Shruthi & Upadhyaya, Makarand & Ray, Abhra & C, Manjunath. (2020). Sarcasm detection in natural language processing. Materials Today: Proceedings. 37. 10.1016/j.matpr.2020.09.124. 

Carvalho, A., Levitt, A., Levitt, S., Khaddam, E., & Benamati, J. (2019). Off-The-Shelf Artificial Intelligence Technologies for Sentiment and Emotion Analysis: A Tutorial on Using IBM Natural Language Processing. Communications of the Association for Information Systems, 44, pp-pp. https://doi.org/10.17705/1CAIS.04443

Emotion Analysis en Docker en Docker - 2021
