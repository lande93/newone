from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
load_model=pickle.load(open('saved_kuda_model.sav','rb'))

@app.route('/')
def home():
    result=''
    return render_template('kuda.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        # Collect input features from the form
        features = [float(request.form['feat_0']),
                    float(request.form['feat_2']),
                    float(request.form['feat_4']),
                    float(request.form['feat_6']),
                    float(request.form['feat_10']),
                    float(request.form['feat_11']),
                    float(request.form['feat_13']),
                    float(request.form['feat_15']),
                    float(request.form['feat_16']),
                    float(request.form['feat_17']),
                    float(request.form['feat_18']),
                    float(request.form['feat_19']),
                    float(request.form['feat_7'])]
                    
        features = [np.array(features)]
        features = np.array(features).reshape(1, -1)
        prediction =load_model.predict(features)
        output = 'Yes' if prediction[0] else 'No'
        return render_template('kuda.html', prediction_text='Customer churn prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
