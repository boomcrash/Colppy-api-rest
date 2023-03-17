from pydantic import BaseModel


class leerCliente(BaseModel):
    idEmpresa: int = None
    idCliente: int = None


class leerFondosPagos(BaseModel):
    idEmpresa: int = None
    idCobro: int = None
    add: int = None