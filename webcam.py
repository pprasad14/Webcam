from flask import Flask, jsonify, send_file
import os
import requests
import base64
import io
import cv2
import numpy as np
from PIL import Image
import datetime
from random import randint

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
    
    try: 
        response = requests.get(url)

        image_data = response.__dict__['_content']

        ## Method 1:
        
        date_folder = str(datetime.datetime.now()).split(' ')[0]
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)

        img_name = str(datetime.datetime.now()).split(' ')[1]
        

        # replacing all occurences of [':',' ','.','-'] in date_time with '_'
        for ch in [':','.']:
             if ch in img_name:
                img_name = img_name.replace(ch,'_')

        img_name = img_name + "__" + str(randint(1,9999999)) + ".png"

        image_path = date_folder + "/" + img_name
        
        with open(image_path, "wb") as fh:
            fh.write(image_data);    

        return jsonify({"status":"success", "image_path":image_path})
    
    except:
        return jsonify({"status":"failure", "image_path":"NULL"})


## Method 2:
#eee = base64.b64encode(image_data)
#ddd = eee.decode()
#img = base64.b64decode(ddd)
#upimage = Image.open(io.BytesIO(img))
# with open("img_static/imageToSave.png", "wb") as fh:
#     fh.write(upimage)
# image_path = "img_static/imageToSave.png"
# return send_file(image_path, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
