-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 192.168.50.30    Database: MonitorCenter
-- ------------------------------------------------------
-- Server version	5.7.29-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `MonitorCenter_metricshostsinfo`
--

DROP TABLE IF EXISTS `MonitorCenter_metricshostsinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MonitorCenter_metricshostsinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `hosts_info_id` bigint(20) NOT NULL,
  `metric_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MonitorCenter_metric_hosts_info_id_f8302c91_fk_hostinfo_` (`hosts_info_id`),
  KEY `MonitorCenter_metricshostsinfo_metric_id_837ef663_fk_metrics_id` (`metric_id`),
  CONSTRAINT `MonitorCenter_metric_hosts_info_id_f8302c91_fk_hostinfo_` FOREIGN KEY (`hosts_info_id`) REFERENCES `hostinfo` (`id`),
  CONSTRAINT `MonitorCenter_metricshostsinfo_metric_id_837ef663_fk_metrics_id` FOREIGN KEY (`metric_id`) REFERENCES `metrics` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MonitorCenter_metricshostsinfo`
--

LOCK TABLES `MonitorCenter_metricshostsinfo` WRITE;
/*!40000 ALTER TABLE `MonitorCenter_metricshostsinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `MonitorCenter_metricshostsinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MonitorCenter_metricsmonitorobject`
--

DROP TABLE IF EXISTS `MonitorCenter_metricsmonitorobject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MonitorCenter_metricsmonitorobject` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `metric_id` bigint(20) NOT NULL,
  `monitor_object_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MonitorCenter_metric_metric_id_611905a4_fk_metrics_i` (`metric_id`),
  KEY `MonitorCenter_metric_monitor_object_id_645fa141_fk_monitorob` (`monitor_object_id`),
  CONSTRAINT `MonitorCenter_metric_metric_id_611905a4_fk_metrics_i` FOREIGN KEY (`metric_id`) REFERENCES `metrics` (`id`),
  CONSTRAINT `MonitorCenter_metric_monitor_object_id_645fa141_fk_monitorob` FOREIGN KEY (`monitor_object_id`) REFERENCES `monitorobject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MonitorCenter_metricsmonitorobject`
--

LOCK TABLES `MonitorCenter_metricsmonitorobject` WRITE;
/*!40000 ALTER TABLE `MonitorCenter_metricsmonitorobject` DISABLE KEYS */;
/*!40000 ALTER TABLE `MonitorCenter_metricsmonitorobject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MonitorCenter_metricssysinfomanage`
--

DROP TABLE IF EXISTS `MonitorCenter_metricssysinfomanage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MonitorCenter_metricssysinfomanage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `metric_id` bigint(20) NOT NULL,
  `sys_info_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MonitorCenter_metric_metric_id_77f5977d_fk_metrics_i` (`metric_id`),
  KEY `MonitorCenter_metric_sys_info_id_725a6d96_fk_sysinfoma` (`sys_info_id`),
  CONSTRAINT `MonitorCenter_metric_metric_id_77f5977d_fk_metrics_i` FOREIGN KEY (`metric_id`) REFERENCES `metrics` (`id`),
  CONSTRAINT `MonitorCenter_metric_sys_info_id_725a6d96_fk_sysinfoma` FOREIGN KEY (`sys_info_id`) REFERENCES `sysinfomanage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MonitorCenter_metricssysinfomanage`
--

LOCK TABLES `MonitorCenter_metricssysinfomanage` WRITE;
/*!40000 ALTER TABLE `MonitorCenter_metricssysinfomanage` DISABLE KEYS */;
INSERT INTO `MonitorCenter_metricssysinfomanage` VALUES (1,4,1);
/*!40000 ALTER TABLE `MonitorCenter_metricssysinfomanage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 系统信息管理',7,'add_sysinfomanage'),(26,'Can change 系统信息管理',7,'change_sysinfomanage'),(27,'Can delete 系统信息管理',7,'delete_sysinfomanage'),(28,'Can view 系统信息管理',7,'view_sysinfomanage'),(29,'Can add 监控对象表',8,'add_monitorobject'),(30,'Can change 监控对象表',8,'change_monitorobject'),(31,'Can delete 监控对象表',8,'delete_monitorobject'),(32,'Can view 监控对象表',8,'view_monitorobject'),(33,'Can add 监控指标表',9,'add_metrics'),(34,'Can change 监控指标表',9,'change_metrics'),(35,'Can delete 监控指标表',9,'delete_metrics'),(36,'Can view 监控指标表',9,'view_metrics'),(37,'Can add 主机IP信息管理',10,'add_hostsinfo'),(38,'Can change 主机IP信息管理',10,'change_hostsinfo'),(39,'Can delete 主机IP信息管理',10,'delete_hostsinfo'),(40,'Can view 主机IP信息管理',10,'view_hostsinfo'),(41,'Can add metrics monitor object',11,'add_metricsmonitorobject'),(42,'Can change metrics monitor object',11,'change_metricsmonitorobject'),(43,'Can delete metrics monitor object',11,'delete_metricsmonitorobject'),(44,'Can view metrics monitor object',11,'view_metricsmonitorobject'),(45,'Can add metrics sys info manage',12,'add_metricssysinfomanage'),(46,'Can change metrics sys info manage',12,'change_metricssysinfomanage'),(47,'Can delete metrics sys info manage',12,'delete_metricssysinfomanage'),(48,'Can view metrics sys info manage',12,'view_metricssysinfomanage'),(49,'Can add metrics hosts info',13,'add_metricshostsinfo'),(50,'Can change metrics hosts info',13,'change_metricshostsinfo'),(51,'Can delete metrics hosts info',13,'delete_metricshostsinfo'),(52,'Can view metrics hosts info',13,'view_metricshostsinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_bin,
  `object_repr` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'MonitorCenter','hostsinfo'),(9,'MonitorCenter','metrics'),(13,'MonitorCenter','metricshostsinfo'),(11,'MonitorCenter','metricsmonitorobject'),(12,'MonitorCenter','metricssysinfomanage'),(8,'MonitorCenter','monitorobject'),(7,'MonitorCenter','sysinfomanage'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-03-24 06:57:24.777705'),(2,'contenttypes','0002_remove_content_type_name','2023-03-24 06:57:25.211170'),(3,'MonitorCenter','0001_initial','2023-03-24 06:57:26.835076'),(4,'auth','0001_initial','2023-03-24 06:57:29.221623'),(5,'admin','0001_initial','2023-03-24 06:57:29.813625'),(6,'admin','0002_logentry_remove_auto_add','2023-03-24 06:57:29.938677'),(7,'admin','0003_logentry_add_action_flag_choices','2023-03-24 06:57:30.079714'),(8,'auth','0002_alter_permission_name_max_length','2023-03-24 06:57:30.286799'),(9,'auth','0003_alter_user_email_max_length','2023-03-24 06:57:30.485773'),(10,'auth','0004_alter_user_username_opts','2023-03-24 06:57:30.618962'),(11,'auth','0005_alter_user_last_login_null','2023-03-24 06:57:30.817993'),(12,'auth','0006_require_contenttypes_0002','2023-03-24 06:57:30.934647'),(13,'auth','0007_alter_validators_add_error_messages','2023-03-24 06:57:31.060958'),(14,'auth','0008_alter_user_username_max_length','2023-03-24 06:57:31.290003'),(15,'auth','0009_alter_user_last_name_max_length','2023-03-24 06:57:31.540255'),(16,'auth','0010_alter_group_name_max_length','2023-03-24 06:57:31.769287'),(17,'auth','0011_update_proxy_permissions','2023-03-24 06:57:32.081824'),(18,'auth','0012_alter_user_first_name_max_length','2023-03-24 06:57:32.277450'),(19,'sessions','0001_initial','2023-03-24 06:57:32.608616'),(20,'MonitorCenter','0002_monitorobject_is_deleted_and_more','2023-03-24 08:39:15.246174'),(21,'MonitorCenter','0003_remove_hostsinfo_sys_id_and_more','2023-03-26 19:27:04.201632'),(22,'MonitorCenter','0004_hostsinfo_is_deleted','2023-03-26 20:06:27.456218'),(23,'MonitorCenter','0005_remove_metrics_metrics_sys_and_more','2023-03-26 23:22:39.839305'),(24,'MonitorCenter','0006_metrics_is_deleted','2023-03-27 00:00:27.085644');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb4_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostinfo`
--

DROP TABLE IF EXISTS `hostinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `obj_id_id` bigint(20) NOT NULL,
  `sysinfo_content_type_id` int(11) NOT NULL,
  `sysinfo_object_id` int(10) unsigned NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hostinfo_obj_id_id_c8e00a12_fk_monitorobject_id` (`obj_id_id`),
  KEY `hostinfo_sysinfo_content_type_af2bcab5_fk_django_co` (`sysinfo_content_type_id`),
  CONSTRAINT `hostinfo_obj_id_id_c8e00a12_fk_monitorobject_id` FOREIGN KEY (`obj_id_id`) REFERENCES `monitorobject` (`id`),
  CONSTRAINT `hostinfo_sysinfo_content_type_af2bcab5_fk_django_co` FOREIGN KEY (`sysinfo_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostinfo`
--

LOCK TABLES `hostinfo` WRITE;
/*!40000 ALTER TABLE `hostinfo` DISABLE KEYS */;
INSERT INTO `hostinfo` VALUES (1,'192.168.50.25','2023-03-26 20:06:35.882284','2023-03-26 20:06:35.882284',2,1,1,0),(2,'192.168.50.23','2023-03-26 20:08:43.883636','2023-03-27 02:06:11.124307',4,1,1,1),(3,'192.168.50.12','2023-03-26 20:58:19.783325','2023-03-26 20:58:19.783325',3,1,1,0),(4,'192.168.50.125','2023-03-27 02:05:24.542692','2023-03-27 02:05:24.542692',2,1,1,0);
/*!40000 ALTER TABLE `hostinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `metrics`
--

DROP TABLE IF EXISTS `metrics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `metrics` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `metric_ID` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `metric_name` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `metric_type` smallint(6) NOT NULL,
  `metric_desc` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `Threshold` int(11) NOT NULL,
  `metric_unit` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `collect_type` smallint(6) NOT NULL,
  `trigger_rule` varchar(256) COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `metric_ID` (`metric_ID`),
  UNIQUE KEY `metric_name` (`metric_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metrics`
--

LOCK TABLES `metrics` WRITE;
/*!40000 ALTER TABLE `metrics` DISABLE KEYS */;
INSERT INTO `metrics` VALUES (1,'BCLinux-003','CPU Usage',0,'CPU使用率',90,'%',0,'greater','2023-03-26 23:38:04.483740','2023-03-26 23:38:04.483740',1),(2,'MEM Usage','内存使用率',0,'检查系统内磁盘的使用率',80,'%',0,'greater','2023-03-26 23:51:31.399207','2023-03-27 01:58:40.870961',1),(3,'DISK Usage','磁盘使用率',0,'检查系统磁盘使用率，一般默认80%以上告警',90,'%',0,'greater','2023-03-27 02:03:33.968485','2023-03-27 02:03:33.968485',0),(4,'CPU Usage','CPU使用率',0,'The usage of CPU for BCLinux-001 server',80,'%',0,'greater','2023-03-27 06:18:04.062159','2023-03-27 06:18:04.062159',0);
/*!40000 ALTER TABLE `metrics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitorobject`
--

DROP TABLE IF EXISTS `monitorobject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monitorobject` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sysinfo_object_id` int(10) unsigned NOT NULL,
  `object_type` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `object_name` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `sysinfo_content_type_id` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `monitorobject_sysinfo_content_type_c551fa66_fk_django_co` (`sysinfo_content_type_id`),
  CONSTRAINT `monitorobject_sysinfo_content_type_c551fa66_fk_django_co` FOREIGN KEY (`sysinfo_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitorobject`
--

LOCK TABLES `monitorobject` WRITE;
/*!40000 ALTER TABLE `monitorobject` DISABLE KEYS */;
INSERT INTO `monitorobject` VALUES (2,1,'container','checkcode-auth','2023-03-24 08:36:50.399225','2023-03-27 02:11:27.264886',7,0),(3,1,'container','checkcode-auth','2023-03-24 08:36:59.623715','2023-03-24 08:36:59.623715',7,0),(4,1,'container','checkcode-auth','2023-03-24 08:37:15.079023','2023-03-24 08:37:15.079023',7,0),(5,1,'container','checkcode-javac','2023-03-27 02:13:52.463008','2023-03-27 02:13:52.463008',7,0);
/*!40000 ALTER TABLE `monitorobject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sysinfomanage`
--

DROP TABLE IF EXISTS `sysinfomanage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sysinfomanage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Sys_name` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `Sys_abbreviation` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `Sys_level` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `Sys_dev_pricipal` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  `Sys_ops_pricipal` varchar(32) COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sysinfomanage_Sys_abbreviation_8a58283b_uniq` (`Sys_abbreviation`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sysinfomanage`
--

LOCK TABLES `sysinfomanage` WRITE;
/*!40000 ALTER TABLE `sysinfomanage` DISABLE KEYS */;
INSERT INTO `sysinfomanage` VALUES (1,'流水线','pipeline','third_level_layer','肖丹','翰林','2023-03-24 07:05:46.694525','2023-03-27 02:16:46.182791'),(2,'代码检查','codechecks','third_level_layer','小明','李华','2023-03-24 07:05:57.360223','2023-03-24 07:05:57.360223'),(3,'制品库','cpack','third_level_layer','贤国','钧韦','2023-03-27 02:15:47.379394','2023-03-27 02:15:47.379394');
/*!40000 ALTER TABLE `sysinfomanage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'MonitorCenter'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27 16:01:10
