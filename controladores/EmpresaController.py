from fastapi import APIRouter
from clases.Sesion import Sesion
# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
import json
import requests
listarEmpresaJson = json.load(
    open("./ModulosJson/empresa/listarEmpresas.json"))

empresa_router = APIRouter()


@empresa_router.post("/getEmpresaByColppy")
async def getEmpresaByColppy():
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarEmpresaJson['auth']['usuario'] = configuracion['development'].USER
            listarEmpresaJson['auth']['password'] = configuracion['development'].PASSWORD

            listarEmpresaJson['parameters']['sesion']['claveSesion'] = login[1]
            # print(listarEmpresaJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarEmpresaJson), headers={'Content-Type': 'application/json'})
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
