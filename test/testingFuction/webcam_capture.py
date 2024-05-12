import cv2
import os

def capture_webcam():
    # Create a VideoCapture object
    # The argument '0' gets the default webcam.
    cap = cv2.VideoCapture(0)

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

        # Wait for the 'c' key to be pressed to capture and save an image
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Define the path where the image will be saved
            save_path = '/Users/kritsadakruapat/Desktop/project/take_A_pic/captured_image.jpg'
            # Save the current frame to the specified path
            cv2.imwrite(save_path, frame)
            print(f"Image saved to {save_path}")

        # Wait for the 'q' key to be pressed to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_webcam()
