from fastapi import FastAPI
from pydantic import BaseModel
from router import ModelRouter

app = FastAPI()
model_router = ModelRouter()

# define data models
class TextCategoryRequest(BaseModel):
    text: str

class TextCategoryResponse(BaseModel):
    response: str

@app.on_event("startup")
def startup_event() -> None:
    """Run on startup"""
    model_router.startup_event()


@app.get("/healthcheck")
def healthcheck() -> str:
    return {"status": "ok"}

@app.post("/text-category")
def get_text_category(request: TextCategoryRequest, response_model=TextCategoryResponse) -> str:
    return model_router.predict(request.text)
