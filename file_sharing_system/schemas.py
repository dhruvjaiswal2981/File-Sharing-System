from pydantic import BaseModel

class FileBase(BaseModel):
    filename: str
    file_url: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int

    class Config:
        orm_mode = True
