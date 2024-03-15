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
def healthcheck():
    return {"status": "ok"}

@app.post("/text-category")
def get_text_category(request: TextCategoryRequest, response_model=TextCategoryResponse):
    # Your code to process the text and return its category using the pretrained Hugging Face model goes here
    # You can access the text using request.text
    return model_router.predict(request.text)