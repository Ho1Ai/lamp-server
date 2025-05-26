from db_connect import db

from dataModels.accs import accsGlobalDataModels as accs_data

async def createUser(nuser_data: accs_data.RegistrationData):
    pool = await db.db_conn()
    conn = await pool.acquire()
    uname_test = conn.fetchrow('select * from lampdb_users where name = $1', nuser_data.uname)
    email_test = conn.fetchrow('select * from lampdb_users where email = $1', nuser_data.email)
    if(uname_test or email_test):
        return {'is_ok': False}

    conn.close()
    pool.close()
