from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = r'img_static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload_pic", methods = ['POST'])
def upload_pic():
	try:
		image = request.files['snappicture']

		image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

		return jsonify({"status":"success"})
	
	except:
		return jsonify({"status":"error"})

if __name__ == "__main__":
    app.run()