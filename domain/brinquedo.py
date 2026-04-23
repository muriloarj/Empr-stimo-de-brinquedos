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
    produto = service.obter_produto(codigo)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return ProdutoOut(**produto.__dict__)

