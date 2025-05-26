#libs imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#routers imports
from router.accs import accs


app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

app.include_router(accs.router)
