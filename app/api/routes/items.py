from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def getMenu():
    return {"message": "Hello World"}


@router.get('/{item_id}')
async def getItem():
    return


@router.post('/')
async def postItem():
    return


@router.delete('/{item_id}')
async def deleteItem():
    return
