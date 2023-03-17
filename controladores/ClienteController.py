from fastapi import APIRouter, Body
from clases.Sesion import Sesion
# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
import json
import requests
from clases.Cliente import leerCliente, leerFondosPagos


listarClientesJson = json.load(open("./ModulosJson/clientes/listarClientes.json"))
leerClienteJson = json.load(open("./ModulosJson/clientes/leerCliente.json"))
leerDetalleClienteJson = json.load(open("./ModulosJson/clientes/leerDetalleCliente.json"))
leerFondosPagosJson = json.load(open("./ModulosJson/clientes/leerFondosPagos.json"))


cliente_router = APIRouter()


@cliente_router.post("/getClientesByColppy/{idEmpresa}")
async def getClientesByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarClientesJson['auth']['usuario'] = configuracion['development'].USER
            listarClientesJson['auth']['password'] = configuracion['development'].PASSWORD
            listarClientesJson['parameters']['sesion']['claveSesion'] = login[1]
            listarClientesJson['parameters']['idEmpresa'] = str(idEmpresa)
            # print(listarClientesJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarClientesJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    print(result['response']['message'])
                    return False
            
    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")





@cliente_router.post("/getClienteByIdByColppy")
async def getClienteByIdByColppy(parametros: leerCliente = Body(...)):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerClienteJson['auth']['usuario'] = configuracion['development'].USER
            leerClienteJson['auth']['password'] = configuracion['development'].PASSWORD
            leerClienteJson['parameters']['sesion']['claveSesion'] = login[1]
            leerClienteJson['parameters']['idEmpresa'] = str(parametros.idEmpresa)
            leerClienteJson['parameters']['idCliente'] = str(parametros.idCliente)
            
            # print(leerClienteJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerClienteJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            #print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    print(result['response']['message'])
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")





@cliente_router.post("/getDetalleClienteByColppy")
async def getDetalleClienteByColppy(parametros: leerCliente = Body(...)):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerDetalleClienteJson['auth']['usuario'] = configuracion['development'].USER
            leerDetalleClienteJson['auth']['password'] = configuracion['development'].PASSWORD
            leerDetalleClienteJson['parameters']['sesion']['claveSesion'] = login[1]
            leerDetalleClienteJson['parameters']['idEmpresa'] = str(parametros.idEmpresa)
            leerDetalleClienteJson['parameters']['idCliente'] = str(parametros.idCliente)

            # print(leerDetalleClienteJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerDetalleClienteJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    print(result['response']['message'])
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")






@cliente_router.post("/getFondosPagosByColppy")
async def getFondosPagosByColppy(parametros: leerFondosPagos = Body(...)):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerFondosPagosJson['auth']['usuario'] = configuracion['development'].USER
            leerFondosPagosJson['auth']['password'] = configuracion['development'].PASSWORD
            leerFondosPagosJson['parameters']['sesion']['claveSesion'] = login[1]
            leerFondosPagosJson['parameters']['idEmpresa'] = str(parametros.idEmpresa)
            leerFondosPagosJson['parameters']['idCobro'] = str(parametros.idCobro)
            leerFondosPagosJson['parameters']['add'] = str(parametros.add)

            # print(leerFondosPagosJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerFondosPagosJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    print(result['response']['message'])
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")
