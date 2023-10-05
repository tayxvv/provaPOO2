from pydantic import BaseModel

class CursoByIdRequest(BaseModel):
    id: int