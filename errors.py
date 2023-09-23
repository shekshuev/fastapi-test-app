from sqlalchemy.exc import IntegrityError


class EntityAlreadyExistsError(ValueError):
    pass


class EntityNotFoundError(ValueError):
    pass


class EntityIntegrityError(IntegrityError):
    pass
