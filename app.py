from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import io

app = FastAPI()

# Allow your HTML frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can change "*" to specific domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained XGBoost model
model = joblib.load("xgboost.joblib")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read CSV
        df = pd.read_csv(file.file)

        # Required raw columns (from your dataset)
        required_raw = [
            "Projects_Handled", "Overtime_Hours", "Sick_Days",
            "Training_Hours", "Employee_Satisfaction_Score",
            "Work_Hours_Per_Week", "Monthly_Salary"
        ]

        # Validate required columns
        for col in required_raw:
            if col not in df.columns:
                return {"error": f"Missing required column: {col}"}

        # === Feature Engineering (must match model training) ===
        df["Attendance_Rate"] = (1 - df["Sick_Days"] / 260) * 100
        df["Salary_Per_Hour"] = df["Monthly_Salary"] / df["Work_Hours_Per_Week"]

        # Final model features
        model_features = [
            "Projects_Handled", "Overtime_Hours", "Attendance_Rate",
            "Salary_Per_Hour", "Training_Hours",
            "Employee_Satisfaction_Score", "Work_Hours_Per_Week", "Monthly_Salary"
        ]

        # Prepare features
        X = df[model_features]

        # Make predictions
        preds = model.predict(X)
        # Convert numeric class → text labels
        label_map = {
             0: "Low",
             1: "Below Average",
             2: "Average",
             3: "Above Average",
             4: "High"
        }
        df["Predicted_Performance"] = [label_map.get(int(p), "Unknown") for p in preds]
        
        # Return output CSV as string
        output = io.StringIO()
        df.to_csv(output, index=False)
        return {"csv": output.getvalue()}

    except Exception as e:
        return {"error": str(e)}
