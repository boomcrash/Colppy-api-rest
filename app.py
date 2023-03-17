# libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
# inicializar flask con fastApi
from fastapi import FastAPI, Request
# router
from fastapi import APIRouter
# uvicorn execute fastApi
import uvicorn
# pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
# evitar cors
from fastapi.middleware.cors import CORSMiddleware
from controladores.ClienteController import cliente_router
from controladores.EmpresaController import empresa_router
from controladores.ContabilidadController import contabilidad_router


#inicializar fastApi
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    cliente_router,
    prefix='/api/v1/Clientes',
    tags=['Clientes'],
    responses={404: {'description': 'Error de acceso a la ventana de clientes'}},
) 

app.include_router(
    empresa_router,
    prefix='/api/v1/Empresas',
    tags=['Empresas'],
    responses={404: {'description': 'Error de acceso a la ventana de empresas'}},
)

app.include_router(
    contabilidad_router,
    prefix='/api/v1/Contabilidad',
    tags=['Contabilidad'],
    responses={404: {'description': 'Error de acceso a la ventana de contabilidad'}},
)

#app.include_router(user_router, prefix="/api/v1")

if __name__=="__main__":
    uvicorn.run(app,host=configuracion['development'].HOST,port=configuracion['development'].PORT)

