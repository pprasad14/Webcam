from flask import Flask, jsonify, send_file
import os
import requests
import base64
import datetime

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
    
    image_data = response.__dict__['_content']

    # # Method 1:
    # encoded_string = base64.b64encode(image_data)
    
    # with open("img_static/imageToSave.png", "wb") as fh:
    #     fh.write(base64.decodebytes(encoded_string))

    # image_path = "img_static/imageToSave.png"

    # return send_file(image_path, mimetype='image/png') 

    #############

    ## Method 2:
    date_time = str(datetime.datetime.now())  #get current datetime, and make it string
    
    # replacing all occurences of [':',' ','.','-'] in date_time with '_'
    for ch in [':',' ','.','-']:
         if ch in date_time:
            date_time = date_time.replace(ch,'_')

    image_path = "img_static/"+date_time+".png"
    
    with open(image_path, "wb") as fh:
        fh.write(image_data);    

    return send_file(image_path, mimetype='image/png')


if __name__ == "__main__":
    app.run()