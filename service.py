from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users_hjghj(db: Session):
    res = {}
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_app_data(db: Session):

    query = db.query(models.AppData)

    app_data_all = query.all()
    app_data_all = (
        [new_data.to_dict() for new_data in app_data_all]
        if app_data_all
        else app_data_all
    )
    res = {
        "app_data_all": app_data_all,
    }
    return res


async def get_users_hgf(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def put_users_id(db: Session, id: int, username: str, password: str, email: str):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "password": password,
            "username": username,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def get_app_data_id(db: Session, id: int):

    query = db.query(models.AppData)
    query = query.filter(and_(models.AppData.id == id))

    app_data_one = query.first()

    app_data_one = (
        (
            app_data_one.to_dict()
            if hasattr(app_data_one, "to_dict")
            else vars(app_data_one)
        )
        if app_data_one
        else app_data_one
    )

    res = {
        "app_data_one": app_data_one,
    }
    return res


async def put_app_data_id(db: Session, id: int, user_id: int, data: str):

    query = db.query(models.AppData)
    query = query.filter(and_(models.AppData.id == id))
    app_data_edited_record = query.first()

    if app_data_edited_record:
        for key, value in {"id": id, "data": data, "user_id": user_id}.items():
            setattr(app_data_edited_record, key, value)

        db.commit()
        db.refresh(app_data_edited_record)

        app_data_edited_record = (
            app_data_edited_record.to_dict()
            if hasattr(app_data_edited_record, "to_dict")
            else vars(app_data_edited_record)
        )
    res = {
        "app_data_edited_record": app_data_edited_record,
    }
    return res


async def delete_app_data_id(db: Session, id: int):

    query = db.query(models.AppData)
    query = query.filter(and_(models.AppData.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        app_data_deleted = record_to_delete.to_dict()
    else:
        app_data_deleted = record_to_delete
    res = {
        "app_data_deleted": app_data_deleted,
    }
    return res


async def post_app_data(db: Session, id: int, user_id: int, data: str):

    record_to_be_added = {"id": id, "data": data, "user_id": user_id}
    new_app_data = models.AppData(**record_to_be_added)
    db.add(new_app_data)
    db.commit()
    db.refresh(new_app_data)
    app_data_inserted_record = new_app_data.to_dict()

    test = aliased(models.AppData)
    query = db.query(models.Users, test)

    query = query.join(test, and_(models.Users.id == test.id))

    test1234 = query.all()
    test1234 = (
        [
            {
                "test1234_1": s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__,
                "test1234_2": s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__,
            }
            for s1, s2 in test1234
        ]
        if test1234
        else test1234
    )
    res = {
        "app_data_inserted_record": app_data_inserted_record,
        "test1234": test1234,
    }
    return res


async def post_users(db: Session, id: int, username: str, password: str, email: str):

    record_to_be_added = {
        "id": id,
        "email": email,
        "password": password,
        "username": username,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    test = aliased(models.AppData)
    query = db.query(models.Users, test)

    query = query.join(test, and_(models.Users.username == models.Users.username))

    test = query.first()
    test = (
        [
            {
                "test_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "test_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in test
        ]
        if test
        else test
    )

    res = {
        "users_inserted_record": users_inserted_record,
        "test": test,
    }
    return res
