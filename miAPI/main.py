#1.imprtaciones
from fastapi import FastAPI


#2.Inicializacion APP
app= FastAPI() #Funcion


#3.Endpoints
@app.get("/")#Endpoint de Arranque o inicio
async def holaMundo():
    return {"mensaje":"Hola mundo FASTAPI"} 

@app.get("/")#Endpoint de Arranque o inicio
async def bien():
    return {"mensaje":"Bienvenidos"} 