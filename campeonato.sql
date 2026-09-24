CREATE DATABASE IF NOT EXISTS `campeonato`;
USE `campeonato`;

CREATE TABLE `time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

CREATE TABLE `jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `data_fim_contrato` date DEFAULT NULL,
  `posicao` enum('Goleiro','Zagueiro','Lateral','Meia','Centro-avante','Atacante') DEFAULT NULL,
  `time_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_jogador_time_id` (`time_id`),
  CONSTRAINT `fk_jogador_time_id` FOREIGN KEY (`time_id`) REFERENCES `time` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;


INSERT INTO `time` VALUES (1,'Sociedade Esportiva Palmeiras','São Paulo'),(2,'Clube Atlético Mineiro','Belo Horizonte'),(3,'Cruzeiro Esporte Clube','Belo Horizonte'),(4,'Nacional Atlético Clube','Muriaé'),(5,'Esporte Clube Ribeiro Junqueira','Leopoldina'),(6,'Grêmio Foot-Ball Porto Alegrense','Porto Alegre'),(7,'Esporte Clube Vitória','Salvador'),(8,'Esporte Clube Bahia','Salvador'),(9,'Futbol CLub Barcelona','Barcelona'),(10,'Real Madrid Club de Fútbol','Madrid'),(11,'Liverpool Futeball Club','Liverpool'),(12,'Chelsea Football Club','Londres'),(13,'Operário Futebol Clube','Cataguases');
INSERT INTO `jogador` VALUES (1,'Fernando Büttenbender Prass',500000.00,'2017-12-05','Goleiro',1),(2,'Gabriel Jesus',1000000.00,'2016-12-31','Atacante',1),(4,'José das Couves',350.00,'2020-06-12','Atacante',4),(5,'Marcelo Grohe',180000.00,'2018-05-22','Goleiro',6);


