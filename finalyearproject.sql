-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2024 at 10:41 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finalyearproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'employee'),
(2, 'Guard');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add rtsp camera', 7, 'add_rtspcamera'),
(26, 'Can change rtsp camera', 7, 'change_rtspcamera'),
(27, 'Can delete rtsp camera', 7, 'delete_rtspcamera'),
(28, 'Can view rtsp camera', 7, 'view_rtspcamera'),
(29, 'Can add camera', 8, 'add_camera'),
(30, 'Can change camera', 8, 'change_camera'),
(31, 'Can delete camera', 8, 'delete_camera'),
(32, 'Can view camera', 8, 'view_camera'),
(33, 'Can add employee', 9, 'add_employee'),
(34, 'Can change employee', 9, 'change_employee'),
(35, 'Can delete employee', 9, 'delete_employee'),
(36, 'Can view employee', 9, 'view_employee'),
(37, 'Can add admin', 10, 'add_admin'),
(38, 'Can change admin', 10, 'change_admin'),
(39, 'Can delete admin', 10, 'delete_admin'),
(40, 'Can view admin', 10, 'view_admin'),
(41, 'Can add attendance', 11, 'add_attendance'),
(42, 'Can change attendance', 11, 'change_attendance'),
(43, 'Can delete attendance', 11, 'delete_attendance'),
(44, 'Can view attendance', 11, 'view_attendance'),
(45, 'Can add guard', 12, 'add_guard'),
(46, 'Can change guard', 12, 'change_guard'),
(47, 'Can delete guard', 12, 'delete_guard'),
(48, 'Can view guard', 12, 'view_guard'),
(49, 'Can add temporary person', 13, 'add_temporaryperson'),
(50, 'Can change temporary person', 13, 'change_temporaryperson'),
(51, 'Can delete temporary person', 13, 'delete_temporaryperson'),
(52, 'Can view temporary person', 13, 'view_temporaryperson');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$600000$Mz7Y06yqpTbYzBmUfbYuzM$hokultBKRP5UdCr7Ax5O6F7lc1bo4epKeyktjsKfge4=', '2024-05-08 08:37:06.380486', 1, 'Admin', '', '', 'ar256381@gmail.com', 1, 1, '2023-12-12 12:43:14.882409');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-12-13 12:29:27.861829', '1', 'employee', 1, '[{\"added\": {}}]', 3, 2),
(2, '2024-03-06 08:44:59.440011', '2', 'Guard', 1, '[{\"added\": {}}]', 3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'finalyearproject', 'admin'),
(11, 'finalyearproject', 'attendance'),
(8, 'finalyearproject', 'camera'),
(9, 'finalyearproject', 'employee'),
(12, 'finalyearproject', 'guard'),
(7, 'finalyearproject', 'rtspcamera'),
(13, 'finalyearproject', 'temporaryperson'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-12-12 10:12:25.691729'),
(2, 'auth', '0001_initial', '2023-12-12 10:12:51.206763'),
(3, 'admin', '0001_initial', '2023-12-12 10:12:57.167455'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-12-12 10:12:57.618203'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-12-12 10:12:57.738365'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-12-12 10:13:01.775840'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-12-12 10:13:05.538542'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-12-12 10:13:06.033969'),
(9, 'auth', '0004_alter_user_username_opts', '2023-12-12 10:13:06.242511'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-12-12 10:13:10.352073'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-12-12 10:13:10.447442'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-12-12 10:13:10.518331'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-12-12 10:13:10.732814'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-12-12 10:13:11.028571'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-12-12 10:13:11.347020'),
(16, 'auth', '0011_update_proxy_permissions', '2023-12-12 10:13:11.763175'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-12-12 10:13:12.096615'),
(18, 'sessions', '0001_initial', '2023-12-12 10:13:13.770033'),
(19, 'finalyearproject', '0001_initial', '2023-12-14 11:59:35.388692'),
(20, 'finalyearproject', '0002_camera_employee', '2023-12-17 09:05:02.052976'),
(21, 'finalyearproject', '0003_alter_employee_profile_picture', '2023-12-17 11:20:03.218445'),
(22, 'finalyearproject', '0004_alter_employee_profile_picture', '2023-12-23 11:47:47.258477'),
(23, 'finalyearproject', '0005_admin', '2023-12-23 11:47:48.262705'),
(24, 'finalyearproject', '0006_attendance', '2024-01-14 11:20:53.440536'),
(25, 'finalyearproject', '0007_alter_attendance_person_id', '2024-01-15 15:10:57.697942'),
(26, 'finalyearproject', '0008_alter_attendance_person_id', '2024-02-09 09:29:36.756549'),
(27, 'finalyearproject', '0009_guard', '2024-03-08 10:52:26.441520'),
(28, 'finalyearproject', '0010_temporaryperson', '2024-03-13 07:28:42.768098');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('48kfjfj2o6dlbah8qsbd8dyma2l6zapr', 'e30:1rD27u:fPXuwqpd8tNbrJxypTxHT-cm0e6hwguv7K4U2MuoBqg', '2023-12-26 12:44:42.541178'),
('a2qj45haf9yx6csf7qrz85fmn1sgs3l2', '.eJxVjMsOwiAQRf-FtSHQYRBcuvcbCI8ZqRqalHZl_HfbpAvd3nPOfYsQ16WGtdMcxiIuQqM4_Y4p5ie1nZRHbPdJ5qkt85jkrsiDdnmbCr2uh_t3UGOvW41gDTCy88Um6yyDMpodK5OMgozESGfS2rMqjBGiH4B03opBFW1AfL74_jfc:1rOzqa:a8E_ffe36daN7V9MUo75yHIFomU_tTQw7LXrdTUfl-E', '2024-01-28 12:44:16.828711'),
('aukifp0y2u0mqfpxnvyivib7w1wpfi8z', '.eJxtjktuwzAMRO-idSGIFGlJWXbfExSFQetjO23sIo5XRe9eGc0igb1982bIH9XKehvadcnXdkzqpFC9PLJO4meetiCdZepnHefpdh07vSn6ni76bU756_XuPg0Msgy1zY6xMGYPEgQ8U4rkIDmI4rtgohTvG1sk1shjiNyAL0GSK1i64qWOjvXwmrY_L9LnRZ3eFRokQ0iAzBz0-buv3gNszBG0T5CNBySy7gAy7CAb2JkWrNltVki0h3RUJ_t_6OP3D1iObhk:1s4cnS:A4cLbU9MQ-8RmMuNGWsjyGfSU3JU5yndhuTwBDDnwAk', '2024-05-22 08:37:06.466307'),
('ggdqw0i3h5hfa06sc6b1f0jv7lerddc6', '.eJxVjDsOwjAQBe_iGllerze2KelzBsvrDw6gRMqnQtydREoB7ZuZ9xYhbmsL21LmMGRxFYDi8jtyTM8yHiQ_4nifZJrGdR5YHoo86SL7KZfX7XT_Dlpc2l4jdAUrZQLjwFFKoE20FDV7UFyhQqHa1YqsjCX01rB1e6CzIkTP4vMF7cc3Qw:1rH1rY:TodvoCJah-laweNQENZNRWK22ludc13LgYiczqHwryc', '2024-01-06 13:16:20.887945'),
('h8lolg3b1rsp1avt2zty94ah98rsjesf', '.eJxVjEEOwiAQRe_C2hDBUgaX7nsGMswwUjU0Ke3KeHfbpAvd_vfef6uI61Li2vIcR1ZXZdXpd0tIz1x3wA-s90nTVJd5THpX9EGbHibOr9vh_h0UbGWrnXdWnM1gMKAB1zF13rA3hJDCmVAA-osgbQhsINcbkIDsxUoSQPX5AtgyOCE:1rPfd0:lUZIbRdK_fBGFkDWKlmJVsO1Hv3i5anEnTUI-5GtVh4', '2024-01-30 09:21:02.752419'),
('je9m22o9149iyv3k6mgp8ctc9z68swr2', '.eJxVjDsOAiEUAO9CbQj_j6X9noE8HiCrBpJltzLe3ZBsoe3MZN4kwLHXcIy8hTWRK-GKXH5hBHzmNk16QLt3ir3t2xrpTOhpB116yq_b2f4NKow6vyZy40Dr4lGzLEH4Atwa54vj6AqiSRllLMqwqITRRYKWEIVNliUmyecLC6s4NQ:1rH2t6:qYAn2xzo9Ndvmf9gANxiM_uou6Buo4XGuJoXLXV7xVQ', '2024-01-06 14:22:00.672951'),
('pst1zgq9itiawxkdk1zeg3nsc0cqugou', '.eJxVjEEOwiAQRe_C2hBgoDAu3XsGMsBUqoYmpV0Z765NutDtf-_9l4i0rTVunZc4FXEWYMTpd0yUH9x2Uu7UbrPMc1uXKcldkQft8joXfl4O9--gUq_fOigbjFLZppEteBd4JF14QIfgFOZMqiREoOwMAWgfvCetVQDPA1sU7w_zfzdO:1rq7pQ:4nCFlBCDyZ-CuvKrr2Qv5YviO_yQ_VuwIZ_sSyLYNmA', '2024-04-12 08:43:12.293609'),
('sjb5o64evjlqqv0xw24yl3mdpcz9efz0', '.eJxVjEEOwiAQRe_C2hCmIENduu8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3ERWonT7xgoPrjuJN2p3pqMra7LHOSuyIN2ObXEz-vh_h0U6uVbA1qFxEZbh0BGs405UQY12vHMCgcGhDwEpSllhw4zawsuWTKKGUi8P_GVN9Y:1rjEOs:7JSoZzipcGPvfrj6TEISwFd-Lm2F-kfUuCawyaSXB1g', '2024-03-24 08:19:18.513904'),
('y70nuar7yhlmqi97wqr3mtyj0fiw5td7', '.eJxVjEEOwiAQRe_C2hDBUgaX7nsGMswwUjU0Ke3KeHfbpAvd_vfef6uI61Li2vIcR1ZXZdXpd0tIz1x3wA-s90nTVJd5THpX9EGbHibOr9vh_h0UbGWrnXdWnM1gMKAB1zF13rA3hJDCmVAA-osgbQhsINcbkIDsxUoSQPX5AtgyOCE:1rYOSA:bAwbCVuQCyOBSRjoouL6ZEDu7mVW40ZIqa4hh73Uh3g', '2024-02-23 10:49:54.859420');

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_admin`
--

CREATE TABLE `finalyearproject_admin` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `admin_id` varchar(20) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `finalyearproject_admin`
--

INSERT INTO `finalyearproject_admin` (`id`, `name`, `admin_id`, `phone`, `email`, `address`, `profile_picture`) VALUES
(1, 'Admin', '1', '11111112', 'alirazanaveed28@gmail.com', 'a', 'img/1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_attendance`
--

CREATE TABLE `finalyearproject_attendance` (
  `id` bigint(20) NOT NULL,
  `person_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `finalyearproject_attendance`
--

INSERT INTO `finalyearproject_attendance` (`id`, `person_id`, `date`, `time`) VALUES
(1, 10, '2024-04-24', '13:11:28.000000');

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_camera`
--

CREATE TABLE `finalyearproject_camera` (
  `id` bigint(20) NOT NULL,
  `camera_link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_employee`
--

CREATE TABLE `finalyearproject_employee` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `employee_id` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_guard`
--

CREATE TABLE `finalyearproject_guard` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `guard_id` varchar(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `finalyearproject_guard`
--

INSERT INTO `finalyearproject_guard` (`id`, `name`, `guard_id`, `phone`, `email`, `address`, `profile_picture`) VALUES
(13, 'employee', '16', '123445nms', 'ar256381@gmail.com', 'aa', 'img/16.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_rtspcamera`
--

CREATE TABLE `finalyearproject_rtspcamera` (
  `id` bigint(20) NOT NULL,
  `camera_link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `finalyearproject_rtspcamera`
--

INSERT INTO `finalyearproject_rtspcamera` (`id`, `camera_link`) VALUES
(65, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(66, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(67, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(68, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(69, 'rtsp://192.168.0.110/h264_ulaw.sdp'),
(70, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(71, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(72, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(73, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(74, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(75, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(76, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(77, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(78, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(79, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(80, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(81, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(82, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(83, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(84, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(85, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(86, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(87, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(88, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(89, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(90, 'rtsp://192.168.0.110:8080/h264_ulaw.sdp'),
(91, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(92, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(93, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(94, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(95, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(96, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(97, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(98, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(99, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(100, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(101, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(102, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(103, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(104, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(105, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(106, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(107, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(108, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(109, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(110, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(111, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(112, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(113, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(114, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(115, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(116, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(117, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp'),
(118, 'rtsp://192.168.0.107:8080/h264_ulaw.sdp');

-- --------------------------------------------------------

--
-- Table structure for table `finalyearproject_temporaryperson`
--

CREATE TABLE `finalyearproject_temporaryperson` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `person_id` varchar(10) NOT NULL,
  `reason_for_visiting` longtext NOT NULL,
  `expiration_datetime` datetime(6) NOT NULL,
  `photo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `finalyearproject_admin`
--
ALTER TABLE `finalyearproject_admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Indexes for table `finalyearproject_attendance`
--
ALTER TABLE `finalyearproject_attendance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `finalyearproject_camera`
--
ALTER TABLE `finalyearproject_camera`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `finalyearproject_employee`
--
ALTER TABLE `finalyearproject_employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `finalyearproject_guard`
--
ALTER TABLE `finalyearproject_guard`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `finalyearproject_rtspcamera`
--
ALTER TABLE `finalyearproject_rtspcamera`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `finalyearproject_temporaryperson`
--
ALTER TABLE `finalyearproject_temporaryperson`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `finalyearproject_admin`
--
ALTER TABLE `finalyearproject_admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `finalyearproject_attendance`
--
ALTER TABLE `finalyearproject_attendance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `finalyearproject_camera`
--
ALTER TABLE `finalyearproject_camera`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `finalyearproject_employee`
--
ALTER TABLE `finalyearproject_employee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `finalyearproject_guard`
--
ALTER TABLE `finalyearproject_guard`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `finalyearproject_rtspcamera`
--
ALTER TABLE `finalyearproject_rtspcamera`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=119;

--
-- AUTO_INCREMENT for table `finalyearproject_temporaryperson`
--
ALTER TABLE `finalyearproject_temporaryperson`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
