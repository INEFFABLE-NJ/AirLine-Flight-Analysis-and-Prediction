from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

model = pickle.load(open('Trained_Model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('Screen.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        dep_time = request.form['Dep_Time']

        Journey_day = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").day
        Journey_month = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").month

        Departure_hour = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").hour
        Departure_min = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").minute

        arrival_time = request.form['Arrival_Time']
        Arrival_hour =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").hour
        Arrival_min =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").minute

        Total_stops = int(request.form['stops'])

        dur_hour = abs(Arrival_hour-Departure_hour)
        dur_min = abs(Arrival_min-Departure_min)

        airline=request.form['airline']

        # Create dictionaries for airline, source, and destination
        airline_dict = {
            'Jet Airways': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'IndiGo': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Air India': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            'Multiple carriers': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            'SpiceJet': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            'Vistara': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            'GoAir': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            'Multiple carriers Premium economy': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            'Jet Airways Business': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            'Vistara Premium economy': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            'Trujet': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        }

        source_dict = {
            'Delhi': [1, 0, 0, 0],
            'Kolkata': [0, 1, 0, 0],
            'Mumbai': [0, 0, 1, 0],
            'Chennai': [0, 0, 0, 1]
        }

        destination_dict = {
            'Cochin': [1, 0, 0, 0],
            'Delhi': [0, 1, 0, 0],
            'Hyderabad': [0, 0, 1, 0],
            'Kolkata': [0, 0, 0, 1],
            'Banglore': [0, 0, 0, 0]  # Assuming Bangalore isn't mapped here as per original code
        }

        Source = request.form["Source"]
        Destination = request.form["Destination"]

        # Get the airline, source, and destination values from the input
        airline_data = airline_dict.get(airline, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        source_data = source_dict.get(Source, [0, 0, 0, 0])
        destination_data = destination_dict.get(Destination, [0, 0, 0, 0])

        # Prepare the feature vector for prediction
        input_data = [
            Total_stops, Journey_day, Journey_month, Departure_hour, Departure_min,
            Arrival_hour, Arrival_min, dur_hour, dur_min,
            *airline_data, *source_data, *destination_data
        ]

        # Predict using the model
        output = model.predict([input_data])

        output = round(output[0],2)
        return render_template('Screen.html',predictions='Approx Price ₹{}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)