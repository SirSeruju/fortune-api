from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Dict
from typing import Optional

from .log import setup_logging
from .storage import get_random_fortune

setup_logging()
app = FastAPI(
    openapi_url=f"/api/openapi.json",
    docs_url=f"/api/docs"
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
