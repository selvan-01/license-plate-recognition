import cv2
import pytesseract

# ==============================
# 🔧 CONFIGURATION
# ==============================

# Set Tesseract OCR path (Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Image path (change if needed)
IMAGE_PATH = "data/raw/car1.jpg"


# ==============================
# 🚀 LOAD IMAGE
# ==============================

# Read the image
image = cv2.imread(IMAGE_PATH)

# Check if image is loaded properly
if image is None:
    print("❌ Error: Image not found!")
    exit()

# Show original image
cv2.imshow("Original Image", image)


# ==============================
# 🎨 PREPROCESSING
# ==============================

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)

# Apply Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 170, 200)
cv2.imshow("Canny Edge", canny_edge)


# ==============================
# 🔍 FIND LICENSE PLATE CONTOUR
# ==============================

# Find contours from edges
contours, _ = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours based on area (largest first)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

# Initialize variables
plate = None
x = y = w = h = 0

# Loop through contours to find rectangle (license plate)
for contour in contours:
    # Calculate perimeter
    perimeter = cv2.arcLength(contour, True)

    # Approximate contour shape
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

    # Check if contour has 4 corners (rectangle)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contour)

        # Crop the license plate region
        plate = gray_image[y:y + h, x:x + w]
        break


# ==============================
# ⚠️ CHECK IF PLATE FOUND
# ==============================

if plate is None:
    print("❌ No license plate detected!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()

cv2.imshow("Detected Plate", plate)


# ==============================
# 🧹 IMAGE CLEANING FOR OCR
# ==============================

# Apply threshold to convert to binary image
_, plate_thresh = cv2.threshold(plate, 127, 255, cv2.THRESH_BINARY)

# Remove noise using bilateral filter
plate_clean = cv2.bilateralFilter(plate_thresh, 11, 17, 17)

cv2.imshow("Processed Plate", plate_clean)


# ==============================
# 🔤 TEXT RECOGNITION (OCR)
# ==============================

# Extract text using Tesseract
text = pytesseract.image_to_string(plate_clean, config='--psm 8')

# Clean output text
text = text.strip()

print("🚗 License Plate:", text)


# ==============================
# 🖍️ DRAW RESULT ON IMAGE
# ==============================

# Draw rectangle around detected plate
output = image.copy()
cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 3)

# Put detected text above the plate
cv2.putText(output, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Show final output
cv2.imshow("Final Output", output)


# ==============================
# ⏹️ EXIT WINDOW
# ==============================

cv2.waitKey(0)
cv2.destroyAllWindows()