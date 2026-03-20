import cv2
import pytesseract

# ==============================
# 🔧 CONFIGURATION
# ==============================

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


# ==============================
# 🎥 START WEBCAM
# ==============================

# 0 = default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot access webcam")
    exit()

print("✅ Press 'q' to exit")


# ==============================
# 🔁 REAL-TIME LOOP
# ==============================

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # ==============================
    # 🎨 PREPROCESSING
    # ==============================

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 170, 200)

    # ==============================
    # 🔍 FIND CONTOURS
    # ==============================

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

    plate = None
    x = y = w = h = 0

    # ==============================
    # 🚗 DETECT LICENSE PLATE
    # ==============================

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

        # Check for rectangle shape
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            plate = gray[y:y + h, x:x + w]
            break

    # ==============================
    # 🔤 OCR (ONLY IF PLATE FOUND)
    # ==============================

    text = ""

    if plate is not None:
        # Threshold + Noise removal
        _, thresh = cv2.threshold(plate, 127, 255, cv2.THRESH_BINARY)
        clean = cv2.bilateralFilter(thresh, 11, 17, 17)

        # OCR
        text = pytesseract.image_to_string(clean, config='--psm 8')
        text = text.strip()

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

        # Put text
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show detected plate window
        cv2.imshow("Detected Plate", clean)

    # ==============================
    # 🖥️ DISPLAY OUTPUT
    # ==============================

    cv2.imshow("Webcam - License Plate Recognition", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ==============================
# 🛑 RELEASE RESOURCES
# ==============================

cap.release()
cv2.destroyAllWindows()