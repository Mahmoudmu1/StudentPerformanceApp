# Student Performance Predictor

This is a web application that predicts student performance based on key inputs such as study hours, attendance rate, previous exam scores, assignments completed, and extracurricular participation. The app uses a **Lasso Regression model** to predict performance while minimizing the number of required inputs, making it user-friendly and efficient.

## Features
- **User-Friendly Interface**: Simple form-based UI where users can enter relevant details about study habits and engagement.
- **Efficient Prediction Model**: Uses Lasso Regression to focus on the most impactful features, allowing accurate predictions with fewer inputs.
- **Immediate Feedback**: Provides an instant prediction score upon submission of the form.

## How It Works
1. **Input Form**: Users enter the following details in the provided fields:
   - **Study Hours per Week**: The average number of hours the student studies weekly (range: 0-40).
   - **Attendance Rate (%)**: Percentage of classes attended by the student (range: 0-100).
   - **Previous Exam Scores**: Average score from previous exams (range: 0-100).
   - **Assignments Completed**: Number of assignments completed out of a maximum of 20.
   - **Extracurricular Participation**: Level of participation in extracurricular activities (range: 0-10).

2. **Prediction Process**:
   - The user fills in the form and clicks on the "Predict" button.
   - The application sends the input data to the server, where the Lasso Regression model processes it.
   - The model predicts the student's performance score based on the entered data.

3. **Result Display**:
   - The predicted performance score is displayed on a new page.
   - Users can click "Go Back" to return to the input form and make another prediction.

## Why Lasso Regression?
The Lasso Regression model was chosen because it automatically selects the most impactful features by reducing the coefficients of less relevant ones to zero. This feature selection process makes the application simpler and more efficient by requiring fewer inputs, without compromising accuracy.

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mahmoudmu1/student-performance-predictor.git
   cd student-performance-predictor



2.Install Dependencies: Make sure you have Python installed. Then, install the necessary Python packages:

```pip install -r requirements.txt```

3.Run the Application: Start the Flask server by running:

```python app.py```

The application will be available at http://127.0.0.1:5000.

4.Using the App: Open your browser and go to http://127.0.0.1:5000. Fill in the required fields in the form and click **"Predict"** to get the performance prediction.


File Structure
app.py: Contains the Flask backend for handling form submissions and prediction requests.
model.pkl: The trained Lasso Regression model used for predictions.
templates/
index.html: The main form page where users enter data.
results.html: Displays the prediction result.

Future Improvements
Add more input features if needed, as well as further regularization techniques to improve prediction accuracy.
Enhance the UI to make it more engaging and user-friendly.
Deploy the app to a cloud platform for remote access.

Feel free to contribute or report any issues. Enjoy predicting student performance with this easy-to-use app!


This `README.md` provides a comprehensive overview of the project, setup instructions, and a description of how the app works, which should help users understand and run the application smoothly.
