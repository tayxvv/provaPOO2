from pydantic import BaseModel

class CursoRequest(BaseModel):
    id: int
    titulo: str
    aulas: int
    horas: str
    dia: str