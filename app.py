from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Capture the five input features
        study_hours_per_week = float(request.form['study_hours_per_week'])
        attendance_rate = float(request.form['attendance_rate'])
        previous_exam_scores = float(request.form['previous_exam_scores'])
        assignments_completed = float(request.form['assignments_completed'])
        extracurricular_participation = float(request.form['extracurricular_participation'])

        # Prepare the input data array
        input_data = np.array([
            study_hours_per_week, attendance_rate, previous_exam_scores,
            assignments_completed, extracurricular_participation
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)

        # Render the result template with the prediction
        return render_template('results.html', prediction=round(prediction[0], 2))
    except ValueError:
        return "Please enter valid inputs."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
