import uvicorn
from fastapi import FastAPI
from controllers.account import router as accounts_router
from data.dal.setup import Base, engine
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from errors import EntityIntegrityError, EntityNotFoundError, EntityAlreadyExistsError


app = FastAPI()
app.include_router(accounts_router)
Base.metadata.create_all(engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, e: RequestValidationError):
    return JSONResponse(status_code=400, content={
        "detail": e.errors()[0]["msg"]
    })


@app.exception_handler(EntityIntegrityError)
async def account_integrity_exception_handler(request, e: EntityIntegrityError):
    return JSONResponse(status_code=400, content={
        "detail": str(e.orig)
    })


@app.exception_handler(EntityNotFoundError)
async def account_not_found_exception_handler(request, e: EntityNotFoundError):
    return JSONResponse(status_code=400, content={
        "detail": str(e)
    })


@app.exception_handler(EntityAlreadyExistsError)
async def account_exists_exception_handler(request, e: EntityAlreadyExistsError):
    return JSONResponse(status_code=400, content={
        "detail": str(e)
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
