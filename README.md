# flask-app-hackathon-frontend
Ready to go flask app for doing demo during Computer Vision and Deep learning hackathons.

## Dependencies
Flask (0.12.2)<br />
Python 2 or 3

## app.py
This python script contains the required functions for uploading the image, displaying the image and the corresponding output

## templates/input.html
This html takes the image from the user and temporarily saves in /images 

## templates/output.html
This html displays the output of the function "result" imported from the label.py along with the uploaded image.

## Usage
To use during hackathons ,replace the code inside "result" function in label.py with your function's code.

## To Run
### Run the following commands in the terminal

export FLASK_APP = app.py<br />
flask run<br />

## Note
This is a very minimal and functional only flask app for doing demo for Computer vision and Deep Learning hackathons.Feel free to add to your own styling and other functionalities to make to more suitable for your necessities.
