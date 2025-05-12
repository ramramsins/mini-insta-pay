from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Reporting Service")

app.include_router(router)
from prometheus_client import start_http_server, Counter
import threading

# عداد للطلبات
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

def start_metrics_server():
    start_http_server(9000)

# تشغيل السيرفر في الخلفية
threading.Thread(target=start_metrics_server, daemon=True).start()

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response
