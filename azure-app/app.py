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
            <title>Azure DevOps CI/CD Project</title>
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
                    width: 65%;
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
                .badge {
                    display: inline-block;
                    padding: 10px 18px;
                    background: #e0f2fe;
                    border-radius: 20px;
                    color: #0369a1;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Azure Container Apps CI/CD Project</h1>
                <p>Deployed using Docker, GitHub Actions, Terraform, and Azure Container Apps.</p>
                <p class="badge">Status: Running Successfully</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "azure-container-apps-devops-project",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "azure"),
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/version")
def version():
    return jsonify({
        "app": "azure-container-apps-devops-project",
        "version": "1.0.0",
        "deployed_by": "GitHub Actions",
        "platform": "Azure Container Apps"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)