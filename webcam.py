import cv2
import random

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Webcam not opening")
    exit()

cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", 800, 600)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame not received")
        break

    # ---- Dummy label (replace with ML model output) ----
    label = random.choice([0, 1])  # 0 = Not stressed, 1 = Stressed

    if label == 1:
        text = "STRESSED"
        color = (0, 0, 255)   # Red
    else:
        text = "NOT STRESSED"
        color = (0, 255, 0)   # Green

    # ---- Draw rectangle ----
    cv2.rectangle(frame, (100, 100), (400, 300), color, 2)

    # ---- Put text ----
    cv2.putText(frame, text, (110, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()