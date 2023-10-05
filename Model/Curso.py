from typing import Optional

class Curso():
    id: int
    titulo: str
    aulas: int
    horas: str
    dia: str

    def __init__(self, id, titulo, aulas, horas, dia):
        self.id = id
        self.titulo = titulo
        self.aulas = aulas
        self.horas = horas
        self.dia = dia