from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/hjghj')
async def get_users_hjghj(db: Session = Depends(get_db)):
    try:
        return await service.get_users_hjghj(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/app_data/')
async def get_app_data(db: Session = Depends(get_db)):
    try:
        return await service.get_app_data(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/hgf')
async def get_users_hgf(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_hgf(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, username, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/app_data/id')
async def get_app_data_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_app_data_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/app_data/id/')
async def put_app_data_id(id: int, user_id: int, data: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_app_data_id(db, id, user_id, data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/app_data/id')
async def delete_app_data_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_app_data_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/app_data/')
async def post_app_data(id: int, user_id: int, data: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_app_data(db, id, user_id, data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(id: int, username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, id, username, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

