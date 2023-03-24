from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


app = FastAPI(
    title="FAST API",  # Meta Data
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "sujith",
        "email": "sujith@yopmail.com",
    },
    license_info={
        "name": "MIT",
    },
)
users: List = []
tags_metadata = [
    {"name": "Get Users", "description": "The Operation will get all the users data"},
    {"name": "Post Users", "description": "The Operation is to create the user"},
    {
        "name": "Get User By Id",
        "description": "This Operation is used the retrieve the Particular User Details",
    },
]


@app.get("/users", response_model=List[User], tags=["Get Users"])
async def get_users():
    return users


@app.post("/users", tags=["Post Users"])
async def post_users(user: User):
    users.append(user)
    return "success"


@app.get("/users/{id}", tags=["Get User By Id"])
async def get_user_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),
    q: str = Query(None, max_length=5),
):  # gt=2 --> greater than or equals to 2
    return {"user": users[id], "query": q}
