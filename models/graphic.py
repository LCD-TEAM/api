import requests
from datetime import date, datetime, timedelta
import xml.etree.ElementTree as ET

def get_valutes():
    response = requests.get('http://www.cbr.ru/scripts/XML_valFull.asp').content
    tree = ET.fromstring(response)
    ls = tree.findall('Item')
    codes = [code for code in map(lambda l: l.find('ISO_Char_Code').text, ls) if code is not None]
    return codes

def get_course_values(char_code: str):
    date_end = date.today()
    date_start = date.today() - timedelta(weeks=1)
    course = []
    while date_start != date_end:
        date_str = date_start.strftime('%d/%m/%Y')
        response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}').content
        tree = ET.fromstring(response)
        elem = tree.find(f"Valute[CharCode=\'{char_code}\']")
        course.append({
            'date': date_start,
            'value': float(elem.find('Value').text.replace(',', '.'))
        })
        date_start += timedelta(days=1)
    return course
