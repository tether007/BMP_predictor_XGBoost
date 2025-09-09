from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np
import logging
import traceback
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load model
try:
    model = joblib.load("XGBoost.joblib")
except Exception as exc:
    
    raise RuntimeError(f"Failed to load model: {exc}")


class InputData(BaseModel):
    RhythmScore: float
    AudioLoudness: float
    VocalContent: float
    AcousticQuality: float
    InstrumentalScore: float
    LivePerformanceLikelihood: float
    MoodScore: float
    TrackDurationMs: float
    Energy: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "RhythmScore": 0.42,
                "AudioLoudness": -7.3,
                "VocalContent": 0.61,
                "AcousticQuality": 0.35,
                "InstrumentalScore": 0.18,
                "LivePerformanceLikelihood": 0.05,
                "MoodScore": 0.72,
                "TrackDurationMs": 210000.0,
                "Energy": 0.8,
            }
        }
    }
   

FEATURE_ORDER = [
    "RhythmScore",
    "AudioLoudness",
    "VocalContent",
    "AcousticQuality",
    "InstrumentalScore",
    "LivePerformanceLikelihood",
    "MoodScore",
    "TrackDurationMs",
    "Energy",
]

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}



@app.get("/predict", response_class=HTMLResponse)
def get_predict_form():
    inputs_html = "".join(
        f'<label for="{f}">{f}</label>\n<input type="number" step="any" name="{f}" id="{f}" required>\n<br/>\n'
        for f in FEATURE_ORDER
    )
    html = f"""
    <html>
      <head>
        <title>BPM Predictor</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
          }}
          .container {{
            background: white;
            padding: 32px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
          }}
          h2 {{ text-align: center; margin-bottom: 20px; }}
          label {{ display:block; margin-top: 12px; font-weight: 600; }}
          input {{ width: 100%; padding: 8px; box-sizing: border-box; }}
          button {{
            margin-top: 20px;
            padding: 10px 16px;
            width: 100%;
            background: #007BFF;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
          }}
          button:hover {{ background: #0056b3; }}
          p {{ text-align: center; margin-top: 16px; }}
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Predict BPM</h2>
          <form method="post" action="/predict">
            {inputs_html}
            <button type="submit">Predict</button>
          </form>
          <p><a href="/docs">API Docs</a></p>
        </div>
      </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.post("/predict", response_class=HTMLResponse)
def post_predict_form(
    RhythmScore: float = Form(...),
    AudioLoudness: float = Form(...),
    VocalContent: float = Form(...),
    AcousticQuality: float = Form(...),
    InstrumentalScore: float = Form(...),
    LivePerformanceLikelihood: float = Form(...),
    MoodScore: float = Form(...),
    TrackDurationMs: float = Form(...),
    Energy: float = Form(...),
):
    try:
        values = [
            RhythmScore,
            AudioLoudness,
            VocalContent,
            AcousticQuality,
            InstrumentalScore,
            LivePerformanceLikelihood,
            MoodScore,
            TrackDurationMs,
            Energy,
        ]

        X_df = pd.DataFrame([values], columns=FEATURE_ORDER)
        prediction = model.predict(X_df)
        pred_value = float(prediction[0])
    except Exception as exc:
        logger.exception("Model prediction failed")
        exc_name = type(exc).__name__
        return HTMLResponse(status_code=500, content=f"<h3>Error</h3><pre>{exc_name}: {exc}</pre>")

    result_html = f"""
    <html>
      <head>
        <title>BPM Predictor</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
          }}
          .container {{
            background: white;
            padding: 32px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
          }}
          h2 {{ text-align: center; margin-bottom: 20px; }}
          label {{ display:block; margin-top: 12px; font-weight: 600; }}
          input {{ width: 100%; padding: 8px; box-sizing: border-box; }}
          button {{
            margin-top: 20px;
            padding: 10px 16px;
            width: 100%;
            background: #007BFF;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
          }}
          button:hover {{ background: #0056b3; }}
          .result {{ margin-top: 24px; font-size: 18px; font-weight: 700; text-align: center; }}
          p {{ text-align: center; margin-top: 16px; }}
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Predict BPM</h2>
          <form method="post" action="/predict">
            {''.join([f'<label for="{f}">{f}</label><input type="number" step="any" name="{f}" id="{f}" value="{values[i]}" required><br/>' for i, f in enumerate(FEATURE_ORDER)])}
            <button type="submit">Predict</button>
          </form>
          <div class="result">Prediction: {pred_value}</div>
          <p><a href="/docs">API Docs</a></p>
        </div>
      </body>
    </html>
    """
    return HTMLResponse(content=result_html)




if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="localhost", port=port, reload=False)
