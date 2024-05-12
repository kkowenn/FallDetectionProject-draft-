import cv2
import os
from datetime import datetime

def capture_webcam():
    # Create a VideoCapture object
    # The argument '0' gets the default webcam.
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        # Capture frame-by-frame from the webcam
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Live', frame)

        # Wait for the 'c' key to be pressed to start recording
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            # Define the path where the video will be saved
            save_path = f'/Users/kritsadakruapat/Desktop/project/recorded_video/recorded_{timestamp}.avi'
            # Set up the VideoWriter object
            out = cv2.VideoWriter(save_path, fourcc, 20.0, (640, 480))

            # Record video for 5 seconds
            start_time = datetime.now()
            while (datetime.now() - start_time).seconds < 5:
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                    cv2.imshow('Webcam Live', frame)
                else:
                    break
            out.release()
            print(f"Video saved to {save_path}")

        # Wait for the 'q' key to be pressed to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_webcam()
