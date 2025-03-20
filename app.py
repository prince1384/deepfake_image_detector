from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = load_model("C:/Users/princ/Desktop/deepfake/deepfake_detector.h5")

# Function to load and preprocess image
def preprocess_image(image_path, target_size=(224, 224)):
    try:
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0  # Normalize the image
        return np.expand_dims(img_array, axis=0)  # Add batch dimension
    except Exception as e:
        return None  # Return None if the image can't be processed

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    # Validate file extension (basic validation for images)
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    filename = file.filename
    if '.' not in filename or filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({"error": "Invalid file type. Only image files are allowed."})
    
    # Save the file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Preprocess the image
    image = preprocess_image(filepath)
    if image is None:
        return jsonify({"error": "Failed to process the image"})
    
    # Make prediction
    prediction = model.predict(image)
    
    # Return prediction result
    if prediction[0] > 0.5:
        result = 'Deepfake'
    else:
        result = 'Real'

    return jsonify({'prediction': result})

# Define the home route to render the upload form
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
