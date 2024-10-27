# dan_toropov_cw_7
Для работы программы необходимо:

1. Установить зависимости
2. Создать .env по примеру .env.example
3. Команда для создания суперпользователя python manage.py csu
   логин пользователя и пароль можно изменить в файле /users/management/commands/csu.py
4. Фикстуры лежат в каталоге /data/fixtures
5. settings.CACHE_ENABLED флаг включения кеширования. Необходимо установить в ОС сервер redis 

