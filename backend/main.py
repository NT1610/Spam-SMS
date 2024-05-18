from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
from fastapi.staticfiles import StaticFiles
import logistic_regression, SVM

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PATH2 = os.getenv("OUTPUT_PATH2")

# Initialize FastAPI app
app = FastAPI(
    title="API Cybergame",
    version="1.0.0",
    openapi_url="/openapi.json",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define data model for input
class InputData(BaseModel):
    input_comment: str
    input_option: str


# Define function to make predictions
def make_predictions(list_inputs, algorithm):
    # print(list_inputs, algorithm)
    vectorizer_file = "loaded_models/tfidf_vectorizer.pkl"

    if algorithm == "Logistic Regression":
        model_file = "loaded_models/tfidf_logistic_regression.pkl"
        return logistic_regression.make_predictions(
            list_inputs=list_inputs,
            vectorizer_file=vectorizer_file,
            model_file=model_file,
        )
    elif algorithm == "SVM":
        model_file = "loaded_models/tfidf_SVM.pkl"

        predict = SVM.make_predictions(
            list_inputs=list_inputs,
            vectorizer_file=vectorizer_file,
            model_file=model_file,
        )

        return list(predict)


# Endpoint to handle text predictions
@app.post("/predict/")
async def predict(input_data: InputData):
    list_inputs = input_data.input_comment.split("\n")

    predictions = make_predictions(list_inputs, input_data.input_option)
    # predictions = [print(i) for i in predictions]

    predictions = [str(i) for i in predictions]
    print(predictions)
    return predictions


# Endpoint to handle file uploads
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


# Serve static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
    # print(make_predictions(["ádasd", "list"], "SVM"))
    # print(type(make_predictions(["ádasd", "list"], "SVM")))
