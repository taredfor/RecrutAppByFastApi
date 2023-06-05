create database recrut;
use recrut;

CREATE TABLE Users (
  id int NOT NULL AUTO_INCREMENT,
  first_name varchar(255) DEFAULT NULL,
  second_name varchar(255) DEFAULT NULL,
  e_mail varchar(255) DEFAULT NULL,
  pswd_hash varchar(255) DEFAULT NULL,
  planet varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO Users(first_name, second_name, planet, e_mail) VALUES("Jorg","Bush","Florida","usa@usa.com");
INSERT INTO Users(first_name, second_name, planet, e_mail) VALUES("Steve","Sigal","Siatl","sigal@mail.ru");

