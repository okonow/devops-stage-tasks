from flask import Flask, jsonify
import os
import socket
from dotenv import load_dotenv

load_dotenv()

container_hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
container_ip = s.getsockname()[0]
s.close()

author = os.getenv('AUTHOR', 'Error with .env file')
server_hostname = os.getenv('SERVER_HOSTNAME', 'Need to set SERVER_HOSTNAME through env variable with script.sh')
server_ip = os.getenv('SERVER_IP', 'Need to set SERVER_HOSTNAME through env variable with script.sh')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({
        "author": author,
        "server": {
            "hostname": server_hostname,
            "ip": server_ip
        },
        "container": {
            "hostname": container_hostname,
            "ip": container_ip
        }
    })