
from flask import Flask
import time

# Create Flask application
app = Flask(__name__)

# Capture the start time of the application
start_time = time.time()

@app.route("/health")
def health():
    """
    This endpoint is used by the Kubernetes LIVENESS PROBE.
    
    For the first 30 seconds:
        - It returns 200 -> meaning the app is healthy
    
    After 30 seconds:
        - It returns 500 -> meaning the app is UNHEALTHY
        - Kubernetes will detect this and restart the container
    """
    if time.time() - start_time > 30:  # After 30 sec
        return "UNHEALTHY", 500        # Liveness probe FAILS
    return "OK", 200                   # Liveness probe PASSES

@app.route("/")
def home():
    """General homepage endpoint for manual testing"""
    return "App is running"

# Run the server on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

