from fastapi import FastAPI, status, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel, Field
import asyncio
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI(
    title='mi primer API',
    description="Fabian Osiel Perez Regino",
    version='1.0.0'
)

usuarios = [
    {"id": 1, "nombre": "osiel", "edad": "22"},
    {"id": 2, "nombre": "daniel", "edad": "43"},
    {"id": 3, "nombre": "diego", "edad": "20"}
]


class Usuario(BaseModel):
    id: str = Field(min_length=1)
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(gt=0, lt=100)


# seguridad http basic
seguridad = HTTPBasic()


def verificar_peticion(credenciales: HTTPBasicCredentials = Depends(seguridad)):
    userAuth = secrets.compare_digest(credenciales.username, "osiel")
    passAuth = secrets.compare_digest(credenciales.password, "123456")

    if not (userAuth and passAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no Autorizadas"
        )
    return credenciales.username


@app.get("/", tags=['Inicio'])
async def holaMundo():
    return {"mensaje": "Hola mundo FASTAPI"}


@app.get("/v1/bienvenidos", tags=['Inicio'])
async def bien():
    return {"mensaje": "Bienvenidos"}


@app.get("/v2/promedio", tags=['Calificaciones'])
async def promedio():
    await asyncio.sleep(3)
    return {
        "Calificacion": "7.5",
        "estatus": "200"
    }


@app.get("/v3/usuarioss/{id}", tags=['Parametros'])
async def consultaUno(id: int):
    await asyncio.sleep(3)

    for usuario in usuarios:
        if usuario["id"] == id:
            return {
                "Resultado": "usuario encontrado",
                "Estatus": "200",
                "usuario": usuario
            }

    return {"Mensaje": "Usuario no encontrado"}


@app.get("/v4/usuarios_op/", tags=['Parametro Opcional'])
async def consultaOp(id: Optional[int] = None):
    await asyncio.sleep(2)

    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Usuario encontrado": id, "Datos": usuario}

        return {"Mensaje": "Usuario no encontrado"}

    else:
        return {"Aviso": "No se proporciono id"}


@app.get("/v5/usuarios/", tags=['CRUD HTTP'])
async def consultaT():
    return {
        "status": "200",
        "total": len(usuarios),
        "data": usuarios
    }


@app.post("/v1/usuarios/", tags=['CRUD HTTP'])
async def crear_usuario(usuario: Usuario):

    for usr in usuarios:
        if usr["id"] == int(usuario.id):
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )

    usuarios.append({
        "id": int(usuario.id),
        "nombre": usuario.nombre,
        "edad": str(usuario.edad)
    })

    return {
        "mensaje": "usuario agregado correctamente",
        "status": "200",
        "usuario": usuario
    }


@app.put("/v1/usuarios/", tags=['CRUD HTTP'])
async def actualizar_usuario(id: int, usuario_actualizado: dict):

    for usr in usuarios:
        if usr["id"] == id:
            usuario_actualizado["id"] = id
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


@app.delete("/v1/usuarios/{id}", tags=['CRUD HTTP'])
async def elimina_usuario(id: int, userAuth: str = Depends(verificar_peticion)):

    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)

            return {
                "mensaje": f"Usuario eliminado por {userAuth}"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
               
                            
                                       
                                        


                                         
                                           
                                             
                                              
                                               
                                                
                                                 
                                                  
                                                   

                                                    
                                                     
                                                      
                                                       
                                                        

                                                         
                                                          
                                                           
                                                            
                                                            