from fastapi import APIRouter

#data models
from dataModels.accs import accsGlobalDataModels as accs_data

#services
from services.acc import acc_service


router = APIRouter(prefix='/api/accounts')

@router.post('/registration')
async def regUser(nuser_data: accs_data.RegistrationData):
    tester = await acc_service.createUser(nuser_data)
    #return {'uname': nuser_data.uname,
    #        'email': nuser_data.email,
    #        'passwd': nuser_data.passwd}
    return tester
