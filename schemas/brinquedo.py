from pydantic import BaseModel

class BrinquedoCreate(BaseModel):
    id: : int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = true

class BrinquedoOut(BaseModel):
    id: : int
    nome: str
    categoria: str
    faixa_etaria_minima: float
    disponivel: str