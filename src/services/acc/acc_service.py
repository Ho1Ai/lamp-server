from db_connect import db
import bcrypt

from dataModels.accs import accsGlobalDataModels as accs_data

async def checkUserAvailability(nuser_data: accs_data.RegistrationData):
    pool = await db.db_conn()
    conn = await pool.acquire()
    uname_test = await conn.fetchrow('select * from lampdb_users where uname = $1', nuser_data.uname)
    email_test = await conn.fetchrow('select * from lampdb_users where email = $1', nuser_data.email)
    if(uname_test or email_test):
        return {'is_ok': False}
    else:
        return {'is_ok': True}

    conn.close()
    pool.close()


async def createUser(nuser_data: accs_data.RegistrationData):
    pool = await db.db_conn()
    conn = await pool.acquire()
    
    func_return = {'is_ok':True}
    
    try:
        hashed_passwd = bcrypt.hashpw(nuser_data.passwd.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        testCreation = await conn.execute('insert into lampdb_users (email, uname, passwd) values ($1, $2, $3)', nuser_data.email, nuser_data.uname, hashed_passwd)
        if testCreation:
            func_return['is_ok']=True
        else:
            func_return['is_ok']=False
    except Exception:
        print('Exception!')
        func_return['is_ok']=False

    #return func_return

    await conn.close()
    await pool.close()
    return func_return


async def signIn(user_data: accs_data.SignIn):
    pool = await db.db_conn()
    conn = await pool.acquire()

    func_return={'is_ok': True}

    try:
        getUserDataDB = await conn.fetchrow('select * from lampdb_users where email = $1', user_data.email) # you can sign in only using email. I did it in order to make it more safe
        if(getUserDataDB):
            #print('existence = True')
            passwdTest = bcrypt.checkpw(user_data.passwd.encode('utf-8'), getUserDataDB.get('passwd').encode('utf-8'))
            if(passwdTest):
                func_return['is_ok']=True
                func_return['email']=getUserDataDB.get('email')
                func_return['uname']=getUserDataDB.get('uname')
                func_return['user_id']=getUserDataDB.get('id')
            else:
                func_return['is_ok']=False
        else:
            func_return['is_ok']=False
    except Exception:
        print('Exception!')
        func_return['is_ok']=False


    await conn.close()
    await pool.close()

    return func_return
    
