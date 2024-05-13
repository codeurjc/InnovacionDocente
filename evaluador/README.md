# Instrucciones

- Situa el fichero de resultados en la carpeta `results/` y renómbralo a `Results.xlsx`
- Lanza la aplicación 

En Docker:

Se puede usar la imagen ya construida `maes95/evaluador:v1`
```
$ docker build -t evaluador .
$ docker run -p 7860:7860 -v $PWD/results:/usr/src/app/results evaluador
```

Con Python
```
$ pip install -r requirements.txt
$ python app.py
```