from pydantic import BaseModel
class EmprestimoCreate(BaseModel):
    id_crianca: int
    id_brinquedo: int
   

class EmprestimoOut(BaseModel):
    id: int
    id_crianca: int
    status: bool