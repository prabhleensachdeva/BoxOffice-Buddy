CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.7.43-log

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `login_id` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `email_id` varchar(25) DEFAULT NULL,
  `dateofshow` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `typeofseat` varchar(20) DEFAULT NULL,
  `theatrename` varchar(20) DEFAULT NULL,
  `no_of_tickets` varchar(20) DEFAULT NULL,
  `amount_per_ticket` varchar(20) DEFAULT NULL,
  `total` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `movie_name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('alice123','Alice','1647894758','alice@yahoo.com','02-06-2024','9:00pm-12:00am','diamond','Cineplex','6','25','150','Booked','La La Land'),('bob456','Bob','1234567898','bob@yahoo.com','09-12-2024','5:00pm to 7:00pm','gold','Landmark','4','15','60','Booked','Barbie'),('carol789','Carol','6475558978','carol@gmail.com','02-02-2024','5:00pm to 7:00pm','premium','Galaxy','10','20','200','Booked','The Proposal'),('dave321','Dave','6475589903','dave@yahoo.com','28-12-2024','1:00pm to 3:00pm','diamond','Wonders','2','25','50','Booked','Top Gun: Maverick'),('emma654','Emma','6478693884','emma@gmail.com','02-02-2024','9:00pm to 12:00am','diamond','Pixes','5','25','125','Booked','Oppenheimer'),('Sarah23','Sarah','6478956789','sarah13@yahoo.com','02-06-2024','1:00pm to 3:00pm','premium','Wonders','3','20','60','Booked','Top Gun: Maverick'),('alice123','Alice','1647894758','alice@yahoo.com','09-07-2024','9:00 PM to 12:00 AM','regular','Landmark','2','10','20','Booked','Barbie'),('lily12','Lily','6476782345','lily98@gmail.com','10-06-2024','5:00 PM to 7:00 PM','premium','Pixes','3','20','60','Booked','Me Before You'),('harry67','Harry','6547890765','harry@yahoo.com','08-07-2024','5:00 PM to 7:00 PM','premium','Pixes','5','20','100','Booked','Me Before You'),('alice123','Alice','6475689990','alice@yahoo.com','20-03-2024','9:00 PM to 12:00 AM','regular','Cineplex','4','10','40','Cancel','Spider-Man 4'),('leo11','Leo','6578921346','leo123@gmail.com','22-05-2024','5:00 PM to 7:00 PM','regular','Galaxy','3','10','30','Booked','Oppenheimer');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_name` varchar(25) DEFAULT NULL,
  `Rating` varchar(30) DEFAULT NULL,
  `cast` varchar(100) DEFAULT NULL,
  `producer` varchar(20) DEFAULT NULL,
  `theatre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('La La Land','4.75','Ryan Gosling, Emma Stone','Damien Chazelle','INOX'),('Barbie','3.99','Ryan Gosling, Margot Robbie','Greta Gerwig','Landmark'),('The Proposal','5','Ryan Reynolds, Sandra Bullock','David Hoberman','Cineplex'),('Top Gun: Maverick','4.5','Tom Cruise, Jennifer Connelly','Tom Cruise','Wonders'),('Me Before You','3.99','Emilia Clarke , Sam Claflin','Alison Owen','Pixes'),('Spider-Man 4','4.99','Tom Holland, Zendaya','Amy Pascal','Cineplex'),('Oppenheimer','4.1','Cillian Murphy, Emily Blunt','Christopher Nolan','Galaxy');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `login_id` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `email_id` varchar(25) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES ('alice123','alice_pass','Alice','6475689990','alice@yahoo.com','17','F','Toronto'),('bob456','bobpass','Bob','1234567898','bob@yahoo.com','21','M','Vancouver'),('carol789','carolpass','Carol','6475558978','carol@gmail.com','23','F','Calgary'),('dave321','davepass','Dave','6475589903','dave@yahoo.com','29','M','Ottawa'),('emma654','emmapass','Emma','6478693884','emma@gmail.com','34','F','Montreal'),('Sarah23','sarah_99','Sarah','6478956789','sarah13@yahoo.com','21','F','Guelph'),('lily12','lily_99','Lily','6476782345','lily98@gmail.com','19','F','Georgetown'),('harry67','harry12','Harry','6547890765','harry@yahoo.com','19','M','Toronto'),('leo11','leo_89','Leo','6578921346','leo123@gmail.com','23','M','Guelph');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-09  8:38:39
