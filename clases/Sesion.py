import requests
import json
import os
iniciarSesionJson=json.load(open("ModulosJson/sesiones/iniciarSesion.json"))
cerrarSesionJson=json.load(open("ModulosJson/sesiones/cerrarSesion.json"))



class Sesion:
    def __init__(self) :
        self.usuario=os.environ.get('usuarioItiers')
        self.password=os.environ.get('passwordItiers')

    def iniciarSesion(self,urlLogin):
        try:
            #print(iniciarSesionJson)
            iniciarSesionJson['auth']['usuario']=self.usuario
            iniciarSesionJson['auth']['password']=self.password

            solicitud = requests.post(urlLogin,data=json.dumps(iniciarSesionJson),headers={'Content-Type': 'application/json'})
            #print(response.status_code)
            #print(solicitud.text)
            #print(response)
            result=json.loads(solicitud.text);
            response=result["response"]["success"]
            claveSesion=result['response']['data']['claveSesion']
            return [response,claveSesion]
        except Exception as e:
            return "Error al iniciar sesion",e 
    
    def cerrarSesion(self,urlLogin,clave):
        try:
            #print(args[0],args[1],args[2])
            urlLogin=urlLogin
            clave=clave
            if(clave[0]==True):
                cerrarSesionJson['parameters']['sesion']['claveSesion']=clave[1]
                #print(cerrarSesionJson)
                solicitud = requests.post(urlLogin,data=json.dumps(cerrarSesionJson),headers={'Content-Type':'application/json'})
                #print(response.status_code)
                #print(response.text)
                #convert text to dict
                result=json.loads(solicitud.text)
                response=result["response"]["success"]
                return response
            else:
                return False
        except:
            return "Error al cerrar sesion"