from fastapi import FastAPI
from fastapi_profiler import PyInstrumentProfilerMiddleware

from src.routers.routers import process_router
from src.middlewares import ContentTypeMiddleware


app = FastAPI(title='Process data service')
app.add_middleware(PyInstrumentProfilerMiddleware)
app.add_middleware(ContentTypeMiddleware)

app.include_router(process_router, prefix="/api")
