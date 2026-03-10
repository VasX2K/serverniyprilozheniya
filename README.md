# Контрольная работа №1. FastAPI  
  
## Структура проекта  
  
- `app.py` - основное приложение FastAPI  
- `models.py` - Pydantic модели  
- `index.html` - HTML страница для задания 1.2  
- `requirements.txt` - зависимости 
  
## Установка и запуск  
  
```bash  
pip install -r requirements.txt  
uvicorn app:app --reload  
``` 
  
## API Endpoints  
  
- `GET /` - Задание 1.1: Приветственное сообщение  
- `GET /html` - Задание 1.2: HTML страница  
- `POST /calculate` - Задание 1.3: Сумма двух чисел  
- `GET /users` - Задание 1.4: Данные пользователя  
- `POST /user` - Задание 1.5: Проверка совершеннолетия  
- `POST /feedback` - Задание 2.1: Отправка отзыва  
- `POST /feedback/validated` - Задание 2.2: Отзыв с валидацией 
