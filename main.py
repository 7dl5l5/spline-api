from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import numpy as np
from scipy.interpolate import interp1d
from pydantic import BaseModel
from typing import List

app = FastAPI()  # ✅ 반드시 가장 먼저 선언해야 함!

# GET 방식 (기존 그대로 유지)
@app.get("/")
def spline(x: float, xdata: str, ydata: str):
    x_array = np.array([float(i) for i in xdata.split(",")])
    y_array = np.array([float(i) for i in ydata.split(",")])
    f = interp1d(x_array, y_array, kind="cubic", fill_value="extrapolate")
    y = float(f(x))
    return PlainTextResponse(str(y))

# POST 방식 (길이 제한 해결용)
class SplineInput(BaseModel):
    x: float
    xdata: List[float]
    ydata: List[float]

@app.post("/post")
def spline_post(data: SplineInput):
    f = interp1d(data.xdata, data.ydata, kind="cubic", fill_value="extrapolate")
    y = float(f(data.x))
    return PlainTextResponse(str(y))
