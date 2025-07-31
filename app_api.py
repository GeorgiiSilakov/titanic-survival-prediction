from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from   pydantic import BaseModel

"""
    curl -X GET http://127.0.0.1:5000/stats
    curl -X GET http://127.0.0.1:5000/health
    curl -X POST http://127.0.0.1:5000/predict_model -H "Content-Type: application/json" -d "{\"Pclass\": 1, \"Sex\": \"female\", \"Age\": 2.0, \"Fare\": 76.266}"
    """

app = FastAPI()

# Загрузка модели из файла pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Счетчик запросов
request_count = 0

# Модель для валидации входных данных
class PredictionInput(BaseModel):
    Pclass : int
    Sex    : str
    Age    : float
    Fare   : float

@app.get("/stats")
def stats():
    return {"request_count" : request_count}

@app.get("/health")
def health():
    return {"status" : "OK"}

@app.post("/predict_model")
def predict_model(input_data: PredictionInput):
    global request_count
    request_count += 1


    new_data = pd.DataFrame({
        'Pclass' : [input_data.Pclass],
        'Sex'    : [input_data.Sex],
        'Age'    : [input_data.Age],
        'Fare'   : [input_data.Fare]
    })

    # Предсказание
    predictions = model.predict(new_data)

    # Преобразование результата
    result = "Survived" if predictions[0] == 1 else "Not Survived"

    return {"prediction" : result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
