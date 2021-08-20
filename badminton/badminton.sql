-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 20, 2021 at 07:34 AM
-- Server version: 5.7.19
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `badminton`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) COLLATE utf8_bin NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('b27edd965cf307756b1a2c97dca680007983b113', '2021-08-09 11:07:44.066172', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Token', 6, 'add_token'),
(22, 'Can change Token', 6, 'change_token'),
(23, 'Can delete Token', 6, 'delete_token'),
(24, 'Can view Token', 6, 'view_token'),
(25, 'Can add token', 7, 'add_tokenproxy'),
(26, 'Can change token', 7, 'change_tokenproxy'),
(27, 'Can delete token', 7, 'delete_tokenproxy'),
(28, 'Can view token', 7, 'view_tokenproxy'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add club', 9, 'add_club'),
(34, 'Can change club', 9, 'change_club'),
(35, 'Can delete club', 9, 'delete_club'),
(36, 'Can view club', 9, 'view_club'),
(37, 'Can add club responsable', 10, 'add_clubresponsable'),
(38, 'Can change club responsable', 10, 'change_clubresponsable'),
(39, 'Can delete club responsable', 10, 'delete_clubresponsable'),
(40, 'Can view club responsable', 10, 'view_clubresponsable'),
(41, 'Can add contact', 11, 'add_contact'),
(42, 'Can change contact', 11, 'change_contact'),
(43, 'Can delete contact', 11, 'delete_contact'),
(44, 'Can view contact', 11, 'view_contact'),
(45, 'Can add structure', 12, 'add_structure'),
(46, 'Can change structure', 12, 'change_structure'),
(47, 'Can delete structure', 12, 'delete_structure'),
(48, 'Can view structure', 12, 'view_structure'),
(49, 'Can add team', 13, 'add_team'),
(50, 'Can change team', 13, 'change_team'),
(51, 'Can delete team', 13, 'delete_team'),
(52, 'Can view team', 13, 'view_team'),
(53, 'Can add team player', 14, 'add_teamplayer'),
(54, 'Can change team player', 14, 'change_teamplayer'),
(55, 'Can delete team player', 14, 'delete_teamplayer'),
(56, 'Can view team player', 14, 'view_teamplayer'),
(57, 'Can add competition', 15, 'add_competition'),
(58, 'Can change competition', 15, 'change_competition'),
(59, 'Can delete competition', 15, 'delete_competition'),
(60, 'Can view competition', 15, 'view_competition'),
(61, 'Can add group', 16, 'add_group'),
(62, 'Can change group', 16, 'change_group'),
(63, 'Can delete group', 16, 'delete_group'),
(64, 'Can view group', 16, 'view_group'),
(65, 'Can add level', 17, 'add_level'),
(66, 'Can change level', 17, 'change_level'),
(67, 'Can delete level', 17, 'delete_level'),
(68, 'Can view level', 17, 'view_level'),
(69, 'Can add type', 18, 'add_type'),
(70, 'Can change type', 18, 'change_type'),
(71, 'Can delete type', 18, 'delete_type'),
(72, 'Can view type', 18, 'view_type'),
(73, 'Can add game', 19, 'add_game'),
(74, 'Can change game', 19, 'change_game'),
(75, 'Can delete game', 19, 'delete_game'),
(76, 'Can view game', 19, 'view_game'),
(77, 'Can add position', 20, 'add_position'),
(78, 'Can change position', 20, 'change_position'),
(79, 'Can delete position', 20, 'delete_position'),
(80, 'Can view position', 20, 'view_position');

-- --------------------------------------------------------

--
-- Table structure for table `clubs`
--

DROP TABLE IF EXISTS `clubs`;
CREATE TABLE IF NOT EXISTS `clubs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `city` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `clubs`
--

INSERT INTO `clubs` (`id`, `name`, `city`) VALUES
(1, 'BC Martigny', 'Martigny'),
(2, 'BC Vollèges', NULL),
(3, 'BC Swaff', NULL),
(4, 'BC Ayent', NULL),
(5, 'BC Brig', 'Brig'),
(6, 'BC Nendaz', NULL),
(7, 'BC Sierre', NULL),
(8, 'BC Fully', 'Fully'),
(9, 'BC Sion', NULL),
(10, 'BC Granges', NULL),
(11, 'BC St-Maurice', NULL),
(12, 'BC Monthey', NULL),
(13, 'BC Riddes', NULL),
(14, 'BC Anniviers', NULL),
(15, 'BC Champéry', NULL),
(16, 'BC Collombey-Muraz', NULL),
(17, 'BC Conthey', NULL),
(18, 'BC Leytron', NULL),
(19, 'BC Savièse', NULL),
(21, 'BC Olympica-Brig', NULL),
(22, 'BC Team Monthey', NULL),
(23, 'BC Val-d\'Illiez', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `club_responsible`
--

DROP TABLE IF EXISTS `club_responsible`;
CREATE TABLE IF NOT EXISTS `club_responsible` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `function` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `club_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `club_responsible_club_id_46ec60a3` (`club_id`),
  KEY `club_responsible_user_id_f81f91ed` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `club_responsible`
--

INSERT INTO `club_responsible` (`id`, `function`, `club_id`, `user_id`) VALUES
(1, 'Président', 1, 2),
(2, 'Président', 14, 3),
(3, 'Resp. IC', 14, 4),
(4, 'Resp. juniors', 14, 5),
(5, 'Resp. IC', 4, 6),
(6, 'Resp. juniors', 4, 7),
(7, 'Président', 15, 8),
(8, 'Resp. IC', 15, 9),
(9, 'Président', 16, 10),
(10, 'Resp. IC', 16, 11),
(11, 'Resp. juniors', 16, 12),
(12, 'Président', 17, 13),
(13, 'Président', 8, 14),
(14, 'Resp. IC', 8, 15),
(15, 'Resp. juniors', 8, 16),
(16, 'Président', 10, 17),
(17, 'Resp. IC', 10, 18),
(18, 'Resp. juniors', 10, 19),
(19, 'Resp. IC', 18, 20),
(20, 'Resp. juniors', 18, 21),
(21, 'Resp. IC', 1, 22),
(22, 'Resp. juniors', 1, 23),
(23, 'Président', 6, 24),
(24, 'Resp. IC', 6, 25),
(25, 'club', 21, 26),
(26, 'Président', 21, 27),
(27, 'Resp. juniors', 21, 28),
(28, 'club', 13, 29),
(29, 'Resp. IC', 13, 30),
(30, 'Resp. juniors', 13, 31),
(31, 'Resp.admin.', 19, 32),
(32, 'Resp. IC', 19, 33),
(33, 'Resp. juniors', 19, 34),
(34, 'Président', 7, 35),
(35, 'Resp. IC', 7, 36),
(36, 'Resp. juniors', 7, 37),
(37, 'Président', 9, 38),
(38, 'Resp. IC', 9, 39),
(39, 'Resp. juniors', 9, 40),
(40, 'Président', 11, 41),
(41, 'Resp. IC', 11, 42),
(42, 'Resp. juniors', 11, 43),
(43, 'Resp. juniors', 11, 44),
(44, 'Président', 22, 45),
(45, 'Resp. IC', 22, 46),
(46, 'Resp. juniors', 22, 47),
(47, 'Président', 23, 48),
(48, 'Vice-Président', 23, 49),
(49, 'Secrétaire', 23, 50),
(50, 'Resp. IC', 2, 51),
(51, 'Resp. juniors', 2, 52),
(52, 'co-Président', 3, 53);

-- --------------------------------------------------------

--
-- Table structure for table `competitions_competition`
--

DROP TABLE IF EXISTS `competitions_competition`;
CREATE TABLE IF NOT EXISTS `competitions_competition` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `datatime` datetime(6) DEFAULT NULL,
  `turn` varchar(100) COLLATE utf8_bin NOT NULL,
  `matches_h` int(10) UNSIGNED DEFAULT NULL,
  `matches_a` int(10) UNSIGNED DEFAULT NULL,
  `set_h` int(10) UNSIGNED DEFAULT NULL,
  `set_a` int(10) UNSIGNED DEFAULT NULL,
  `group_id` bigint(20) DEFAULT NULL,
  `level_id` bigint(20) DEFAULT NULL,
  `team_a_id` bigint(20) NOT NULL,
  `team_h_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `competitions_competition_group_id_e3e39c08` (`group_id`),
  KEY `competitions_competition_level_id_e7ffe54d` (`level_id`),
  KEY `competitions_competition_team_a_id_e7d62ebb` (`team_a_id`),
  KEY `competitions_competition_team_h_id_4a634536` (`team_h_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
CREATE TABLE IF NOT EXISTS `contacts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `phone` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `address` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `npa` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `city` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `phone`, `address`, `npa`, `city`, `user_id`) VALUES
(1, '078 729 85 76', 'Plandisso 37', '3961', 'Vissoie', 3),
(2, '079 398 23 12 ', 'Rte des Barmes ', '3961', 'St-Jean', 4),
(3, '079 639 93 62', 'Plandisso 47', '3961', 'Vissoie', 5),
(4, '076 636 35 36', 'Rte du Rawil 21', '1966', 'Ayent', 6),
(5, '079 579 51 34', 'Rte de St.Romain 31', '1966', 'Ayent', 7),
(6, '076 519 79 08', 'Ch. de la Barme 25 ', '1868', 'Collombey ', 8),
(7, '079 214 38 73', 'Revenettaz 4 ', '1872', 'Troistorrents', 9),
(8, '079 383 91 74', 'Rue de Clos-Novex 62A', '1868', 'Collombey', 10),
(9, '079 409 94 04 ', 'Ch. Aimé Nicollerat 34', '1880', 'Bex', 11),
(10, '078 845 61 40', 'Ch.du Gaudard 25', '1868', 'Collombey', 12),
(11, '078 745 01 81', 'Crêté du Roh 6', '1976', 'Daillon', 13),
(12, '079 542 64 83', 'Ch. des Clares 41', '1926', 'Fully', 14),
(13, '078 876 10 81', NULL, '1926', 'Fully', 15),
(14, '076 414 25 51', NULL, '1926', 'Fully', 16),
(15, '079 563 82 11', 'Rue de Pré-de-Savioz 20B', '3977', 'Granges', 17),
(16, '079 712 67 24', 'Rue des Ronques 22', '3977', 'Granges', 18),
(17, '079 748 58 25', 'Rue des Ronques 22', '3977', 'Granges', 19),
(18, '079 237 52 85', 'Rue de la Sauge 17', '1912', 'Leytron', 20),
(19, '078 759 74 62', 'Vissigen 86', '1950', 'Sion', 21),
(20, '079 762 90 54', ' Rue Oscar-Bider 132', ' 1950', ' Sion', 2),
(21, ' 0787149304', ' Rue du Bourg 12', ' 1920', 'Martigny ', 22),
(22, '079 870 86 65', 'Grand\'Rue 97', '1904', 'Vernayaz', 23),
(23, '078 835 58 02', 'Ch. Du Vieux Canal 2A', '1950', 'Sion', 24),
(24, '078 679 99 29', 'Rte de Nendaz 63', '1996', 'Brignon', 25),
(25, '027 924 35 50', 'Industriestrasse 94', '3902', 'Brig-Glis', 26),
(26, '079 378 37 65', 'Sonnenstrasse 27', '3930', 'Visp', 27),
(27, '079 860 80 75', 'Nordstrasse 29', '3900', 'Brig', 28),
(28, '079 466 78 33', 'Rte de Fare 36', '1908', 'Riddes', 29),
(29, '076 402 38 62', 'Rouatope 14', '1912', 'Leytron', 30),
(30, '078 883 12 94', 'Rue des Artisans 1', '1908', 'Riddes', 31),
(31, '079 673 48 84', 'Ch. de la Vâsse 13', '1965', 'Savièse', 32),
(32, '079 450 62 21', 'Rue d\'Ormône 10', '1965', 'Savièse', 33),
(33, '079  430 40 56', 'Rte de Roumaz 77', '1965', 'Savièse', 34),
(34, '079 518 69 57', 'Allée du Glarier 8 ', '3960', 'Sierre', 35),
(35, '079 712 84 34', 'Rue de la Rèche 33', '3966', 'Réchy', 36),
(36, '079 460 53 95', 'Schafgasse 47 ', '3970', 'Salquenen', 37),
(37, '079 483 75 75', 'Jonction 18', '1958', 'St-Léonard', 38),
(38, '079 646 24 52', 'Ch. des Pâquerettes 41', '1950', 'Sion', 39),
(39, '079 277 65 11', 'Rte du Simplon 51', '1958', 'St-Léonard', 40),
(40, '079 725 62 91 ', 'Ch des Crèches 3', '1890', 'St-Maurice', 41),
(41, '079 303 08 22', 'Grand-Clos 35A', '1869', 'Massongex', 42),
(42, '076 489 28 05', 'Av.de Vérolliez 55', '1890', 'St-Maurice', 43),
(43, '076 530 64 78', 'Ch. Des Arnoux', '1867', 'Ollon', 44),
(44, '078 722 11 56 ', 'Rte de Choëx 74', '1871', 'Choëx', 45),
(45, '079 278 23 0 3', 'Rte de Massillon 1C', '1871', 'Choëx', 46),
(46, '079 663 00 62', NULL, NULL, NULL, 47),
(47, '079 694 95 88', 'Ch. de la Cheminée 17', '1872', 'Troistorrents', 48),
(48, '079 314 06 99', 'Ch. de Margoison 13', '1872', 'Troistorrents', 49),
(49, '079 232 39 51', 'Ch. de Buchelieule 3', '1873', 'Val-d\'Illiez', 50),
(50, '079 128 00 04', 'Ch. de la Cotze 4', '1941', 'Vollèges', 51),
(51, '079 474 53 78', 'Ch. des Crêtes 10', '1941', 'Vollèges', 52),
(52, '079 282 31 94', NULL, NULL, NULL, 53);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-08-09 12:15:11.710577', '21', 'BC Swaff', 2, '[{\"changed\": {\"fields\": [\"Club\", \"Level\", \"Group\"]}}]', 13, 1),
(2, '2021-08-15 08:41:42.858805', '1', 'Captain', 1, '[{\"added\": {}}]', 20, 1),
(3, '2021-08-15 08:41:50.425459', '2', 'Extra', 1, '[{\"added\": {}}]', 20, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'authtoken', 'token'),
(7, 'authtoken', 'tokenproxy'),
(8, 'clubs', 'user'),
(9, 'clubs', 'club'),
(10, 'clubs', 'clubresponsable'),
(11, 'clubs', 'contact'),
(12, 'clubs', 'structure'),
(13, 'clubs', 'team'),
(14, 'clubs', 'teamplayer'),
(15, 'competitions', 'competition'),
(16, 'competitions', 'group'),
(17, 'competitions', 'level'),
(18, 'competitions', 'type'),
(19, 'competitions', 'game'),
(20, 'clubs', 'position');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-08-09 08:40:59.300075'),
(2, 'clubs', '0001_initial', '2021-08-09 08:40:59.577075'),
(3, 'admin', '0001_initial', '2021-08-09 08:40:59.681074'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-08-09 08:40:59.688075'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-08-09 08:40:59.695075'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-08-09 08:40:59.749107'),
(7, 'auth', '0001_initial', '2021-08-09 08:40:59.971671'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-08-09 08:41:00.003674'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-08-09 08:41:00.011643'),
(10, 'auth', '0004_alter_user_username_opts', '2021-08-09 08:41:00.020679'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-08-09 08:41:00.029671'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-08-09 08:41:00.033675'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-08-09 08:41:00.043690'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-08-09 08:41:00.051670'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-08-09 08:41:00.060680'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-08-09 08:41:00.091641'),
(17, 'auth', '0011_update_proxy_permissions', '2021-08-09 08:41:00.103641'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-08-09 08:41:00.112640'),
(19, 'authtoken', '0001_initial', '2021-08-09 08:41:00.157669'),
(20, 'authtoken', '0002_auto_20160226_1747', '2021-08-09 08:41:00.178675'),
(21, 'authtoken', '0003_tokenproxy', '2021-08-09 08:41:00.183914'),
(22, 'competitions', '0001_initial', '2021-08-09 08:41:00.793585'),
(23, 'clubs', '0002_initial', '2021-08-09 08:41:01.499831'),
(24, 'sessions', '0001_initial', '2021-08-09 08:41:01.541861'),
(25, 'clubs', '0003_auto_20210815_1036', '2021-08-15 08:36:45.921846'),
(26, 'clubs', '0004_rename_user_teamplayer_player', '2021-08-15 12:32:54.175489'),
(27, 'competitions', '0002_alter_level_name', '2021-08-20 07:06:13.635800');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('l4lrgy6ke2l113jxljuw5mpw1ibhf4tj', '.eJxVjDEOwjAMRe-SGUUkmMRmZO8ZKjtxSAG1UtNOiLtDpQ6w_vfef5me16X2a9O5H7K5GGcOv5tweui4gXzn8TbZNI3LPIjdFLvTZrsp6_O6u38HlVv91iFlDJ6kgKDE6F0soTCQMiMBnRUgohIAO0knKi67YyFMEtBrCGjeH-gXN9M:1mD2P2:qyTKE64Zvc9GSyvP78GYj8nwZ9GNUyE3XWYNKStovMg', '2021-08-23 10:21:04.668868');

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
CREATE TABLE IF NOT EXISTS `games` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `score_h_1` int(10) UNSIGNED DEFAULT NULL,
  `score_a_1` int(10) UNSIGNED DEFAULT NULL,
  `score_h_2` int(10) UNSIGNED DEFAULT NULL,
  `score_a_2` int(10) UNSIGNED DEFAULT NULL,
  `score_h_3` int(10) UNSIGNED DEFAULT NULL,
  `score_a_3` int(10) UNSIGNED DEFAULT NULL,
  `match_h` int(10) UNSIGNED DEFAULT NULL,
  `match_a` int(10) UNSIGNED DEFAULT NULL,
  `set_h` int(10) UNSIGNED DEFAULT NULL,
  `set_a` int(10) UNSIGNED DEFAULT NULL,
  `competition_id` bigint(20) NOT NULL,
  `player_a_id` bigint(20) NOT NULL,
  `player_a2_id` bigint(20) DEFAULT NULL,
  `player_h_id` bigint(20) NOT NULL,
  `player_h2_id` bigint(20) DEFAULT NULL,
  `type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `games_competition_id_0aef6834` (`competition_id`),
  KEY `games_player_a_id_c917b2d8` (`player_a_id`),
  KEY `games_player_a2_id_475146c8` (`player_a2_id`),
  KEY `games_player_h_id_b1baedd9` (`player_h_id`),
  KEY `games_player_h2_id_28ef33a5` (`player_h2_id`),
  KEY `games_type_id_bcd3bd26` (`type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
CREATE TABLE IF NOT EXISTS `groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `groups`
--

INSERT INTO `groups` (`id`, `name`, `reference`) VALUES
(1, '5ème ligue', NULL),
(2, '6ème ligue groupe 1', NULL),
(3, '6ème ligue groupe 2', NULL),
(4, 'Juniors A', NULL),
(5, 'Juniors B', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `levels`
--

DROP TABLE IF EXISTS `levels`;
CREATE TABLE IF NOT EXISTS `levels` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `levels`
--

INSERT INTO `levels` (`id`, `name`) VALUES
(1, '1e ligue'),
(2, '2e ligue'),
(3, '3e ligue'),
(4, '4e ligue'),
(5, '5e ligue'),
(6, '6e ligue'),
(7, 'Junior');

-- --------------------------------------------------------

--
-- Table structure for table `positions`
--

DROP TABLE IF EXISTS `positions`;
CREATE TABLE IF NOT EXISTS `positions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `positions`
--

INSERT INTO `positions` (`id`, `name`) VALUES
(1, 'Captain'),
(2, 'Extra');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
CREATE TABLE IF NOT EXISTS `teams` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `reference` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `club_id` bigint(20) DEFAULT NULL,
  `group_id` bigint(20) DEFAULT NULL,
  `level_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `reference` (`reference`),
  KEY `teams_club_id_edbd260e` (`club_id`),
  KEY `teams_group_id_37001956` (`group_id`),
  KEY `teams_level_id_5508e47b` (`level_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `reference`, `club_id`, `group_id`, `level_id`) VALUES
(1, 'St-Maurice 3', '5001', 11, 1, 5),
(2, 'Granges', '5002', 10, 1, 5),
(3, 'Martigny 4', '5003', 1, 1, 5),
(4, 'Sion 7', '5004', 9, 1, 5),
(5, 'Ayent', '5006', 4, 1, 5),
(6, 'Fully 2', '5007', 8, 1, 5),
(7, 'Savièse', '6101', 19, 2, 6),
(8, 'Val d\'Illiez 2', '6102', 23, 2, 6),
(9, 'Ayent 2', '6103', 4, 2, 6),
(10, 'Olympica Brig 5', '6104', 21, 2, 6),
(11, 'Anniviers', '6105', 14, 2, 6),
(12, 'Sion 8', '6106', 9, 2, 6),
(13, 'Leytron 2', '6107', 18, 2, 6),
(14, 'Sierre 3', '6108', 7, 2, 6),
(15, 'Val d\'Illiez ', '6201', 23, 3, 6),
(16, 'Anniviers 2', '6202', 14, 3, 6),
(17, 'Champéry ', '6203', 15, 3, 6),
(18, 'Leytron', '6204', 18, 3, 6),
(19, 'Vollèges 2', '6205', 2, 3, 6),
(20, 'Martigny 5', '6206', 1, 3, 6),
(21, 'BC Swaff', '6207', 3, NULL, NULL),
(22, 'Vollèges 3', '7001', 2, 4, 7),
(23, 'St-Maurice 4', '7002', 11, 4, 7),
(24, 'Sion 9', '7003', 9, 4, 7),
(25, 'Sion 10', '7004', 9, 4, 7),
(26, 'Fully-Martigny', '7005', 8, 4, 7),
(27, 'Sierre 4', '7006', 7, 4, 7),
(28, 'Ayent 3', '7007', 4, 4, 7),
(29, 'Leytron-Riddes', '8001', 18, 5, 7),
(30, 'Fully-Martigny 2', '8002', 8, 5, 7),
(31, 'Sion 11', '8003', 9, 5, 7),
(32, 'Sierre 5', '8004', 7, 5, 7),
(33, 'St-Maurice 5', '8005', 11, 5, 7),
(34, 'Martigny', NULL, 1, NULL, 3),
(35, 'Martigny 2', NULL, 1, NULL, 3),
(36, 'Martigny 3', NULL, 1, NULL, 4);

-- --------------------------------------------------------

--
-- Table structure for table `team_player`
--

DROP TABLE IF EXISTS `team_player`;
CREATE TABLE IF NOT EXISTS `team_player` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_id` bigint(20) NOT NULL,
  `player_id` bigint(20) NOT NULL,
  `position_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `team_player_team_id_031b9c1d` (`team_id`),
  KEY `team_player_user_id_6b3a0fcb` (`player_id`),
  KEY `team_player_position_id_b1a13799` (`position_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `team_player`
--

INSERT INTO `team_player` (`id`, `team_id`, `player_id`, `position_id`) VALUES
(1, 20, 1, NULL),
(9, 3, 1, 2),
(10, 34, 2, 1),
(11, 3, 22, 2);

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
CREATE TABLE IF NOT EXISTS `types` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `first_name` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `licence` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `sex` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `club_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `licence` (`licence`),
  KEY `users_club_id_89c058eb` (`club_id`)
) ENGINE=MyISAM AUTO_INCREMENT=54 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `password`, `last_login`, `is_superuser`, `username`, `is_staff`, `is_active`, `date_joined`, `first_name`, `last_name`, `email`, `licence`, `sex`, `birthday`, `club_id`) VALUES
(1, 'pbkdf2_sha256$260000$5zuvtxHhvq5CkPkXIGIdkG$rS97RRV4UePv9aT3doji3xztpNsxKztPxDoDpNfUINc=', '2021-08-09 10:21:04.668109', 1, 'fen', 1, 1, '2021-07-10 17:32:12.000000', 'Fen', 'Zheng', 'tozhengfen@gmail.com', NULL, 'F', '1985-04-16', 1),
(2, 'pbkdf2_sha256$260000$jvLTb7c1ORNM36I8xlxz3a$Fi/gIB2nO7URY+4eNlnnERwzBNAU1T5XOUHVKK/wuso=', NULL, 0, 'David_A', 0, 1, '2021-07-22 06:45:15.000000', 'David', 'Amslter', 'david.amsler@allianz-suisse.ch', NULL, NULL, NULL, 1),
(3, '', NULL, 0, 'frederic.cardona', 0, 1, '2021-07-26 12:26:16.272211', 'Frédéric', 'Cardona', 'info@badanniviers.ch', NULL, NULL, NULL, 14),
(4, '', NULL, 0, 'sébastien.kampf', 0, 1, '2021-07-26 12:28:24.467725', 'Sébastien', 'Kämpf', 'sebkampf@gmail.com', NULL, NULL, NULL, 14),
(5, '', NULL, 0, 'yann.bouduban', 0, 1, '2021-07-26 12:28:24.472719', 'Yann', 'Bouduban', 'yann.boudu@gmail.com', NULL, NULL, NULL, 14),
(6, '', NULL, 0, 'rené.bonvin', 0, 1, '2021-07-26 12:28:24.477719', 'René', 'Bonvin', 'rene.bonvin@bluewin.ch', NULL, NULL, NULL, 4),
(7, '', NULL, 0, 'barbara.barbara', 0, 1, '2021-07-26 12:28:24.486719', 'Barbara', 'Blanc ', 'barbouilleblanc@bluewin.ch', NULL, NULL, NULL, 4),
(8, '', NULL, 0, 'angélique.perrin', 0, 1, '2021-07-26 12:28:24.491719', 'Angélique', 'Perrin', 'angelique.perrin@bluewin.ch', NULL, NULL, NULL, 15),
(9, '', NULL, 0, 'yann.oppliger', 0, 1, '2021-07-26 12:28:52.502560', 'Yann', 'Oppliger', 'yann@talum.ch', NULL, NULL, NULL, 15),
(10, '', NULL, 0, 'antonija.tutic', 0, 1, '2021-07-26 12:28:52.507560', 'Antonija', 'Tutic', 'antonija.bccm@gmail.com', NULL, NULL, NULL, 16),
(11, '', NULL, 0, 'léa.amos', 0, 1, '2021-07-26 12:28:52.512511', 'Léa', 'Amos', 'amos.lea@outlook.com', NULL, NULL, NULL, 16),
(12, '', NULL, 0, 'mariline.avanzato', 0, 1, '2021-07-26 12:28:52.518175', 'Mariline', 'Avanzato', 'avanzatomariline@gmail.com', NULL, NULL, NULL, 16),
(13, '', NULL, 0, 'xavier.saillen', 0, 1, '2021-07-26 12:28:52.523171', 'Xavier', 'Saillen', 'info@bcconthey.ch', NULL, NULL, NULL, 17),
(14, '', NULL, 0, 'dominique.rémondeulaz', 0, 1, '2021-07-26 12:28:52.527170', 'Dominique', 'Rémondeulaz', 'dominique.remondeulaz@mycable.ch', NULL, NULL, NULL, 8),
(15, '', NULL, 0, 'emeline.zufferey', 0, 1, '2021-07-26 12:28:52.531717', 'Emeline', 'Zufferey', 'emeline.zufferey@gmail.com', NULL, NULL, NULL, 8),
(16, '', NULL, 0, 'alexandre.vannay', 0, 1, '2021-07-26 12:28:52.537718', 'Alexandre', 'Vannay', 'alex.vanay@netplus.ch', NULL, NULL, NULL, 8),
(17, '', NULL, 0, 'laetitia.elsener', 0, 1, '2021-07-26 12:28:52.541718', 'Laetitia', 'Elsener', 'president@bcgranges.ch', NULL, NULL, NULL, 10),
(18, '', NULL, 0, 'rachel.grand', 0, 1, '2021-07-26 12:28:52.545718', 'Rachel', 'Grand', 'grandfam@netplus.ch', NULL, NULL, NULL, 10),
(19, '', NULL, 0, 'muriel.grand', 0, 1, '2021-07-26 12:28:52.550719', 'Muriel', 'Grand', 'muriel.grand@netcourrier.com', NULL, NULL, NULL, 10),
(20, '', NULL, 0, 'anne-marie.beytrison', 0, 1, '2021-07-26 12:28:52.557719', 'Anne-Marie', 'Beytrison', 'beytrisona@gmail.com', NULL, NULL, NULL, 18),
(21, '', NULL, 0, 'cindy.beytrison', 0, 1, '2021-07-26 12:28:52.564718', 'Cindy', 'Beytrison', 'cindyb5p@hotmail.com', NULL, NULL, NULL, 18),
(22, '', NULL, 0, 'jonas.paccolat', 0, 1, '2021-07-26 12:28:52.573718', 'Jonas', 'Paccolat', ' Jonas.paccolat@outlook.com', NULL, NULL, NULL, 1),
(23, '', NULL, 0, 'damien.genolet', 0, 1, '2021-07-26 12:28:52.576718', 'Damien', 'Genolet', 'damiengenolet@gmail.com', NULL, NULL, NULL, 1),
(24, '', NULL, 0, 'maxime.reynard', 0, 1, '2021-07-26 12:28:52.581718', 'Maxime', 'Reynard', 'maxime.reynard@gmail.com', NULL, NULL, NULL, 6),
(25, '', NULL, 0, 'francis.peronetti', 0, 1, '2021-07-26 12:28:52.586718', 'Francis', 'Peronetti', 'f.peronetti@icloud.com', NULL, NULL, NULL, 6),
(26, '', NULL, 0, 'info@bc-olympica-brig.ch', 0, 1, '2021-07-26 12:38:54.632562', NULL, NULL, 'info@bc-olympica-brig.ch', NULL, NULL, NULL, 21),
(27, '', NULL, 0, 'marco.fux ', 0, 1, '2021-07-26 12:38:54.636571', 'Marco', 'Fux ', 'marco_fux84@hotmail.com', NULL, NULL, NULL, 21),
(28, '', NULL, 0, 'kai.waldenberger', 0, 1, '2021-07-26 12:38:54.640571', 'Kai', 'Waldenberger', 'kai.waldenberger83@hotmail.com', NULL, NULL, NULL, 21),
(29, '', NULL, 0, 'tamara.lopez', 0, 1, '2021-07-26 12:38:54.648559', 'Tamara', 'Lopez', 'info.bcriddes@gmail.com', NULL, NULL, NULL, 13),
(30, '', NULL, 0, 'lionel.monnat', 0, 1, '2021-07-26 12:38:54.652542', 'Lionel', 'Monnat', 'lionel.monnat@gmail.com', NULL, NULL, NULL, 13),
(31, '', NULL, 0, 'gilles-arnaud.comby', 0, 1, '2021-07-26 12:38:54.660575', 'Gilles-Arnaud', 'Comby', 'gilles-arnaud.comby@unifr.ch', NULL, NULL, NULL, 13),
(32, '', NULL, 0, 'sandra.clivaz', 0, 1, '2021-07-26 12:38:54.665591', 'Sandra', 'Clivaz', 'sandra.clivaz@netplus.ch', NULL, NULL, NULL, 19),
(33, '', NULL, 0, 'simone.farquet', 0, 1, '2021-07-26 12:38:54.669571', 'Simone', 'Farquet', 'simone.dumoulin@ubs.com', NULL, NULL, NULL, 19),
(34, '', NULL, 0, 'valérie.solliard', 0, 1, '2021-07-26 12:38:54.673572', 'Valérie', 'Solliard', 'valeriesolliard@bluewin.ch', NULL, NULL, NULL, 19),
(35, '', NULL, 0, 'françois.steiner', 0, 1, '2021-07-26 12:38:54.677571', 'François', 'Steiner', 'president@bcsierre.ch', NULL, NULL, NULL, 7),
(36, '', NULL, 0, 'sandrine.mayoraz', 0, 1, '2021-07-26 12:38:54.680572', 'Sandrine', 'Mayoraz', 'smayoraz29@gmail.com', NULL, NULL, NULL, 7),
(37, '', NULL, 0, 'baptiste.cavin', 0, 1, '2021-07-26 12:38:54.685542', 'Baptiste', 'Cavin', 'baptiste.cavin@bluewin.ch', NULL, NULL, NULL, 7),
(38, '', NULL, 0, 'thierry.piffaretti', 0, 1, '2021-07-26 12:38:54.690544', 'Thierry', 'Piffaretti', 'thierry.piffaretti@bluewin.ch', NULL, NULL, NULL, 9),
(39, '', NULL, 0, 'grégoire.locher', 0, 1, '2021-07-26 12:38:54.694541', 'Grégoire', 'Locher', 'greg73@netplus.ch', NULL, NULL, NULL, 9),
(40, '', NULL, 0, 'arsène.berra', 0, 1, '2021-07-26 12:38:54.697542', 'Arsène', 'Berra', 'a.berra@bluewin.ch', NULL, NULL, NULL, 9),
(41, '', NULL, 0, 'yoann.clerc', 0, 1, '2021-07-26 12:38:54.702543', 'Yoann', 'Clerc', 'yclerc@hotmail.com', NULL, NULL, NULL, 11),
(42, '', NULL, 0, 'droz.nicole', 0, 1, '2021-07-26 12:38:54.705544', 'Droz', 'Nicole', 'nicole.droz@bluewin.ch', NULL, NULL, NULL, 11),
(43, '', NULL, 0, 'tosi.frédéric', 0, 1, '2021-07-26 12:38:54.709572', 'Tosi', 'Frédéric', 'fredo_tosi@hotmail.com', NULL, NULL, NULL, 11),
(44, '', NULL, 0, 'gabioud.ami', 0, 1, '2021-07-26 12:38:54.712541', 'Gabioud', 'Ami', 'agabioud@bluewin.ch', NULL, NULL, NULL, 11),
(45, '', NULL, 0, 'cindy.vuilloud', 0, 1, '2021-07-26 12:38:54.719589', 'Cindy', 'Vuilloud', 'cindyvuilloud@gmail.com', NULL, NULL, NULL, 22),
(46, '', NULL, 0, 'tony.nicoulaz', 0, 1, '2021-07-26 12:38:54.722542', 'Tony', 'Nicoulaz', 'nicoulaz@bluewin.ch', NULL, NULL, NULL, 22),
(47, '', NULL, 0, 'sarah.coeytaux', 0, 1, '2021-07-26 12:38:54.726542', 'Sarah', 'Coeytaux', 'aa_edette@hotmail.com', NULL, NULL, NULL, 22),
(48, '', NULL, 0, 'christophe.valvona', 0, 1, '2021-07-26 12:38:54.730554', 'Christophe', 'Valvona', 'ch.valvona@gmail.com', NULL, NULL, NULL, 23),
(49, '', NULL, 0, 'fabrice.perrin', 0, 1, '2021-07-26 12:38:54.735554', 'Fabrice', 'Perrin', 'fabrice.perrin@netplus.ch', NULL, NULL, NULL, 23),
(50, '', NULL, 0, 'jean-jacques.pasche', 0, 1, '2021-07-26 12:38:54.739571', 'Jean-Jacques', 'Pasche', 'jjpasche48@netplus.ch', NULL, NULL, NULL, 23),
(51, '', NULL, 0, 'elodie.moulin', 0, 1, '2021-07-26 12:38:54.743570', 'Elodie', 'Moulin', 'moulin.elodie95@gmail.com', NULL, NULL, NULL, 2),
(52, '', NULL, 0, 'claudine.moulin', 0, 1, '2021-07-26 12:38:54.751544', 'Claudine', 'Moulin', 'claudinefro@hotmail.com', NULL, NULL, NULL, 2),
(53, '', NULL, 0, 'fabien.jacot', 0, 1, '2021-07-26 12:38:54.755542', 'Fabien', 'Jacot', 'info.bcswaff@gmail.com', NULL, NULL, NULL, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users_groups`
--

DROP TABLE IF EXISTS `users_groups`;
CREATE TABLE IF NOT EXISTS `users_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_groups_user_id_group_id_fc7788e8_uniq` (`user_id`,`group_id`),
  KEY `users_groups_user_id_f500bee5` (`user_id`),
  KEY `users_groups_group_id_2f3517aa` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `users_user_permissions`
--

DROP TABLE IF EXISTS `users_user_permissions`;
CREATE TABLE IF NOT EXISTS `users_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_permissions_user_id_permission_id_3b86cbdf_uniq` (`user_id`,`permission_id`),
  KEY `users_user_permissions_user_id_92473840` (`user_id`),
  KEY `users_user_permissions_permission_id_6d08dcd2` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
