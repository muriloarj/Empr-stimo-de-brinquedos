from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.livro import BrinquedoCreate, LivroOut
from services.biblioteca_service import (
    criar_brinquedo,
    listar_brinquedo,
    buscar_brinquedo,
    alterar_preco_brinquedo,
)

router = APIRouter(prefix="/livros", tags=["Livros"])

class AlterarPrecoInput(BaseModel):
    preco: float

@router.post("", response_model=LivroOut)
def post_livro(data: BrinquedoCreat):
    return criar_briquedo(data)

@router.get("", response_model=list[brinqudoOut])
def get_brinquedo():
    return listar_brinquedo()

@router.get("/{codigo}", response_model=BrinqudoOutOut)
def get_brinquedo(codigo: int):
    brinquedo = buscar_brinquedo(codigo)
    if not brinquedo:
        raise HTTPException(status_code=404, detail="Brinquedo não encontrado.")
    return livro

@router.put("/{codigo}/preco", response_model=BrinquedoOutOut)
    def put_preco_brinquedo(codigo: int, data: AlterarPrecoInput):
        brinquedo = alterar_preco_brinquedo(codigo, data.preco)
        if not brinquedo:
            raise HTTPException(status_code=404, detail="Brinquedo não encontrado.")
        return livro

@router.get("/{codigo}/preco-final")
def get_preco_final(codigo: int):
    if not brinquedo:
        raise HTTPException(status_code=404, detail="Brinquedo não encontrado")
    return {"codigo": livro.codigo, "titulo": livro.titulo, "preco_final": brinquedo.preco_final()}