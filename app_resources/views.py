# import os
from flask import Blueprint, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import ffmpeg

from .extract_audio import os, extract

view =  Blueprint("main", __name__)

@view.route("/")
def home():
    return render_template("home.html")

# receives video
@view.route("/api/home", methods=["POST"])
def receive():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    
    # If the user does not select a file, the browser submits an empty file without a filename
    if not filename:
        return jsonify({'error': 'No selected file'}), 400
    # Check if the file is allowed
    allowed_extensions = {'mp4', 'avi', 'mov'}
    if '.' not in file.filename or file.filename.split('.')[-1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file format'}), 400
        
    file.save(os.path.join("uploads", filename))
    try:
        output_data = extract(f"uploads/{filename}", f'uploads/{os.path.splitext(filename)[0]}.wav')
    except Exception as e:
        # print(e)
        return jsonify({'error': str(e)}), 500

    # Return a success response
    return send_file(output_data, mimetype='audio/wav')