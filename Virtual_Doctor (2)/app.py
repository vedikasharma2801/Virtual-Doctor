# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import joblib

# app = Flask(__name__)

# # Load the pre-trained model
# model = joblib.load('model.pkl')

# # Load the disease precaution data
# disease_precaution = pd.read_csv('../Disease precaution.csv')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/diagnose', methods=['POST'])
# def diagnose():
#     data = request.get_json()
#     symptoms = data['symptoms']

#     # Predict the disease
#     disease = model.predict([symptoms])[0]

#     # Get precautions and remedies for the predicted disease
#     precautions = disease_precaution[disease_precaution['Disease'] == disease]['Precaution'].values[0]
#     remedies = disease_precaution[disease_precaution['Disease'] == disease]['Remedy'].values[0]

#     return jsonify({
#         'disease': disease,
#         'precautions': precautions,
#         'remedies': remedies
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify, render_template
# import joblib
# import pandas as pd

# app = Flask(__name__)

# # Load the trained model
# model = joblib.load('disease_model.joblib')

# # Load the precaution data
# disease_precaution = pd.read_csv('../Disease precaution.csv')

# # Combine all precautions into a single string for each disease
# disease_precaution['Precautions'] = disease_precaution.apply(
#     lambda row: ', '.join([str(row[f'Precaution_{i}']).strip() for i in range(1, 5) if pd.notna(row[f'Precaution_{i}'])]),
#     axis=1
# )

# # Create a dictionary for easy lookup
# precaution_dict = {}
# for _, row in disease_precaution.iterrows():
#     precaution_dict[row['Disease'].strip().lower()] = {
#         'Precautions': row['Precautions']
#     }

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/diagnose', methods=['POST'])
# def diagnose():
#     data = request.get_json()
#     symptoms = data['symptoms']
#     prediction = model.predict([symptoms])[0]
#     precautions = precaution_dict.get(prediction.lower(), {})
#     return jsonify({
#         'disease': prediction,
#         'precautions': precautions.get('Precautions', 'Not available')
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify, render_template
# import joblib
# import pandas as pd

# app = Flask(__name__)

# # Load the trained model and encoder
# model = joblib.load('disease_model.joblib')
# encoder = joblib.load('encoder.joblib')

# # Load the precaution data
# disease_precaution = pd.read_csv('data /Disease precaution.csv')

# # Combine all precautions into a single string for each disease
# disease_precaution['Precautions'] = disease_precaution.apply(
#     lambda row: ', '.join([str(row[f'Precaution_{i}']).strip() for i in range(1, 5) if pd.notna(row[f'Precaution_{i}'])]),
#     axis=1
# )

# # Create a dictionary for easy lookup
# precaution_dict = {}
# for _, row in disease_precaution.iterrows():
#     precaution_dict[row['Disease'].strip().lower()] = {
#         'Precautions': row['Precautions']
#     }

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/diagnose', methods=['POST'])
# def diagnose():
#     data = request.get_json()
#     symptoms = ' '.join(data['symptoms']).strip()  # Combine symptoms into a single string

#     # Encode the symptoms
#     encoded_symptoms = encoder.transform([[symptoms]])

#     # Make a prediction
#     prediction = model.predict(encoded_symptoms)[0]
#     precautions = precaution_dict.get(prediction.lower(), {})
#     return jsonify({
#         'disease': prediction,
#         'precautions': precautions.get('Precautions', 'Not available')
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

#new at 11
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('disease_model.joblib')

# Load the precaution data
disease_precaution = pd.read_csv('data\Disease precaution.csv')

# Combine all precautions into a single string for each disease
disease_precaution['Precautions'] = disease_precaution.apply(
    lambda row: ', '.join([str(row[f'Precaution_{i}']).strip() for i in range(1, 5) if pd.notna(row[f'Precaution_{i}'])]),
    axis=1
)

# Create a dictionary for easy lookup
precaution_dict = {}
for _, row in disease_precaution.iterrows():
    precaution_dict[row['Disease'].strip().lower()] = {
        'Precautions': row['Precautions']
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    symptoms = data['symptoms']
    prediction = model.predict([symptoms])[0]
    precautions = precaution_dict.get(prediction.lower(), {})
    return jsonify({
        'disease': prediction,
        'precautions': precautions.get('Precautions', 'Not available')
    })

if __name__ == '__main__':
    app.run(debug=True)

