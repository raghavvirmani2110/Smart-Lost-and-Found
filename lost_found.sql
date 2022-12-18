-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2022 at 02:49 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lost_found`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_users`
--

CREATE TABLE `app_users` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(1024) NOT NULL,
  `phoneNumber` varchar(15) NOT NULL,
  `bio` varchar(1024) NOT NULL,
  `point` varchar(5) NOT NULL,
  `completeProfile` varchar(5) NOT NULL,
  `location` varchar(50) NOT NULL,
  `messengerUrl` varchar(100) NOT NULL,
  `whatsappUrl` varchar(100) NOT NULL,
  `telegramUrl` varchar(100) NOT NULL,
  `profileImg` varchar(100) DEFAULT NULL,
  `nidFrontImg` varchar(100) DEFAULT NULL,
  `nidBackImg` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_users`
--

INSERT INTO `app_users` (`id`, `name`, `email`, `password`, `phoneNumber`, `bio`, `point`, `completeProfile`, `location`, `messengerUrl`, `whatsappUrl`, `telegramUrl`, `profileImg`, `nidFrontImg`, `nidBackImg`, `created_at`) VALUES
(1, 'Admin', 'admin@gmail.com', 'pbkdf2_sha256$260000$l7crZeHP6EcwU0daTpBS2I$IKc7tUUpPaeN0tc20e+1ZeoeUI39ZtpIPrHclR9IPpE=', '', '', '200', '25%', '', '', '', '', '', '', '', '2022-12-06 09:39:41.489630'),
(2, 'SAHIL AKRAM SHEKH', 'iamsahilsk99@gmail.com', 'pbkdf2_sha256$260000$f0SAAnNZo5qNmvDrZhmOdN$OBHtCeJC1SnJgEK/9G03YWPO6i265WmaasFZDPTlILI=', '7972846137', 'This is sample user account', '300', '100%', 'C/103 Jay Shankar, Sahnivas, zenda Chowk, Mahal, N', 'https://messenger.com/', 'https://web.whatsapp.com/', 'https://telegram.com/', '', '', '', '2022-12-06 09:40:33.797662'),
(3, 'Sahil Lost ', 'me.sahilsk99@gmail.com', 'pbkdf2_sha256$260000$jLEQn90EG1LDLQit4tjurv$Hnk/U5DkhJHSCrsPOsgDtVWQXnPET9BWd8/V4nfmTvE=', '9393939293', 'This is sample user account for lost item', '-50', '100%', 'Nagpur', 'https://messenger.com/', 'https://web.whatsapp.com/', 'https://telegram.com/', '', '', '', '2022-12-06 09:45:17.209204'),
(4, 'Lost Item Account', 'my.kot.app@gmail.com', 'pbkdf2_sha256$260000$W7KOmQ8WfWlncF8fCvmfD5$K4oGKZnr4Wp1YDdDgaxl4ZPFLh47w+Ty5i6B486ibUE=', '7972846137', 'This is sample user account for lost item', '0', '100%', 'C/103 Jay Shankar, Sahnivas, zenda Chowk, Mahal, N', 'https://messenger.com/', 'https://web.whatsapp.com/', 'https://telegram.com/', '', '', '', '2022-12-06 09:46:02.659943'),
(5, 'Demo Demo', 'demo@gmail.com', 'pbkdf2_sha256$260000$MBkHH5FY2pSyHGB5T5veQB$LLyXqNAHSMQ76FOYQQJn4zJ3thRWTQXG/oUyELsknK0=', '', '', '200', '25%', '', '', '', '', '', '', '', '2022-12-06 15:43:04.767228'),
(6, 'Sharu', 'sharu@gmail.com', 'pbkdf2_sha256$260000$jd3XL5bnDwaCUbOxu1ibv0$h3oTC67pz+EhM0P8jxP9vOr8hPaGUV6V6lK8KmBcFtg=', '', '', '200', '25%', '', '', '', '', '', '', '', '2022-12-07 07:22:38.959712');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(25, 'Can add bkash payment', 7, 'add_bkashpayment'),
(26, 'Can change bkash payment', 7, 'change_bkashpayment'),
(27, 'Can delete bkash payment', 7, 'delete_bkashpayment'),
(28, 'Can view bkash payment', 7, 'view_bkashpayment'),
(29, 'Can add claim owner', 8, 'add_claimowner'),
(30, 'Can change claim owner', 8, 'change_claimowner'),
(31, 'Can delete claim owner', 8, 'delete_claimowner'),
(32, 'Can view claim owner', 8, 'view_claimowner'),
(33, 'Can add post model', 9, 'add_postmodel'),
(34, 'Can change post model', 9, 'change_postmodel'),
(35, 'Can delete post model', 9, 'delete_postmodel'),
(36, 'Can view post model', 9, 'view_postmodel'),
(37, 'Can add user contact', 10, 'add_usercontact'),
(38, 'Can change user contact', 10, 'change_usercontact'),
(39, 'Can delete user contact', 10, 'delete_usercontact'),
(40, 'Can view user contact', 10, 'view_usercontact'),
(41, 'Can add user feedback', 11, 'add_userfeedback'),
(42, 'Can change user feedback', 11, 'change_userfeedback'),
(43, 'Can delete user feedback', 11, 'delete_userfeedback'),
(44, 'Can view user feedback', 11, 'view_userfeedback'),
(45, 'Can add user model', 12, 'add_usermodel'),
(46, 'Can change user model', 12, 'change_usermodel'),
(47, 'Can delete user model', 12, 'delete_usermodel'),
(48, 'Can view user model', 12, 'view_usermodel'),
(49, 'Can add reset pwd tokens', 13, 'add_resetpwdtokens'),
(50, 'Can change reset pwd tokens', 13, 'change_resetpwdtokens'),
(51, 'Can delete reset pwd tokens', 13, 'delete_resetpwdtokens'),
(52, 'Can view reset pwd tokens', 13, 'view_resetpwdtokens');

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
-- Table structure for table `bkash_payment`
--

CREATE TABLE `bkash_payment` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `bkashNumber` varchar(20) NOT NULL,
  `bkashTransaction` varchar(512) NOT NULL,
  `point` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `claim_owner`
--

CREATE TABLE `claim_owner` (
  `id` bigint(20) NOT NULL,
  `foundPostId` varchar(20) NOT NULL,
  `foundPostUserName` varchar(50) NOT NULL,
  `foundPostUserEmail` varchar(40) NOT NULL,
  `lostPostId` varchar(20) NOT NULL,
  `lostPostUserEmail` varchar(40) NOT NULL,
  `lostPostUserName` varchar(50) NOT NULL,
  `foundPostImg` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `foundPostUserId` varchar(20) DEFAULT NULL,
  `lostPostImg` varchar(100) DEFAULT NULL,
  `foundPostDescription` varchar(1000) DEFAULT NULL,
  `foundPostTittle` varchar(500) DEFAULT NULL,
  `lostPostDescription` varchar(1000) DEFAULT NULL,
  `lostPostTittle` varchar(500) DEFAULT NULL,
  `lostPostUserId` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `claim_owner`
--

INSERT INTO `claim_owner` (`id`, `foundPostId`, `foundPostUserName`, `foundPostUserEmail`, `lostPostId`, `lostPostUserEmail`, `lostPostUserName`, `foundPostImg`, `created_at`, `foundPostUserId`, `lostPostImg`, `foundPostDescription`, `foundPostTittle`, `lostPostDescription`, `lostPostTittle`, `lostPostUserId`) VALUES
(5, '1', 'SAHIL AKRAM SHEKH', 'iamsahilsk99@gmail.com', '3', 'me.sahilsk99@gmail.com', 'Sahil Lost ', 'uploads/20221206152517-headphone.png', '2022-12-06 15:48:29.011203', '2', 'uploads/20221206153230-headphone.png', 'I have found a pair of headphones in Nagpur, and it has black color, and it is wired headphones and the brand name is boat.', 'Found a Headphone', 'I have lost my headphone brand name is a boat and the headphone color is black.', 'Lost My Headphone', '3');

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
(7, 'home', 'bkashpayment'),
(8, 'home', 'claimowner'),
(9, 'home', 'postmodel'),
(13, 'home', 'resetpwdtokens'),
(10, 'home', 'usercontact'),
(11, 'home', 'userfeedback'),
(12, 'home', 'usermodel'),
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
(1, 'contenttypes', '0001_initial', '2022-12-06 09:37:50.148163'),
(2, 'auth', '0001_initial', '2022-12-06 09:37:50.783876'),
(3, 'admin', '0001_initial', '2022-12-06 09:37:50.922937'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-12-06 09:37:50.934099'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-12-06 09:37:50.944101'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-12-06 09:37:51.016944'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-12-06 09:37:51.063831'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-12-06 09:37:51.087026'),
(9, 'auth', '0004_alter_user_username_opts', '2022-12-06 09:37:51.099533'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-12-06 09:37:51.144137'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-12-06 09:37:51.148135'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-12-06 09:37:51.158133'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-12-06 09:37:51.176702'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-12-06 09:37:51.196251'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-12-06 09:37:51.212769'),
(16, 'auth', '0011_update_proxy_permissions', '2022-12-06 09:37:51.222977'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-12-06 09:37:51.239980'),
(18, 'home', '0001_initial', '2022-12-06 09:37:51.555759'),
(19, 'home', '0002_postmodel_posttype', '2022-12-06 09:37:51.575503'),
(20, 'home', '0003_postmodel_poststatus', '2022-12-06 09:37:51.601037'),
(21, 'home', '0004_claimowner_claimerpostid', '2022-12-06 09:37:51.617827'),
(22, 'sessions', '0001_initial', '2022-12-06 09:37:51.680204'),
(23, 'home', '0005_claimowner_postfileimg', '2022-12-06 10:51:36.131435'),
(24, 'home', '0006_auto_20221206_1632', '2022-12-06 11:03:00.684799');

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
('066kugeu1dh0rkw1x2dgtrbqqi1nd3fl', 'e30:1p2WeU:YXpVQY3qP-XH9RMrazRfZNUMtQg5j8hrua_ki_Y0pW4', '2022-12-20 12:02:22.909651'),
('86827vrmdatq2ykwc9zi3yj0yxoyqexj', 'eyJlbWFpbCI6ImlhbXNhaGlsc2s5OUBnbWFpbC5jb20ifQ:1p2sdn:-UQR661EcBVrRQ2YcqhFioeaXnHBGaK1NXPKDH1oD9A', '2022-12-21 11:31:07.734267');

-- --------------------------------------------------------

--
-- Table structure for table `reset_pwd_tokens`
--

CREATE TABLE `reset_pwd_tokens` (
  `id` bigint(20) NOT NULL,
  `forget_password_token` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reset_pwd_tokens`
