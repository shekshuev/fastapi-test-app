from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.dal.setup import get_db
from data.dto.account import CreateAccountDTO, UpdateAccountDTO
from services.account import get_all_accounts, create_account, get_account_by_id, update_account, \
    delete_account, get_accounts_count
from typing import Optional

router = APIRouter()

api_url = f"/api/v1/accounts"


@router.get(api_url)
async def get_accounts(db: Session = Depends(get_db), count: Optional[int] = 10, offset: Optional[int] = 0):
    return {
        "total_count": await get_accounts_count(db),
        "accounts": await get_all_accounts(db, offset=offset, limit=count)
    }


@router.get(f"{api_url}/{{account_id}}")
async def get_account(account_id: int, db: Session = Depends(get_db)):
    return await get_account_by_id(db, account_id)


@router.post(api_url, status_code=201)
async def create_account_async(account: CreateAccountDTO, db: Session = Depends(get_db)):
    return await create_account(db, account)


@router.put(f"{api_url}/{{account_id}}")
async def update_account_async(account: UpdateAccountDTO, account_id: int, db: Session = Depends(get_db)):
    return await update_account(db, account, account_id)


@router.delete(f"{api_url}/{{account_id}}", status_code=204)
async def delete_account_async(account_id: int, db: Session = Depends(get_db)):
    await delete_account(db, account_id)
