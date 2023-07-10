-- File: ExportSchool.sql

-- Dumping database structure for school
CREATE DATABASE IF NOT EXISTS `school` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `school`;

-- Dumping structure for table school.users
CREATE TABLE IF NOT EXISTS `users` (
  `personID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `userpassword` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`personID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table school.users: ~4 rows (approximately)
REPLACE INTO `users` (`personID`, `username`, `userpassword`) VALUES
	(1, 'Supermanusia', '12345'),
	(3, 'shirochan', '12345'),
	(4, 'kuro', '54321');