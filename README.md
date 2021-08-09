
1) rename file .env_example for .env and fill in variables
2) run the command in the console: docker-compose run django
3) after: docker-compose up
4) enter the container shell: docker exec -it django sh
5) apply migrations: python manage.py migrate => exit
6) restart "docker-compose up"

http://127.0.0.1:8000/register/- register user => login => start chat
