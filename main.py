from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils.functions import load_json
from users import User

app = FastAPI()

users = load_json()

@app.get('/')
async def main():
    return {
        "status": 200,
        "message": "Pagina principal"
    }

@app.get('/users/{id}')
async def getUser(id: int):
        for user in users:
            if user['id'] == id:
                return user 
        return JSONResponse(
                status_code=404,
                content={"message": f"the user with id {id} was not found"}
        )
  
# @app.post('user')
# def create(user: User):
#     users.add(user)
