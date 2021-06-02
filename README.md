## **Clasificador de hojas de vida por cargo**

Sistema para clasificar hojas de vida para una empresa especifica de acuerdo a las áreas de dicha compañía en las siguientes categorías:
- Analista datos      
- RPA
- WEB_DEVELOPER
- Área Administrativa     
- Área Operativa       
- Área de IT

Se entrena el modelo con 302 hojas de vida distribuidas en un promedio de 53 hojas por categoría.
Para seleccionar el mejor  modelo se probaron 3 algoritmos de clasificación 
- Support vector machine
- Random forest 
- Arboles de decisión 

Despues de hacer el entrenamiento del modelo y su respectivo test, se evidencia que el mejor modelo es random forest con un 85% de accuracy, y métrcas de *Precision, recall y F1-Score* muy similares. por tanto este fue el modelo usado para el despliegue de la aplicación.


Puedes ver la app funcionando en el siguiente enlace....
https://desolate-hamlet-55652.herokuapp.com/
