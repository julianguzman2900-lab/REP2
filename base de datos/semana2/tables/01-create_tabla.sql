CREATE TABLE persons(
    id,
    name,
    age,
    email,
    fecha_nacimiento
)


CREATE TABLE persons(
    id int,
    name varchar(100),
    email varchar(50)
    fecha_nacimiento date
)


CREATE TABLE persons2(
    id int NOT NULL,
    name varchar(100)NOT NULL,
    age int
    email varchar(50)
    fecha_nacimiento date
)


CREATE TABLE persons3(
    id int NOT NULL,
    name varchar(100)NOT NULL,
    email varchar(50)
    age int,
    fecha_nacimiento date
    UNIQUE (id)
)


CREATE TABLE persons4(
    id int NOT NULL,
    name varchar(100)NOT NULL,
    email varchar(50)
    age int,
    fecha_nacimiento date
    UNIQUE (id),
    PRIMARY KEY (id)
)

CREATE TABLE persons5(
    id int NOT NULL,
    name varchar(100)NOT NULL,
    email varchar(50)
    age int,
    fecha_nacimiento date
    UNIQUE (id),
    PRIMARY KEY (id),
    CHECK (age>=18)
)

CREATE TABLE persons6(
    id int NOT NULL,
    name varchar(100)NOT NULL,
    email varchar(50) DEFAULT 'invitado@gmail.com'
    age int,
    fecha_nacimiento date
    UNIQUE (id),
    PRIMARY KEY (id),
    CHECK (age>=18)
)

CREATE TABLE persons7(
    id int NOT NULL,
    name varchar(100)NOT NULL,auto_increment
    email varchar(50) DEFAULT 'invitado@gmail.com'
    age int,
    fecha_nacimiento date
    UNIQUE (id),
    PRIMARY KEY (id),
    CHECK (age>=18)
)
insert into persons7( name,email,age,fecha_nacimiento) VALUES ('Miguel'30, 'miguel@gmail.com,'1996-01-01')
insert into persons7 (name) values