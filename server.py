from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'mp4-file' not in request.files:
        return "No file part"
    
    file = request.files['mp4-file']
    
    if file.filename == '':
        return "No selected file"
    
    if file and file.filename.endswith('.mp4'):
        output_folder = 'uploads'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        video_path = os.path.join(output_folder, file.filename)
        file.save(video_path)
        
        # Forward the file to the Colab server
        colab_url = 'ADD NGROK LINK HERE'
        with open(video_path, 'rb') as f:
            response = requests.post(colab_url, files={'file': f})
        
        if response.status_code == 200:
            pdf_path = os.path.join(output_folder, 'notes.pdf')
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            return send_file(pdf_path, as_attachment=True)
        else:
            return "Failed to process the video", 500
    
    return "Invalid file type"

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(port=33060, debug=True)
