from flask import Flask
import time

app = Flask(__name__)

# Capture app start time
start_time = time.time()

@app.route("/ready")
def readiness():
    """
    This endpoint is used by the Kubernetes READINESS PROBE.

    First 30 seconds:
        - Returns 200 (READY)
        - Pod receives traffic

    After 30 seconds:
        - Returns 503 (NOT READY)
        - Pod is REMOVED from Service endpoints
        - Container is NOT restarted
    """
    if time.time() - start_time > 30:
        return "NOT READY", 503   # Readiness FAILS (traffic stopped)
    return "READY", 200           # Readiness PASSES

@app.route("/")
def home():
    return "App is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

