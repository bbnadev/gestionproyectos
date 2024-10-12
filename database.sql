CREATE DATABASE  IF NOT EXISTS `gestionproyectos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gestionproyectos`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gestionproyectos
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `gerente_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gerente_id` (`gerente_id`),
  CONSTRAINT `departamento_ibfk_1` FOREIGN KEY (`gerente_id`) REFERENCES `empleado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Informatica',NULL),(2,'Administración',NULL);
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `departamento_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departamento_id` (`departamento_id`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (2,'1-9','Rodrigo Ruiz','san felipe 176','56962218','rodrigo.ruiz05@inacapmail.cl','1971-07-28',3000000.00,1),(3,'2-7','sdf','sdf','33333','sdfds','2000-02-21',300000.00,2);
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-25 14:25:56

CREATE TABLE IF NOT EXISTS Proyecto(
	id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  descripcion VARCHAR(255),
  fecha_inicio DATE
);

INSERT INTO Proyecto VALUES (1,'Proyecto 1','Descripcion 1','2023-09-25'),(2,'Proyecto 2','Descripcion 2','2024-09-25');

CREATE TABLE IF NOT EXISTS ProyectoXEmpleado(
  id_proyecto INT NOT NULL,
  id_empleado INT NOT NULL,
  FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id)
);

INSERT INTO ProyectoXEmpleado VALUES (1,2),(2,3);

CREATE TABLE IF NOT EXISTS RegistroTiempo (
	id INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATE NOT NULL,
  horas_trabajadas FLOAT NOT NULL,
  descripcion VARCHAR(255),
  id_empleado INT NOT NULL,
  id_proyecto INT NOT NULL,
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id),
  FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id)
);

INSERT INTO RegistroTiempo VALUES (1,'2024-09-25',8,'Descripcion 1',2,1);