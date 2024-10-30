CREATE DATABASE  IF NOT EXISTS `gestionproyectos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gestionproyectos`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: gestionproyectos
-- ------------------------------------------------------
-- Server version	8.0.39

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

DROP TABLE IF EXISTS departamento;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE departamento (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(100) NOT NULL,
  gerente_id int DEFAULT NULL,
  PRIMARY KEY (id),
  KEY gerente_id (gerente_id),
  CONSTRAINT departamento_ibfk_1 FOREIGN KEY (gerente_id) REFERENCES empleado (id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES departamento WRITE;
/*!40000 ALTER TABLE departamento DISABLE KEYS */;
INSERT INTO departamento VALUES (1,'Informática',4),(2,'Administración',NULL),(4,'Marketing',NULL);
/*!40000 ALTER TABLE departamento ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS empleado;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE empleado (
  id int NOT NULL AUTO_INCREMENT,
  rut varchar(12) NOT NULL,
  nombre varchar(100) NOT NULL,
  direccion varchar(255) DEFAULT NULL,
  telefono varchar(15) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  fecha_inicio date DEFAULT NULL,
  salario decimal(10,2) DEFAULT NULL,
  departamento_id int DEFAULT NULL,
  PRIMARY KEY (id),
  KEY departamento_id (departamento_id),
  CONSTRAINT empleado_ibfk_1 FOREIGN KEY (departamento_id) REFERENCES departamento (id)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES empleado WRITE;
/*!40000 ALTER TABLE empleado DISABLE KEYS */;
INSERT INTO empleado VALUES (2,'1-9','Rodrigo Ruiz','S/N','912345678','rodrigo.ruiz@example.cl','1971-07-28',3000000.00,1),(4,'3-3','Juan Perez','S/N','912345678','juan.perez@example.cl','2024-10-02',30000.00,1),(5,'21-1','Nicolas Bahamonde','S/N','912345678','nicolas.bahamonde@example.cl','2024-10-10',3000000.00,1);
/*!40000 ALTER TABLE empleado ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto`
--

DROP TABLE IF EXISTS proyecto;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE proyecto (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(50) DEFAULT NULL,
  descripcion varchar(255) DEFAULT NULL,
  fecha_inicio date DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto`
--

LOCK TABLES proyecto WRITE;
/*!40000 ALTER TABLE proyecto DISABLE KEYS */;
INSERT INTO proyecto VALUES (2,'2do proyecto','lorem3000','2024-10-20'),(3,'3er proyecto','lorem20','2024-10-16'),(4,'lol','','2024-10-26');
/*!40000 ALTER TABLE proyecto ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoxempleado`
--

DROP TABLE IF EXISTS proyectoxempleado;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE proyectoxempleado (
  id_proyecto int NOT NULL,
  id_empleado int NOT NULL,
  PRIMARY KEY (id_proyecto,id_empleado),
  KEY id_empleado (id_empleado),
  CONSTRAINT proyectoxempleado_ibfk_1 FOREIGN KEY (id_proyecto) REFERENCES proyecto (id),
  CONSTRAINT proyectoxempleado_ibfk_2 FOREIGN KEY (id_empleado) REFERENCES empleado (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoxempleado`
--

LOCK TABLES proyectoxempleado WRITE;
/*!40000 ALTER TABLE proyectoxempleado DISABLE KEYS */;
INSERT INTO proyectoxempleado VALUES (2,5),(3,5);
/*!40000 ALTER TABLE proyectoxempleado ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrotiempo`
--

DROP TABLE IF EXISTS registrotiempo;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE registrotiempo (
  id int NOT NULL AUTO_INCREMENT,
  fecha date NOT NULL,
  horas_trabajadas float NOT NULL,
  descripcion varchar(255) DEFAULT NULL,
  id_empleado int NOT NULL,
  id_proyecto int NOT NULL,
  PRIMARY KEY (id),
  KEY id_empleado (id_empleado),
  KEY id_proyecto (id_proyecto),
  CONSTRAINT registrotiempo_ibfk_1 FOREIGN KEY (id_empleado) REFERENCES empleado (id),
  CONSTRAINT registrotiempo_ibfk_2 FOREIGN KEY (id_proyecto) REFERENCES proyecto (id)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrotiempo`
--

LOCK TABLES registrotiempo WRITE;
/*!40000 ALTER TABLE registrotiempo DISABLE KEYS */;
INSERT INTO registrotiempo VALUES (1,'2024-10-12',4.5,'no hay',5,2),(2,'2024-10-16',10,'lol',5,3),(3,'2024-10-26',10,'',5,2);
/*!40000 ALTER TABLE registrotiempo ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-29 22:07:32