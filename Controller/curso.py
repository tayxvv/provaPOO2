from fastapi import APIRouter
from Model.Curso import Curso
from Model.CursoRequest import CursoRequest
from Model.CursoByIdRequest import CursoByIdRequest
from fastapi.responses import JSONResponse
import json  

curso_router = APIRouter(tags=["Curso"])

cursos = dict()
listaCurso = []

@curso_router.post('/curso/create', summary="Criar um novo curso")
async def post_curso(curso: CursoRequest):
    curso = Curso(id=curso.id, titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas, dia=curso.dia)
    listaCurso.append({'id': curso.id, 'titulo': curso.titulo, 'aulas': curso.aulas, 'horas': curso.horas, 'dia': curso.dia})
    return JSONResponse(content={"message": "Curso criado com sucesso!"}, status_code=201)

@curso_router.get('/curso/getCurso', summary="Mostrar os cursos")
async def get_curso():
    return JSONResponse(content={"message": listaCurso}, status_code=201)

@curso_router.get('/curso/getCursoById', summary="Mostrar os cursos")
async def get_curso_id(curso: CursoByIdRequest):
    print(listaCurso)
    for cursos in listaCurso:
        if cursos['id'] == curso.id:
            return JSONResponse(content={"message": cursos}, status_code=201)
    return JSONResponse(content={"message": "Curso não encontrado!"}, status_code=201)

@curso_router.put('/curso/alter', summary="Alterar um curso")
async def put_curso(curso: CursoRequest):
    for cursos in listaCurso:
        if cursos['id'] == curso.id:
            cursos['titulo'] = curso.titulo
            cursos['aulas'] = curso.aulas
            cursos['horas'] = curso.horas
            cursos['dia'] = curso.dia
            return JSONResponse(content={"message": cursos}, status_code=201)
    return JSONResponse(content={"message": "Curso não encontrado!"}, status_code=201)

@curso_router.delete('/curso/delete', summary="Deletar um curso")
async def delete_curso(curso: CursoByIdRequest):
    for cursos in listaCurso:
        if cursos['id'] == curso.id:
            listaCurso.remove(cursos)
            return JSONResponse(content={"message": "Deletado com sucesso"}, status_code=201)
    return JSONResponse(content={"message": "Curso não encontrado!"}, status_code=201)