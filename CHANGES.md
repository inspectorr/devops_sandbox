## v2

### Added

- .docs/1.md - разбиваем readme на несколько файлов
- .docs/2.md - разбиваем readme на несколько файлов
- .gitignore - игнорируем файл .env
- .template.env - шаблон для .env
- docker-compose.yml - конфиг для docker compose
- init.sql - скрипт для инициализации базы данных


### Changed

- fastapi.good.Dockerfile - фикс: копируем в образ только нужные файлы
- README.md - ссылки на разбитые readme файлы
- main.py - ручки для создания и получения сообщений
- requirements.txt - добавляем psycopg2


## v1

### Added

- fastapi.bad.Dockerfile
- fastapi.good.Dockerfile
- main.py
- README.md
- requirements.txt
