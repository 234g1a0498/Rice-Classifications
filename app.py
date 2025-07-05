from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask
app = Flask(__name__, static_folder='static')

# Load the trained rice model
try:
    model = load_model("rice.h5")  # Ensure rice.h5 is in the same directory
except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")

# Define rice types
classes = ['Basmati', 'Jasmine', 'SonaMasoori', 'WhiteRice']  # Adjust based on your dataset

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "Error: No file part"

    file = request.files['file']
    if file.filename == '':
        return "Error: No selected file"

    # Save uploaded file to static folder with a unique filename to avoid conflicts
    filename = os.path.join(app.static_folder, file.filename)
    file.save(filename)

    # Preprocess image
    img = image.load_img(filename, target_size=(224, 224))
    
if __name__ == '__main__':
    app.run(debug=True, port=5100, host='0.0.0.0')  # Explicitly set port and host