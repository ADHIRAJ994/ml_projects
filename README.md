# Student Performance Predictor (End-to-End ML Project)

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic and academic features.  
This project includes a complete ML pipeline (ingestion → transformation → training → evaluation), a deployed inference pipeline, and a web application UI for real-time predictions.

---

## 🚀 Live Demo
- **Web App:**   
- **API Health Check:** 

---

## 📌 Problem Statement
Predict the **math score** of a student using:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Writing score
- Reading score

This helps demonstrate how real-world ML systems can be built using structured/tabular data.

---

## ✨ Key Features
✅ End-to-End ML Pipeline  
✅ Modular project structure using `src/` architecture  
✅ Data preprocessing using `ColumnTransformer` (numerical + categorical pipelines)  
✅ Model training with hyperparameter tuning  
✅ Model evaluation and best-model selection  
✅ Saved artifacts (model + preprocessor) for inference  
✅ Web UI built with Flask (HTML form input → prediction output)  
✅ Deployment on Render

---

## 🧠 ML Workflow (Pipeline)
The ML system follows the standard production workflow:

1. **Data Ingestion**
   - Reads dataset (train/test split or CSV input)
   - Stores raw data into artifacts

2. **Data Transformation**
   - Numerical pipeline: median imputation + scaling
   - Categorical pipeline: mode imputation + one-hot encoding
   - Saves preprocessing object (`preprocessor.pkl`)

3. **Model Training**
   - Trains multiple algorithms
   - Performs tuning using parameter grids
   - Selects the best performing model

4. **Prediction Pipeline**
   - Loads `preprocessor.pkl` and `model.pkl`
   - Transforms user input
   - Predicts output in real time

---

## 🏗️ System Architecture

```text
User (Web Form)
      ↓
Flask App
      ↓
PredictPipeline
      ↓
Preprocessor (.pkl)  → Feature Transformation
      ↓
Trained Model (.pkl) → Prediction
      ↓
Result Displayed on UI
