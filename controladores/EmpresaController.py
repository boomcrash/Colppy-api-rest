from fastapi import APIRouter, Body
from clases.Sesion import Sesion
# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
import json
import requests
from clases.Empresa import leerNumeroRecibo, listarCCostos

listarEmpresaJson = json.load(
    open("./ModulosJson/empresa/listarEmpresas.json"))
listarCCostosJson = json.load(
    open("./ModulosJson/empresa/listarCCostos.json"))
leerEmpresaJson = json.load(
    open("./ModulosJson/empresa/leerEmpresa.json"))
leerTalonarioJson = json.load(
    open("./ModulosJson/empresa/leerTalonario.json"))
leerNumeroReciboJson = json.load(
    open("./ModulosJson/empresa/leerNumeroRecibo.json"))


empresa_router = APIRouter()


@empresa_router.post("/getEmpresasByColppy")
async def getEmpresasByColppy():
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





@empresa_router.post("/getCCostosByColppy")
async def getCCostosByColppy(parametros: listarCCostos = Body(...)):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarCCostosJson['auth']['usuario'] = configuracion['development'].USER
            listarCCostosJson['auth']['password'] = configuracion['development'].PASSWORD
            listarCCostosJson['parameters']['sesion']['claveSesion'] = login[1]
            listarCCostosJson['parameters']['idEmpresa'] = str(parametros.idEmpresa)
            listarCCostosJson['parameters']['ccosto'] = str(parametros.ccosto)
            # Los valores posibles para 'ccosto' son "0", "1" y "2".

            # print(listarCCostosJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarCCostosJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['codigos']
                    return data
                else:
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")




@empresa_router.post("/getEmpresaByColppy/{idEmpresa}")
async def getEmpresaByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerEmpresaJson['auth']['usuario'] = configuracion['development'].USER
            leerEmpresaJson['auth']['password'] = configuracion['development'].PASSWORD
            leerEmpresaJson['parameters']['sesion']['claveSesion'] = login[1]
            leerEmpresaJson['parameters']['idEmpresa'] = str(idEmpresa)

            # print(leerEmpresaJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerEmpresaJson), headers={'Content-Type': 'application/json'})
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


# talonarioDefault y descTipoComprobante son otros parametros OPCIONALES
@empresa_router.post("/getTalonarioColppy/{idEmpresa}")
async def getTalonarioColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerTalonarioJson['auth']['usuario'] = configuracion['development'].USER
            leerTalonarioJson['auth']['password'] = configuracion['development'].PASSWORD
            leerTalonarioJson['parameters']['sesion']['claveSesion'] = login[1]
            leerTalonarioJson['parameters']['idEmpresa'] = str(idEmpresa)

            # print(leerTalonarioJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerTalonarioJson), headers={'Content-Type': 'application/json'})
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





@empresa_router.post("/getNumeroReciboColppy")
async def getNumeroReciboColppy(parametros: leerNumeroRecibo = Body(...)):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerNumeroReciboJson['auth']['usuario'] = configuracion['development'].USER
            leerNumeroReciboJson['auth']['password'] = configuracion['development'].PASSWORD
            leerNumeroReciboJson['parameters']['sesion']['claveSesion'] = login[1]
            leerNumeroReciboJson['parameters']['idEmpresa'] = str(parametros.idEmpresa)
            leerNumeroReciboJson['parameters']['prefijo'] = str(parametros.prefijo)
            # 'prefijo' = Primeros cuatro dígitos de un número de factura.

            # print(leerNumeroReciboJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerNumeroReciboJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            #print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['data']
                    return data
                else:
                    print(result["response"]["message"])
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")
