from flask import Flask, render_template, request, send_file
import os
from utility import process_image_to_csv

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process the image and generate CSV if the image is clear
    clarity_message, csv_path = process_image_to_csv(filepath, PROCESSED_FOLDER)

    if clarity_message != "Image is clear":
        # If the image is not clear, show a message and return without processing
        return render_template("result.html", clarity_message=clarity_message)

    # Otherwise, proceed with showing the results
    return render_template("result.html", clarity_message=clarity_message, csv_path=csv_path)

if __name__ == "__main__":
    app.run(debug=True)
