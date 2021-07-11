import os
import urllib.request
import numpy as np
import detect_mask_video as dmv
from flask import Flask, request, jsonify, render_template,Response
import pickle
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
# model = pickle.load(open('', '')
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/stream',methods=['GET'])
def stream():
	return Response(dmv.start(), mimetype='multipart/x-mixed-replace; boundary=frame')
#@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
 #  if request.method == 'POST':
  #    f = request.files['file']
   #   f.save(secure_filename(f.filename))
      #Model Code
    #  return 'file uploaded successfully' 
def upload_form():
	return render_template('index.html')

@app.route('/uploader', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		print('Image successfully uploaded and displayed below',filename)
       
		return render_template('index.html', filename=filename)
	else:
		print('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)
@app.route('/display/<filename>')
def display_image():
	return redirect(url_for('static', filename='dataset/' + filename), code=301,prediction=classification)

UPLOAD_FOLDER = 'static/dataset/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 *2400* 2400
app.config["TEMPLATES_AUTO_RELOAD"]=True


if __name__ == "__main__":
    app.run(debug=True)
    