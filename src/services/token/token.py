from jose import jwt
from datetime import datetime, timedelta
from dotenv import dotenv_values

from dataModels.token import token as token_model

de_val = dotenv_values('.env').get()


def createAccessJWT(user_data: token_model.TokenData):
    jwt_access = jwt.encode(user_data, cfg_token.get('access_secret'), cfg_token.get('algorithm'))




def createTokenPair(user_data: token_model.TokenData):
    print(user_data)
    func_return = {
            'access_JWT': None,
            'refresh_JWT': None
            }
    
    jwt_access = createAccessJWT(user_data)

    return func_return
