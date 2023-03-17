from fastapi import APIRouter
from clases.Sesion import Sesion
# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
import json
import requests
import datetime

listarCuentasDiarioJson = json.load(open("./ModulosJson/contabilidad/listarCuentasDiario.json"))
leerArbolContabilidadJson = json.load(open("./ModulosJson/contabilidad/leerArbolContabilidad.json"))
listarAsientosManualesJson = json.load(open("./ModulosJson/contabilidad/listarAsientosManuales.json"))
listarMovimientosDiarioJson = json.load(open("./ModulosJson/contabilidad/listarMovimientosDiario.json"))


contabilidad_router = APIRouter()


@contabilidad_router.post("/getCuentasDiarioByColppy/{idEmpresa}")
async def getCuentasDiarioByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarCuentasDiarioJson['auth']['usuario'] = configuracion['development'].USER
            listarCuentasDiarioJson['auth']['password'] = configuracion['development'].PASSWORD
            listarCuentasDiarioJson['parameters']['sesion']['claveSesion'] = login[1]
            listarCuentasDiarioJson['parameters']['idEmpresa'] = str(idEmpresa)

            #print(listarCuentasDiarioJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarCuentasDiarioJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            #print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['cuentas']
                    return data
                else:
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")




@contabilidad_router.post("/getArbolContabilidadByColppy/{idEmpresa}")
async def getArbolContabilidadByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            leerArbolContabilidadJson['auth']['usuario'] = configuracion['development'].USER
            leerArbolContabilidadJson['auth']['password'] = configuracion['development'].PASSWORD
            leerArbolContabilidadJson['parameters']['sesion']['claveSesion'] = login[1]
            leerArbolContabilidadJson['parameters']['idEmpresa'] = str(idEmpresa)
            # OPCIONAL FILTRAR POR FECHA
            # leerArbolContabilidadJson['parameters']['fechaDesde'] = str(fechaDesde) 
            leerArbolContabilidadJson['parameters']['fechaHasta'] = datetime.datetime.now().strftime('%d/%m/%Y')

            #print(leerArbolContabilidadJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                leerArbolContabilidadJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            #print(response.text)
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





@contabilidad_router.post("/getAsientosManualesByColppy/{idEmpresa}")
async def getAsientosManualesByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarAsientosManualesJson['auth']['usuario'] = configuracion['development'].USER
            listarAsientosManualesJson['auth']['password'] = configuracion['development'].PASSWORD
            listarAsientosManualesJson['parameters']['sesion']['claveSesion'] = login[1]
            listarAsientosManualesJson['parameters']['idEmpresa'] = str(idEmpresa)

            #print(listarAsientosManualesJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarAsientosManualesJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            print(response.text)
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




@contabilidad_router.post("/getMovimientosDiarioByColppy/{idEmpresa}")
async def getMovimientosDiarioByColppy(idEmpresa: int):
    session = Sesion()
    login = session.iniciarSesion()
    try:
        if login[0] == True:
            print("Sesion iniciada")

            listarMovimientosDiarioJson['auth']['usuario'] = configuracion['development'].USER
            listarMovimientosDiarioJson['auth']['password'] = configuracion['development'].PASSWORD
            listarMovimientosDiarioJson['parameters']['sesion']['claveSesion'] = login[1]
            listarMovimientosDiarioJson['parameters']['idEmpresa'] = str(idEmpresa)
            # OPCIONAL FILTRAR POR FECHA
            # listarMovimientosDiarioJson['parameters']['fromDate'] = str(fechaDesde)
            listarMovimientosDiarioJson['parameters']['toDate'] = datetime.datetime.now().strftime('%Y-%m-%d')
            
            #print(listarMovimientosDiarioJson)
            response = requests.post(configuracion['development'].URLBASE, data=json.dumps(
                listarMovimientosDiarioJson), headers={'Content-Type': 'application/json'})
            # print(response.status_code)
            #print(response.text)
            if response.status_code == 200:
                result = json.loads(response.text)
                success = result["response"]["success"]
                if success == True:
                    data = result['response']['movimientos']
                    return data
                else:
                    return False

    except Exception as e:
        print(e)
        return "Error al obtener datos"
    finally:
        if session.cerrarSesion(login) == True:
            print("Sesion cerrada")
