create database statusapidb;
use statusapidb;

drop database statusapidb;


set sql_mode=IGNORE_SPACE;
show full columns from csp;

####Trocando os IDS de primary key#######
create table avaliacao_csp (
id INT NOT NULL AUTO_INCREMENT,
avaliadorid INT not null,
provedorid INT not null,
tempoid INT not null,
q1 VARCHAR(20), 
q2 VARCHAR(20),
q3 VARCHAR(20),
q4 VARCHAR(20),
q5 VARCHAR(20),
q6 VARCHAR(20),
q7 VARCHAR(20),
q8 VARCHAR(20), 
q9 VARCHAR(20),
q10 VARCHAR(20), 
q11 VARCHAR(20), 
q12 VARCHAR(20), 
q13 VARCHAR(20),
q14 VARCHAR(20),
q15 VARCHAR(20),
q16 VARCHAR(20), 
q17 VARCHAR(20), 
q18 VARCHAR(20), 
q19 VARCHAR(20), 
q20 VARCHAR(20), 
q21 VARCHAR(20), 
q22 VARCHAR(20),
q23 VARCHAR(20), 
q24 VARCHAR(20),
PRIMARY KEY (id),


constraint fk_csp_avaliador FOREIGN KEY (avaliadorid) REFERENCES avaliadores(avaliadorid) ON DELETE CASCADE ON UPDATE CASCADE,
constraint fk_csp_provedor FOREIGN KEY (provedorid) REFERENCES provedores(provedorid) ON DELETE CASCADE ON UPDATE CASCADE,
constraint fk_csp_tempo FOREIGN KEY (tempoid) REFERENCES tempos(tempoid) ON DELETE CASCADE ON UPDATE CASCADE


);

####Trocando os IDS de primary key#######
create table avaliacao_csp (
id INT NOT NULL AUTO_INCREMENT,
avaliador VARCHAR (50) NOT NULL,
provedor VARCHAR (50) NOT NULL,
mes int NOT NULL,
ano int NOT NULL,
q1 VARCHAR(20), 
q2 VARCHAR(20),
q3 VARCHAR(20),
q4 VARCHAR(20),
q5 VARCHAR(20),
q6 VARCHAR(20),
q7 VARCHAR(20),
q8 VARCHAR(20), 
q9 VARCHAR(20),
q10 VARCHAR(20), 
q11 VARCHAR(20), 
q12 VARCHAR(20), 
q13 VARCHAR(20),
q14 VARCHAR(20),
q15 VARCHAR(20),
q16 VARCHAR(20), 
q17 VARCHAR(20), 
q18 VARCHAR(20), 
q19 VARCHAR(20), 
q20 VARCHAR(20), 
q21 VARCHAR(20), 
q22 VARCHAR(20),
q23 VARCHAR(20), 
q24 VARCHAR(20),
PRIMARY KEY (id),
UNIQUE KEY (avaliador,provedor,mes,ano),


constraint fk_csp_avaliador FOREIGN KEY (avaliador) REFERENCES avaliadores(avaliador) ON DELETE CASCADE ON UPDATE CASCADE,
constraint fk_csp_provedor FOREIGN KEY (provedor) REFERENCES provedores(provedor) ON DELETE CASCADE ON UPDATE CASCADE

);



show tables;
describe avaliacao_csp;

insert into csp (tempo) values ("julho");
drop table csp;
select * from csp;
select * from avaliacao_csp;

select * from csp where avaliadorid not in (select distinct id from avaliadores);


SET FOREIGN_KEY_CHECKS = 0;

drop table avaliadores;
select * from avaliadores;
select * from provedores;
select * from tempos;
select * from avaliacao_csp;
select * from avaliacao_csp where avaliadorusr=joaquim;
show create table avaliadores;
show create table csp;

#####Trocando primary key das 3 tabelas dos IDs######
create table avaliadores (
avaliadorid INT NOT NULL AUTO_INCREMENT,
avaliador VARCHAR (50) NOT NULL UNIQUE,
avaliadorusr VARCHAR (50) NOT NULL UNIQUE ,
avaliadorpw VARCHAR (50) NOT NULL,
atividade INT NOT NULL,
gestor INT NOT NULL,
PRIMARY KEY (avaliador),
unique Key(avaliadorid)
);
create table provedores (
provedorid INT NOT NULL AUTO_INCREMENT,
provedor VARCHAR (50) NOT NULL UNIQUE,
atividade INT NOT NULL,
PRIMARY KEY (provedor),
unique key(provedorid)
);
create table tempos (
tempoid INT NOT NULL UNIQUE AUTO_INCREMENT,
mes INT NOT NULL,
ano INT NOT NULL,
PRIMARY KEY (tempoid),
UNIQUE KEY(mes,ano)
);
describe tempos;
drop table avaliadores;
drop table tempos;
drop table provedores;
select * from tempos;
select * from avaliadores;
select * from provedores;
select * from avaliacao_csp;
INSERT INTO avaliadores(avaliador) SELECT avaliador FROM avaliadores WHERE NOT EXISTS(SELECT avaliador FROM avaliadores WHERE avaliador=avaliador) LIMIT 1;
insert ignore into avaliadores(avaliador) values("Hugo");

