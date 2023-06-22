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

CREATE TABLE Questions (
  id int NOT NULL AUTO_INCREMENT,
  question_id int NOT NULL,
  type_question varchar(255) DEFAULT NULL,
  correct_answer ENUM('TRUE','FALSE'),
  content varchar(255),
  PRIMARY KEY (id)
);

INSERT INTO Questions(question_id, type_question, correct_answer, content) VALUES(1,'Question','TRUE','Are you from England');
INSERT INTO Questions(question_id, type_question, correct_answer, content) VALUES(2,'Question','TRUE','Where was you born');

CREATE TABLE Admins (
  id int NOT NULL AUTO_INCREMENT,
  first_name varchar(255) DEFAULT NULL,
  second_name varchar(255) DEFAULT NULL,
  e_mail varchar(255) DEFAULT NULL,
  pswd_hash varchar(255) DEFAULT NULL,
  login varchar(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO Admins(first_name, second_name, e_mail, login) VALUES("Steve","Jobs","apple@apple.com","admin");


CREATE TABLE Recruts (
  id int NOT NULL AUTO_INCREMENT,
  login varchar(255) NOT NULL,
  first_name varchar(255) DEFAULT NULL,
  second_name varchar(255) DEFAULT NULL,
  e_mail varchar(255) DEFAULT NULL,
  pswd_hash varchar(255) DEFAULT NULL,
  planet varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
);


