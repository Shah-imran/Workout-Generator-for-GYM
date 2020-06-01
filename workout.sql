-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2020 at 11:27 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `workout`
--

-- --------------------------------------------------------

--
-- Table structure for table `exercise`
--

CREATE TABLE `exercise` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `info` text DEFAULT NULL,
  `muscle_group_id` int(11) DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `images` varchar(255) DEFAULT NULL,
  `visible_for_user` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `exercise`
--

INSERT INTO `exercise` (`id`, `name`, `info`, `muscle_group_id`, `calories`, `time`, `images`, `visible_for_user`) VALUES
(11, 'rtertqq', ' df gsdf sdfg sd', 1, 2, 5, 'E:/Upwork/2020/workout/images/1.jpg', 1),
(13, 'rttre', ' dfg sfsdf sdf sd', 4, 2, 2, 'E:/Upwork/2020/workout/images/2.jpg', 1),
(25, 'asda', 'dsafds ', 1, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(26, 'asda', 'dsafds ', 2, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(27, 'asda', 'dsafds ', 3, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(28, 'asda', 'dsafds ', 14, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(29, 'asda', 'dsafds ', 12, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(30, 'asda', 'dsafds ', 5, 2, 2, 'E:/Upwork/2020/workout/images/3.jpg', 1),
(61, 'dfasd fad fd', ' g df gsdfg sdfg sdfgsdfg', 1, 2, 2, '', 1),
(62, 'rtertqq', ' df gsdf sdfg sd', 2, 2, 5, 'E:/Upwork/2020/workout/images/1.jpg', 1),
(78, 'asdf sdf', ' sdf sdf sdfsd ', 1, 2, 2, '', 1),
(79, 'asdf sdf', ' sdf sdf sdfsd ', 4, 2, 2, '', 1),
(80, 'fgdfghfdh', 'dfgdfs', 1, 2, 2, '', 1),
(81, 'dfgdsfg', 'jh	jk', 14, 2, 2, '', 1),
(82, 'ghfgh', 'fghfdgh', 12, 2, 2, '', 1),
(83, 'fghfdgh', 'fghdfghfdg', 3, 2, 2, '', 1),
(84, 'gfhdfghf', 'fghfdgh', 4, 2, 2, '', 1),
(85, 'fghfgh', 'fghfgdhdfg', 23, 2, 2, '', 1),
(86, 'fghfghdfg', 'fghfdghdfgh', 5, 2, 2, '', 1),
(87, 'fghfg', 'fghfdghdfgh fg fg', 4, 2, 2, '', 1),
(88, 'fgh fgdh', ' fghf gdhfg ', 5, 2, 2, '', 1),
(89, 'fgh fdgh dfghdfg hdfgh ', 'fg hfgdh dfgh dfgh', 12, 2, 2, '', 1),
(90, 'fgh fgh fg', 'hf ghfgd hfgdh fgdh', 3, 2, 2, '', 1),
(91, 'fgh fgh', ' fgh fgh fghfg fgh ', 23, 2, 2, '', 1),
(92, 'fg hfgh ', 'g fhfgh fgh', 14, 2, 2, '', 1),
(93, 'fgh fgh fg', ' fgdhfghgfdh dgf', 14, 2, 2, '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `muscle_groups`
--

CREATE TABLE `muscle_groups` (
  `id` int(11) NOT NULL,
  `muscle_name` varchar(255) NOT NULL,
  `visible_for_user` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `muscle_groups`
--

INSERT INTO `muscle_groups` (`id`, `muscle_name`, `visible_for_user`) VALUES
(1, 'Abs', 1),
(2, 'Biceps', 1),
(3, 'Calves', 1),
(4, 'Chest', 1),
(5, 'Hamstrings', 1),
(12, 'fdsfdg', 1),
(14, 'ererr', 1),
(23, 'sdfsa vd', 1);

-- --------------------------------------------------------

--
-- Table structure for table `workouts`
--

CREATE TABLE `workouts` (
  `id` int(11) NOT NULL,
  `w_name` varchar(255) NOT NULL,
  `info` text DEFAULT NULL,
  `exercise_id` int(11) DEFAULT NULL,
  `set_count` int(11) DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `time` int(11) DEFAULT 0,
  `reps` int(11) DEFAULT 0,
  `rounds` int(11) DEFAULT 1,
  `visible_for_user` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `workouts`
--

INSERT INTO `workouts` (`id`, `w_name`, `info`, `exercise_id`, `set_count`, `type`, `time`, `reps`, `rounds`, `visible_for_user`) VALUES
(186, 'test', 'dsfg dfg dsgfh fdghfd hfg', 13, 1, 'EMOM', 0, 0, 3, 1),
(187, 'test 1', 'dsf sd asfg', 13, 1, 'Reps', 0, 15, 3, 1),
(188, 'test 1', 'dsf sd asfg', 11, 1, 'Reps', 0, 15, 3, 1),
(189, 'test 1', 'dsf sd asfg', 11, 1, 'Reps', 0, 15, 3, 1),
(190, 'test 1', 'dsf sd asfg', 13, 1, 'Reps', 0, 15, 3, 1),
(191, 'test 1', 'dsf sd asfg', 61, 2, 'Reps', 0, 15, 3, 1),
(192, 'test 1', 'dsf sd asfg', 61, 2, 'Reps', 0, 15, 3, 1),
(193, 'test 1', 'dsf sd asfg', 11, 2, 'Reps', 0, 15, 3, 1),
(194, 'test 1', 'dsf sd asfg', 11, 2, 'EMOM', 0, 0, 3, 1),
(195, 'test 1', 'dsf sd asfg', 11, 3, 'EMOM', 0, 0, 3, 1),
(196, 'test 1', 'dsf sd asfg', 11, 3, 'Time', 15, 0, 3, 1),
(197, 'test 1', 'dsf sd asfg', 61, 3, 'Time', 15, 0, 3, 1),
(198, 'test 1', 'dsf sd asfg', 25, 3, 'Reps', 0, 15, 3, 1),
(199, 'test 1', 'dsf sd asfg', 61, 3, 'EMOM', 0, 0, 3, 1),
(200, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 13, 1, 'Reps', 0, 15, 3, 1),
(201, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 1, 'Reps', 0, 15, 3, 1),
(202, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 1, 'Reps', 0, 15, 3, 1),
(203, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 13, 1, 'Reps', 0, 15, 3, 1),
(204, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 61, 2, 'Time', 15, 0, 3, 1),
(205, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 61, 2, 'Time', 15, 0, 3, 1),
(206, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 2, 'Time', 15, 0, 3, 1),
(207, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 2, 'Time', 0, 0, 3, 1),
(208, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 3, 'EMOM', 12, 12, 3, 1),
(209, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 3, 'EMOM', 25, 25, 3, 1),
(210, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 61, 3, 'EMOM', 5, 25, 3, 1),
(211, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 25, 3, 'EMOM', 5, 25, 3, 1),
(212, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 61, 3, 'EMOM', 25, 25, 3, 1),
(213, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 13, 4, 'Reps', 0, 15, 3, 1),
(214, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 13, 4, 'Reps', 0, 15, 3, 1),
(215, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 11, 4, 'Time', 15, 0, 3, 1),
(216, 'test 2', 'df gsdfg sdfgs dfsdf sdf dfgsdfg', 61, 4, 'Time', 15, 0, 3, 1),
(217, 'test big', 'dfsf asdf sadf asdf', 13, 1, 'Reps', 0, 15, 3, 1),
(218, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(219, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(220, 'test big', 'dfsf asdf sadf asdf', 13, 1, 'Reps', 0, 15, 3, 1),
(221, 'test big', 'dfsf asdf sadf asdf', 83, 1, 'Reps', 0, 15, 3, 1),
(222, 'test big', 'dfsf asdf sadf asdf', 83, 1, 'Reps', 0, 15, 3, 1),
(223, 'test big', 'dfsf asdf sadf asdf', 83, 1, 'Reps', 0, 15, 3, 1),
(224, 'test big', 'dfsf asdf sadf asdf', 78, 1, 'Reps', 0, 15, 3, 1),
(225, 'test big', 'dfsf asdf sadf asdf', 78, 1, 'Reps', 0, 15, 3, 1),
(226, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(227, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(228, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(229, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(230, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(231, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(232, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(233, 'test big', 'dfsf asdf sadf asdf', 85, 1, 'Reps', 0, 15, 3, 1),
(234, 'test big', 'dfsf asdf sadf asdf', 81, 1, 'Reps', 0, 15, 3, 1),
(235, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(236, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(237, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(238, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(239, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(240, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(241, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(242, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(243, 'test big', 'dfsf asdf sadf asdf', 83, 1, 'Reps', 0, 15, 3, 1),
(244, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(245, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Reps', 0, 15, 3, 1),
(246, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(247, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(248, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(249, 'test big', 'dfsf asdf sadf asdf', 92, 1, 'Reps', 0, 15, 3, 1),
(250, 'test big', 'dfsf asdf sadf asdf', 81, 1, 'Reps', 0, 15, 3, 1),
(251, 'test big', 'dfsf asdf sadf asdf', 85, 1, 'Reps', 0, 15, 3, 1),
(252, 'test big', 'dfsf asdf sadf asdf', 13, 1, 'Reps', 0, 15, 3, 1),
(253, 'test big', 'dfsf asdf sadf asdf', 11, 1, 'Time', 15, 0, 3, 1),
(254, 'test big', 'dfsf asdf sadf asdf', 91, 1, 'Reps', 0, 15, 3, 1),
(255, 'test big', 'dfsf asdf sadf asdf', 88, 1, 'Reps', 0, 15, 3, 1),
(256, 'test big', 'dfsf asdf sadf asdf', 88, 1, 'Time', 15, 0, 3, 1),
(257, 'test big', 'dfsf asdf sadf asdf', 91, 1, 'Reps', 0, 15, 3, 1),
(258, 'test big', 'dfsf asdf sadf asdf', 81, 1, 'Reps', 0, 15, 3, 1),
(259, 'test big', 'dfsf asdf sadf asdf', 13, 1, 'Reps', 0, 15, 3, 1),
(260, 'test big', 'dfsf asdf sadf asdf', 87, 1, 'Reps', 0, 15, 3, 1),
(261, 'test big', 'dfsf asdf sadf asdf', 87, 1, 'Reps', 0, 15, 3, 1),
(262, 'test big', 'dfsf asdf sadf asdf', 90, 1, 'Reps', 0, 15, 3, 1),
(263, 'test big', 'dfsf asdf sadf asdf', 80, 1, 'Reps', 0, 15, 3, 1),
(264, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(265, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(266, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(267, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(268, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(269, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(270, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(271, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(272, 'test big', 'dfsf asdf sadf asdf', 86, 1, 'Reps', 0, 15, 3, 1),
(273, 'test big', 'dfsf asdf sadf asdf', 61, 2, 'Time', 15, 0, 3, 1),
(274, 'test big', 'dfsf asdf sadf asdf', 61, 2, 'Time', 15, 0, 3, 1),
(275, 'test big', 'dfsf asdf sadf asdf', 11, 2, 'Time', 15, 0, 3, 1),
(276, 'test big', 'dfsf asdf sadf asdf', 11, 2, 'Time', 0, 0, 3, 1),
(277, 'test big', 'dfsf asdf sadf asdf', 11, 3, 'EMOM', 12, 12, 3, 1),
(278, 'test big', 'dfsf asdf sadf asdf', 11, 3, 'EMOM', 25, 25, 3, 1),
(279, 'test big', 'dfsf asdf sadf asdf', 61, 3, 'EMOM', 5, 25, 3, 1),
(280, 'test big', 'dfsf asdf sadf asdf', 25, 3, 'EMOM', 5, 25, 3, 1),
(281, 'test big', 'dfsf asdf sadf asdf', 61, 3, 'EMOM', 25, 25, 3, 1),
(282, 'test big', 'dfsf asdf sadf asdf', 13, 4, 'Reps', 0, 15, 3, 1),
(283, 'test big', 'dfsf asdf sadf asdf', 13, 4, 'Reps', 0, 15, 3, 1),
(284, 'test big', 'dfsf asdf sadf asdf', 11, 4, 'Time', 15, 0, 3, 1),
(285, 'test big', 'dfsf asdf sadf asdf', 61, 4, 'Time', 15, 0, 3, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `exercise`
--
ALTER TABLE `exercise`
  ADD PRIMARY KEY (`id`),
  ADD KEY `muscle_group_id` (`muscle_group_id`);

--
-- Indexes for table `muscle_groups`
--
ALTER TABLE `muscle_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `muscle_name` (`muscle_name`);

--
-- Indexes for table `workouts`
--
ALTER TABLE `workouts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `exercise_id` (`exercise_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `exercise`
--
ALTER TABLE `exercise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `muscle_groups`
--
ALTER TABLE `muscle_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `workouts`
--
ALTER TABLE `workouts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=286;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `exercise`
--
ALTER TABLE `exercise`
  ADD CONSTRAINT `exercise_ibfk_1` FOREIGN KEY (`muscle_group_id`) REFERENCES `muscle_groups` (`id`);

--
-- Constraints for table `workouts`
--
ALTER TABLE `workouts`
  ADD CONSTRAINT `workouts_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
