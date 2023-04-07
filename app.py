from flask import Flask, request

app = Flask(__name__)


@app.route("/health-check")
def health_check():
    response = f"<p>request.remote_addr: {request.remote_addr}</p>"
    return response
