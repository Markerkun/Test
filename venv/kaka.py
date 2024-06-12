from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# модельь користувача
class User(BaseModel):
    id: int
    name: str
    email: str


# список користувачів
users = [
    User(id=1, name="Rick", email="Rick@gmail.com"),
    User(id=2, name="Bob", email="Bob@gmail.com")
]


# отримання користувача по id
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# отримання всіх користувачів
@app.get("/users", response_model=List[User])
async def get_users():
    return users


# додавання користувача
@app.post("/create_user", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)