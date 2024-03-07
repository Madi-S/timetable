import uuid
from passlib.context import CryptContext


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class Secret:
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classproperty
    def token(cls) -> str:
        return 'token-' + str(uuid.uuid4())

    @classproperty
    def slug(cls) -> str:
        return uuid.uuid4().hex[:22]

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)
