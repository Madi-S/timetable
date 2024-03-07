import uuid
import asyncio
import aiobcrypt


class classproperty(property):
    def __get__(self, cls, owner):
        """Wrapper for @property and @classmethod"""
        return classmethod(self.fget).__get__(None, owner)()


class Secret:
    @classproperty
    def token(cls) -> str:
        """Returns a random uuid4 token"""
        return 'token-' + str(uuid.uuid4())

    @classproperty
    def slug(cls) -> str:
        """Returns a random 22-character length slug"""
        return uuid.uuid4().hex[:22]

    @classmethod
    async def generate_password_hash(cls, password: str) -> bytes:
        """Generates bytes password hash from given password"""
        salt = await aiobcrypt.gensalt()
        hashed_password = await aiobcrypt.hashpw(password.encode(), salt)
        return hashed_password

    @classmethod
    async def verify_password(cls, plain_password: str, hashed_password: bytes) -> bool:
        """Validates whether or not plain password match with hash"""
        return await aiobcrypt.checkpw(plain_password.encode(), hashed_password)


async def _test():
    """Test function for Secret password generation & verification"""
    password = b'123qwerty'
    hashed_password = await Secret.generate_password_hash(password)
    verified = await Secret.verify_password(password, hashed_password)
    return verified


if __name__ == '__main__':
    asyncio.run(_test())
