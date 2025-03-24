from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    build_version = os.environ.get('CLOUD_BUILD_VERSION', 'Unknown')
    return f"""
    <html>
        <head>
            <title>Hello Cloud App</title>
        </head>
        <body>
            <h1>Hello Cloud!</h1>
            <p><strong>CloudBuild Version: {build_version}</strong></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
