from asyncpg import create_pool

async def db_conn():
    return await create_pool('postgres://postgres:root@localhost/lampdb')
