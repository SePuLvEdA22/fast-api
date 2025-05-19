from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name: str
    surname: str
    email: str
    age: int

users_list = [
    User(id=1, name="Helger", surname="Santiago", email="helgersantiago22@gmail.com", age=22),
    User(id=2, name="Carlos", surname="Santiago", email="helgersantiago22@gmail.com", age=22),
    User(id=3, name="Brayan", surname="Santiago", email="helgersantiago22@gmail.com", age=22),
    ] 

@app.get('/users')
async def getUsers():
    return users_list

# Path
@app.get('/user/{id}')
async def getUser(id: int):
    return search_user(id)

# Query
# http://127.0.0.1:8000/userquery?id=3
@app.get('/userquery')
async def user(id: int):
    return search_user(id)
    
def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se encontro el usuario."}

@app.post('/user', status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe.")
        
    else: 
        users_list.append(user)
        return {
                "message": "Usuario creado correctamente",
                "user": user
            }
    
@app.put('/user')
async def updateUser(user: User):
    
    found: bool = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error": "No se ha encontrado el usuario."}
    else:
        return {
            "message": "usuario actualizado correctamente",
            "user": user
        }

@app.delete('/user/{id}')
async def deleteUser(id: int):
    for index, user in enumerate(users_list):
        if user.id == id:
            del users_list[index]