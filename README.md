# BPM_predictor

A machine learning project that predicts the BPM (Beats Per Minute) of audio tracks using various audio features and characteristics.

## Overview

This project uses machine learning algorithms to predict the tempo of music tracks based on audio analysis features. The model is trained using scikit-learn and deployed with a FastAPI web service for easy integration and real-time predictions.

## Features

The BPM prediction model uses the following audio features:

- **RhythmScore**: Measure of rhythmic complexity and consistency
- **AudioLoudness**: Overall loudness level of the track
- **VocalContent**: Presence and characteristics of vocal elements
- **AcousticQuality**: Audio fidelity and recording quality metrics
- **InstrumentalScore**: Instrumental complexity and arrangement scoring
- **LivePerformanceLikelihood**: Probability that the track is a live performance
- **MoodScore**: Emotional tone and mood classification
- **TrackDurationMs**: Duration of the track in milliseconds
- **Energy**: Overall energy level and intensity of the track

## Technologies Used

- **Python 3.8+**
- **scikit-learn**: Machine learning model development
- **FastAPI**: Web API framework for model deployment
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **uvicorn**: ASGI server for FastAPI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BPM_predictor.git
cd BPM_predictor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

```python
from bpm_predictor import BPMPredictor

# Initialize and train the model
predictor = BPMPredictor()
predictor.train(training_data_path='data/training_data.csv')
```

### Making Predictions

```python
# Predict BPM for a single track
features = {
    'RhythmScore': 0.75,
    'AudioLoudness': -8.5,
    'VocalContent': 0.6,
    'AcousticQuality': 0.8,
    'InstrumentalScore': 0.7,
    'LivePerformanceLikelihood': 0.2,
    'MoodScore': 0.65,
    'TrackDurationMs': 240000,
    'Energy': 0.8
}

predicted_bpm = predictor.predict(features)
print(f"Predicted BPM: {predicted_bpm}")
```

### FastAPI Web Service

Start the API server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

#### API Endpoints

- **POST `/predict`**: Predict BPM for given audio features
- **GET `/health`**: Health check endpoint
- **GET `/docs`**: Interactive API documentation


## Model Performance

The trained model achieves the following performance metrics:
- **R² Score**: [.00009]
- **Mean Absolute Error**: [21.3]
- **Root Mean Square Error**: [26.4]

