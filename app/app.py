from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from app.routes.summarize import router as sum_router


app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*", 'http://127.0.0.1:5500/','https://localhost:3000','https://localhost:3001'],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(sum_router)

