from flask import Flask, render_template, request, flash, jsonify
from main import translation
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder = 'templates')
app.secret_key = "manbearpig_MUDMAN888"
cors = CORS(app)

translationtext = {
        'translatedtext' : '',
        'detected_language' : ''
    }

@app.route("/")
def home():
	return "Please navigate to /translate"

@app.route("/test", methods=["POST"])
def test():
    
    if request.method == 'POST':
        data = request.json
        print(data['text'], data['lang'])
        translationtext['translatedtext'], translationtext['detected_lang'] = translation(data["text"],data['lang'])
        print(translationtext['translatedtext'], translationtext['detected_lang'])
        return "DATA POST"
    return(translationtext)
@app.route("/testget", methods=["GET"])
def testget():
    if request.method == 'GET':
        return (jsonify(translationtext['translatedtext']))
    return(jsonify(translationtext))
    




@app.route("/translate", methods=["GET", "POST"])
def translate():
    if request.method == 'POST':
        print(request.form)
        print(request.form.get("text"))
        print(request.form.get("lang"))
        ttext, detected_language = translation(request.form.get("text"),request.form.get("lang"))
        return render_template("form.html", text = ttext, detected_language = detected_language)
    
    return render_template("form.html")
# def get_lang(language, text):
#     language_params = {
#         "language" : language,
#         "text" : text
#     }

#     extra = request.args.get("extra")
#     if extra:
#         language_params["extra"] = extra
#     return jsonify(user_data),200

# @app.route("/translate", methods = ['GET' , 'POST'])
# def post_lang():
#     if request.method == 'POST':
#         language = request.form.get('language')
#         text = request.form.get('text')
#         translation = {
#             "language" : language,
#             "text" : text
#         }
#         return jsonify(translation),201
#     else:
#         return "No data to work on"

if __name__ == "__main__":
    app.run(debug=True, host = '192.168.56.1')
