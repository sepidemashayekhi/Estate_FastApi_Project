from .conection import Conection
from .ErrorList import error_list
from .functions import roman_numerals

from fastapi import APIRouter,status,Response
from pydantic import BaseModel, EmailStr

import bcrypt
import jwt



con=Conection()
router=APIRouter()

returnData={
    "message":None,
    'data':None,
    "code":None,
    "success":None
}


class UserCreate(BaseModel):
    Name: str | None = None
    Family : str  | None = None
    RoleId: str
    Password: str
    Email: EmailStr

class UserLogin(BaseModel):
    Email : EmailStr
    Password : str


@router.post('/user/create')
def create_user(user_in:UserCreate,response:Response):

    query=f"SELECT ID FROM ROLE WHERE RoleCode= '{user_in.RoleId}' "
    con.cursor.execute(query)
    role_id=con.cursor.fetchone()

    if not role_id:

        returnData['message']=error_list[104]
        returnData['code']=400
        response.status_code=status.HTTP_400_BAD_REQUEST

        return returnData

    check_email=f"""
        SELECT ID FROM [User] WHERE Email='{user_in.Email}'
    """
    con.cursor.execute(check_email)
    repetitious=con.cursor.fetchall()

    if repetitious:
        returnData['message']=error_list[201]
        returnData['code'] = 400
        response.status_code = status.HTTP_400_BAD_REQUEST
        return returnData


    con.cursor.execute("select isnull(MAX(ID),0)+1 from [User]")
    max_id=con.cursor.fetchone()[0]
    roman_number=roman_numerals(max_id)

    insert_query=f"""
        INSERT INTO [User](UserCode,RoleId,Name,Family,Email,Password)
        VALUES ('{roman_number}',
        (select ID from  Role where RoleCode='{user_in.RoleId}')
        ,N'{user_in.Name}'
        ,N'{user_in.Family}'
        ,'{user_in.Email}'
        ,CONVERT(VARCHAR(max), HASHBYTES('SHA1', '{user_in.Password}'), 2)
         )
    """

    con.cursor.execute(insert_query)
    con.cursor.commit()

    encoded_jwt = jwt.encode({"UserCode":   str(roman_number),
                              "RoleId"  :   user_in.RoleId
                              },
                             "secret", algorithm="HS256")
    returnData['message']=error_list[100]
    returnData['code']=201
    returnData['data']=encoded_jwt
    returnData['success']=True
    response.status_code=status.HTTP_201_CREATED
    return returnData


@router.post('/user/login')
def login_user(user_in:UserLogin,response:Response):
    user_email=user_in.Email
    query=f"""
        SELECT ID,UserCode
        FROM [User]
        WHERE CONVERT(VARCHAR(max), HASHBYTES('SHA1', '{user_in.Password}'), 2) = [User].Password  
        AND Email='{user_email}' 
    """
    con.cursor.execute(query)
    user_info=con.cursor.fetchone()

    if not user_info:
        returnData['message'] = error_list[202]
        returnData['code'] = 400
        response.status_code = status.HTTP_400_BAD_REQUEST
        return returnData

    encoded_jwt = jwt.encode({"UserCode":user_info[1],
                              "RoleId": user_info[0],
                              },
                             "secret", algorithm="HS256")
    returnData['message'] = error_list[100]
    returnData['code'] = 200
    returnData['data']=encoded_jwt
    response.status_code = status.HTTP_200_OK
    return returnData















