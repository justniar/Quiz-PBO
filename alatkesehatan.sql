-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2022 at 04:26 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kesehatan`
--

-- --------------------------------------------------------

--
-- Table structure for table `alatkesehatan`
--

CREATE TABLE `alatkesehatan` (
  `idalkes` int(11) NOT NULL,
  `kode_alkes` varchar(10) NOT NULL,
  `nama_alkes` varchar(20) NOT NULL,
  `harga` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alatkesehatan`
--

INSERT INTO `alatkesehatan` (`idalkes`, `kode_alkes`, `nama_alkes`, `harga`) VALUES
(3, '208', 'Tabung Oksigen', 2000000),
(4, '300', 'Tensi Meter', 500000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alatkesehatan`
--
ALTER TABLE `alatkesehatan`
  ADD PRIMARY KEY (`idalkes`),
  ADD UNIQUE KEY `kode_alkes` (`kode_alkes`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alatkesehatan`
--
ALTER TABLE `alatkesehatan`
  MODIFY `idalkes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
