Celery является незаменимым инструментом для веб-приложений, в которых требуется обрабатывать большое количество продолжительных задач. В данном материале мы рассмотрим, как Celery используется вместе с Flask.

Предположим, что есть веб-приложение, которое позволяет пользователям загружать изображения для обработки. Мы хотим предоставить им опции одновременной загрузки и обработки нескольких изображений с возможностью отслеживания статуса обработки каждого изображения.

```python
import random  
  
from flask import Flask, request, jsonify  
from celery import Celery, group  
import time  
  
app = Flask(__name__)  
  
# Конфигурация Celery  
celery = Celery(  
   app.name,  
   broker='redis://localhost:6379/0',  
   backend='redis://localhost:6379/0',  
)  
  
# Задача Celery для обработки изображения  
@celery.task  
def process_image(image_id: str):  
   # В реальной ситуации здесь может быть обработка изображения  
   # В данном примере просто делаем задержку для демонстрации  
   time.sleep(random.randint(5, 15))  
   return f'Image {image_id} processed'  
  
@app.route('/process_images', methods=['POST'])  
def process_images():  
   images = request.json.get('images')  
  
   if images and isinstance(images, list):  
       # Создаём группу задач  
       task_group = group(  
           process_image.s(image_id)  
           for image_id in images  
       )  
  
       # Запускаем группу задач и сохраняем её  
       result = task_group.apply_async()  
       result.save()  
  
       # Возвращаем пользователю ID группы для отслеживания  
       return jsonify({'group_id': result.id}), 202  
   else:  
       return jsonify({'error': 'Missing or invalid images parameter'}), 400  
  
@app.route('/status/<group_id>', methods=['GET'])  
def get_group_status(group_id: str):  
   result = celery.GroupResult.restore(group_id)  
  
   if result:  
       # Если группа с таким ID существует,  
       # возвращаем долю выполненных задач  
       status = result.completed_count() / len(result)  
       return jsonify({'status': status}), 200  
   else:  
       # Иначе возвращаем ошибку  
       return jsonify({'error': 'Invalid group_id'}), 404  
  
if __name__ == '__main__':  
   app.run(debug=True)
```

Запустите Redis (в качестве брокера Celery):

```bash
docker run -p 6379:6379 --name my-redis -d redis
```

Запустите воркеры Celery для обработки задач:

```bash
celery -A app.celery worker --loglevel=info
```

Запустите Flask-приложение:

```bash
python app.py
```

Теперь вы можете отправлять POST-запросы на `/process_images` в вашем Flask-приложении, передавая список images в JSON-формате. Приложение создаст группу задач для обработки каждого изображения в списке и вернёт `group_id`, который позволит отслеживать статус обработки группы задач. Вы также можете получить текущий статус группы задач, отправив GET-запрос на `/status/<group_id>`.

Если какое-либо изображение не успело обработаться, вы увидите другое значение, например 0.66667.

Многие сайты используют именно такую модель взаимодействия — раз в секунду они делают запрос к серверу, как будто спрашивают: «Ну как там?» — получают ответ и отображают его пользователю.

Этот пример демонстрирует, как использование группировки задач и отслеживание их статуса с помощью Celery позволяют параллельно обрабатывать множество задач и контролировать их выполнение, улучшая производительность и управляемость веб-приложения.

----
## Практика

Доработайте приложение, добавив следующие endpoints:

- `/cancel/<group_id>`  
    Отменяет группу задач. В этом вам поможет [метод revoke](https://docs.celeryq.dev/en/stable/userguide/workers.html#revoke-revoking-tasks).
- `/control`  
    Отображает информацию о задачах и очередях с помощью [методов celery.app.control](https://docs.celeryq.dev/en/latest/reference/celery.app.control.html). Сделайте так, чтобы информация актуализировалась раз в 10 секунд, а не при каждом запросе.