from fastapi import FastAPI

app = FastAPI()

items = []


@app.get('/')
def read_root():
    """Главная страница API."""
    return {'message': 'Hello API'}


@app.post('/items')
def create_item(name: str):
    """Добавляет элемент в список."""
    items.append(name)
    return {'item': name, 'total': len(items)}


@app.get('/items')
def get_items():
    """Возвращает все элементы."""
    return items
