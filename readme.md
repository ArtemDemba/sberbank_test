# Process data service
***

### Требования к тестовому заданию:
- [X] Принятие дерева извлечений
- [X] Постпроцессинг
- [X] Функции нормализации 


### Запуск приложения
```
pip install pipenv
pipenv shell
pipenv install 
uvicorn main:app --reload --host 0.0.0.0
```

### Endpoints

| Method | Url                                      | Description      | Headers                                         |
|:-------|:-----------------------------------------|:-----------------|:------------------------------------------------|
| GET    | http://0.0.0.0:8000/docs                 | Swagger          | *                                               |
| POST   | http://0.0.0.0:8000/api/v1/process_tree/ | Process json/xml | Content-Type: application/json, application/xml |

### Тестовые xml и json данные находятся в папке: `examples/`
### Postman коллекция находится по пути examples/sber_test.postman_collection.json