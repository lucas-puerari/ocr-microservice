import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from src.apis.core.liveness import liveness_handler
from src.apis.core.readiness import readiness_handler
from src.apis.core.checkup import checkup_handler
from src.apis.extract_text import extract_text_handler


load_dotenv('default.env')

app = FastAPI(
    openapi_url="/documentation/json",
    docs_url=None,
    redoc_url=None
)

# Core
app.include_router(liveness_handler.router)
app.include_router(readiness_handler.router)
app.include_router(checkup_handler.router)

# OCR
app.include_router(extract_text_handler.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)
