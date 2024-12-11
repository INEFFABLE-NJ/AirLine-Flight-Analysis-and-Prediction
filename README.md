
# Flight Price Prediction

This project predicts flight ticket prices based on various factors such as airline, source, destination, date, time, duration, and number of stops. 

## Features

- **Data Preprocessing**: Handles missing values, feature extraction (e.g., journey day, month, departure/arrival times), and categorical encoding.
- **Exploratory Data Analysis (EDA)**: Includes visualizations like box plots and heatmaps to analyze trends and correlations.
- **Machine Learning Model**: Utilizes a Random Forest Regressor with hyperparameter tuning to predict flight prices.
- **Flask Web App**: Provides a user-friendly interface for users to input flight details and receive predicted prices.

## How to Run the Project

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory and set up a virtual environment:
   ```bash
   cd Flight-Price-Prediction
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000` to use the application.

## Dataset

The dataset used for this project contains information about flights, including airlines, sources, destinations, departure/arrival times, duration, and price. It is preprocessed and saved in the `Data_Train.xlsx` file.

## Output

The application predicts flight prices based on user-provided inputs and displays the predicted price on the web interface.

## Requirements

See the `requirements.txt` file for a complete list of dependencies.

