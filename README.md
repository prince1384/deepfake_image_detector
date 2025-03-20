# Deepfake Detector

This is a deepfake detection web application built using **Flask** and **TensorFlow/Keras**. The application allows users to upload an image, and the model predicts whether the image is real or deepfake.

## Features
- Upload an image via a web interface
- Preprocess the image and pass it through a deep learning model
- Display the prediction ("Real" or "Deepfake") on the webpage
- AJAX-based form submission for a smooth user experience

## Technologies Used
- **Flask** (Backend framework)
- **TensorFlow/Keras** (Deep learning model)
- **HTML, CSS, JavaScript** (Frontend)
- **AJAX Fetch API** (To handle form submission without reloading the page)

## Folder Structure
```
project-folder/
│── static/
│   ├── uploads/         # Stores uploaded images
│── templates/
│   ├── index.html       # Frontend UI
│── app.py               # Flask application
│── deepfake_detector.h5 # Pre-trained deepfake detection model
│── requirements.txt     # Required Python packages
│── README.md            # Project documentation
```

## Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/deepfake-detector.git
   cd deepfake-detector
   ```

2. **Create and activate a virtual environment (Recommended)**
   ```sh
   python -m venv venv  # Create virtual environment
   source venv/bin/activate  # Activate on macOS/Linux
   venv\Scripts\activate  # Activate on Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application**
   ```sh
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage
1. Open `http://127.0.0.1:5000/` in your web browser.
2. Upload an image using the file input field.
3. Click **Upload** and wait for the model to process the image.
4. The result (Real or Deepfake) will be displayed below the form.

## Notes
- The model file `deepfake_detector.h5` must be in the project directory.
- Only image formats (`jpg`, `jpeg`, `png`, `gif`) are supported.
- Make sure that the `static/uploads/` folder exists to store uploaded images.

## License
This project is open-source and available under the MIT License.

---
If you encounter any issues, feel free to create an issue on GitHub!

