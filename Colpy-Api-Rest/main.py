import requests
import json

urlLogin="https://login.colppy.com/lib/frontera2/service.php"
urlDeveloper="https://staging.colppy.com/lib/frontera2/service.php"
iniciarSesionJson=json.load(open("sesion.json"))


def iniciarSesion():
    try:
        response = requests.post(urlLogin,data=json.dumps(iniciarSesionJson),headers={'Content-Type': 'application/json'})
        print(response.status_code)
        print(response.text)
        return "Sesion iniciada"
    except Exception as e:
        return "Error al iniciar sesion",e 

def obtenerDatos():
    try:
        response = requests.get(url,data=json.dumps(mijson),headers={'Content-Type':'application/json'})
        print(response.status_code)
        print(response.text)
        return "Datos obtenidos"
    except:
        return "Error al obtener datos"


if __name__=="__main__":
    print(iniciarSesion())
