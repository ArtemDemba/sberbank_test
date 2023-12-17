from fastapi import FastAPI
from fastapi_profiler import PyInstrumentProfilerMiddleware
import uvicorn

from src.routers.routers import process_router
from src.middlewares import ContentTypeMiddleware


if __name__ == '__main__':

    app = FastAPI(title='Process data service')

    app.add_middleware(ContentTypeMiddleware)
    app.add_middleware(PyInstrumentProfilerMiddleware)

    app.include_router(process_router, prefix="/api")
    uvicorn.run(app, host='0.0.0.0', port=8000)
