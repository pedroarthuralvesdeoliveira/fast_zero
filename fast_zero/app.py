from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import (
    Message,
    OneUser,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = user_exists(user.username, session)

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/user_exists/', response_model=Message)
def user_exists(username: str, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.username == username))

    if db_user:
        raise HTTPException(
            status_code=400, detail='Username already registered'
        )

    return {'detail': 'You can now register your account'}


@app.get('/users/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@app.put('/users/{user_id}', response_model=OneUser)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = read_user(user_id, session)
    db_user['user'].username = user.username
    db_user['user'].password = user.password
    db_user['user'].email = user.email
    session.commit()
    session.refresh(db_user['user'])

    return db_user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = read_user(user_id, session)
    session.delete(db_user['user'])
    session.commit()

    return {'detail': 'User deleted'}


@app.get('/read_user/', response_model=OneUser)
def read_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return {'user': db_user}
