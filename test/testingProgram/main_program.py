import tensorflow as tf
from twilio.rest import Client
from testing.webcam_capturetest2 import capture_webcam

# 1) Create CNN model (do the same as last project in machine learning class then save it
# 2) Load a trained TensorFlow model in main program here

model = tf.saved_model.load('path_to_saved_model')

def detect_objects(image_np):
    input_tensor = tf.convert_to_tensor([image_np])
    detections = model(input_tensor)
    return detections['detection_scores'].numpy()[0] > 0.5  # Assuming threshold of 0.5

def send_sms(message, from_num, to_num):
    message = twilio_client.messages.create(
        to=to_num,
        from_=from_num,
        body=message
    )
    print(f"SMS sent: {message.sid}")

if __name__ == "__main__":
    capture_webcam(detect_objects, send_sms)
