from dataclasses import dataclass
@dataclass
class brinquedo:
    id: : int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = true

@router.get("/{codigo}", response_model=ProdutoOut)
def obter(codigo: int):
    brinquedo = service.obter_brinquedo(codigo)
    if not brinquedo:
        raise HTTPException(status_code=404, detail="Brinquedo não encontrado")
    return BrinquedoOut(**brinquedo.__dict__)

