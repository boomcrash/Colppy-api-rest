import requests
import json
import os
listarClienteJson=json.load(open("ModulosJson/clientes/listarClientes.json"))



class Cliente:

    def __init__(self) :
        self.usuario=os.environ.get('usuarioItiers')
        self.password=os.environ.get('passwordItiers')
    
    def listarCliente(self,urlLogin,clave):
        try:
            listarClienteJson['auth']['usuario']=self.usuario
            listarClienteJson['auth']['password']=self.password
            urlLogin=urlLogin
            clave=clave
            if(clave[0]==True):
                listarClienteJson['parameters']['sesion']['claveSesion']=clave[1]
                #print(listarClienteJson)
                response = requests.post(urlLogin,data=json.dumps(listarClienteJson),headers={'Content-Type':'application/json'})
                #print(response.status_code)
                #print(response.text)
                return True
            else:
                return False
        except:
            return "Error al obtener datos"