import requests

# создадим нового питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 999999999, "category": {"id": 0, "name": "string"},
        "name": "Jack", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
res_post = requests.post('https://petstore.swagger.io/v2/pet',
                         headers=headers, json=data)
print(f'Статус кода: {res_post.status_code}\n')
print(res_post.json(), '\n')

# переименуем питомца
headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
data_put = {"id": 999999999, "category": {"id": 0, "name": "string"}, "name": "Meggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}], "status": "available"}
res_put = requests.put('https://petstore.swagger.io/v2/pet',
                       headers=headers_put, json=data_put)
print(f'Статус кода: {res_put.status_code}\n')
print(res_put.json(), '\n')

# проверим смену имени по ID питомца
res_getID = requests.get(f'https://petstore.swagger.io/v2/pet/{999999999}',
                         headers = {'accept': 'application/json'})
print(f'Статус кода: {res_getID.status_code}\n')
print(res_getID.json(), '\n')

#удалим питомца
res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{999999999}',
                             headers={'accept': 'application/json'})
print(f'Статус кода: {res_delete.status_code}\n')
print(res_delete.json(), '\n')
