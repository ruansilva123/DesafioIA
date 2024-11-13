from fastapi import FastAPI, HTTPException, status, Depends, UploadFile
from fastapi.responses import JSONResponse
from typing import Any, List
import os

from core.settings import FILES_PATH
from db.models import Ata, Call
from db.database import engine, get_db, Base


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/upload_data", status_code = status.HTTP_200_OK)
async def upload_data(files: List[UploadFile], db: Any = Depends(get_db)):
    try:
        saved_files = []
        for file in files:
            file_location = os.path.join(FILES_PATH, file.filename)
            
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