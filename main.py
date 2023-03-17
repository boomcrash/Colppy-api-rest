import requests
import json

from clases.Sesion import Sesion

urlLogin="https://login.colppy.com/lib/frontera2/service.php"
urlDeveloper="https://staging.colppy.com/lib/frontera2/service.php"


if __name__=="__main__":
    session=Sesion()
    login=session.iniciarSesion(urlLogin=urlLogin)
    if login[0]==True:
        print("Sesion iniciada")
        #print(listarEmpresas(clave))
        #print(listarCliente(clave))
        #print(clave)
        if session.cerrarSesion(urlLogin,login)==True:
            print("Sesion cerrada")