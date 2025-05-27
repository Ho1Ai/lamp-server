from fastapi import APIRouter

#data models
from dataModels.accs import accsGlobalDataModels as accs_data

#services
from services.acc import acc_service


router = APIRouter(prefix='/api/accounts')

@router.post('/registration')
async def regUser(nuser_data: accs_data.RegistrationData):
    response_status = {'is_ok': True, 'status_code': 0}

    testAvailability = await acc_service.checkUserAvailability(nuser_data)

    if(testAvailability.get('is_ok')):
        #print('available')
        userCreationStatus = await acc_service.createUser(nuser_data)
        
        if(userCreationStatus.get('is_ok')==True):
            response_status['created']='Yes'
        else:
            response_status['is_ok']=False
            response_status['status_code']=-1
            response_status['created']='False'
    else:
        response_status['is_ok'] = False
        response_status['status_code'] = 5
    #return {'uname': nuser_data.uname,
    #        'email': nuser_data.email,
    #        'passwd': nuser_data.passwd}
    return response_status

@router.post('/signin')
async def signInUser(user_data: accs_data.SignIn):
    response_status = {'is_ok': True, 'status_code': 0}
    
    testSignIn = await acc_service.signIn(user_data)
    
    if(testSignIn.get('is_ok')):
        response_status['is_ok'] = True
    else:
        response_status['is_ok'] = False
        response_status['status_code'] = 4

    return response_status
