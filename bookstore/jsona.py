import json

json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genres": ["Fiction", "Classic"],
    "available": true
}
'''

book = json.loads(json_string)

print("Title:", book["title"])
print("Author:", book["author"])
print("Year:", book["year"])
print("Genres:", ", ".join(book["genres"]))
print("Available:", book["available"])