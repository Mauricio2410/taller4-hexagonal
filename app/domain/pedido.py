from pydantic import BaseModel

class Pedido(BaseModel):
    idpedido: int        
    idusuario: int       
    total: float         