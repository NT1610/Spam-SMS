from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
from fastapi.staticfiles import StaticFiles
import logistic_regression,SVM,ANN
from crawl.crawl_data import FacebookScraper
import os
from dotenv import load_dotenv
# import nest_asyncio
# nest_asyncio.apply()


# Load environment variables
load_dotenv()
PATH2 = os.getenv("OUTPUT_PATH2")

# Initialize FastAPI app
app = FastAPI(
    title="Spam SMS",
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

# Define data model for input
class InputDataFB(BaseModel):
    link_fb: str
    input_option: str


# Define function to make predictions
def make_predictions(list_inputs, algorithm):
    # print(list_inputs, algorithm)
    vectorizer_file = "../Model/countvecterize.pkl"

    if algorithm == "logistic-regression":
        model_file = "../Model/logistic.pkl"
        return logistic_regression.make_predictions_vectorrizer(
            data=list_inputs,
            model_vectorizer=vectorizer_file,
            model_predict=model_file,
        )
    elif algorithm == "SVM":
        model_file = "../Model/svm_model.pkl"

        predict = SVM.make_predictions_vectorrizer(
            data=list_inputs,
            model_vectorizer=vectorizer_file,
            model_predict=model_file,
        )
    elif algorithm == "ANN":
        model_file = "../Model/ann.pkl"

        predict = ANN.make_predictions_vectorrizer(
            data=list_inputs,
            model_vectorizer=vectorizer_file,
            model_predict=model_file,
        )
    # print(predict)
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

@app.post("/crawl/")
async def predict_crawl(input_data: InputDataFB):
    login_url = "https://www.facebook.com/?stype=lo&deoia=1&jlou=AfczHBzuFgKc5jde3dWHkPnlaB20s2OgvO2xVhdv5IidANHiSADnJtBKCyAvR6aWz5VMH83wtWkYKvxYe9USaIG-fC_7HhCmNfGXIp6jg_Ax3w&smuh=37746&lh=Ac-dfKrOH4QAtVz7HRw"

    scraper = FacebookScraper(login_url, input_data.link_fb)
    await scraper.scrape()
    output, text = scraper.extract_comment()

    df = scraper.save_data(output)
    try:
        scraper.store_to_db(df.values)
    except Exception as e:
        print("Unable to store data:", e)

    predictions = make_predictions(df["comment"], input_data.input_option)

    id = [str(i) for i in df['id']]
    author = [str(i) for i in df['name']]
    comment = [str(i) for i in df['comment']]
    predictions = [str(i) for i in predictions]

    df['label'] = predictions
    df.to_csv("predict")
    # print(df)

    return id, author, comment, predictions


# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
    # print(make_predictions(["ádasd", "list"], "SVM"))
    # print(type(make_predictions(["ádasd", "list"], "SVM")))
