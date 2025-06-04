# main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import numpy as np
from scipy.interpolate import interp1d

app = FastAPI()

@app.get("/")
def spline(x: float, xdata: str, ydata: str):
    x_array = np.array([float(i) for i in xdata.split(",")])
    y_array = np.array([float(i) for i in ydata.split(",")])
    f = interp1d(x_array, y_array, kind="cubic", fill_value="extrapolate")
    y = float(f(x))
    return PlainTextResponse(str(y))
