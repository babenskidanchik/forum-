from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_forum():
    return {"message": "Forum works!"}