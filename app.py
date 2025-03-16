import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running successfully!"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Render का PORT यूज़ करें
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True) # remove reload=true





