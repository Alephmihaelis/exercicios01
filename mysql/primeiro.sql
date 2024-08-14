
-- Meu primeiro arquivo DUMP para mySQL

-- Apaga o banco de dados caso ele exista
-- ------------------ ATENÇÃO! ------------------
-- Remova este comando após a publicação da versão de produção
-- Versão de produção = a versão que está na Internet

DROP DATABASE IF EXISTS primeiro;

-- ------------------ ATENÇÃO! ------------------
-- Cria o banco de dados
-- Sempre configurar o banco de dados para UTF-8
-- Define a tabela de caracteres UTF-8 (utf8mb4)
-- Define as buscas para UFT-8 case-insensitive

CREATE DATABASE primeiro
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;


-- Definir o banco de dados com o qual vamos trabalhar

USE primeiro;

-- Modela a tabela `user`

CREATE TABLE employee (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(127) NOT NULL,
    employee_email VARCHAR(255) NOT NULL,
    employee_password VARCHAR(63) NOT NULL,
    employee_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    employee_status ENUM('ON', 'OFF', 'DEL') DEFAULT 'ON'
);

-- Inserindo alguns `employee` fake

INSERT INTO employee (
    employee_name,
    employee_email,
    employee_password
) VALUES (
    'Joca da Silva',
    'joca@silva.com',
    SHA1('senha123')
), (
    'Setembrino Trocatapas',
    'set@brino.com',
    SHA1('senha123')
), (
    'Marineuza Siriliano',
    'mari@neuza.com',
    SHA1('senha123')
);
-- Modela a tabela `contact`

CREATE TABLE contact (
    cont_id INT PRIMARY KEY AUTO_INCREMENT,
    cont_name VARCHAR(127) NOT NULL,
    cont_email VARCHAR(255) NOT NULL,
    cont_subject VARCHAR(63),
    cont_message TEXT NOT NULL,
    cont_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cont_status ENUM('AGUARDANDO RESPOSTA', 'RESPONDIDO') DEFAULT 'AGUARDANDO RESPOSTA'
);

-- Insere alguns `contact` fake para testes


INSERT INTO contact (
    cont_name,
    cont_email,
    cont_subject,
    cont_message
) VALUES (
    'José da Silva',
    'jose@dasilva.com',
    'PRIMEIRO TESTE',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
), (
    'Blitzcrank',
    'blitao@crank.com',
    'PREPARADO E PRONTO PARA SERVIR',
    'tsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsctsc'
);

-- Modela a tabela `article`

CREATE TABLE article (
    art_id INT PRIMARY KEY AUTO_INCREMENT,
    art_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    art_title VARCHAR(127),
    art_intro VARCHAR(255),
    art_content TEXT,
    art_author INT, -- Chave estrangeira para `employee`
    art_status ENUM('On', 'Off', 'Apagado') DEFAULT 'On',
-- Especifica a chave estrangeira
    FOREIGN KEY (art_author) REFERENCES employee(employee_id)
);

-- Insere um `article` fake para testes

INSERT INTO article (
    art_title,
    art_intro,
    art_content,
    art_author,
    ) VALUES (
        'COMO ESPIRRAR NA ARGENTINA',
        'bizu',
        'lorem ipsum blalblalnalananlanlnalnalanlnalanllaaadgags\\gop snosdgojsdfgjopasfjoasjdfoasopiofiafoiafoppoi IIIIIIIIIIIiiiiiiiBUGBUBGUBGUBU',
        '1'
);


