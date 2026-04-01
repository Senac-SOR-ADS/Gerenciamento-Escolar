CREATE DATABASE IF NOT EXISTS gerenciamento_escolar;
USE gerenciamento_escolar;

CREATE TABLE IF NOT EXISTS `salas` (
  `id` int(11) NOT NULL,
  `turmas` varchar(30) NOT NULL,
  `ativo` tinyint(1) DEFAULT 1,
  `data` date NOT NULL DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `alunos` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `nome_social` varchar(150) DEFAULT NULL,
  `CPF` varchar(12) NOT NULL,
  `data_nasc` date NOT NULL,
  `RA` varchar(15) NOT NULL,
  `RM` varchar(15) NOT NULL,
  `Observacao` text DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `data_registro` date NOT NULL DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `responsaveis` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `CPF` varchar(12) NOT NULL,
  `responsavel_legal` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE IF NOT EXISTS `usuarios` (
  `user_id` int(11) NOT NULL,
  `nome_user` varchar(150) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo_user` enum('adm','secretaria','agente') NOT NULL,
  `ativo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

 

CREATE TABLE IF NOT EXISTS `sala_alunos` (
  `id` int(11) NOT NULL,
  `id_aluno` int(11) NOT NULL,
  `id_sala` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `responsavel_aluno` (
  `id` int(11) NOT NULL,
  `aluno_id` int(11) NOT NULL,
  `responsavel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `enderecos` (
  `id` int(11) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `bairro` varchar(100) NOT NULL,
  `rua` varchar(100) NOT NULL,
  `numero` varchar(5) DEFAULT NULL,
  `complemento` varchar(100) DEFAULT NULL,
  `CEP` varchar(9) DEFAULT NULL,
  `responsavel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `telefones` (
  `id` int(11) NOT NULL,
  `telefone` varchar(18) NOT NULL,
  `responsavel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `relatorios` (
  `id` int(11) NOT NULL,
  `data` date NOT NULL DEFAULT curdate(),
  `descricao` text NOT NULL,
  `aluno_id` int(11) NOT NULL,
  `responsavel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;