from typing import Optional

from fastapi import FastAPI

from tkinter import X
from pydantic.dataclasses import dataclass
import json
import pandas as pd

from joblib import load

from typing import Union

from fastapi import FastAPI
from sklearn.metrics import mean_squared_error

from DataModel import DataModel



app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    return result.tolist()
