from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from .log import setup_logging
from .storage import get_random_fortune

setup_logging()
app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FortuneRequest(BaseModel):
    language: Optional[str]


class FortuneResponseParams(BaseModel):
    pass


class FortuneResponse(BaseModel):
    id: str
    text: str
    params: Optional[FortuneResponseParams]


@app.post('/apiv1/fortune', response_model=FortuneResponse)
async def fortune(fortune_request: FortuneRequest):
    fortune = get_random_fortune()
    if fortune:
        return FortuneResponse(**fortune)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
