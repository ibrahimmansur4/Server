from flask import Flask, render_template, send_file
import socket

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/download')
def download():
    # Replace this with the path to your actual file
    file_path = 'path/to/your/cool/file.txt'
    return send_file(file_path, as_attachment=True)
if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    
    print(f"Server running at: https://{ip_address}:8080")
    app.run(debug=True, ssl_context=context, host='0.0.0.0', port=8080)