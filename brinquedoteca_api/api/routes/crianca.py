from fastapi import APIRouter, HTTPException
from schemas.crianca import CriancaCreate, CriancaOut
from services.brinquedoteca_service import service

router = APIRouter(prefix="/crianca", tags=["criancas"])

@router.post("", response_model=CriancaOut)
def criar(payload: CriancaCreate):
    crianca = service.criar_crianca(payload.id, payload.nome)
    return CriancaOut(id=crianca.id, nome=crianca.nome)

@router.get("/{id}", response_model=CriancaOut)
def obter(id: int):
    crianca = service.obter_crianca(id)
    if not crinaca:
        raise HTTPException(
            status_code=404, 
            detail="crianca não encontrado"
            )
    return CriancaOut(id=crinaca.id, nome=crianca.nome)