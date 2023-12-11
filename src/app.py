
# Importing essential libraries and modules

from flask import Flask, render_template, request , redirect, url_for
import pickle
import io
from PIL import Image
import pickle
from utils.preprocessing import clean_resume
from utils.textextraction import convert_file_to_text 
from utils.config import category_mapping

#loading models
clf = pickle.load(open('Models/clf.pkl','rb'))
tf = pickle.load(open('Models/tfidf.pkl','rb'))



app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html")

@app.route("/extract", methods=['GET', 'POST'])
def extract():
    title = "Resume Parsers"
    if request.method =="POST": 
        if "file" not in request.files:
            return redirect(redirect.url)
        resume = request.files.get("file")
        resume_file_path = f"E:/ResumeParser/tests/{resume.filename}"
        
        resume_text = convert_file_to_text(resume_file_path)  
        clean_text = clean_resume(resume_text)
        prediction = predict_result(clean_text)
             
    return render_template('prediction.html', status = 200, result = prediction, title=title)  # Redirect to the home page
    # return render_template('index.html', status=500, res = "Internal Server Error ")

def predict_result(text):
    input_features = tf.transform([text])
    prediction_id = clf.predict(input_features)[0]
    return category_mapping[prediction_id]

if __name__ == "__main__":
    app.run(debug =True)