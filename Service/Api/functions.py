from .conection import Conection
con=Conection()

def roman_numerals(num):
    roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_num = ''
    for key in roman_dict:
        while num >= key:
            roman_num += roman_dict[key]
            num -= key

    return roman_num


def fetch(query_str):
    con.cursor.execute(query_str)
    return {'results':
            [dict(zip([column[0] for column in con.cursor.description], row))
             for row in con.cursor.fetchall()]}



def insert(query_str):
    con.cursor.execute(query_str)
    con.cursor.commit()