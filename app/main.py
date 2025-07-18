from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from strawberry.fastapi import GraphQLRouter

from app.logger import logger
from app.config import PORT
from app.db import get_session, init_db
from app.graphql.schema import schema

app = FastAPI(title="Flight Catalog Microservice")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://54.225.75.133:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_context(request: Request):
    return {
        "request": request,
        "session": await get_session().__anext__()  
    }

graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/api/flight-catalog")


@app.options("/api/flight-catalog")
async def graphql_options_handler(request: Request):
    return JSONResponse(
        content={},
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "http://54.225.75.133:3000",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Allow-Headers": "Authorization, Content-Type",
            "Access-Control-Allow-Credentials": "true",
        }
    )


@app.on_event("startup")
async def startup_event():
    await init_db()
    logger.info("🚀 Microservicio ms-flight-catalog iniciado")
