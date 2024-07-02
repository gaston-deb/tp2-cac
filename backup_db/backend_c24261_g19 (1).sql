-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: backend_c24261_g19
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Juan Pérez','juan.perez@gmail.com','612345678',1),(2,'María García','maria.garcia@hotmail.com','623456789',1),(3,'Carlos López','carlos.lopez@gmail.com','634567890',1),(4,'Ana Martínez','ana.martinez@hotmail.com','645678901',1),(5,'Pedro Sánchez','pedro.sanchez@yahoo.com.ar','656789012',1),(6,'Laura Rodríguez','laura.rodriguez@gmail.com','667890123',1),(7,'Miguel Fernández','miguel.fernandez@hotmail.com','678901234',0),(8,'Carmen Gómez','carmen.gomez@hotmail.com','689012345',1),(9,'David Torres','david.torres@yahoo.com.ar','690123456',1),(10,'Isabel Ruiz','isabel.ruiz@yahoo.com.ar','601234567',0),(11,'Javier Hernández','javier.hernandez@gmail.com','612345679',1),(12,'Sofía Jiménez','sofia.jimenez@gmail.com','623456780',1),(13,'Antonio Díaz','antonio.diaz@yahoo.com.ar','634567891',1),(14,'Elena Moreno','elena.moreno@hotmail.com','645678902',0),(15,'Francisco Álvarez','francisco.alvarez@yahoo.com.ar','656789013',1),(16,'Lucía Muñoz','lucia.munoz@gmail.com','667890124',1),(17,'Raúl Romero','raul.romero@yahoo.com.ar','678901235',1),(18,'Beatriz Alonso','beatriz.alonso@hotmail.com','689012346',1),(19,'Alberto Gutiérrez','alberto.gutierrez@gmail.com','690123457',0),(20,'Cristina Navarro','cristina.navarro@hotmail.com','601234568',1),(21,'Andrés Vázquez','andres.vazquez@gmail.com','612345680',1),(22,'Marta Ramos','marta.ramos@yahoo.com.ar','623456781',1),(23,'Roberto Castro','roberto.castro@gmail.com','634567892',0),(24,'Patricia Ortega','patricia.ortega@hotmail.com','645678903',1),(25,'Alejandro Delgado','alejandro.delgado@yahoo.com.ar','656789014',1),(26,'Natalia Serrano','natalia.serrano@gmail.com','667890125',1),(27,'Fernando Ortiz','fernando.ortiz@yahoo.com.ar','678901236',1),(28,'Rosa Morales','rosa.morales@gmail.com','689012347',0),(29,'Gabriel Suárez','gabriel.suarez@hotmail.com','690123458',1),(30,'Victoria Medina','victoria.medina@gmail.com','601234569',1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `tipo` tinyint(1) NOT NULL DEFAULT 0,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `detalle` varchar(200) NOT NULL,
  `precio` double(20,2) NOT NULL,
  `imagen` varchar(150) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,1,'Samsung','Galaxy S21','Smartphone 5G, 128GB',799.99,'samsung_s21.jpg',1),(2,1,'Apple','iPhone 13','iOS 15, 256GB',999.99,'iphone_13.jpg',1),(3,2,'Sony','WH-1000XM4','Auriculares inalámbricos con cancelación de ruido',349.99,'sony_wh1000xm4.jpg',1),(4,1,'Xiaomi','Redmi Note 10 Pro','108MP cámara, 128GB',299.99,'xiaomi_redmi_note10pro.jpg',3),(5,2,'Anker','PowerCore 10000','Batería externa 10000mAh',29.99,'anker_powercore.jpg',1),(6,1,'Google','Pixel 6','Android 12, 128GB',699.99,'google_pixel6.jpg',1),(7,2,'JBL','Flip 5','Altavoz Bluetooth portátil',119.99,'jbl_flip5.jpg',0),(8,1,'OnePlus','9 Pro','Snapdragon 888, 256GB',899.99,'oneplus_9pro.jpg',1),(9,2,'Belkin','BoostCharge','Cargador inalámbrico 10W',39.99,'belkin_boostcharge.jpg',1),(10,1,'Motorola','Moto G Power','Batería 5000mAh, 64GB',249.99,'motorola_gpower.jpg',2),(11,2,'Jabra','Elite 75t','Auriculares True Wireless',149.99,'jabra_elite75t.jpg',1),(12,1,'Huawei','P40 Pro','Cámara Leica, 256GB',899.99,'huawei_p40pro.jpg',3),(13,2,'Spigen','Tough Armor','Funda protectora para iPhone 13',19.99,'spigen_tougharmor.jpg',1),(14,1,'Sony','Xperia 1 III','Pantalla 4K, 256GB',1199.99,'sony_xperia1iii.jpg',1),(15,2,'Samsung','Galaxy Watch 4','Smartwatch, NFC, GPS',249.99,'samsung_galaxywatch4.jpg',1),(16,1,'LG','Velvet','5G, 128GB',599.99,'lg_velvet.jpg',0),(17,2,'Bose','QuietComfort Earbuds','Auriculares con cancelación de ruido',279.99,'bose_quietcomfort.jpg',1),(18,1,'Oppo','Find X3 Pro','Cámara microscópica, 256GB',1099.99,'oppo_findx3pro.jpg',1),(19,2,'Anker','Nano II','Cargador GaN 65W',49.99,'anker_nano2.jpg',3),(20,1,'Nokia','8.3','5G, 128GB',499.99,'nokia_8.3.jpg',1),(21,2,'Apple','AirPods Pro','Auriculares con cancelación activa de ruido',249.99,'airpods_pro.jpg',1),(22,1,'Asus','ROG Phone 5','Gaming phone, 256GB',999.99,'asus_rogphone5.jpg',1),(23,2,'Fitbit','Versa 3','Smartwatch con GPS',229.99,'fitbit_versa3.jpg',0),(24,1,'Realme','GT','Snapdragon 888, 128GB',599.99,'realme_gt.jpg',1),(25,2,'Logitech','K480','Teclado Bluetooth multidispositivo',49.99,'logitech_k480.jpg',1),(26,1,'Vivo','X60 Pro','Gimbal camera, 256GB',749.99,'vivo_x60pro.jpg',2),(27,2,'Razer','Kishi','Controlador de juegos para smartphone',89.99,'razer_kishi.jpg',1),(28,1,'ZTE','Axon 30 Ultra','Cámara triple 64MP, 256GB',749.99,'zte_axon30ultra.jpg',1),(29,2,'Mophie','Juice Pack','Funda con batería para iPhone',99.99,'mophie_juicepack.jpg',3),(30,1,'TCL','20 Pro 5G','AMOLED curvo, 256GB',549.99,'tcl_20pro5g.jpg',1),(31,2,'Garmin','Venu 2','Smartwatch con GPS y monitor de salud',399.99,'garmin_venu2.jpg',1),(32,1,'BlackBerry','Key2','Teclado físico, 128GB',649.99,'blackberry_key2.jpg',0),(33,2,'Sennheiser','Momentum True Wireless 2','Auriculares premium',299.99,'sennheiser_momentum.jpg',1),(34,1,'CAT','S62 Pro','Rugged phone, cámara térmica',649.99,'cat_s62pro.jpg',1),(35,2,'Tile','Pro','Localizador Bluetooth',34.99,'tile_pro.jpg',1),(36,1,'Sharp','Aquos R6','Sensor 1 pulgada, 128GB',999.99,'sharp_aquosr6.jpg',2),(37,2,'Nomad','Base Station Pro','Cargador inalámbrico multidispositivo',199.99,'nomad_basestation.jpg',1),(38,1,'Fairphone','4','Smartphone ético y sostenible, 256GB',579.99,'fairphone_4.jpg',1),(39,2,'DJI','OM 5','Estabilizador para smartphone',159.99,'dji_om5.jpg',3),(40,1,'Nothing','Phone 1','Diseño transparente, 256GB',499.99,'nothing_phone1.jpg',1),(41,2,'PopSockets','PopGrip','Agarre para smartphone',9.99,'popsockets_popgrip.jpg',1),(42,1,'Microsoft','Surface Duo 2','Doble pantalla, 256GB',1499.99,'microsoft_surfaceduo2.jpg',1),(43,2,'Twelve South','HiRise','Soporte de carga para iPhone',59.99,'twelveouth_hirise.jpg',0),(44,1,'Poco','F3','Snapdragon 870, 256GB',399.99,'poco_f3.jpg',1),(45,2,'Moment','Lente Anamórfico','Lente para smartphone',149.99,'moment_anamorphic.jpg',1),(46,1,'Doogee','S96 Pro','Rugged phone, visión nocturna',389.99,'doogee_s96pro.jpg',2),(47,2,'Zhiyun','Smooth 5','Estabilizador de 3 ejes para smartphone',169.99,'zhiyun_smooth5.jpg',1),(48,1,'Ulefone','Armor 11T 5G','Rugged phone, cámara térmica',599.99,'ulefone_armor11t.jpg',1),(49,2,'Incipio','Organicore','Funda biodegradable para smartphone',39.99,'incipio_organicore.jpg',3),(50,1,'Unihertz','Titan Pocket','Mini smartphone con teclado QWERTY',299.99,'unihertz_titanpocket.jpg',1);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-01 23:15:56
