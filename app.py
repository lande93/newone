from flask import Flask, request, render_template
import pickle
import numpy as np
application = Flask(__name__)
app=application
# Load the model
load_model=pickle.load(open('savedmodel.sav','rb'))

@app.route('/')
def home():
    result=''
    return render_template('deploy.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        # Collect input features from the form
        features = [float(request.form['account_length']),
                    float(request.form['area_code']),
                    float(request.form['number_vmail_messages']),
                    float(request.form['total_day_minutes']),
                    float(request.form['total_day_calls']),
                    float(request.form['total_day_charge']),
                    float(request.form['total_eve_minutes']),
                    float(request.form['total_eve_calls']),
                    float(request.form['total_eve_charge']),
                    float(request.form['total_night_minutes']),
                    float(request.form['total_night_calls']),
                    float(request.form['total_night_charge']),
                    float(request.form['total_intl_minutes']),
                    float(request.form['total_intl_calls']),
                    float(request.form['total_intl_charge']),
                    float(request.form['customer_service_calls']),
                    float(request.form['state']),
                    float(request.form['international plan']),
                    float(request.form['voice mail plan'])]
        features = [np.array(features)]
        features = np.array(features).reshape(1, -1)
        prediction =load_model.predict(features)
        output = 'Yes' if prediction[0] else 'No'
        return render_template('deploy.html', prediction_text='Customer churn prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    #debug=True
    #app.run(host='0.0.0.0', port=8080) 
