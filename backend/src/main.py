from fastapi import FastAPI, HTTPException, status, Depends, File, UploadFile
from db.database import engine, get_db
from typing import Any, List
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import os

app = FastAPI()

UPLOAD_DIR = "./files"

@app.get("/")
async def hello_world() -> str:
    return "Hello world"


@app.post("/upload_data")
async def upload_data(files: List[UploadFile], db: Any = Depends(get_db)):
    try:
        saved_files = []
        for file in files:
            file_location = os.path.join(UPLOAD_DIR, file.filename)
            
            with open(file_location, "wb") as f:
                f.write(await file.read())
            
            saved_files.append(file_location)
        
        return JSONResponse(content={"uploaded_files": saved_files})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi possível fazer o upload dos dados!")


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)