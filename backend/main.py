from music21 import metadata, instrument

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from models.config import Config
from scripts.routers.exercise_router import route_exercise


app = FastAPI()

# Allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-exercise")
def generate_exercise(request: Config):
    print("generating exercise")
    part_stream = route_exercise(request)

    part_stream.metadata = metadata.Metadata()
    part_stream.metadata.title = ""
    part_stream.metadata.composer = ""
    xml = part_stream.write("musicxml")

    with open(xml, "r") as f:
        data = f.read()

    return Response(content=data, media_type="application/xml")