from flask import Flask, render_template, Response
from flask import jsonify
from Webcam import WebCam
from flask_cors import CORS
from Robot import Robot 

app = Flask(__name__)

CORS(app)
cam = WebCam()

my_robot = Robot('dolzay')

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

@app.route('/forward')
def forward():
    my_robot.forward()
    return jsonify(msg='forward')

@app.route('/backward')
def backward():
    my_robot.backward()
    return jsonify(msg='backward')

@app.route('/left')
def left():
    my_robot.left()
    return jsonify(msg='left')

@app.route('/right')
def right():
    my_robot.right()
    return jsonify(msg='right')

@app.route('/stop')
def stop():
    my_robot.stop()
    return jsonify(msg='stop')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
