import pytesseract
import pandas as pd
import cv2
import os

# Set the path to the Tesseract executable (ensure the path is correct)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\risha\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111 (1).exe"

def process_image_to_csv(image_path, output_folder):
    # Check image clarity before processing
    clarity_message = check_image_clarity(image_path)
    if clarity_message != "Image is clear":
        return clarity_message, None  # If image is not clear, return the message and None for CSV path

    # Preprocess Image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)

    # Convert OCR Output to CSV
    rows = []
    for line in text.split("\n"):
        if line.strip():
            rows.append(line.split())

    # Create DataFrame
    df = pd.DataFrame(rows)
    output_csv_path = os.path.join(output_folder, "output.csv")
    df.to_csv(output_csv_path, index=False)

    return "Image is clear", output_csv_path

def check_image_clarity(image_path):
    # Check image clarity using Laplacian variance (sharpness indicator)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the Laplacian of the image and then the variance
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # If variance is too low, the image is blurry
    if laplacian_var < 100:
        return "Please upload a clear image"
    
    return "Image is clear"
