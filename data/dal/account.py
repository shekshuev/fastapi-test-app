from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from data.dto.account import CreateAccountDTO, UpdateAccountDTO
from data.dao.account import AccountEntity
from bcrypt import hashpw, gensalt
from errors import EntityNotFoundError, EntityIntegrityError, EntityAlreadyExistsError


async def get_total_count(db: Session) -> int:
    return db.query(AccountEntity).count()


async def get_all(db: Session, offset: int = 0, limit: int = 100) -> list:
    return db.query(AccountEntity).offset(offset).limit(limit).all()


async def get_by_id(db: Session, id: int) -> AccountEntity:
    account = db.query(AccountEntity).filter(AccountEntity.id == id).first()
    if account:
        return account
    else:
        raise EntityNotFoundError(f"Account with id={id} not found!")


async def get_by_username(db: Session, username: str):
    account = db.query(AccountEntity).filter(
        AccountEntity.username == username).first()
    if account:
        return account
    else:
        raise EntityNotFoundError(
            f"Account with username={username} not found!")


async def get_by_email(db: Session, email: str):
    account = db.query(AccountEntity).filter(
        AccountEntity.email == email).first()
    if account:
        return account
    else:
        raise EntityNotFoundError(f"Account with email={email} not found!")


async def create(db: Session, account_dto: CreateAccountDTO) -> AccountEntity:
    try:
        await get_by_username(db, account_dto.username)
        raise EntityAlreadyExistsError(
            f"Account with username={account_dto.username} already exists!")
    except EntityNotFoundError:
        pass
    try:
        await get_by_email(db, account_dto.email)
        raise EntityAlreadyExistsError(
            f"Account with username={account_dto.username} already exists!")
    except EntityNotFoundError:
        pass
    entity = AccountEntity(username=account_dto.username,
                           password_hash=hashpw(
                               account_dto.password.encode('utf-8'), gensalt()),
                           role=account_dto.role,
                           email=account_dto.email,
                           firstname=account_dto.firstname,
                           lastname=account_dto.lastname)
    db.add(entity)
    try:
        db.commit()
    except IntegrityError as e:
        raise EntityIntegrityError(
            orig=e.orig, statement=e.statement, params=e.params)
    db.refresh(entity)
    return entity


async def update(db: Session, account_dto: UpdateAccountDTO, id: int) -> AccountEntity:
    entity = await get_by_id(db, id)
    if not entity:
        raise EntityNotFoundError(f"Account with id={id} not found!")
    for key in vars(account_dto).keys():
        if hasattr(account_dto, key):
            if key == "password":
                setattr(entity, key, hashpw(
                    account_dto.password.encode('utf-8'), gensalt()))
            elif getattr(entity, key) != getattr(account_dto, key):
                setattr(entity, key, getattr(account_dto, key))
    try:
        db.commit()
    except IntegrityError as e:
        raise EntityIntegrityError(
            orig=e.orig, statement=e.statement, params=e.params)
    return entity


async def delete_by_id(db: Session, id: int):
    entity = await get_by_id(db, id)
    if not entity:
        raise EntityNotFoundError(f"Account with id={id} not found!")
    db.delete(entity)
    db.commit()
