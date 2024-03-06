from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "modified_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL,
    "password_hash" BYTEA NOT NULL,
    "token" VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "note" (
    "modified_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(150) NOT NULL,
    "description" TEXT,
    "datetime_from" TIMESTAMPTZ NOT NULL,
    "datetime_to" TIMESTAMPTZ NOT NULL,
    "color" SMALLINT NOT NULL  DEFAULT 1,
    "category" VARCHAR(100) NOT NULL  DEFAULT 'physical',
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "note"."color" IS 'RED: 1\nBLUE: 2\nGREEN: 3\nYELLOW: 4';
COMMENT ON COLUMN "note"."category" IS 'SOCIAL: social\nPHYSICAL: physical\nSPIRITUAL: spiritual\nPSYCHOLOGICAL: psychological';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
