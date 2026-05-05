-- relacion 1:1
-- un usuario se relaciona solo con un dni y un dni se relaciona con un usuario
CREATE TABLE dni (
    dni_id INT AUTO_INCREMENT,
    dni_number INT NOT NULL,
    user_id INT,
    PRIMARY KEY (dni_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- relacion 1:N (uno a muchos)
-- Relación que indica que un registro en la tabla A puede tener varios registros relacionados en la
-- tabla B, pero un registro en la tabla B se relaciona con un solo registro en la tabla A.

CREATE TABLE companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);

alter table users
add company_id int;

-- convertir a foreign key
alter table users
add constraint fk_companies
foreign key (company_id) references companies (company_id);
    