insert into avaliacao_csp 
select avaliadorid FROM avaliadores WHERE NOT EXISTS(SELECT avaliador FROM avaliadores WHERE avaliador=avaliadorid) LIMIT 1 insert into avaliadores (avaliador) values ("Hugo")  ;
INSERT INTO csp (avaliadorid, provedorid, tempoid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24) VALUES ("Hugo", "Locaweb", "Abril", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1");
INSERT INTO avaliacao_csp (avaliadorid, provedorid,tempoid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24) VALUES (1, 2, 1, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23","24");
INSERT INTO avaliacao_csp (avaliador, provedor,mes,ano, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24) VALUES ("joaquim","Locaweb",01,2020, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23","24");
INSERT INTO avaliacao_csp (avaliadorid, provedorid,tempoid,data_avaliacao, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24) VALUES (1, 2, 1,'2021-05-11', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23","24");
INSERT INTO csp (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24) VALUES ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23","24");
insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor) values ("Hugo", "biller", "123",1) ;
insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor) values ("Administrador", "admin", "123",1) ;
insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor) values ("Joaquim", "joaquim", "123",0) ;
insert into provedores (provedor) values ("Locaweb");
insert into provedores (provedor) values ("AWS");


insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor,atividade) values ("Administrador", "admin", "123",1,1) ;
insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor,atividade) values ("Joaquim", "joaquim", "123",0,1) ;
insert into avaliadores (avaliador, avaliadorusr, avaliadorpw, gestor,atividade) values ("Joaquina", "joaquina", "123",0,0) ;
insert into provedores (provedor,atividade) values ("Locaweb",1);
insert into provedores (provedor,atividade) values ("AWS",1);
insert into tempos (mes,ano) values (01,2020);
insert into tempos (tempo) values ("maio");
insert into tempos (tempo) values ("abril");
insert into tempos (tempo) values ("qui abr 22 2021");
insert into tempos (tempo) values ("01/2021");


insert into avaliadores (avaliador) values ("Amandio");
insert into avaliadores (avaliador) values ("Ferrucio");
show engine innodb status;
select avaliador from avaliadores where avaliadorusr="vamp?";

update avaliadores set avaliador="maria", avaliadorusr="maria", avaliadorpw=123, atividade=1, gestor=0 where avaliadorid=3;
update avaliadores set avaliador=maria where avaliadorid=3;
select * from avaliadores;
select * from provedores;
select * from tempos;
select * from avaliacao_csp;
update avaliadores set avaliador = replace(replace(avaliador, ',', ''), '"', '');
update avaliadores set avaliador = replace(replace(avaliador, ',', ''), '\'', '') where avaliadorid>=1;
update avaliadores2 set avaliador2="joao" where avaliadorid2 IS NULL;
update avaliadores set avaliador="Hugo" where avaliadorid IS NULL;
update avaliadores set avaliador="Amandio" where avaliadorid=2;
update avaliadores set avaliador="Ferrucio" where avaliadorid=3;
update avaliadores set avaliador="Asa" where avaliadorid=4;



create table tempos (
tempoid INT NOT NULL AUTO_INCREMENT	,
tempo VARCHAR(20) NOT NULL,

PRIMARY KEY(tempoid)
);

drop table avaliadores;
drop table csp;
drop table provedores;
drop table provedores2;
drop table tempos;

create table avaliadores (
avaliadorid INT NOT NULL AUTO_INCREMENT,
parentavaliadorid int unsigned default null,
dummy int,
avaliador VARCHAR (50) NOT NULL ,
avaliadorcod INT NOT NULL ,
PRIMARY KEY (avaliadorid),
UNIQUE INDEX (parentavaliadorid, avaliador), 
UNIQUE INDEX(dummy,avaliador),
UNIQUE INDEX (parentavaliadorid, avaliadorcod), 
UNIQUE INDEX(dummy,avaliadorcod)

);

UPDATE csp set avaliador="{}" WHERE id = 6 .format(avaliador, provedor, mes, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24);
