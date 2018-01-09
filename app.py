import os
import cv2
from flask import Flask, request, redirect, url_for, send_from_directory,render_template,jsonify
from werkzeug.utils import secure_filename
from label import result
import shutil



UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_folder(folder_location):
	if not os.path.exists(folder_location):
		os.makedirs(folder_location)

def refresh_folder(folder_location):
	if len(os.listdir(folder_location)) > 0:
		for i in os.listdir(folder_location):
			file_path = os.path.join(folder_location, i)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
			except Exception as e:
				print(e)
	else:
		return 0

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	#create the folder ./images
	create_folder(UPLOAD_FOLDER)

	#refreshing the folder by deleting the previous images in it.
	refresh_folder(UPLOAD_FOLDER)

	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))
	return render_template('input.html')

@app.route('/show/<filename>')
def uploaded_file(filename):
	file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	score =result(file_location)
	return render_template('output.html', filename=filename,score=score)

@app.route('/uploads/<filename>')
def send_file(filename):
	return send_from_directory(UPLOAD_FOLDER, filename)