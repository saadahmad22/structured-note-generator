import os
from flask import Blueprint, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from io import BytesIO
import ffmpeg

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
        # Read the file into memory
        input_loc = f"uploads/{filename}"
        output_loc = f'uploads/{os.path.splitext(filename)[0]}.wav'
        if not os.path.isfile(input_loc):
            input_ = ffmpeg.input(input_loc)
            input_.output(output_loc, acodec='pcm_s16le', ar='16000', ac='1').run()
        output_data = open(output_loc, "rb")
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Return a success response
    return send_file(output_data, mimetype='audio/wav')