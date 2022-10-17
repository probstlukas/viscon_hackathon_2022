-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Oct 16, 2022 at 10:03 AM
-- Server version: 10.9.3-MariaDB-1:10.9.3+maria~ubu2204
-- PHP Version: 8.0.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodfinder`
--

-- --------------------------------------------------------

--
-- Table structure for table `ehfht`
--

CREATE TABLE `ehfht` (
  `eventsId` int(11) NOT NULL,
  `tagsId` int(11) NOT NULL,
  `foodsId` int(11) NOT NULL,
  `portions` int(11) DEFAULT NULL,
  `interest` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ehfht`
--

INSERT INTO `ehfht` (`eventsId`, `tagsId`, `foodsId`, `portions`, `interest`) VALUES
(1, 2, 10, 3, 14),
(1, 5, 4, 16, 4),
(2, 4, 13, 7, 3),
(3, 6, 2, 7, 11),
(4, 3, 1, 14, 15),
(5, 5, 4, 7, 9),
(6, 3, 9, 17, 15),
(7, 4, 5, 10, 4),
(8, 4, 11, 19, 14),
(9, 1, 8, 2, 3),
(10, 2, 3, 18, 15),
(11, 3, 6, 7, 20),
(12, 3, 9, 12, 8),
(13, 3, 7, 19, 4),
(14, 4, 12, 5, 2),
(15, 5, 4, 8, 2),
(16, 4, 1, 18, 15),
(17, 3, 9, 13, 20),
(18, 3, 1, 14, 12),
(19, 6, 1, 3, 16),
(20, 5, 1, 5, 15),
(21, 7, 14, 12, 22),
(21, 8, 15, 6, 17);

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `user` int(11) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `creationDate` datetime DEFAULT NULL,
  `expirationDate` datetime DEFAULT NULL,
  `visibility` tinyint(1) DEFAULT NULL,
  `imageId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`id`, `name`, `user`, `location`, `creationDate`, `expirationDate`, `visibility`, `imageId`) VALUES
(1, 'Die ETH Zürich an der Olma 2022', 2, 'Olma-Messe, St. Gallen: Halle 6, Stand 09', '2022-10-16 11:24:00', '2022-10-16 18:24:00', 1, 1),
(2, 'Wellen - Tauch ein!', 1, 'Sonneggstrasse 5, 8006 Zürich', '2022-10-16 11:31:00', '2022-10-16 18:31:00', 1, 2),
(3, 'Linien aus Ostasien', 1, 'ETH Zürich Graphische Sammlung, Rämistrasse 101, 8092 Zürich', '2022-10-16 11:38:00', '2022-10-16 18:38:00', 1, 3),
(4, 'Schreibwerkstatt Deutsch A2-C1', 1, 'ETH Zürich - Campus Hönggerberg, Stefano-Franscini-Platz 5, 8093 Zürich', '2022-10-16 11:45:00', '2022-10-16 18:45:00', 1, 4),
(5, 'Coffee Break Deutsch & Architektur B1-C2', 1, 'ETH Zürich - Campus Hönggerberg, Stefano-Franscini-Platz 5, 8093 Zürich, HIL E2 (Baubibliothek)', '2022-10-16 11:53:00', '2022-10-16 18:53:00', 1, 5),
(6, 'Sprachtreff Englisch A1-C1', 2, 'UZH, Campus Zentrum, Rämistrasse 74, Zürich', '2022-10-16 12:00:00', '2022-10-16 19:00:00', 1, 6),
(7, 'Sprachtreff Schweizerdeutsch', 2, 'ETH Zürich - Campus Hönggerberg, Stefano-Franscini-Platz 5, 8093 Zürich, HIL E 2 (Baubibliothek)', '2022-10-16 12:07:00', '2022-10-16 19:07:00', 1, 7),
(8, 'High-voltage aqueous lithium-ion batteries', 2, 'Zürich Hönggerberg, HCI J 498', '2022-10-16 12:14:00', '2022-10-16 19:14:00', 1, 8),
(9, 'Massive MU-MIMO: Algorithms and VLSI Designs', 1, 'Zürich Zentrum, HG D 22', '2022-10-16 12:21:00', '2022-10-16 19:21:00', 1, 9),
(10, 'Proteome-wide selectivity of diverse electrophiles', 2, 'Zürich Hönggerberg, HCI J 7', '2022-10-16 12:29:00', '2022-10-16 19:29:00', 1, 10),
(11, 'Rossby waves in polar weather and climate', 3, 'Zürich Zentrum, CAB G 11', '2022-10-16 12:36:00', '2022-10-16 19:36:00', 1, 11),
(12, 'Workshop Spielevent', 3, 'ETH Zürich - Campus Zürich, Stefano-Franscini-Platz 5, 8093 Zürich', '2022-10-16 12:43:00', '2022-10-16 19:43:00', 1, 12),
(13, 'Sprachtreff Deutsch A1', 3, 'ETH Zürich - Campus Zürich, Stefano-Franscini-Platz 5, 8093 Zürich', '2022-10-16 12:50:00', '2022-10-16 19:50:00', 1, 13),
(14, 'Unified Perspectives on Nonlinear Model Reduction', 3, 'Zürich Zentrum, LEE E 101', '2022-10-16 12:57:00', '2022-10-16 19:57:00', 1, 14),
(15, 'Sprachtreff Französisch A1-C1', 3, 'UZH, Campus Zentrum, Rämistrasse 74, Zürich', '2022-10-16 13:05:00', '2022-10-16 20:05:00', 1, 15),
(16, 'Sprachtreff Russisch A1-C1', 4, 'UZH, Campus Zentrum, Rämistrasse 74, Zürich', '2022-10-16 13:12:00', '2022-10-16 20:12:00', 1, 16),
(17, 'Automated Design of Additive Manufactured Flow Components', 4, 'Zürich Zentrum, LEE E 126', '2022-10-16 13:19:00', '2022-10-16 20:19:00', 1, 17),
(18, 'VSETH Activity Fair: Freizeitsbeschäftigungen für Studierende', 4, 'ETH Zürich HG', '2022-10-16 13:26:00', '2022-10-16 20:26:00', 1, 18),
(19, 'Relation-Centered Approaches to Technology Ethics', 4, 'ETH Zürich - Campus Hönggerberg, Stefano-Franscini-Platz 5, 8093 Zürich, HIL E 2 (Baubibliothek)', '2022-10-16 13:33:00', '2022-10-16 20:33:00', 1, 19),
(20, 'ETHeart Joint Scientific Colloquium', 4, 'ETH Zürich - Campus Zürich, Stefano-Franscini-Platz 5, 8093 Zürich', '2022-10-16 13:41:00', '2022-10-16 20:41:00', 1, 20),
(21, 'VIS Con Hackathon', 2, 'ETH HG H, Zürich', '2022-10-16 11:23:31', '2022-10-16 12:57:00', 0, 21);

-- --------------------------------------------------------

--
-- Table structure for table `foods`
--

CREATE TABLE `foods` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `foods`
--

INSERT INTO `foods` (`id`, `name`) VALUES
(1, 'Buffet'),
(2, 'Chicken'),
(3, 'Dessert'),
(4, 'Fish'),
(5, 'Gnocci'),
(6, 'Groceries'),
(7, 'Lasagne'),
(8, 'Nuts'),
(9, 'Pasta'),
(10, 'Salad'),
(11, 'Sandwiches'),
(12, 'Saussage'),
(13, 'Toast'),
(14, 'Croissant'),
(15, 'Lasagne');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `suffix` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `suffix`) VALUES
(1, 'jpeg'),
(2, 'jpg'),
(3, 'jpeg'),
(4, 'jpg'),
(5, 'jpg'),
(6, 'jpeg'),
(7, 'jpg'),
(8, 'jpeg'),
(9, 'jpg'),
(10, 'jpg'),
(11, 'jpeg'),
(12, 'jpg'),
(13, 'jpeg'),
(14, 'jpeg'),
(15, 'jpg'),
(16, 'jpg'),
(17, 'jpg'),
(18, 'jpeg'),
(19, 'jpeg'),
(20, 'jpeg'),
(21, 'jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `name`) VALUES
(1, 'Vegan'),
(2, 'Vegetarian'),
(3, 'Beef'),
(4, 'Pork'),
(5, 'Fish'),
(6, 'Chicken'),
(7, 'Vegetarisch'),
(8, 'Beef');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `password` varchar(150) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `password`, `email`, `name`) VALUES
(1, 'sha256$mzRxywJV60ZZzhgT$4d69abb8c569aaa84db59e9579112256869015320a8e926e9671ff2d8efd2c4a', 'phil@phil.de', 'Phil'),
(2, 'sha256$mzRxywJV60ZZzhgT$4d69abb8c569aaa84db59e9579112256869015320a8e926e9671ff2d8efd2c4a', 'sisure@student.ethz.ch', 'Simon'),
(3, 'sha256$mzRxywJV60ZZzhgT$4d69abb8c569aaa84db59e9579112256869015320a8e926e9671ff2d8efd2c4a', 'herwig@herwig.de', 'Herwig'),
(4, 'sha256$mzRxywJV60ZZzhgT$4d69abb8c569aaa84db59e9579112256869015320a8e926e9671ff2d8efd2c4a', 'lukas@lukas.de', 'Lukas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ehfht`
--
ALTER TABLE `ehfht`
  ADD PRIMARY KEY (`eventsId`,`tagsId`,`foodsId`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `foods`
--
ALTER TABLE `foods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `foods`
--
ALTER TABLE `foods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
