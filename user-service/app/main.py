from fastapi import FastAPI
from app.routes import router
from prometheus_client import start_http_server, Counter
import threading

app = FastAPI(title="User Service")

# Include the router
app.include_router(router)

# Prometheus Counter for HTTP requests
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

def start_metrics_server():
    """Start Prometheus metrics server on port 9000."""
    start_http_server(9000)

# Start the Prometheus metrics server in a background thread
threading.Thread(target=start_metrics_server, daemon=True).start()

@app.middleware("http")
async def count_requests(request, call_next):
    """Middleware to count HTTP requests."""
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response
