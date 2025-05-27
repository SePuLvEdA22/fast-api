from fastapi import APIRouter, HTTPException
from models.user import User
from data.users_list import users_list

router = APIRouter()

@router.get('/users')
async def getUsers():
    return users_list

# Path
@router.get('/user/{id}')
async def getUser(id: int):
    return search_user(id)

# Query
# http://127.0.0.1:8000/userquery?id=3
@router.get('/userquery')
async def user(id: int):
    return search_user(id)
    
def search_user(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se encontro el usuario."}

@router.post('/user', response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe.")
    else: 
        users_list.routerend(user)
        return user
            
    
@router.put('/user')
async def updateUser(user: User):
    
    found: bool = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
    else:
        return {
            "message": "usuario actualizado correctamente",
            "user": user
        }

@router.delete('/user/{id}')
async def deleteUser(id: int):
    for index, user in enumerate(users_list):
        if user.id == id:
            del users_list[index]