# files api
from .functions import fetch

from fastapi import APIRouter,status,Response
from pydantic import BaseModel
from typing import List, Dict


file_router = APIRouter()

HOMESIZEPAGE=2

class FileCreate(BaseModel):
    Title : str
    Address :str
    CategoryId : int
    EstateId : int
    StateId : int
    CreatorId : int
    PhoneNumber : str | None
    Laws : str
    Wlelfare : List[Dict[str,str]]



@file_router.get('/files/')
def files(page_number : int | None = None , page_size: int | None = None):
    query = """
        select
        F.FilesCode file_id
        ,F.Title file_title
        ,F.Address file_address
        ,T.Title file_type
        ,C.Title file_category
        from Files F
        inner join [Types] T on T.ID=F.TypeId
        inner join Category C on C.ID=F.CategoryId
        order by F.ID DESC
    """
    if not (page_size or page_number):
        query += F"OFFSET 0 ROWS FETCH NEXT {HOMESIZEPAGE} ROWS ONLY"
        result=fetch(query)
        return result


    offset=(page_size*(page_number-1))
    query += f"OFFSET {offset} ROWS FETCH NEXT {page_size} ROWS ONLY"
    result=fetch(query)
    return result




@file_router.post('/files/create')
def create_files(file_info:FileCreate):
    pass



