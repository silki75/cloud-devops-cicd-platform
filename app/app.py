from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Cloud Deployment Project</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f8;
                    text-align: center;
                    padding-top: 80px;
                }
                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    width: 60%;
                    margin: auto;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #1f2937;
                }
                p {
                    color: #4b5563;
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Production-Style DevOps CI/CD Project</h1>
                <p>Deployed using Docker, Terraform, GitHub Actions, AWS, and Azure.</p>
                <p>Status: Running Successfully</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloud-devops-cicd-platform",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "local"),
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/version")
def version():
    return jsonify({
        "app": "cloud-devops-cicd-platform",
        "version": "1.0.0",
        "deployed_by": "GitHub Actions"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)