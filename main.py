from flask import Flask, request
from rembg import remove

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

output_path = 'output.png'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route("/api/rembg", methods=['POST'])
def rem_bg():
    if 'file' not in request.files:
        return "No file part in request", 400
    file = request.files["file"]

    if file.filename == '':
        return "Empty file submitted", 400
    if file and allowed_file(file.filename):
        try:
            with open(output_path, 'wb') as o:
                input = file.read()
                output = remove(input)
                o.write(output)
            return "Success at handling file", 200
        except Exception as e:
            print(f"Error occured: {e}")
            return f"Error handling file {e}", 400

    return "<h1>This is rembg</h1>"

@app.route("/<path:path>")
def catch_all(path):
    return f"{path} Page not found...", 409
