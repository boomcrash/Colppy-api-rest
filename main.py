import requests
import json

urlLogin="https://login.colppy.com/lib/frontera2/service.php"
urlDeveloper="https://staging.colppy.com/lib/frontera2/service.php"
iniciarSesionJson=json.load(open("sesiones/iniciarSesion.json"))
cerrarSesionJson=json.load(open("sesiones/cerrarSesion.json"))
listarEmpresasJson=json.load(open("empresa/listarEmpresas.json"))
listarClienteJson=json.load(open("clientes/listarClientes.json"))

def iniciarSesion():
    try:
        #print(iniciarSesionJson)
        response = requests.post(urlLogin,data=json.dumps(iniciarSesionJson),headers={'Content-Type': 'application/json'})
        #print(response.status_code)
        #print(response.text)
        #print(response)
        nuevoJson=json.loads(response.text);
        return nuevoJson['response']['data']['claveSesion']
    except Exception as e:
        return "Error al iniciar sesion",e 

def cerrarSesion(clave):
    try:
        cerrarSesionJson['parameters']['sesion']['claveSesion']=clave
        #print(cerrarSesionJson)
        response = requests.post(urlLogin,data=json.dumps(cerrarSesionJson),headers={'Content-Type':'application/json'})
        #print(response.status_code)
        #print(response.text)
        return "Sesion cerrada"
    except:
        return "Error al cerrar sesion"

def listarEmpresas(clave):
    try:
        listarEmpresasJson['parameters']['sesion']['claveSesion']=clave
        #print(listarEmpresasJson)
        response = requests.post(urlLogin,data=json.dumps(listarEmpresasJson),headers={'Content-Type':'application/json'})
        #print(response.status_code)
        #print(response.text)
        return "Datos obtenidos"
    except:
        return "Error al obtener datos"

def listarCliente(clave):
    try:
        listarClienteJson['parameters']['sesion']['claveSesion']=clave
        #print(listarClienteJson)
        response = requests.post(urlLogin,data=json.dumps(listarClienteJson),headers={'Content-Type':'application/json'})
        print(response.status_code)
        print(response.text)
        return "Datos obtenidos"
    except:
        return "Error al obtener datos"

if __name__=="__main__":
    clave=iniciarSesion()
    #print(listarEmpresas(clave))
    print(listarCliente(clave))
    print(cerrarSesion(clave))
