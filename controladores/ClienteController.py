from fastapi import APIRouter
from clases.Sesion import Sesion
# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
import json
import requests
listarClienteJson = json.load(
    open("./ModulosJson/clientes/listarClientes.json"))

cliente_router = APIRouter()


@cliente_router.post("/getClientByColppy")
async def getClientByColppy():
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarClienteJson['auth']['usuario'] = configuracion['development'].USER
            listarClienteJson['auth']['password'] = configuracion['development'].PASSWORD
           
            listarClienteJson['parameters']['sesion']['claveSesion'] = login[1]
            # print(listarClienteJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarClienteJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    return False
            
    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")

