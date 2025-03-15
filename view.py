from app import app
from flask import request, render_template

import os

from skimage.matrics import structural_similarity
import imutils
import cv2
from PIL import Image

app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

@app.route("/",methods = ['GET','POST'])
def index():
	if request.method == "GET":
		return render_template = ("index.html")
	if request.method == "POST":
		file_upload = request.files['file_upload']
		filename = file_upload.filename

		uploaded_image = Image.open(file_upload).resize((250,160))
		uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'],'image.jpg'))

		original_image = Image.open(os.path.join(app.config['EXISTING_FILE'],'image.jpg')).resize((250,160
		original_image.save(os.path.join(app.config['EXISTING_FILE'],'image.jpg'))

		original_image= cv2.imread(os.path.join(app.config['EXISTING_FILE'],'image.jpg'))
		uploaded_image= cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'],'image.jpg'))

		original_gray = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
		uploaded_image = cv2.cvtColor(uploaded_image,cv2.COLOR_BGR2GRAY)
