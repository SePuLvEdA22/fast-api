from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.users import User
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', StaticFiles(directory="static"), name="static")


@app.get('/')
async def main():
    return {
        "status": 200,
        "message": "Pagina principal"
    }

# @app.get('/users/{id}')
# async def getUser(id: int):
#         for user in users:
#             if user['id'] == id:
#                 return user 
#         return JSONResponse(
#                 status_code=404,
#                 content={"message": f"the user with id {id} was not found"}
#         )
  
# @app.post('user')
# def create(user: User):
#     users.add(user)
