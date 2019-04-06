from flask import Flask, jsonify, send_file
import os
import requests
import base64

app = Flask(__name__)

# UPLOAD_FOLDER = r'static'
UPLOAD_FOLDER = r'img_static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def show():
	pass

@app.route('/takepic', methods = ['GET'])
def takepic():
    
    url = "http://192.168.0.191:88/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=foscam@123&pwd=foscam@123";
    response = requests.get(url)

    
    image = response.__dict__['_content']
    encoded_string = base64.b64encode(image)
    
    with open("img_static/imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(encoded_string))

    image_name = "img_static/imageToSave.png"

    return send_file(image_name, mimetype='image/png') 
		
		
if __name__ == "__main__":
    app.run()