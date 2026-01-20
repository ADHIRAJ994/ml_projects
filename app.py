from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

# Mapping functions for categorical variables
gender_mapping = {'male': 0, 'female': 1}
race_ethnicity_mapping = {'group A': 0, 'group B': 1, 'group C': 2, 'group D': 3, 'group E': 4}
parental_education_mapping = {
    "some high school": 0,
    "high school": 1,
    "some college": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}
lunch_mapping = {'free/reduced': 0, 'standard': 1}
test_prep_mapping = {'none': 0, 'completed': 1}

@app.route('/')
def index():
    """Render the landing page"""
    return render_template('index.html')

@app.route('/home')
def home():
    """Render the dashboard page"""
    return render_template('home.html')

@app.route('/predict_datapoint', methods=['POST'])
def predict_datapoint():
    """Handle prediction requests from the form"""
    try:
        # Get form data
        gender = request.form.get('gender')
        race_ethnicity = request.form.get('race_ethnicity')
        parental_level_of_education = request.form.get('parental_level_of_education')
        lunch = request.form.get('lunch')
        test_preparation_course = request.form.get('test_preparation_course')
        reading_score = float(request.form.get('reading_score'))
        writing_score = float(request.form.get('writing_score'))

        # Convert categorical variables to numerical
        gender_encoded = gender_mapping.get(gender, 0)
        race_encoded = race_ethnicity_mapping.get(race_ethnicity, 0)
        education_encoded = parental_education_mapping.get(parental_level_of_education, 0)
        lunch_encoded = lunch_mapping.get(lunch, 0)
        test_prep_encoded = test_prep_mapping.get(test_preparation_course, 0)

        # Create feature vector
        features = np.array([
            gender_encoded,
            race_encoded,
            education_encoded,
            lunch_encoded,
            test_prep_encoded,
            reading_score,
            writing_score
        ])

        # ============================================
        # REPLACE THIS WITH YOUR ACTUAL ML MODEL
        # ============================================
        # Example: predictions = your_model.predict([features])[0]
        # For now, we're using a simple linear combination as placeholder
        prediction = (
            reading_score * 0.35 +
            writing_score * 0.35 +
            (education_encoded * 5) +
            (lunch_encoded * 3) +
            (test_prep_encoded * 8)
        )
        prediction = max(0, min(100, round(prediction, 2)))  # Clamp between 0-100
        # ============================================

        # Render home template with prediction result
        return render_template('home.html', results=prediction)

    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return render_template('home.html', error="An error occurred during prediction")

if __name__ == '__main__':
    app.run(debug=True)
