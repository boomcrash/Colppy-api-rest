from pydantic import BaseModel


class leerNumeroRecibo(BaseModel):
    idEmpresa: int = None
    prefijo: int = None


class listarCCostos(BaseModel):
    idEmpresa: int = None
    ccosto: int = None
