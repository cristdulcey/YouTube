# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`
import io

from firebase_functions import https_fn
from firebase_admin import initialize_app
from minio import Minio
# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")

client = Minio(
    "api-minio.loducode.com",
    access_key="tLrVSmAykaHvmNYx0D0x",
    secret_key="nLKjbOgldQxLKeYhoazCZiN5nQOafo6HfUj2etqT",
    secure=False
)

@https_fn.on_request()
def upload_file(req: https_fn.Request) -> https_fn.Response:
    try:
        file = req.files.get("file")
        if not file:
            return https_fn.Response("No file found", status=400)
        file_name = file.filename
        file_data = file.stream.read()  # read file data into bytes
        file_size = len(file_data)  # size in bytes
        client.put_object("miniotest", file_name, io.BytesIO(file_data), file_size)
        return https_fn.Response("File uploaded successfully to Minio")
    except Exception as e:
        return https_fn.Response(str(e), status=500)
