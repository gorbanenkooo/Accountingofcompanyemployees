-- 1. Создание таблиц (цепочка 1:M по ТЗ)
CREATE TABLE predm (
    id_pred SERIAL PRIMARY KEY,
    nazvanie VARCHAR(50) NOT NULL,
    chasy TIME WITHOUT TIME ZONE
);

CREATE TABLE stud (
    id SERIAL PRIMARY KEY,
    familiya VARCHAR(20) NOT NULL,
    imya VARCHAR(20) NOT NULL,
    otchestvo VARCHAR(20),
    data_rozhdeniya DATE,
    id_pred INT NOT NULL REFERENCES predm(id_pred) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ocenki (
    id_ocenki SERIAL PRIMARY KEY,
    id_stud INT NOT NULL REFERENCES stud(id) ON DELETE CASCADE ON UPDATE CASCADE,
    ocenka INT NOT NULL,
    data DATE NOT NULL
);

-- 2. Заполнение данными
INSERT INTO predm (nazvanie, chasy) VALUES
('Базы данных', '02:00:00'),
('Программирование Python', '03:00:00'),
('Дискретная математика', '01:30:00');

INSERT INTO stud (familiya, imya, otchestvo, data_rozhdeniya, id_pred) VALUES
('Горбаненко', 'Кирилл', 'Дмитриевич', '2004-05-15', 1),
('Иванов', 'Алексей', 'Сергеевич', '2004-08-20', 1),
('Петров', 'Михаил', 'Игоревич', '2003-11-10', 2);

INSERT INTO ocenki (id_stud, ocenka, data) VALUES
(1, 5, '2026-09-20'),
(1, 5, '2026-09-25'),
(2, 4, '2026-09-21'),
(3, 5, '2026-09-22');
