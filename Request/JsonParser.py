import json

demo_json = '{"name":"John", "age":30, "car":null, "languages": ["java", "c++", "python"]}'

# Loads method parse json string and it returns dictionary

dict_type = json.loads(demo_json)
print(type(dict_type))
print(dict_type)
print(dict_type['name'])
print(dict_type['languages'][2])

# parse content from external json file

with open('C:\\Users\\ragenwark\\PycharmProjects\\pythonProject1\\TestData\\APITestData\\DemoJson.txt') as f:
    data = json.load(f)
    print(type(data))
    print(data['employee1'])
    print(data['employee1']['languages'][2])

    # Validating Age under Employess

    print(type(data['employee1']))
    for lang in data['employee1']:
        print(lang)
        # # #     print(type(image))
        if lang == "name":
            print("program passed")
        else:
            print("program failed")

#  Asserting two Json responses using local json responses

with open(
        "C:\\Users\\ragenwark\\PycharmProjects\\pythonProject1\\TestData\\APITestData\\AssertingWithDemoJson.txt") as t:
    data2 = json.load(t)
    print(data == data2)
    assert data == data2
