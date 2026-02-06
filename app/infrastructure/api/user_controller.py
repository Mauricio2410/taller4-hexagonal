from fastapi import APIRouter, HTTPException
from app.domain.user import User
from app.infrastructure.adapters.memory_user_repo import MemoryUserRepository

router = APIRouter()
repo = MemoryUserRepository()

@router.post("/usuarios")
def create_user(user: User):
    return repo.save(user)

@router.get("/usuarios")
def list_users():
    return repo.get_all()

@router.get("/usuarios/{user_id}")
def read_user(user_id: int):
    user = repo.get_by_id(user_id)
    if not user: raise HTTPException(status_code=404, detail="No encontrado")
    return user

@router.put("/usuarios/{user_id}")
def update_user(user_id: int, user: User):
    return repo.update(user_id, user)

@router.delete("/usuarios/{user_id}")
def delete_user(user_id: int):
    if repo.delete(user_id): return {"msg": "Eliminado"}
    raise HTTPException(status_code=404)