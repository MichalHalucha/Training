import json

#some JSON input
x =  '{ "name":"John", "age":30, "city":"New York"}'

#convert from JSON to python
y = json.loads(x)
print(y["age"])
print(y["city"])

#convert from python to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)
