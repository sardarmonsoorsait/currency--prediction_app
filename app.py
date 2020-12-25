#Import necessary libraries
from flask import Flask, render_template, request
from gtts import gTTS
import numpy as np
import os
import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2

#load model
model =load_model("model/currency_accuraccy_75_model.h5")

print('@@ Model loaded')

def pred_currency(curr):
    img = load_img(curr,target_size=(227,227))
    img= img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    pred_prob = model.predict(img).round(3)
    pred = np.argmax(pred_prob)
    print(pred_prob)
    if np.amax(pred_prob)>0.75:
        if pred==0:
            tts = gTTS("welcome to asaiTech currency prediction app this is fifty rupees")
            tts.save('static/user uploaded/file_0.mp3')
            audio_path = 'static/user uploaded/file_0.mp3'
            prediction = "welcome to asaiTech currency prediction app this is fifty rupees"
        elif pred == 1:
            tts = gTTS("welcome to asaiTech currency prediction app this is fifty rupees old")
            tts.save('static/user uploaded/file_1.mp3')
            audio_path = 'static/user uploaded/file_1.mp3'
            prediction = "welcome to asaiTech currency prediction app this is fifty rupees"
        elif pred == 2:
            tts = gTTS("welcome to asaiTech currency prediction app this is five rupees")
            tts.save('static/user uploaded/file_2.mp3')
            audio_path = 'static/user uploaded/file_2.mp3'
            prediction = "welcome to asaiTech currency prediction app this is five rupees"
        elif pred==3:
            tts = gTTS("welcome to asaiTech currency prediction app this is five rupees coin")
            tts.save('static/user uploaded/file_3.mp3')
            audio_path = 'static/user uploaded/file_3.mp3'
            prediction = "welcome to asaiTech currency prediction app this is five rupees coin"
        elif pred == 4:
            tts = gTTS("welcome to asaiTech currency prediction app this is five hundred rupees")
            tts.save('static/user uploaded/file_4.mp3')
            audio_path = 'static/user uploaded/file_4.mp3'
            prediction = "welcome to asaiTech currency prediction app this is five hundred rupees"
        elif pred == 5:
            tts = gTTS("welcome to asaiTech currency prediction app this is hundred rupees")
            tts.save('static/user uploaded/file_5.mp3')
            audio_path = 'static/user uploaded/file_5.mp3'
            prediction = "welcome to asaiTech currency prediction app this is Hundred rupees"
        elif pred==6:
            tts = gTTS("welcome to asaiTech currency prediction app this is hundred rupees old note")
            tts.save('static/user uploaded/file_6.mp3')
            audio_path = 'static/user uploaded/file_6.mp3'
            prediction = "welcome to asaiTech currency prediction app this is Hundred rupees"
        elif pred == 7:
            tts = gTTS("welcome to asaiTech currency prediction app this is one rupees")
            tts.save('static/user uploaded/file_7.mp3')
            audio_path = 'static/user uploaded/file_7.mp3'
            prediction = "welcome to asaiTech currency prediction app this is one rupees"
        elif pred == 8:
            tts = gTTS("welcome to asaiTech currency prediction app this is one rupees coin")
            tts.save('static/user uploaded/file_8.mp3')
            audio_path = 'static/user uploaded/file_8.mp3'
            prediction = "welcome to asaiTech currency prediction app this is one rupees coin "
        elif pred==9:
            tts = gTTS("welcome to asaiTech currency prediction app this is ten rupees coin")
            tts.save('static/user uploaded/file_9.mp3')
            audio_path = 'static/user uploaded/file_9.mp3'
            prediction = "welcome to asaiTech currency prediction app this is ten rupees"
        elif pred == 10:
            tts = gTTS("welcome to asaiTech currency prediction app this is ten rupees coin")
            tts.save('static/user uploaded/file_10.mp3')
            audio_path = 'static/user uploaded/file_10.mp3'
            prediction = "welcome to asaiTech currency prediction app this is ten rupees coin"
        elif pred == 11:
            tts = gTTS("welcome to asaiTech currency prediction app this is twenty rupees")
            tts.save('static/user uploaded/file_11.mp3')
            audio_path = 'static/user uploaded/file_11.mp3'
            prediction = "welcome to asaiTech currency prediction app this is twenty rupees"
        elif pred==12:
            tts = gTTS("welcome to asaiTech currency prediction app this is two rupees")
            tts.save('static/user uploaded/file_12.mp3')
            audio_path = 'static/user uploaded/file_12.mp3'
            prediction = "welcome to asaiTech currency prediction app this is Two rupees"
        elif pred == 13:
            tts = gTTS("welcome to asaiTech currency prediction app this is two rupees coin")
            tts.save('static/user uploaded/file_13.mp3')
            audio_path = 'static/user uploaded/file_13.mp3'
            prediction = "welcome to asaiTech currency prediction app this is Two rupees coin "
        elif pred == 14:
           tts = gTTS("welcome to asaiTech currency prediction app this is twohundred rupees")
           tts.save('static/user uploaded/file_14.mp3')
           audio_path = 'static/user uploaded/file_14.mp3'
           prediction = "welcome to asaiTech currency prediction app this is Two hundred rupees"
        elif pred == 15:
            tts = gTTS("welcome to asaiTech currency prediction app this is two thousand rupees")
            tts.save('static/user uploaded/file_15.mp3')
            audio_path = 'static/user uploaded/file_15.mp3'
            prediction = "welcome to asaiTech currency prediction app this is Two Thousand rupees"
    else:
        tts = gTTS("sorry i cannot understand this note please take another photo")
        tts.save('static/user uploaded/file.mp3')
        audio_path = 'static/user uploaded/file.mp3'
        prediction = "sorry i cannot understand this note please take another photo"
    return  prediction,'prediction.html',audio_path




#------------>>pred_cot_dieas<<--end
    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
         

        print("@@ Predicting class......")
        pred, output_page,audio_path = pred_currency(curr=file_path)
        
        return render_template(output_page, pred_output = pred, user_image = file_path,mp3_path = audio_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,debug=True) 
    
    
