CREATE DATABASE IF NOT EXISTS gerenciamento_escolar
USE gerenciamento_escolar

CREATE TABLE IF NOT EXISTS `salas` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `turmas` VARCHAR(30) NOT NULL UNIQUE,
    `ativo` BOOLEAN,
    `data` DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS `alunos` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(150) NOT NULL,
    `nome_social` VARCHAR(150),
    `CPF` VARCHAR(12) NOT NULL UNIQUE,
    `data_nasc` DATE NOT NULL,
    `RA` VARCHAR(15) NOT NULL UNIQUE,
    `RM` VARCHAR(15) NOT NULL UNIQUE,
    `Observacao` TEXT,
    `status` BOOLEAN NOT NULL DEFAULT 1,
    `data_registro` DATE NOT NULL DEFAULT (CURRENT_DATE)
);
CREATE TABLE IF NOT EXISTS `responsaveis` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(150) NOT NULL,
    `CPF` VARCHAR(12) NOT NULL UNIQUE,
    `responsavel_legal` BOOLEAN NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `nome_user` VARCHAR(150) NOT NULL,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `senha` VARCHAR(255) NOT NULL,
    `tipo_user` ENUM('adm', 'secretaria', 'agente') NOT NULL,
    `ativo` BOOLEAN NOT NULL DEFAULT 1
);

 

CREATE TABLE IF NOT EXISTS `sala_alunos` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `id_aluno` INTEGER NOT NULL,
    `id_sala` INTEGER NOT NULL,
    FOREIGN KEY (`id_aluno`) REFERENCES `alunos`(`id`),
    FOREIGN KEY (`id_sala`) REFERENCES `salas`(`id`) 
);
CREATE TABLE IF NOT EXISTS `responsavel_aluno` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `aluno_id` INTEGER NOT NULL,
    `responsavel_id` INTEGER NOT NULL,
    FOREIGN KEY (`aluno_id`) REFERENCES `alunos`(`id`),
    FOREIGN KEY (`responsavel_id`) REFERENCES `responsaveis`(`id`)
);
CREATE TABLE IF NOT EXISTS `enderecos` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `cidade` VARCHAR(100) NOT NULL,
    `bairro` VARCHAR(100) NOT NULL,
    `rua` VARCHAR(100) NOT NULL,
    `complemento` VARCHAR(100),
    `responsavel_id` INTEGER NOT NULL,
    FOREIGN KEY (`responsavel_id`) REFERENCES `responsaveis`(`id`)
);
CREATE TABLE IF NOT EXISTS `telefones` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `telefone` VARCHAR(18) NOT NULL,
    `responsavel_id` INTEGER NOT NULL,
    FOREIGN KEY (`responsavel_id`) REFERENCES `responsaveis`(`id`)
);
CREATE TABLE IF NOT EXISTS `relatorios` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `data` DATE NOT NULL DEFAULT (CURRENT_DATE),
    `descricao` TEXT NOT NULL,
    `aluno_id` INTEGER NOT NULL,
    `responsavel_id` INTEGER NOT NULL,
    FOREIGN KEY (`aluno_id`) REFERENCES `alunos`(`id`),
    FOREIGN KEY (`responsavel_id`) REFERENCES `responsaveis`(`id`)
);