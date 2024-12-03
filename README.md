# dan_toropov_cw_8

Контекст
Для быстрого масштабирования проекта применяется контейнеризация. Для этого вам предстоит «завернуть» 
ваш проект в Docker и настроить на самостоятельный запуск.


Для работы программы необходимо:

1. установленный docker
2. создать .env по примеру .env.example
3. sudo docker-compose up -d --build #команда для сборки и запука контейнеров
4. sudo docker-compose exec app python manage.py csu #команда для создания суперпользователя 
   логин пользователя и пароль можно изменить в файле /users/management/commands/csu.py
5. загрузить при необходимости фикстуры 
   sudo docker-compose exec app python manage.py loaddata ./data/fixtures/test_data_users.json
   sudo docker-compose exec app python manage.py loaddata ./data/fixtures/test_data_habits.json


