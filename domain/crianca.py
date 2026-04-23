from dataclasses import dataclass

@dataclass(frozen=True)
class crianca:
    id: int
    nome: str
    idade: float
    responsavel: str