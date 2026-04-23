from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.livro import BrinquedoCreate, LivroOut
from services.emprestimo_service import (
)