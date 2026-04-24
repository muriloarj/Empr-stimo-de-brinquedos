from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.crianca import router as crianca_router
from api.routes.brinquedo import router as brinquedo_router

app = FastAPI(
                title="Projeto Brinquedoteca", 
                description="API para emprestimos de brinquedos", 
                version="1.0.0"
            )

app.include_router(health_router)
app.include_router(crianca_router)
app.include_router(brinquedo_router)