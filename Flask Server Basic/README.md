# Secure Flask Server

This project sets up a secure Flask server that serves a simple web page and allows users to download a file.

## Table of Contents

- [Secure Flask Server](#secure-flask-server)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Server](#running-the-server)
  - [Usage](#usage)
  - [Code Explanation](#code-explanation)
    - [app.py](#apppy)
    - [index.html](#indexhtml)
    - [requirements.txt](#requirementstxt)

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ibrahimmansur4/Server.git
   cd Server/Flask\ Server\ Basic/
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Generate SSL certificates:
   ```
   openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```

2. Update the `file_path` in `app.py` to point to your actual file:
   ```python
   file_path = 'path/to/your/cool/file.txt'
   ```

## Running the Server

Run the Flask application:

```
python app.py
```

The server will start, and you'll see a message like:
```
Server running at: https://192.168.1.100:8080
```

## Usage

1. Open a web browser and navigate to the URL displayed when you started the server.
2. You'll see a welcome message and a "Download Something Cool" button.
3. Click the button to download the file specified in `app.py`.

## Code Explanation

### app.py

```python
from flask import Flask, render_template, send_file
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
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
```

This script does the following:
- Creates a Flask app
- Defines routes for the index page and file download
- Sets up SSL context for HTTPS
- Determines the server's IP address
- Runs the server on port 8080, accessible from any IP

### index.html

The `index.html` file contains the structure and styling for the web page. It includes:
- A welcome message
- A styled download button
- CSS for layout and aesthetics

### requirements.txt

This file lists all the Python packages required to run the application. You can install them using `pip install -r requirements.txt`.

Remember to keep your SSL certificates (`cert.pem` and `key.pem`) secure and not to commit them to version control.