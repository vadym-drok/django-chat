Chat web application. 
Login and registration function, chat-room made with django-channels 2 and asgi. 
The message is sent: nickname, time, text. 
The possibility of anonymous messages has been implemented.
The possibility of a delayed message has been implemented (celery).
Made docker-compose file.
DataBase: Postgreslq.
CeleryBroker: Redis


Instruction for running in docker:

1) rename file .env_example for .env and fill in variables
2) run the command in the console: docker-compose run django
3) after: docker-compose up
4) enter the container shell: docker exec -it django sh
5) apply migrations: python manage.py migrate => exit
6) restart "docker-compose up"

http://127.0.0.1:8000/register/- register user => login => start chat
