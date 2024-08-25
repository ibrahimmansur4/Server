import cv2
from flask import Flask, Response, stream_with_context, render_template

app = Flask(__name__)

cap = cv2.VideoCapture(0)  # Global video capture

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Concatenate frame one by one and show result as a stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(stream_with_context(gen_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    global cap
    cap.release()  # Release the video capture
    return "Capture released"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


