# Custom Url Shortener
Mini proyecto de un sistema parecido al de bitly.com, el cual consta de un acortador de direcciones web usando Python.
# How to
Primero debemos de crear una tabla en una base de datos para poder así guardar toda la información que utilizamos en nuestro proyecto

(Puedes modificar a tu manera tu base de datos, pero este ejemplo fue con el que el proyecto fue realizado)

```sql
CREATE TABLE urls (
  idUrl int(11) NOT NULL,
  urlOriginal varchar(250),
  urlCorto varchar(10),
  CONSTRAINT PK_Url PRIMARY KEY (idUrl)
);
```

Una vez creada la base de datos, debes de modificar el archivo llamado ''config.py'' a tus conecciones para el servidor:
```python
host = ""
user = ""
password = ""
database = ""
```

Una vez hecho esto, solo queda correr el archivo ''main.py'' e ingresar en el menu lo que quieres hacer:
```sh
C:\Users\User\ruta_proyecto> python3 main.py
```
