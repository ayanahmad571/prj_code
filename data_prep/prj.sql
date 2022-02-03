-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 03, 2022 at 08:00 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prj`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_status`
--

CREATE TABLE `account_status` (
  `acc_uid` bigint(100) NOT NULL,
  `is_bot` int(2) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `data_lab`
--

CREATE TABLE `data_lab` (
  `uid` int(100) NOT NULL,
  `num_likes_per_num_friends` int(100) DEFAULT NULL,
  `follow_friends_ratio` int(100) DEFAULT NULL,
  `max_time_bw_retweets` int(100) DEFAULT NULL,
  `re_per_tweet` int(100) DEFAULT NULL,
  `num_likes` int(100) DEFAULT NULL,
  `num_likes_per_follower` int(100) DEFAULT NULL,
  `age_account` int(100) DEFAULT NULL,
  `num_tweets` int(100) DEFAULT NULL,
  `location` int(100) DEFAULT NULL,
  `len_username` int(100) DEFAULT NULL,
  `has_photo` int(100) DEFAULT NULL,
  `likes_per_day` int(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
