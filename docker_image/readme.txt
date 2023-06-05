#Команда для сборки Docker image:

-- docker build -t mysqldb .

#Команда для запуска Docker image:

-- docker run mysqldb

#Смотрим id контейнера:

-- docker container ls

#Команда для доступа внутрь контейнера:

-- docker exec -it <имя образа> bash

#Команды для работы с базой внутри контейнера

-- mysql -pMYSQL_ROOT_PASSWORD #подключаемся к БД
-- use recrut;  #выбираем БД Recrut
-- show tables; #показывает таблицы внутри БД

