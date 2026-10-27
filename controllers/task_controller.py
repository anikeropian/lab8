from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from models.task import Database

router = APIRouter()
db = Database()
db.save("Изучить MVC")

@router.get("/tasks", response_class=HTMLResponse)
def get_tasks_view():
    """Представление (View) - отдает HTML."""
    html = "<h1>Задачи</h1><ul>"
    for t in db.get_all():
        html += f"<li>{t.id}. {t.title}</li>"
    html += "</ul>"
    return html

@router.post("/tasks")
def create_task(title: str):
    """Контроллер - вызывает модель."""
    task = db.save(title)
    return {"id": task.id, "title": task.title}
