import requests
from TestData.APITestData.PayLoadData import *

# storing the post API endpoint into add_book variable
add_book = requests.post('http://216.10.245.166/Library/Addbook.php', json=deletebook("uir12356"),
                         headers={'Content-Type': 'application/json'}, )

# asserting response code of API endpoint
assert add_book.status_code == 200

# printing the json response for the post API of add_book
print(add_book.json())

# printing the type of json response to verify its datatype .i.e. tuple, dictionary, list
print(type(add_book.json()))
responseJson = add_book.json()

# storing ID response into bookId variable
bookId = responseJson['ID']
print(responseJson['ID'])

# asserting the response msg after adding the book with expected text
assert responseJson['Msg'] == 'successfully added'

# Delete the book

# storing the post API endpoint into add_book variable
response_deltethebook = requests.post('http://216.10.245.166//Library/DeleteBook.php', json={"ID": bookId},
                                      headers={'Content-Type': "application/json"}, )

# storing msg response into deletedjson variable
assert response_deltethebook.status_code == 200

# asserting the response msg after adding the book with expected text
deletedjson = response_deltethebook.json()
print(deletedjson['msg'])
assert deletedjson['msg'] == "book is successfully deleted"
