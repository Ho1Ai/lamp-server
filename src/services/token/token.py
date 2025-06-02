from jose import jwt
from datetime import datetime, timedelta
from dotenv import dotenv_values

from dataModels.token import token as token_model

denv_val = dotenv_values('.env')

cfg_token={'access_secret':denv_val.get('ACCESS_JWT_SECRET'),
         'refresh_secret': denv_val.get('REFRESH_JWT_SECRET'),
         'algorithm': denv_val.get('ALGORITHM'),
           'access_expire_mins': denv_val.get('ACCESS_EXPIRE_MINS'),
           'refresh_expire_days': denv_val.get('REFRESH_EXPIRE_DAYS')
           }


def createAccessJWT(user_data: token_model.TokenData):
    new_jwt_data = user_data
    new_jwt_data['expire_on']=(datetime.utcnow()+timedelta(minutes=int(cfg_token.get('access_expire_mins')))).isoformat()

    jwt_access = jwt.encode(new_jwt_data, cfg_token.get('access_secret'), cfg_token.get('algorithm'))
    return jwt_access



def createRefreshJWT(user_data: token_model.TokenData):
    new_jwt_data = user_data
    new_jwt_data['expire_on']=(datetime.utcnow()+timedelta(days=int(cfg_token.get('refresh_expire_days')))).isoformat()
    
    jwt_refresh = jwt.encode(new_jwt_data, cfg_token.get('refresh_secret'), cfg_token.get('algorithm'))
    
    return jwt_refresh


def createTokenPair(user_data: token_model.TokenData):
    #print(user_data)
    func_return = {
            #'is_ok': False,
            'access_JWT': None,
            'refresh_JWT': None
            }
    
    jwt_access = createAccessJWT(user_data)
    jwt_refresh = createRefreshJWT(user_data)
    if jwt_access and jwt_refresh:
        #func_return['is_ok']=True
        func_return['access_JWT']=jwt_access
        func_return['refresh_JWT']=jwt_refresh
    #else:
        #func_return['is_ok']=False

    return func_return
