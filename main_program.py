import tensorflow as tf
from recordMP4 import capture_webcam_ffmpeg
from TwilioWhatsApp import send_whatsapp_message

# 1) create CNN model and save it
# 2) Load a trained TensorFlow model
model = tf.saved_model.load('path_to_saved_model')

# just template
def detect_objects(image_np):
    input_tensor = tf.convert_to_tensor([image_np])
    detections = model(input_tensor)
    return detections['detection_scores'].numpy()[0] > 0.5  # Assuming threshold of 0.5


if __name__ == "__main__":
    capture_webcam_ffmpeg()  # Capture video first
    if detect_objects():  # Check for objects in the captured video
        send_whatsapp_message("Object detected with high confidence!")

