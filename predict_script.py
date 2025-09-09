import pandas as pd
import joblib
import os

# Load the model
model = joblib.load("models\XGBoost.joblib")

# Read the test data
test_df = pd.read_csv("dataset/test.csv")

# Get feature columns (exclude 'id' column)
feature_cols = [col for col in test_df.columns if col != 'id']
X = test_df[feature_cols]

# Make predictions
predictions = model.predict(X)

# Create output dataframe
output_df = pd.DataFrame({
    'id': test_df['id'],
    'BPM': predictions
})

# Create output directory if it doesn't exist
os.makedirs('pred_res', exist_ok=True)

# Save predictions
output_df.to_csv('pred_res/predictions.csv', index=False)

print(f"Predictions saved! Total rows: {len(output_df)}")
print(f"Sample predictions:\n{output_df.head()}")