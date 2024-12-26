-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for tugas3prakpmp
CREATE DATABASE IF NOT EXISTS `tugas3prakpmp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tugas3prakpmp`;

-- Dumping structure for table tugas3prakpmp.cat
CREATE TABLE IF NOT EXISTS `cat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `desc` varchar(150) DEFAULT NULL,
  `image_url` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table tugas3prakpmp.cat: ~6 rows (approximately)
REPLACE INTO `cat` (`id`, `name`, `desc`, `image_url`) VALUES
	(7, 'British Shorthair', 'Kucing bulu pendek Britania.', 'british_shorthair.avif'),
	(8, 'Himalaya', 'Memiliki sifat yang tenang dan penyayang.', 'himalaya.webp'),
	(9, 'Sphynx', 'Tidak memiliki bulu atau hanya memiliki bulu halus yang sulit dilihat.', 'sphynx.webp'),
	(10, 'Bengal', 'Kucing dengan pola bulu eksotis.', 'bengal.webp'),
	(11, 'Maine Coon', 'Kucing besar yang ramah dan penyayang.', 'mainecoon.webp'),
	(12, 'Persia', 'Kucing dengan bulu panjang dan wajah imut.', 'persia.webp');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
