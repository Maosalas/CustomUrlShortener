from builtins import print

import connection
import sys
import time
import random
import string

cursor = connection.mydb.cursor()


def main():
    print("********MSS Url Shortener********")
    respuesta = input(""" 
    A: Acortar una nueva dirreción
    B: Ver todas nuestras dirreciones
    C: Salir """)
    if respuesta == "A" or respuesta == "a":
        acortar()
    elif respuesta == "B" or respuesta == "b":
        fetchUrls()
    elif respuesta == "C" or respuesta == "c":
        sys.exit
    else:
        print("Debes de ingresar un dato valido entre A y C")
        print("Porfavor ingresa de nuevo")
        main()


def acortar():
    urlOriginal = input("Ingrese el url que desea acortar: ")
    urlShort = generarRandomUrlId()
    cursor.execute("""INSERT INTO urls (urlOriginal,urlCorto) values (%s,%s)""", (urlOriginal, urlShort,))
    connection.mydb.commit()
    print("Pagina acortada a:" + " servidor/urls?url=" + urlShort)

def fetchUrls():
    cursor.execute("SELECT * FROM urls")
    result = cursor.fetchall()
    for x in result:
        print(" servidor/urls?url=" + x[2])
    time.sleep(3)
    print(chr(27) + '[2j')
    main()


def generarRandomUrlId():
    letras = string.ascii_lowercase
    result_str = ''.join(random.choice(letras) for i in range(6))
    validate = validateUrlIdDB("mss-" + result_str)
    if validate == 1:
        generarRandomUrlId()
    else:
        return "mss-" + result_str


def validateUrlIdDB(randomUrl):
    cursor.execute("""SELECT COUNT(urlCorto) FROM urls WHERE urlCorto= %s""", (randomUrl,))
    result = cursor.fetchone()
    return result[0]


if __name__ == '__main__':
    main()
