#1.imprtaciones
from fastapi import FastAPI, status, HTTPException
from typing import Optional 
import asyncio 
#2.Inicializacion APP
app= FastAPI(
    title='mi primer API',
    description= "Fabian Osiel Perez Regino",
    version= '1.0.0'
    ) #Funcion

#BD ficticia 
usuarios = [
    {"id":"1", "nombre":"osiel","edad":"22"},
    {"id":"2", "nombre":"daniel","edad":"43"},
    {"id":"3", "nombre":"diego","edad":"20"}
]

#Endpoints
@app.get("/", tags= ['Inicio'])#Endpoint de Arranque o inicio
async def holaMundo():
    return {"mensaje":"Hola mundo FASTAPI"} 

@app.get("/v1/bienvenidos", tags= ['Inicio'])#Endpoint de Arranque o inicio
async def bien():
    return {"mensaje":"Bienvenidos"} 

@app.get("/v2/promedio", tags= ['Calificaciones'])#Endpoint de Arranque o inicio
async def promedio():
    await asyncio.sleep(3)#peticion a otra API o consulta a la base de datos .....
    return {"Calificacion":"7.5",
            "estus":"200"
            } 

@app.get("/v3/usuarioss/{id}", tags= ['Parametros'])#Endpoint de Arranque o inicio
async def consultaUno(id:int):
    await asyncio.sleep(3)
    return {
        "Resultado":"usuario encontrado",
        "Estatus":"200",
        } 

@app.get("/v4/usuarios_op/", tags= ['Parametro Opcional'])#Endpoint de Arranque o inicio
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(2)
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==id:
                return {"Usuario encontrado":id,"Datos":usuario }
            return{"Mensaje":"Usuariono encontrado"}
        else:
            return{"Aviso":"No se proporciono id"}
        
@app.get("/v5/usuarios/", tags= ['CRUD HTTP'])#Endpoint de Arranque o inicio
async def consultaT():
    return{
        "status":"200",
        "total": len(usuarios),
        "data":usuarios
    }

@app.post("/v1/usuarios/", tags= ['CRUD HTTP'])
async def crear_usuario(usuario:dict):
    for usr in usuarios:
        if usr ["id"] == usuario.get("id"):
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            ) 
    usuarios.append(usuario)
    return{
        "mensaje": "usuario agregado correctamente",
        "status":"200",
        "usuario":usuario
    }

@app.put("/v1/usuarios/", tags=['CRUD HTTP'])
async def actualizar_usuario(id: int, usuario_actualizado: dict):

    for usr in usuarios:
        if usr["id"] == str(id):
            usuario_actualizado["id"] = str(id)
            
            usr.update(usuario_actualizado)

            return {
                "mensaje": "Usuario actualizado correctamente",
                "status": "200",
                "usuario": usr
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )



@app.delete("/v1/usuarios/", tags=['CRUD HTTP'])
async def eliminar_usuario(id: int):

    for usr in usuarios:
        if usr["id"] == str(id):
            usuarios.remove(usr)
            return {
                "mensaje": "Usuario eliminado correctamente",
                "status": "200",
                "usuario": usr
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
