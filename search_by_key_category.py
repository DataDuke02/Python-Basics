def search_by_category(records, category):
    result = []
    for record in records:
        if record["category"].lower() == category.lower():
            result.append(record)
    return result

def search_by_keyword(records, keyword):
    result = []
    for record in records:
        if keyword.lower() in record["ocr_text"].lower():
            result.append(record)
    return result

images = [
    {"id": 1, "filename": "shot1.png", "category": "code",    "ocr_text": "def hello import os python"},
    {"id": 2, "filename": "shot2.png", "category": "receipt", "ocr_text": "total amount paid invoice"},
    {"id": 3, "filename": "shot3.png", "category": "code",    "ocr_text": "function javascript const"},
    {"id": 4, "filename": "shot4.png", "category": "notes",   "ocr_text": "todo meeting agenda follow up"},
    {"id": 5, "filename": "shot5.png", "category": "code",    "ocr_text": "import pandas numpy dataframe"},
]

print(search_by_category(images, "code"))

print(search_by_keyword(images, "import"))