--

INSERT INTO `reset_pwd_tokens` (`id`, `forget_password_token`, `created_at`, `user_id`) VALUES
(1, '', '2022-12-06 09:39:41.492628', 1),
(2, '8f3cfa2c-7bcb-4791-80cf-af92e54b1fc4', '2022-12-06 09:40:33.799661', 2),
(3, '', '2022-12-06 09:45:17.213217', 3),
(4, '', '2022-12-06 09:46:02.663954', 4),
(5, '', '2022-12-06 15:43:04.770127', 5),
(6, '', '2022-12-07 07:22:38.962754', 6);

-- --------------------------------------------------------

--
-- Table structure for table `users_contacts`
--

CREATE TABLE `users_contacts` (
  `id` bigint(20) NOT NULL,
  `messengerId` varchar(10) NOT NULL,
  `messengerName` varchar(50) NOT NULL,
  `messengerEmail` varchar(40) NOT NULL,
  `message` varchar(3072) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users_feedbacks`
--

CREATE TABLE `users_feedbacks` (
  `id` bigint(20) NOT NULL,
  `messengerId` varchar(10) NOT NULL,
  `messengerName` varchar(50) NOT NULL,
  `messengerEmail` varchar(40) NOT NULL,
  `message` varchar(3072) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_posts`
--

CREATE TABLE `user_posts` (
  `id` bigint(20) NOT NULL,
  `publisherId` varchar(20) NOT NULL,
  `publisherName` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(3072) NOT NULL,
  `location` varchar(50) NOT NULL,
  `lostDateTime` datetime(6) NOT NULL,
  `fileImg` varchar(100) DEFAULT NULL,
  `fileSecretImg` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `postType` varchar(50) DEFAULT NULL,
  `postStatus` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_posts`
--

INSERT INTO `user_posts` (`id`, `publisherId`, `publisherName`, `title`, `description`, `location`, `lostDateTime`, `fileImg`, `fileSecretImg`, `created_at`, `postType`, `postStatus`) VALUES
(1, '2', 'SAHIL AKRAM SHEKH', 'Found a Headphone', 'I have found a pair of headphones in Nagpur, and it has black color, and it is wired headphones and the brand name is boat.', 'Nagpur', '2022-12-06 15:22:00.000000', 'uploads/20221206152517-headphone.png', 'uploads/20221206152517-headphone_SStZa03.png', '2022-12-06 09:55:17.076882', 'Found', 'Claimed'),
(2, '2', 'SAHIL AKRAM SHEKH', 'Found a Wallet', 'I have found a wallet at Nagpur Itwari road and it consists of the following documents 1. Adhar Card 2 Pan Card.', 'Nagpur', '2022-12-06 15:28:00.000000', 'uploads/20221206152723-wallet.jpg', 'uploads/20221206152723-wallet_pBXUNoV.jpg', '2022-12-06 09:57:23.098686', 'Found', 'Pending'),
(3, '3', 'Sahil Lost ', 'Lost My Headphone', 'I have lost my headphone brand name is a boat and the headphone color is black.', 'Nagpur', '2022-12-06 15:32:00.000000', 'uploads/20221206153230-headphone.png', 'uploads/20221206153230-headphone_1HMOAaU.png', '2022-12-06 10:02:30.701259', 'Lost', 'Claimed'),
(4, '4', 'Lost Item Account', 'Lost My Headphone', 'I have lost my JBL Gaming Headphone.', 'Punjab', '2022-12-05 15:36:00.000000', 'uploads/20221206153458-headphone.jpg', 'uploads/20221206153458-headphone_0lW7OtG.jpg', '2022-12-06 10:04:58.962418', 'Lost', 'Pending');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_users`
--
ALTER TABLE `app_users`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `bkash_payment`
--
ALTER TABLE `bkash_payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `claim_owner`
--
ALTER TABLE `claim_owner`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `reset_pwd_tokens`
--
ALTER TABLE `reset_pwd_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `users_contacts`
--
ALTER TABLE `users_contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_feedbacks`
--
ALTER TABLE `users_feedbacks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_posts`
--
ALTER TABLE `user_posts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_users`
--
ALTER TABLE `app_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bkash_payment`
--
ALTER TABLE `bkash_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `claim_owner`
--
ALTER TABLE `claim_owner`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `reset_pwd_tokens`
--
ALTER TABLE `reset_pwd_tokens`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users_contacts`
--
ALTER TABLE `users_contacts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_feedbacks`
--
ALTER TABLE `users_feedbacks`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_posts`
--
ALTER TABLE `user_posts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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

--
-- Constraints for table `reset_pwd_tokens`
--
ALTER TABLE `reset_pwd_tokens`
  ADD CONSTRAINT `reset_pwd_tokens_user_id_7263e5fc_fk_app_users_id` FOREIGN KEY (`user_id`) REFERENCES `app_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
