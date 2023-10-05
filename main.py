import asyncio
import uvicorn
from fastapi import FastAPI
from Controller.curso import curso_router

app = FastAPI()

app.include_router(curso_router)
async def main():
    config = uvicorn.Config("main:app", port=8001, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
    print("Olá")