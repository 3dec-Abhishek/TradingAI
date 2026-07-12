from fastapi import FastAPI



app = FastAPI()



@app.get("/")
def home():

    return {

        "system":
        "Trading AI",

        "status":
        "running"

    }



@app.get("/health")
def health():

    return {

        "broker":"OK",

        "AI":"OK",

        "market":"OK"

    }