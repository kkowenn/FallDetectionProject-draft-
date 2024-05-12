import cv2
import numpy as np
from PIL import Image

def capture_webcam(detect_objects, send_sms):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break

        # Convert frame to format suitable for TensorFlow
        image_np = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_np = np.array(Image.fromarray(image_np))

        # Detect objects
        if detect_objects(image_np):
            # Send SMS notification if object detected
            send_sms(f"Object detected!", 'your_twilio_phone_number', 'your_cell_phone_number')

        cv2.imshow('Webcam Live', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
