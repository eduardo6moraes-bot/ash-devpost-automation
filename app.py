from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from automation import ejecutar_submissao

app = FastAPI()

class AplicativoASH(BaseModel):
    titulo: str
    descricao: str
    github_url: str
    hackathon_url: str

@app.post("/submeter")
async def submeter(app_data: AplicativoASH, background_tasks: BackgroundTasks):
    background_tasks.add_task(ejecutar_submissao, app_data.model_dump())
    return {"status": "Processamento iniciado", "mensagem": f"O agente está submetendo o {app_data.titulo} de forma autônoma"}
