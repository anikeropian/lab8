from fastapi import FastAPI
from controllers.task_controller import router

app = FastAPI(title="MVC App")
app.include_router(router)
