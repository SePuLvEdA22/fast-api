from fastapi import APIRouter
from data.products_list import product_list

router = APIRouter(prefix="/products",
                   tags=["Products"],
                   responses={404: {"message": "No se ha encontrado"}})

@router.get('/')
async def getProducts():
    return product_list

@router.get('/{id}')
async def getProduct(id: int):
    productFound = filter(lambda producto: producto.id == id, product_list)
    try: 
        return list(productFound)[0]
    except:
        return {"error": "no se encontro el producto"}