from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Bienvenue, la doc c'est par ici: /docs"}
