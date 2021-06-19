from typing import Dict
from fastapi_health import health

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from pysentimiento import EmotionAnalyzer
from pysentimiento.preprocessing import preprocess_tweet

emotion_analyzer = EmotionAnalyzer(lang="es")

def get_session():
    return True

def is_database_online(session: bool = Depends(get_session)):
    return session

app = FastAPI()
app.add_api_route("/healthcheck", health([is_database_online]))

class EmotionRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    probabilities: Dict[str, float]
    text: str

@app.post("/predict", response_model=EmotionResponse)
def predict(request: EmotionRequest):
    #sentiment, confidence, probabilities, lang, text = model.predict(request.text)
    result=emotion_analyzer.predict(request.text)
    sResponse=EmotionResponse(
        probabilities=result.probas, text=result.sentence
    )
    return sResponse
