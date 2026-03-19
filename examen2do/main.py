from fastapi import FastAPI, status, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel, Field
import asyncio
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


app = FastAPI(
    title='examen',
    description= "Fabian Osiel Perez Regino",
    version= '1.0.0'
    ) 

reservas = [
    {"id":"1","nombre":"osiel","fecha de inicio":"2 de marzo","fecha del fin":"8"},
    {"id":"2","nombre":"daniel","fecha de inicio":"3 de marzo","fecha del fin":"9"},
    {"id":"3","nombre":"diego","fecha de inicio":"4 de marzo","fecha del fin":"10"},
]

# seguridad http basic
seguridad = HTTPBasic()

def verificar_peticion(credenciales: HTTPBasicCredentials = Depends(seguridad)):
    userAuth = secrets.compare_digest(credenciales.username, "hotel")
    passAuth = secrets.compare_digest(credenciales.password, "r2026")

    if not (userAuth and passAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no Autorizadas"
        )
    return credenciales.username

@app.get("/v1/usuarios/", tags=['Parametros'])
async def consultaUno(id: int):
    await asyncio.sleep(3)

    for usuario in reservas:
        if usuario["id"] == id:
            return {
                "Resultado": "reserva no encontrada",
                "Estatus": "200",
                "usuario": usuario
            }


@app.post("/v1/usuarios/", tags=['CRUD HTTP'])
async def crear_usuario(reservas:Reservas):

    for usr in reservas:
        if usr ["id"] == reservas.get("id"):

            if usr["id"] == int(reservas.id):
                raise HTTPException(
                    status_code=400,
                    detail="El id ya existe"
                ) 
            reservas.append(reservas)
        
            return{        
                reservas.append({
                    "id": int(reservas.id),
                    "nombre": reservas.nombre,
                    "edad": str(reservas.edad)
                })
            }

    return {
        "mensaje": "reservacion agregada correctamente",
        "status":"200",
        "reservas":reservas
    }


@app.put("/v1/usuarios/", tags=['CRUD HTTP'])
async def actualizar_usuario(id: int, reservas_actualizado: dict):

    for usr in reservas:
        if usr["id"] == str(id):
            reservas_actualizado["id"] = str(id)
            
            usr.update(reservas_actualizado)

            return {
                "mensaje": "Reserva actualizada correctamente",
                "status": "200",
                "usuario": usr
            }

    raise HTTPException(
        status_code=404,
        detail="Reserva no encontrado"
    )


@app.delete("/v1/usuarios/", tags=['CRUD HTTP'])
async def eliminar_usuario(id: int):
    for index, usr in enumerate(reservas):
        if usr["id"] == id:
            reservas.pop(index)

    for usr in reservas:
        if usr["id"] == str(id):
            reservas.remove(usr)
            return {
                "mensaje": "reservacion eliminada correctamente",
                "status": "200",
                "usuario": usr,
                "mensaje": f"Usuario eliminado por {userAuth}",
            }

    raise HTTPException(
        status_code=404,
        detail="reservacion no encontrada"
    )

