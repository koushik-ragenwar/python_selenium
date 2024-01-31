import requests
from Utilities.configurations import *
from Utilities.resources import *
from TestData.APITestData.PayLoadData import *

# storing headers parameter in headers variable
headers = {'Content-Type': 'application/json'}

# fetching API url endpoint and from properties.ini and configurations python file and storing it into wordbook
# variable
wordbook = getConfig()['API']['endpoint'] + APIResources.add_book

# storing the post API endpoint into add_book variable
add_book = requests.post(wordbook, json=deletebook("uir123568"),
                         headers=headers, )

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

# storing the post API endpoint into urldeletebook variable
urldeletebook = getConfig()['API']['endpoint'] + APIResources.delete_book

# storing the post API endpoint into add_book variable
response_deltethebook = requests.post(urldeletebook, json={"ID": bookId},
                                      headers=headers, )

# asserting response code of API endpoint
assert response_deltethebook.status_code == 200

# storing msg response into deletedjson variable
deletedjson = response_deltethebook.json()
print(deletedjson['msg'])

# asserting the response msg after adding the book with expected text
assert deletedjson['msg'] == "book is successfully deleted"
