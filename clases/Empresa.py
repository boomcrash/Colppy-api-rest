    
import requests
import json
import os
listarEmpresasJson=json.load(open("ModulosJson/empresa/listarEmpresas.json"))



class Sesion:

    def __init__(self) :
        self.usuario=os.environ.get('usuarioItiers')
        self.password=os.environ.get('passwordItiers')

    def listarEmpresas(self,urlLogin,clave):
        try:
            if(clave[0]==True):
                listarEmpresasJson['parameters']['sesion']['claveSesion']=clave[1]
                #print(listarEmpresasJson)
                solicitud = requests.post(urlLogin,data=json.dumps(listarEmpresasJson),headers={'Content-Type':'application/json'})
                #print(response.status_code)
                #print(solicitud.text)
                #convert text to dict
                result=json.loads(solicitud.text)
                response=result["response"]["success"]
                data=result["response"]["data"]
                return [response,data]
            else:
                return [False,'']   
            
        except:
            return "Error al listar empresas"