import  requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty'}, )

# To convert response in the json format instead of converting string into json, there is method by which we can convert the response directly into json format

# print(type(response.text))
# print(response.text)
# dict_response = json.loads(response.text)
# print(dict_response[0]['isbn'])

#  Converting response into json format

json_response = response.json()
# print(json_response)
# print(type(json_response))
# print(json_response[0]['book_name'])
assert response.status_code == 200
# print(response.headers)
validate_headers = response.headers
assert validate_headers['Server'] == 'Apache'

# retrive the book details with ISBN RGHCC
for actualbook in json_response:
    # print(actualbook)
    # print(type(actualbook))
    if actualbook['isbn'] == 'BNO121192':
        print(actualbook)
        break
    else:
        print('no books are available')
expected_book = {'book_name': 'Learning Rest API with QA academy', 'isbn': 'BNO121192', 'aisle': '227'}

assert actualbook == expected_book