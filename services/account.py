from sqlalchemy.orm import Session
from data.dao.account import AccountEntity
from data.dto.account import CreateAccountDTO, UpdateAccountDTO, ReadAccountDTO
from data.dal.account import create, get_all, get_by_id, update, delete_by_id, get_total_count


async def get_accounts_count(db: Session) -> int:
    return await get_total_count(db)


async def get_all_accounts(db: Session, offset: int, limit: int) -> list:
    return [ReadAccountDTO.from_entity(account_entity) for account_entity in await get_all(db, offset, limit)]


async def get_account_by_id(db: Session, id: int) -> AccountEntity:
    return ReadAccountDTO.from_entity(await get_by_id(db, id))


async def create_account(db: Session, account: CreateAccountDTO) -> AccountEntity:
    return ReadAccountDTO.from_entity(await create(db, account))


async def update_account(db: Session, account: UpdateAccountDTO, id: int) -> AccountEntity:
    return ReadAccountDTO.from_entity(await update(db, account, id))


async def delete_account(db: Session, id: int):
    await delete_by_id(db, id)
