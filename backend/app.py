from flask import Flask, render_template, Response
from Webcam import WebCam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

def gen(webcam):
    while True:
        frame = webcam.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_stream')
def video_feed():
    return Response(gen(WebCam()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
