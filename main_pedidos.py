from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="Microservicio Pedidos - Puerto 8002")

pedidos_db = []

class Pedido(BaseModel):
    idpedido: int
    idusuario: int
    total: float

@app.post("/pedidos")
def crear_pedido(pedido: Pedido):
    pedidos_db.append(pedido)
    return {"status": "success", "pedido": pedido}

@app.get("/pedidos")
def listar_pedidos():
    return pedidos_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)