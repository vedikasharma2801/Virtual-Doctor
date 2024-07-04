# Virtual Doctor - AI-Powered Medical Diagnosis

Virtual Doctor is an AI-powered medical diagnosis tool that leverages machine learning to provide preliminary medical diagnoses based on user-reported symptoms. This tool aims to offer quick and accessible health insights, potentially assisting users in identifying common diseases and understanding necessary precautions and remedies.

## Features

- **Symptom Input**: Users can input symptoms manually or via voice input.
- **Disease Prediction**: The system predicts the most likely disease based on the symptoms provided.
- **Precaution Recommendations**: The system provides recommended precautions for the predicted disease.

## Libraries and Tools Used

- **Flask**: For creating the web application.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For machine learning model building and evaluation.
- **Joblib**: For saving and loading the trained model.
- **SpeechRecognition**: For voice input functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vedikasharma2801/virtual-doctor.git
   cd virtual-doctor
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Ensure you have the following CSV files in the project directory:
   - **DiseaseAndSymptoms.csv**
   - **DiseasePrecaution.csv**

## Usage

1. Train the model using the Jupyter notebook:
   ```bash
   jupyter notebook doct.ipynb

2. Run the Flask application:
   ```bash
   python app.py

3. Open your web browser and navigate to `http://127.0.0.1:5000` to use the Virtual Doctor web application.

      
## Project Structure

- **doct.ipynb**: Jupyter notebook for training the machine learning model.
- **app.py**: Flask application file for serving the web interface.
- **templates/index.html**: HTML file for the web interface.
- **static/css/styles.css**: CSS file for styling the web interface.
- **requirements.txt**: List of required Python packages.

## Data Sources

- **DiseaseAndSymptoms.csv**: Contains data on diseases and their associated symptoms.
- **DiseasePrecaution.csv**: Contains data on diseases and their associated precautions.

## Contributors:
- [Vedika Sharma](https://github.com/vedikasharma2801)

​

