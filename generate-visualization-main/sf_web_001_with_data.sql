/*
 Navicat Premium Data Transfer

 Source Server         : host
 Source Server Type    : MySQL
 Source Server Version : 80041 (8.0.41)
 Source Host           : localhost:3306
 Source Schema         : sf_web_001

 Target Server Type    : MySQL
 Target Server Version : 80041 (8.0.41)
 File Encoding         : 65001

 Date: 30/07/2025 00:54:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for abnormal_card
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_card`;
CREATE TABLE `abnormal_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_card
-- ----------------------------

-- ----------------------------
-- Table structure for abnormal_f_t
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_f_t`;
CREATE TABLE `abnormal_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for abnormal_relative
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_relative`;
CREATE TABLE `abnormal_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_relative
-- ----------------------------

-- ----------------------------
-- Table structure for abnormal_store
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_store`;
CREATE TABLE `abnormal_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_store
-- ----------------------------

-- ----------------------------
-- Table structure for abnormal_trans
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_trans`;
CREATE TABLE `abnormal_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_trans
-- ----------------------------

-- ----------------------------
-- Table structure for abnormal_user
-- ----------------------------
DROP TABLE IF EXISTS `abnormal_user`;
CREATE TABLE `abnormal_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of abnormal_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add card', 7, 'add_card');
INSERT INTO `auth_permission` VALUES (26, 'Can change card', 7, 'change_card');
INSERT INTO `auth_permission` VALUES (27, 'Can delete card', 7, 'delete_card');
INSERT INTO `auth_permission` VALUES (28, 'Can view card', 7, 'view_card');
INSERT INTO `auth_permission` VALUES (29, 'Can add ft', 8, 'add_ft');
INSERT INTO `auth_permission` VALUES (30, 'Can change ft', 8, 'change_ft');
INSERT INTO `auth_permission` VALUES (31, 'Can delete ft', 8, 'delete_ft');
INSERT INTO `auth_permission` VALUES (32, 'Can view ft', 8, 'view_ft');
INSERT INTO `auth_permission` VALUES (33, 'Can add store', 9, 'add_store');
INSERT INTO `auth_permission` VALUES (34, 'Can change store', 9, 'change_store');
INSERT INTO `auth_permission` VALUES (35, 'Can delete store', 9, 'delete_store');
INSERT INTO `auth_permission` VALUES (36, 'Can view store', 9, 'view_store');
INSERT INTO `auth_permission` VALUES (37, 'Can add supermarket', 10, 'add_supermarket');
INSERT INTO `auth_permission` VALUES (38, 'Can change supermarket', 10, 'change_supermarket');
INSERT INTO `auth_permission` VALUES (39, 'Can delete supermarket', 10, 'delete_supermarket');
INSERT INTO `auth_permission` VALUES (40, 'Can view supermarket', 10, 'view_supermarket');
INSERT INTO `auth_permission` VALUES (41, 'Can add trans', 11, 'add_trans');
INSERT INTO `auth_permission` VALUES (42, 'Can change trans', 11, 'change_trans');
INSERT INTO `auth_permission` VALUES (43, 'Can delete trans', 11, 'delete_trans');
INSERT INTO `auth_permission` VALUES (44, 'Can view trans', 11, 'view_trans');
INSERT INTO `auth_permission` VALUES (45, 'Can add user', 12, 'add_user');
INSERT INTO `auth_permission` VALUES (46, 'Can change user', 12, 'change_user');
INSERT INTO `auth_permission` VALUES (47, 'Can delete user', 12, 'delete_user');
INSERT INTO `auth_permission` VALUES (48, 'Can view user', 12, 'view_user');
INSERT INTO `auth_permission` VALUES (49, 'Can add login', 13, 'add_login');
INSERT INTO `auth_permission` VALUES (50, 'Can change login', 13, 'change_login');
INSERT INTO `auth_permission` VALUES (51, 'Can delete login', 13, 'delete_login');
INSERT INTO `auth_permission` VALUES (52, 'Can view login', 13, 'view_login');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `email` varchar(254) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for card
-- ----------------------------
DROP TABLE IF EXISTS `card`;
CREATE TABLE `card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card_id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner_type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner_id',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is_abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal_type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 888 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for credit_card
-- ----------------------------
DROP TABLE IF EXISTS `credit_card`;
CREATE TABLE `credit_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_card
-- ----------------------------

-- ----------------------------
-- Table structure for credit_f_t
-- ----------------------------
DROP TABLE IF EXISTS `credit_f_t`;
CREATE TABLE `credit_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for credit_relative
-- ----------------------------
DROP TABLE IF EXISTS `credit_relative`;
CREATE TABLE `credit_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_relative
-- ----------------------------

-- ----------------------------
-- Table structure for credit_store
-- ----------------------------
DROP TABLE IF EXISTS `credit_store`;
CREATE TABLE `credit_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_store
-- ----------------------------

-- ----------------------------
-- Table structure for credit_trans
-- ----------------------------
DROP TABLE IF EXISTS `credit_trans`;
CREATE TABLE `credit_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_trans
-- ----------------------------

-- ----------------------------
-- Table structure for credit_user
-- ----------------------------
DROP TABLE IF EXISTS `credit_user`;
CREATE TABLE `credit_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_user
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NULL,
  `object_repr` varchar(200) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `model` varchar(100) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (7, 'app01', 'card');
INSERT INTO `django_content_type` VALUES (8, 'app01', 'ft');
INSERT INTO `django_content_type` VALUES (13, 'app01', 'login');
INSERT INTO `django_content_type` VALUES (9, 'app01', 'store');
INSERT INTO `django_content_type` VALUES (10, 'app01', 'supermarket');
INSERT INTO `django_content_type` VALUES (11, 'app01', 'trans');
INSERT INTO `django_content_type` VALUES (12, 'app01', 'user');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `name` varchar(255) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-10-12 16:05:44.929078');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2022-10-12 16:05:45.560167');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2022-10-12 16:05:45.815962');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-10-12 16:05:45.825529');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-12 16:05:45.839466');
INSERT INTO `django_migrations` VALUES (6, 'app01', '0001_initial', '2022-10-26 01:25:56.016615');
INSERT INTO `django_migrations` VALUES (7, 'app01', '0002_login', '2022-10-26 01:25:56.025299');
INSERT INTO `django_migrations` VALUES (8, 'contenttypes', '0002_remove_content_type_name', '2022-10-26 01:25:56.223412');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0002_alter_permission_name_max_length', '2022-10-26 01:25:56.329554');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0003_alter_user_email_max_length', '2022-10-26 01:25:56.374370');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0004_alter_user_username_opts', '2022-10-26 01:25:56.388198');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0005_alter_user_last_login_null', '2022-10-26 01:25:56.479677');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0006_require_contenttypes_0002', '2022-10-26 01:25:56.484541');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0007_alter_validators_add_error_messages', '2022-10-26 01:25:56.495770');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0008_alter_user_username_max_length', '2022-10-26 01:25:56.593338');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0009_alter_user_last_name_max_length', '2022-10-26 01:25:56.692010');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0010_alter_group_name_max_length', '2022-10-26 01:25:56.726185');
INSERT INTO `django_migrations` VALUES (18, 'auth', '0011_update_proxy_permissions', '2022-10-26 01:25:56.745129');
INSERT INTO `django_migrations` VALUES (19, 'auth', '0012_alter_user_first_name_max_length', '2022-10-26 01:25:56.856606');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2022-10-26 01:25:56.918622');
INSERT INTO `django_migrations` VALUES (21, 'app01', '0003_delete_supermarket_alter_user_options', '2022-10-26 01:27:49.053985');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `session_data` longtext CHARACTER SET gb18030 COLLATE gb18030_chinese_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gb18030 COLLATE = gb18030_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('ap2qqxez3d1rxwn0cd34kvuxv19sxtrg', 'eyJ1c2VybmFtZSI6ImVkaXRvciJ9:1tCHjx:lJUPiystBFYnlmP6FrWXWbo1Xq27sYYtBzQrtvtFQ8k', '2024-11-30 20:17:25.133587');
INSERT INTO `django_session` VALUES ('gvvwqrgkcjokmsxtts1dlxyvlklgar6s', 'eyJ1c2VybmFtZSI6ImVkaXRvciJ9:1ugmjv:JSoN3cyyCGYQEU2n_mgq9EPa9jHQYXtoEEnwM61clP8', '2025-08-12 23:59:43.894241');
INSERT INTO `django_session` VALUES ('jjnea7d5dozyo3nx13by8xeym56eju8q', 'eyJ1c2VybmFtZSI6ImFkbWluIn0:1tCJYJ:cb5uRoJ2P2xFR3_KbPQ1LFTCXp5xZ7KjP5IJp_s_pNA', '2024-11-30 22:13:31.596603');
INSERT INTO `django_session` VALUES ('yiwb5asps3cqqwh6vtrrz3nx1hdsl7hm', 'eyJ1c2VybmFtZSI6ImVkaXRvciJ9:1tGqLG:MEGymJV8I03VaNNz50GGN8R0ilXzFUbaA0tY3Ich6Ak', '2024-12-13 10:02:46.798575');

-- ----------------------------
-- Table structure for f_t
-- ----------------------------
DROP TABLE IF EXISTS `f_t`;
CREATE TABLE `f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id_key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 163 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of f_t
-- ----------------------------
INSERT INTO `f_t` VALUES (1, '00022930532894791949683', '9r6hlpz2s4mky', '00020000', '00020000', '648899996944', '628553', '00', '02', '01', 43.00, 43.00, '20221018', '042900', '20221018', '032', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018042900', '01', '0', '00000000', '33140015', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 43.00, '001', 43.00, 6.42, '26966185', '156600951958', '7480519026', '6806592833156066', '0', 43.00, '001');
INSERT INTO `f_t` VALUES (2, '00044955579720943269227', '9r6hlpz2s4mky', '00020000', '00020000', '741454607956', '821430', '00', '02', '03', 944.00, 944.00, '20221018', '044200', '20221018', '130', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018044200', '01', '0', '00000000', '68932385', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 944.00, '001', 944.00, 140.98, '28872011', '586476119403', '4812771318', '8067075401170048', '0', 944.00, '001');
INSERT INTO `f_t` VALUES (3, '00088259644140025834274', '9r6hlpz2s4mky', '00020000', '00020000', '592574508189', '663272', '00', '02', '01', 965.00, 965.00, '20221018', '045300', '20221018', '012', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018045300', '01', '0', '00000000', '49218326', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 965.00, '001', 965.00, 144.12, '72099470', '197216685663', '3469209892', '8559728593235676', '0', 965.00, '001');
INSERT INTO `f_t` VALUES (4, '00027792802016983108809', '9r6hlpz2s4mky', '00020000', '00020000', '555232382707', '595697', '00', '02', '03', 956.00, 956.00, '20221018', '045800', '20221018', '131', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018045800', '01', '0', '00000000', '63291436', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 956.00, '001', 956.00, 142.78, '72239563', '985739901437', '2820727627', '0018190870715262', '0', 956.00, '001');
INSERT INTO `f_t` VALUES (5, '00091791392761250145124', '9r6hlpz2s4mky', '00020000', '00020000', '133423524562', '714641', '00', '02', '03', 973.00, 973.00, '20221018', '050500', '20221018', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018050500', '01', '0', '00000000', '80102192', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 973.00, '001', 973.00, 145.31, '49765228', '749278896788', '5256531956', '4669656462776212', '0', 973.00, '001');
INSERT INTO `f_t` VALUES (6, '00040435307644332518044', '9r6hlpz2s4mky', '00020000', '00020000', '471000318684', '296315', '00', '02', '01', 959.00, 959.00, '20221018', '052000', '20221018', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018052000', '01', '0', '00000000', '00227519', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 959.00, '001', 959.00, 143.22, '97782499', '363271024752', '4751286531', '6359694465303811', '0', 959.00, '001');
INSERT INTO `f_t` VALUES (7, '00096337423833842258570', 'mjghauldyrw0b', '00020002', '00020002', '163625236888', '169921', '00', '02', '07', 84.00, 84.00, '20221018', '010400', '20221018', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018010400', '01', '0', '00000000', '86420653', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 84.00, '001', 84.00, 12.55, '21678924', '515031782520', '0786257791', '1258971504533609', '0', 84.00, '001');
INSERT INTO `f_t` VALUES (8, '00059911284500624653931', 'mjghauldyrw0b', '00020002', '00020002', '315120603018', '707990', '00', '02', '03', 965.00, 965.00, '20221018', '012400', '20221018', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018012400', '01', '0', '00000000', '02315720', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 965.00, '001', 965.00, 144.12, '17049907', '993615552645', '8390486983', '2135128736363333', '0', 965.00, '001');
INSERT INTO `f_t` VALUES (9, '00093204480556035524793', 'mjghauldyrw0b', '00020002', '00020002', '334715344213', '951668', '00', '02', '01', 992.00, 992.00, '20221018', '014100', '20221018', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018014100', '01', '0', '00000000', '64878637', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 992.00, '001', 992.00, 148.15, '12332302', '233654926023', '7064839434', '7385810804318737', '0', 992.00, '001');
INSERT INTO `f_t` VALUES (10, '00093806976999542418941', 'mjghauldyrw0b', '00020002', '00020002', '974113891413', '884261', '00', '02', '07', 937.00, 937.00, '20221018', '014800', '20221018', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018014800', '01', '0', '00000000', '22998125', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 937.00, '001', 937.00, 139.94, '38397882', '695845679876', '7804567265', '1222215985278050', '0', 937.00, '001');
INSERT INTO `f_t` VALUES (11, '00038493031081604463746', 'mjghauldyrw0b', '00020002', '00020002', '539530299103', '443148', '00', '02', '01', 935.00, 935.00, '20221018', '020600', '20221018', '071', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018020600', '01', '0', '00000000', '60835470', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 935.00, '001', 935.00, 139.64, '42431711', '867684765147', '1406759445', '5770801101528987', '0', 935.00, '001');
INSERT INTO `f_t` VALUES (12, '00054792486365267225994', 'mjghauldyrw0b', '00020002', '00020002', '591426385236', '646526', '00', '02', '01', 986.00, 986.00, '20221018', '022500', '20221018', '122', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018022500', '01', '0', '00000000', '75077239', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 986.00, '001', 986.00, 147.26, '62821099', '971728306101', '6622460730', '6971034261847403', '0', 986.00, '001');
INSERT INTO `f_t` VALUES (13, '00074456573673498438348', 'd9cw25beugyfn', '00030002', '00030002', '274085485886', '580938', '00', '02', '03', 57.00, 57.00, '20221018', '042600', '20221018', '120', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018042600', '01', '0', '00000000', '59627228', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 57.00, '001', 57.00, 8.51, '41747284', '992315438100', '8161663490', '8804754878130790', '0', 57.00, '001');
INSERT INTO `f_t` VALUES (14, '00019304262020748051130', 'd9cw25beugyfn', '00030002', '00030002', '110400960685', '141917', '00', '02', '07', 926.00, 926.00, '20221018', '043700', '20221018', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018043700', '01', '0', '00000000', '64686169', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 926.00, '001', 926.00, 138.30, '65181926', '238704179290', '2403588802', '3380228974679644', '0', 926.00, '001');
INSERT INTO `f_t` VALUES (15, '00012511482608723916378', 'd9cw25beugyfn', '00030002', '00030002', '371136866588', '352838', '00', '02', '01', 972.00, 972.00, '20221018', '044300', '20221018', '001', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018044300', '01', '0', '00000000', '26446885', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 972.00, '001', 972.00, 145.17, '01471590', '922351933752', '7807204069', '3251090069013690', '0', 972.00, '001');
INSERT INTO `f_t` VALUES (16, '00092936195445018078470', 'd9cw25beugyfn', '00030002', '00030002', '941218723892', '222773', '00', '02', '07', 930.00, 930.00, '20221018', '044600', '20221018', '002', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018044600', '01', '0', '00000000', '17663787', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 930.00, '001', 930.00, 138.89, '39033960', '754936619909', '7632649619', '1500970664915769', '0', 930.00, '001');
INSERT INTO `f_t` VALUES (17, '00002391608159309721587', 'd9cw25beugyfn', '00030002', '00030002', '222492959070', '740965', '00', '02', '01', 903.00, 903.00, '20221018', '045400', '20221018', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018045400', '01', '0', '00000000', '72546111', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 903.00, '001', 903.00, 134.86, '06432657', '042361113356', '9662443855', '2683941462625061', '0', 903.00, '001');
INSERT INTO `f_t` VALUES (18, '00012656570302991071084', 'd9cw25beugyfn', '00030002', '00030002', '960846876876', '803398', '00', '02', '01', 901.00, 901.00, '20221018', '050300', '20221018', '030', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018050300', '01', '0', '00000000', '95385814', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 901.00, '001', 901.00, 134.56, '21146663', '229254248547', '4453194690', '4700657559097454', '0', 901.00, '001');
INSERT INTO `f_t` VALUES (19, '00079463976102314715194', 'j9gezk82wcxiv', '00030001', '00030001', '115993394179', '867994', '00', '02', '03', 65.00, 65.00, '20221018', '033100', '20221018', '152', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018033100', '01', '0', '00000000', '89433007', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 65.00, '001', 65.00, 9.71, '33029163', '810471632841', '3479923929', '9376841314979246', '0', 65.00, '001');
INSERT INTO `f_t` VALUES (20, '00075480034512212032860', 'j9gezk82wcxiv', '00030001', '00030001', '607458010630', '201263', '00', '02', '07', 976.00, 976.00, '20221018', '033600', '20221018', '020', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018033600', '01', '0', '00000000', '09942332', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 976.00, '001', 976.00, 145.76, '93004190', '959257811953', '1548835956', '9592645063144348', '0', 976.00, '001');
INSERT INTO `f_t` VALUES (21, '00046875244415131266454', 'j9gezk82wcxiv', '00030001', '00030001', '785019340217', '684703', '00', '02', '01', 990.00, 990.00, '20221018', '034800', '20221018', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018034800', '01', '0', '00000000', '06908298', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 990.00, '001', 990.00, 147.85, '91122142', '848872600507', '9771924442', '6346690108455986', '0', 990.00, '001');
INSERT INTO `f_t` VALUES (22, '00000636619324515527232', 'j9gezk82wcxiv', '00030001', '00030001', '712872096925', '562198', '00', '02', '07', 923.00, 923.00, '20221018', '035600', '20221018', '002', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018035600', '01', '0', '00000000', '67213156', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 923.00, '001', 923.00, 137.85, '88655726', '723720021967', '7736167301', '7434653988742752', '0', 923.00, '001');
INSERT INTO `f_t` VALUES (23, '00034034638736900823479', 'j9gezk82wcxiv', '00030001', '00030001', '035254124810', '573579', '00', '02', '07', 921.00, 921.00, '20221018', '041000', '20221018', '112', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018041000', '01', '0', '00000000', '57300521', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 921.00, '001', 921.00, 137.55, '19616042', '921859482758', '2740689487', '8664514875162166', '0', 921.00, '001');
INSERT INTO `f_t` VALUES (24, '00064118849732033410953', 'j9gezk82wcxiv', '00030001', '00030001', '365080367527', '304883', '00', '02', '03', 938.00, 938.00, '20221018', '041800', '20221018', '011', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018041800', '01', '0', '00000000', '10875076', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 938.00, '001', 938.00, 140.09, '19257620', '604947661322', '3071491374', '1099937195791618', '0', 938.00, '001');
INSERT INTO `f_t` VALUES (25, '00050408876546948083237', '9gnfzqobaj8wd', '00030001', '00030001', '571589531603', '393854', '00', '02', '03', 22.00, 22.00, '20221018', '062900', '20221018', '030', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018062900', '01', '0', '00000000', '92100507', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 22.00, '001', 22.00, 3.29, '96789433', '543969956277', '9149186163', '4307442900314824', '0', 22.00, '001');
INSERT INTO `f_t` VALUES (26, '00070841385650779605798', '9gnfzqobaj8wd', '00030001', '00030001', '483893468904', '433284', '00', '02', '07', 932.00, 932.00, '20221018', '064100', '20221018', '012', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018064100', '01', '0', '00000000', '58439775', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 932.00, '001', 932.00, 139.19, '06450508', '951117116128', '4580157270', '5316338124736673', '0', 932.00, '001');
INSERT INTO `f_t` VALUES (27, '00035097456554456281785', '9gnfzqobaj8wd', '00030001', '00030001', '059869657187', '207633', '00', '02', '01', 982.00, 982.00, '20221018', '065400', '20221018', '140', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018065400', '01', '0', '00000000', '11159552', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 982.00, '001', 982.00, 146.66, '88174679', '799791067800', '2334436916', '8102764952852851', '0', 982.00, '001');
INSERT INTO `f_t` VALUES (28, '00059573815922095818544', '9gnfzqobaj8wd', '00030001', '00030001', '629714718159', '839466', '00', '02', '01', 912.00, 912.00, '20221018', '070700', '20221018', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018070700', '01', '0', '00000000', '58644176', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 912.00, '001', 912.00, 136.20, '19744996', '094153486654', '5240034627', '7740702259299062', '0', 912.00, '001');
INSERT INTO `f_t` VALUES (29, '00042794870191533189398', '9gnfzqobaj8wd', '00030001', '00030001', '400772677357', '952904', '00', '02', '07', 994.00, 994.00, '20221018', '072500', '20221018', '030', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018072500', '01', '0', '00000000', '75042081', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 994.00, '001', 994.00, 148.45, '16331382', '960530841227', '8849349070', '4078753831085147', '0', 994.00, '001');
INSERT INTO `f_t` VALUES (30, '00098947079572918877180', '9gnfzqobaj8wd', '00030001', '00030001', '895955333837', '744252', '00', '02', '01', 992.00, 992.00, '20221018', '072600', '20221018', '050', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018072600', '01', '0', '00000000', '32883584', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 992.00, '001', 992.00, 148.15, '94830721', '828628037263', '6403113589', '2431828294406531', '0', 992.00, '001');
INSERT INTO `f_t` VALUES (31, '00039438341952698556118', 'bujfds7m3wngr', '00010002', '00010002', '988602985690', '346268', '00', '02', '01', 94.00, 94.00, '20221018', '033200', '20221018', '050', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018033200', '01', '0', '00000000', '68067726', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 94.00, '001', 94.00, 14.04, '26343112', '929638838876', '1228387861', '9861396975518909', '0', 94.00, '001');
INSERT INTO `f_t` VALUES (32, '00013512524244741372396', 'bujfds7m3wngr', '00010002', '00010002', '903128076019', '529654', '00', '02', '01', 954.00, 954.00, '20221018', '033700', '20221018', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018033700', '01', '0', '00000000', '46707448', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 954.00, '001', 954.00, 142.48, '44409539', '715506951703', '5392939565', '4701185534938995', '0', 954.00, '001');
INSERT INTO `f_t` VALUES (33, '00060167022963738540060', 'bujfds7m3wngr', '00010002', '00010002', '344610208739', '090147', '00', '02', '03', 900.00, 900.00, '20221018', '034100', '20221018', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018034100', '01', '0', '00000000', '68056653', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 900.00, '001', 900.00, 134.41, '66804151', '431606490712', '0144856530', '5427558426530363', '0', 900.00, '001');
INSERT INTO `f_t` VALUES (34, '00059654815250989273634', 'bujfds7m3wngr', '00010002', '00010002', '049903994922', '809570', '00', '02', '03', 978.00, 978.00, '20221018', '034200', '20221018', '050', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018034200', '01', '0', '00000000', '07876372', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 978.00, '001', 978.00, 146.06, '21556630', '975836516726', '4001635214', '3103532080184696', '0', 978.00, '001');
INSERT INTO `f_t` VALUES (35, '00015882325468723403971', 'bujfds7m3wngr', '00010002', '00010002', '980448582220', '644041', '00', '02', '07', 917.00, 917.00, '20221018', '035000', '20221018', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018035000', '01', '0', '00000000', '97913361', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 917.00, '001', 917.00, 136.95, '22003938', '411542932599', '6817555873', '3083826975739923', '0', 917.00, '001');
INSERT INTO `f_t` VALUES (36, '00031701900316600452413', 'bujfds7m3wngr', '00010002', '00010002', '183357212907', '054453', '00', '02', '07', 923.00, 923.00, '20221018', '035800', '20221018', '011', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018035800', '01', '0', '00000000', '95330003', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 923.00, '001', 923.00, 137.85, '89577475', '985630286161', '2807173820', '6122909032813792', '0', 923.00, '001');
INSERT INTO `f_t` VALUES (37, '00005480318711939409780', 'd0ioh3s9ufwnl', '00010001', '00010001', '421387316609', '056854', '00', '02', '07', 96.00, 96.00, '20221017', '053400', '20221017', '032', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017053400', '01', '0', '00000000', '90927837', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 96.00, '001', 96.00, 14.34, '28321682', '927909539384', '9499724690', '0540094479582069', '0', 96.00, '001');
INSERT INTO `f_t` VALUES (38, '00039108198009537901080', 'd0ioh3s9ufwnl', '00010001', '00010001', '018805684955', '937812', '00', '02', '07', 952.00, 952.00, '20221017', '055400', '20221017', '020', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017055400', '01', '0', '00000000', '07968597', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 952.00, '001', 952.00, 142.18, '33464401', '116683717326', '7455448064', '3645418968507590', '0', 952.00, '001');
INSERT INTO `f_t` VALUES (39, '00034279288058654655864', 'd0ioh3s9ufwnl', '00010001', '00010001', '919325353524', '424221', '00', '02', '07', 964.00, 964.00, '20221017', '060700', '20221017', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017060700', '01', '0', '00000000', '48954399', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 964.00, '001', 964.00, 143.97, '48885635', '785694528105', '0782006197', '9907973193581959', '0', 964.00, '001');
INSERT INTO `f_t` VALUES (40, '00080053979818060100184', 'd0ioh3s9ufwnl', '00010001', '00010001', '718969196567', '761559', '00', '02', '07', 950.00, 950.00, '20221017', '061500', '20221017', '101', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017061500', '01', '0', '00000000', '79849704', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 950.00, '001', 950.00, 141.88, '90855859', '185075860096', '6359763253', '5919823425317325', '0', 950.00, '001');
INSERT INTO `f_t` VALUES (41, '00014375237416053863240', 'd0ioh3s9ufwnl', '00010001', '00010001', '629882731176', '106045', '00', '02', '07', 926.00, 926.00, '20221017', '062200', '20221017', '110', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017062200', '01', '0', '00000000', '30805030', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 926.00, '001', 926.00, 138.30, '06005428', '756088962879', '8061992054', '5576583215268172', '0', 926.00, '001');
INSERT INTO `f_t` VALUES (42, '00041282795172913799024', 'd0ioh3s9ufwnl', '00010001', '00010001', '784619801387', '884271', '00', '02', '01', 917.00, 917.00, '20221017', '063300', '20221017', '042', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017063300', '01', '0', '00000000', '01464879', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 917.00, '001', 917.00, 136.95, '98079843', '847957075960', '0853487102', '6025414762788443', '0', 917.00, '001');
INSERT INTO `f_t` VALUES (43, '00063583772434945198924', '6aetn0i214l9g', '00010001', '00010001', '122497924868', '138489', '00', '02', '07', 49.00, 49.00, '20221016', '224200', '20221016', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016224200', '01', '0', '00000000', '06968645', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 49.00, '001', 49.00, 7.32, '27738069', '034384085484', '8506950825', '9878815401106407', '0', 49.00, '001');
INSERT INTO `f_t` VALUES (44, '00025868851500450449681', '6aetn0i214l9g', '00010001', '00010001', '813310049068', '585848', '00', '02', '01', 990.00, 990.00, '20221016', '225700', '20221016', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016225700', '01', '0', '00000000', '68310703', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 990.00, '001', 990.00, 147.85, '19572069', '548336754239', '5780934326', '8246268611879211', '0', 990.00, '001');
INSERT INTO `f_t` VALUES (45, '00093961373839098499066', '6aetn0i214l9g', '00010001', '00010001', '951803395607', '798047', '00', '02', '01', 963.00, 963.00, '20221016', '230500', '20221016', '040', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016230500', '01', '0', '00000000', '52535640', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 963.00, '001', 963.00, 143.82, '01275421', '580867099726', '4986243267', '3447920614611537', '0', 963.00, '001');
INSERT INTO `f_t` VALUES (46, '00022000069868864874343', '6aetn0i214l9g', '00010001', '00010001', '832334263609', '852400', '00', '02', '01', 937.00, 937.00, '20221016', '231700', '20221016', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016231700', '01', '0', '00000000', '28899486', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 937.00, '001', 937.00, 139.94, '49598093', '324862605054', '7594100177', '3550832928514859', '0', 937.00, '001');
INSERT INTO `f_t` VALUES (47, '00045564278785390663421', '6aetn0i214l9g', '00010001', '00010001', '035492473628', '608203', '00', '02', '03', 928.00, 928.00, '20221016', '232400', '20221016', '012', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016232400', '01', '0', '00000000', '98360354', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 928.00, '001', 928.00, 138.59, '11812815', '404560144286', '5657025521', '3762906759655542', '0', 928.00, '001');
INSERT INTO `f_t` VALUES (48, '00013209324234445303947', '6aetn0i214l9g', '00010001', '00010001', '741165236726', '506051', '00', '02', '01', 924.00, 924.00, '20221016', '232800', '20221016', '060', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221016', '1016232800', '01', '0', '00000000', '45826170', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 924.00, '001', 924.00, 138.00, '48766720', '474034009245', '2093571505', '3589055941984575', '0', 924.00, '001');
INSERT INTO `f_t` VALUES (49, '00009788097015421598778', 'zyrsfoxt30e7g', '00030000', '00030000', '925891314285', '417708', '00', '02', '07', 77.00, 77.00, '20221016', '221900', '20221016', '152', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016221900', '01', '0', '00000000', '96450191', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 77.00, '001', 77.00, 11.50, '83190648', '599341194476', '7449625759', '6504944824467445', '0', 77.00, '001');
INSERT INTO `f_t` VALUES (50, '00008365723794289325434', 'zyrsfoxt30e7g', '00030000', '00030000', '320377219768', '156756', '00', '02', '03', 987.00, 987.00, '20221016', '222600', '20221016', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016222600', '01', '0', '00000000', '03575891', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 987.00, '001', 987.00, 147.41, '88314440', '367014693623', '3775152697', '8622808079689243', '0', 987.00, '001');
INSERT INTO `f_t` VALUES (51, '00002187445806554304776', 'zyrsfoxt30e7g', '00030000', '00030000', '261648208716', '648557', '00', '02', '01', 982.00, 982.00, '20221016', '222700', '20221016', '000', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016222700', '01', '0', '00000000', '82684767', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 982.00, '001', 982.00, 146.66, '89501132', '584197913260', '2065213192', '6817772074621613', '0', 982.00, '001');
INSERT INTO `f_t` VALUES (52, '00072467702244911667994', 'zyrsfoxt30e7g', '00030000', '00030000', '831900165896', '391323', '00', '02', '03', 972.00, 972.00, '20221016', '224000', '20221016', '130', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016224000', '01', '0', '00000000', '18168713', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 972.00, '001', 972.00, 145.17, '21320018', '206018811711', '4935370107', '0027316828176750', '0', 972.00, '001');
INSERT INTO `f_t` VALUES (53, '00097615871402121531734', 'zyrsfoxt30e7g', '00030000', '00030000', '106776261714', '000103', '00', '02', '01', 916.00, 916.00, '20221016', '224500', '20221016', '040', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016224500', '01', '0', '00000000', '72567048', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 916.00, '001', 916.00, 136.80, '95125532', '137292011726', '2099054871', '3538597447990488', '0', 916.00, '001');
INSERT INTO `f_t` VALUES (54, '00048203187051272039671', 'zyrsfoxt30e7g', '00030000', '00030000', '013786748490', '413911', '00', '02', '01', 936.00, 936.00, '20221016', '224600', '20221016', '132', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221016', '1016224600', '01', '0', '00000000', '86989636', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 936.00, '001', 936.00, 139.79, '02917460', '220256716861', '8342558728', '7515527440212935', '0', 936.00, '001');
INSERT INTO `f_t` VALUES (55, '00033303053655915148072', '7uqdpkte8jifs', '00030000', '00030000', '051060765567', '665532', '00', '02', '01', 85.00, 85.00, '20221017', '162600', '20221017', '101', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017162600', '01', '0', '00000000', '42128124', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 85.00, '001', 85.00, 12.69, '45987603', '921440464864', '4393402381', '2574910259700478', '0', 85.00, '001');
INSERT INTO `f_t` VALUES (56, '00023277573483937567936', '7uqdpkte8jifs', '00030000', '00030000', '899374876553', '987398', '00', '02', '03', 955.00, 955.00, '20221017', '164400', '20221017', '152', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017164400', '01', '0', '00000000', '46340950', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 955.00, '001', 955.00, 142.63, '70178946', '321019582443', '1171997579', '9844992112255072', '0', 955.00, '001');
INSERT INTO `f_t` VALUES (57, '00099075066870530267945', '7uqdpkte8jifs', '00030000', '00030000', '461542441713', '888304', '00', '02', '07', 947.00, 947.00, '20221017', '165300', '20221017', '130', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017165300', '01', '0', '00000000', '39665092', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 947.00, '001', 947.00, 141.43, '66442241', '372013321975', '4061948626', '4995925176503800', '0', 947.00, '001');
INSERT INTO `f_t` VALUES (58, '00076778404373252044373', '7uqdpkte8jifs', '00030000', '00030000', '352051261147', '938472', '00', '02', '03', 936.00, 936.00, '20221017', '170600', '20221017', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017170600', '01', '0', '00000000', '94604816', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 936.00, '001', 936.00, 139.79, '11080364', '457991961027', '2754487036', '0650105056846175', '0', 936.00, '001');
INSERT INTO `f_t` VALUES (59, '00089068004447272464937', '7uqdpkte8jifs', '00030000', '00030000', '993098274957', '349282', '00', '02', '03', 960.00, 960.00, '20221017', '171000', '20221017', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017171000', '01', '0', '00000000', '50594522', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 960.00, '001', 960.00, 143.37, '88359775', '350038663563', '8971015492', '1303900739162011', '0', 960.00, '001');
INSERT INTO `f_t` VALUES (60, '00070251569991403134456', '7uqdpkte8jifs', '00030000', '00030000', '867623312134', '487242', '00', '02', '01', 949.00, 949.00, '20221017', '172500', '20221017', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017172500', '01', '0', '00000000', '80396589', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 949.00, '001', 949.00, 141.73, '26598168', '973613291230', '9079938923', '3875562037834310', '0', 949.00, '001');
INSERT INTO `f_t` VALUES (61, '00029934559508984235373', 'dbfv30mkn721g', '00030001', '00030001', '232920629779', '057215', '00', '02', '03', 37.00, 37.00, '20221017', '063600', '20221017', '150', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017063600', '01', '0', '00000000', '41525101', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 37.00, '001', 37.00, 5.53, '76021192', '930959406766', '2422908245', '2598245197121173', '0', 37.00, '001');
INSERT INTO `f_t` VALUES (62, '00030728413177195716916', 'dbfv30mkn721g', '00030001', '00030001', '386150267965', '402436', '00', '02', '03', 974.00, 974.00, '20221017', '064700', '20221017', '032', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017064700', '01', '0', '00000000', '29539294', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 974.00, '001', 974.00, 145.46, '93566771', '377296891872', '3372496227', '5915336766383156', '0', 974.00, '001');
INSERT INTO `f_t` VALUES (63, '00055813656545226127492', 'dbfv30mkn721g', '00030001', '00030001', '246420284187', '157134', '00', '02', '07', 924.00, 924.00, '20221017', '070500', '20221017', '020', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017070500', '01', '0', '00000000', '06886160', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 924.00, '001', 924.00, 138.00, '69322236', '579009862505', '3330813992', '9575173137098478', '0', 924.00, '001');
INSERT INTO `f_t` VALUES (64, '00097106581627941048297', 'dbfv30mkn721g', '00030001', '00030001', '457610763133', '012563', '00', '02', '01', 921.00, 921.00, '20221017', '071600', '20221017', '011', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017071600', '01', '0', '00000000', '22220333', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 921.00, '001', 921.00, 137.55, '69165189', '959502119318', '0543492536', '4592575248878411', '0', 921.00, '001');
INSERT INTO `f_t` VALUES (65, '00092325890524208057597', 'dbfv30mkn721g', '00030001', '00030001', '442130727319', '781441', '00', '02', '07', 972.00, 972.00, '20221017', '071700', '20221017', '132', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017071700', '01', '0', '00000000', '16262168', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 972.00, '001', 972.00, 145.17, '02618875', '203410284158', '1084469230', '5850659431799589', '0', 972.00, '001');
INSERT INTO `f_t` VALUES (66, '00073414361483392799254', 'dbfv30mkn721g', '00030001', '00030001', '967328865569', '797376', '00', '02', '07', 925.00, 925.00, '20221017', '073000', '20221017', '030', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017073000', '01', '0', '00000000', '32392677', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 925.00, '001', 925.00, 138.15, '63754333', '017812885409', '2078154119', '5208683153964672', '0', 925.00, '001');
INSERT INTO `f_t` VALUES (67, '00079351669031151157164', '3pjqiufdml7av', '00030000', '00030000', '330730135072', '173929', '00', '02', '03', 74.00, 74.00, '20221018', '005700', '20221018', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018005700', '01', '0', '00000000', '65500128', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 74.00, '001', 74.00, 11.05, '43223800', '481573147207', '3568168787', '9141366458486779', '0', 74.00, '001');
INSERT INTO `f_t` VALUES (68, '00051701396490853572442', '3pjqiufdml7av', '00030000', '00030000', '896997637848', '928127', '00', '02', '07', 979.00, 979.00, '20221018', '010700', '20221018', '040', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018010700', '01', '0', '00000000', '11323354', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 979.00, '001', 979.00, 146.21, '96282774', '119125225332', '1433652705', '2978575370695966', '0', 979.00, '001');
INSERT INTO `f_t` VALUES (69, '00080676468733672732587', '3pjqiufdml7av', '00030000', '00030000', '297133497658', '343954', '00', '02', '03', 1000.00, 1000.00, '20221018', '012600', '20221018', '002', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018012600', '01', '0', '00000000', '70528519', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 1000.00, '001', 1000.00, 149.35, '09096561', '375679581393', '3613752771', '6794792023161707', '0', 1000.00, '001');
INSERT INTO `f_t` VALUES (70, '00096532120204162587791', '3pjqiufdml7av', '00030000', '00030000', '196547802917', '823758', '00', '02', '03', 952.00, 952.00, '20221018', '013900', '20221018', '131', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018013900', '01', '0', '00000000', '18872723', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 952.00, '001', 952.00, 142.18, '60251704', '720598353981', '2261652777', '6404112595938544', '0', 952.00, '001');
INSERT INTO `f_t` VALUES (71, '00064100839717082462832', '3pjqiufdml7av', '00030000', '00030000', '867208065875', '496394', '00', '02', '01', 943.00, 943.00, '20221018', '014000', '20221018', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018014000', '01', '0', '00000000', '70756057', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 943.00, '001', 943.00, 140.83, '35886646', '948099164576', '7863833935', '7604559883950367', '0', 943.00, '001');
INSERT INTO `f_t` VALUES (72, '00080214425326045784530', '3pjqiufdml7av', '00030000', '00030000', '025248907221', '111339', '00', '02', '07', 955.00, 955.00, '20221018', '015100', '20221018', '101', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018015100', '01', '0', '00000000', '44219148', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 955.00, '001', 955.00, 142.63, '87819044', '788300985397', '4977596268', '3430083570988532', '0', 955.00, '001');
INSERT INTO `f_t` VALUES (73, '00033872896368392870212', '8pxdj12et0vhb', '00030001', '00030001', '220075242767', '775130', '00', '02', '03', 71.00, 71.00, '20221018', '061600', '20221018', '000', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018061600', '01', '0', '00000000', '52958329', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 71.00, '001', 71.00, 10.60, '53565620', '595055419511', '4137687017', '7348027916061569', '0', 71.00, '001');
INSERT INTO `f_t` VALUES (74, '00062307446634207916423', '8pxdj12et0vhb', '00030001', '00030001', '796288205310', '336347', '00', '02', '01', 994.00, 994.00, '20221018', '063100', '20221018', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018063100', '01', '0', '00000000', '18906220', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 994.00, '001', 994.00, 148.45, '94017603', '042588898286', '8678788009', '5770851680675011', '0', 994.00, '001');
INSERT INTO `f_t` VALUES (75, '00073572965778385534451', '8pxdj12et0vhb', '00030001', '00030001', '340394305804', '061944', '00', '02', '07', 925.00, 925.00, '20221018', '063600', '20221018', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018063600', '01', '0', '00000000', '14317858', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 925.00, '001', 925.00, 138.15, '80809060', '720796130203', '4823612322', '8419870952244257', '0', 925.00, '001');
INSERT INTO `f_t` VALUES (76, '00064598554563797099967', '8pxdj12et0vhb', '00030001', '00030001', '789002075256', '929012', '00', '02', '01', 932.00, 932.00, '20221018', '063900', '20221018', '032', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018063900', '01', '0', '00000000', '29665745', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 932.00, '001', 932.00, 139.19, '13225970', '137050513025', '1431200870', '7550660451598359', '0', 932.00, '001');
INSERT INTO `f_t` VALUES (77, '00070970351954837725370', '8pxdj12et0vhb', '00030001', '00030001', '106607572718', '062912', '00', '02', '01', 928.00, 928.00, '20221018', '064700', '20221018', '051', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018064700', '01', '0', '00000000', '27492782', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 928.00, '001', 928.00, 138.59, '08359636', '484089312599', '2728485681', '9688272349059520', '0', 928.00, '001');
INSERT INTO `f_t` VALUES (78, '00006070302113329252430', '8pxdj12et0vhb', '00030001', '00030001', '986151233794', '073630', '00', '02', '03', 943.00, 943.00, '20221018', '065500', '20221018', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018065500', '01', '0', '00000000', '84031943', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 943.00, '001', 943.00, 140.83, '97318161', '975396048626', '7756098785', '5757033062881936', '0', 943.00, '001');
INSERT INTO `f_t` VALUES (79, '00055267694823865440037', 'ovcrpuqje08a5', '00030002', '00030002', '352496052965', '878369', '00', '02', '03', 63.00, 63.00, '20221018', '043500', '20221018', '071', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018043500', '01', '0', '00000000', '92275306', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 63.00, '001', 63.00, 9.41, '36637444', '688955067815', '7839732437', '2576145537840194', '0', 63.00, '001');
INSERT INTO `f_t` VALUES (80, '00058436896257023960278', 'ovcrpuqje08a5', '00030002', '00030002', '882208509588', '566332', '00', '02', '03', 965.00, 965.00, '20221018', '044200', '20221018', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018044200', '01', '0', '00000000', '12206427', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 965.00, '001', 965.00, 144.12, '55145347', '654476905544', '8837483789', '8102293709734893', '0', 965.00, '001');
INSERT INTO `f_t` VALUES (81, '00046565555355360854830', 'ovcrpuqje08a5', '00030002', '00030002', '638096000611', '678380', '00', '02', '07', 940.00, 940.00, '20221018', '044600', '20221018', '101', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018044600', '01', '0', '00000000', '33640894', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 940.00, '001', 940.00, 140.39, '34688284', '242177480952', '7166633756', '6857927234338081', '0', 940.00, '001');
INSERT INTO `f_t` VALUES (82, '00000539188107874892825', 'ovcrpuqje08a5', '00030002', '00030002', '312533223580', '797780', '00', '02', '07', 904.00, 904.00, '20221018', '045300', '20221018', '002', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018045300', '01', '0', '00000000', '08115658', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 904.00, '001', 904.00, 135.01, '69018276', '119149217246', '5134880382', '0457363336144902', '0', 904.00, '001');
INSERT INTO `f_t` VALUES (83, '00034121768951204852703', 'ovcrpuqje08a5', '00030002', '00030002', '189225823520', '514401', '00', '02', '07', 993.00, 993.00, '20221018', '045400', '20221018', '111', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018045400', '01', '0', '00000000', '79246287', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 993.00, '001', 993.00, 148.30, '08024554', '736680443697', '8402135974', '2719342504573835', '0', 993.00, '001');
INSERT INTO `f_t` VALUES (84, '00078286290971361902739', 'ovcrpuqje08a5', '00030002', '00030002', '110019703247', '838853', '00', '02', '01', 931.00, 931.00, '20221018', '051300', '20221018', '150', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018051300', '01', '0', '00000000', '00944568', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 931.00, '001', 931.00, 139.04, '78626413', '911339296421', '9656740448', '4769421555424141', '0', 931.00, '001');
INSERT INTO `f_t` VALUES (85, '00063830273626518074561', '2usaq816xzmbi', '00030002', '00030002', '181330262054', '251864', '00', '02', '03', 65.00, 65.00, '20221017', '050800', '20221017', '001', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017050800', '01', '0', '00000000', '59275637', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 65.00, '001', 65.00, 9.71, '69292299', '079413394814', '2971316647', '5977686155224849', '0', 65.00, '001');
INSERT INTO `f_t` VALUES (86, '00079632981884797068062', '2usaq816xzmbi', '00030002', '00030002', '947996499630', '450854', '00', '02', '01', 902.00, 902.00, '20221017', '052600', '20221017', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017052600', '01', '0', '00000000', '83961911', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 902.00, '001', 902.00, 134.71, '78534578', '701879568969', '8953847665', '4536756378497589', '0', 902.00, '001');
INSERT INTO `f_t` VALUES (87, '00035184503521510411311', '2usaq816xzmbi', '00030002', '00030002', '863053618055', '598211', '00', '02', '03', 943.00, 943.00, '20221017', '054300', '20221017', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017054300', '01', '0', '00000000', '20812612', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 943.00, '001', 943.00, 140.83, '87844646', '448181755184', '8206315107', '4573883536553319', '0', 943.00, '001');
INSERT INTO `f_t` VALUES (88, '00038525303357495214673', '2usaq816xzmbi', '00030002', '00030002', '756170886662', '994549', '00', '02', '07', 914.00, 914.00, '20221017', '055100', '20221017', '051', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017055100', '01', '0', '00000000', '16909794', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 914.00, '001', 914.00, 136.50, '23628034', '086394304770', '7341297703', '5614768937536442', '0', 914.00, '001');
INSERT INTO `f_t` VALUES (89, '00037572275201447001189', '2usaq816xzmbi', '00030002', '00030002', '894510095448', '712258', '00', '02', '07', 989.00, 989.00, '20221017', '060900', '20221017', '022', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017060900', '01', '0', '00000000', '10533828', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 989.00, '001', 989.00, 147.70, '32685780', '050433355520', '2880985674', '5475322237419993', '0', 989.00, '001');
INSERT INTO `f_t` VALUES (90, '00086473977183440195657', '2usaq816xzmbi', '00030002', '00030002', '738297926219', '281108', '00', '02', '01', 917.00, 917.00, '20221017', '062600', '20221017', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221017', '1017062600', '01', '0', '00000000', '35806111', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 917.00, '001', 917.00, 136.95, '53318212', '459017556953', '8005854115', '7667837676379754', '0', 917.00, '001');
INSERT INTO `f_t` VALUES (91, '00047599282743591214458', 'd91pbsm5h7iq6', '00030001', '00030001', '502308024666', '968914', '00', '02', '03', 99.00, 99.00, '20221018', '051400', '20221018', '060', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018051400', '01', '0', '00000000', '67084082', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 99.00, '001', 99.00, 14.79, '67393859', '762635634365', '0053424225', '9666170643223344', '0', 99.00, '001');
INSERT INTO `f_t` VALUES (92, '00043607338032672253617', 'd91pbsm5h7iq6', '00030001', '00030001', '535859278595', '634785', '00', '02', '07', 962.00, 962.00, '20221018', '051500', '20221018', '130', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018051500', '01', '0', '00000000', '44576862', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 962.00, '001', 962.00, 143.67, '37376736', '300698694659', '0698247925', '4199452688723305', '0', 962.00, '001');
INSERT INTO `f_t` VALUES (93, '00029556276707119214972', 'd91pbsm5h7iq6', '00030001', '00030001', '797184225793', '126453', '00', '02', '03', 914.00, 914.00, '20221018', '052000', '20221018', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018052000', '01', '0', '00000000', '87539587', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 914.00, '001', 914.00, 136.50, '37450894', '680229367402', '0811341530', '8291712681061784', '0', 914.00, '001');
INSERT INTO `f_t` VALUES (94, '00064441623813360350435', 'd91pbsm5h7iq6', '00030001', '00030001', '453928979332', '745296', '00', '02', '01', 915.00, 915.00, '20221018', '053600', '20221018', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018053600', '01', '0', '00000000', '23226950', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 915.00, '001', 915.00, 136.65, '70602097', '238448098619', '4315350825', '7244343408434437', '0', 915.00, '001');
INSERT INTO `f_t` VALUES (95, '00040141821859787667950', 'd91pbsm5h7iq6', '00030001', '00030001', '492508563717', '239703', '00', '02', '03', 909.00, 909.00, '20221018', '054000', '20221018', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018054000', '01', '0', '00000000', '86140659', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 909.00, '001', 909.00, 135.76, '31494086', '723515537055', '6439196913', '8480692580223864', '0', 909.00, '001');
INSERT INTO `f_t` VALUES (96, '00002519969000382370386', 'd91pbsm5h7iq6', '00030001', '00030001', '431705135701', '586003', '00', '02', '01', 960.00, 960.00, '20221018', '055400', '20221018', '142', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018055400', '01', '0', '00000000', '08566296', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 960.00, '001', 960.00, 143.37, '48366412', '324512660354', '3499478112', '3739273666171929', '0', 960.00, '001');
INSERT INTO `f_t` VALUES (97, '00074230441904324619486', 'lx9jzn7rf20gw', '00030002', '00030002', '740292623991', '209918', '00', '02', '07', 17.00, 17.00, '20221016', '084200', '20221016', '142', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016084200', '01', '0', '00000000', '41596191', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 17.00, '001', 17.00, 2.54, '32957097', '945860338837', '2869014061', '4618788148439590', '0', 17.00, '001');
INSERT INTO `f_t` VALUES (98, '00008172302386041309064', 'lx9jzn7rf20gw', '00030002', '00030002', '732840982541', '769615', '00', '02', '03', 959.00, 959.00, '20221016', '084800', '20221016', '110', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016084800', '01', '0', '00000000', '27519368', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 959.00, '001', 959.00, 143.22, '96567930', '128737014486', '7213886854', '7595033807783185', '0', 959.00, '001');
INSERT INTO `f_t` VALUES (99, '00065869972565456006292', 'lx9jzn7rf20gw', '00030002', '00030002', '966134474428', '686227', '00', '02', '01', 935.00, 935.00, '20221016', '090400', '20221016', '011', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016090400', '01', '0', '00000000', '78818021', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 935.00, '001', 935.00, 139.64, '86040968', '211500366626', '6285122787', '7392080592051938', '0', 935.00, '001');
INSERT INTO `f_t` VALUES (100, '00007779676731065613023', 'lx9jzn7rf20gw', '00030002', '00030002', '586611477932', '159983', '00', '02', '03', 983.00, 983.00, '20221016', '090600', '20221016', '071', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016090600', '01', '0', '00000000', '15288608', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 983.00, '001', 983.00, 146.81, '18136416', '520537033646', '7941726330', '0098428869659871', '0', 983.00, '001');
INSERT INTO `f_t` VALUES (101, '00085367346782751931788', 'lx9jzn7rf20gw', '00030002', '00030002', '161851779556', '306658', '00', '02', '01', 905.00, 905.00, '20221016', '092300', '20221016', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016092300', '01', '0', '00000000', '88091950', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 905.00, '001', 905.00, 135.16, '70062623', '790080340052', '7331997117', '3249596490218786', '0', 905.00, '001');
INSERT INTO `f_t` VALUES (102, '00073132199215295250174', 'lx9jzn7rf20gw', '00030002', '00030002', '345860077224', '741406', '00', '02', '07', 935.00, 935.00, '20221016', '092400', '20221016', '131', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221016', '1016092400', '01', '0', '00000000', '87253947', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 935.00, '001', 935.00, 139.64, '12323604', '161540591501', '5270029688', '2691995667247477', '0', 935.00, '001');
INSERT INTO `f_t` VALUES (103, '00038349348687126758343', '5u6zm9itwkjcr', '00030003', '00030003', '378622285033', '336046', '00', '02', '07', 38.00, 38.00, '20221017', '221900', '20221017', '072', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017221900', '01', '0', '00000000', '53482415', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 38.00, '001', 38.00, 5.68, '46823195', '412626474005', '4482215560', '1504871146976872', '0', 38.00, '001');
INSERT INTO `f_t` VALUES (104, '00059688613602478365845', '5u6zm9itwkjcr', '00030003', '00030003', '077363796984', '901140', '00', '02', '01', 904.00, 904.00, '20221017', '223000', '20221017', '032', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017223000', '01', '0', '00000000', '87671185', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 904.00, '001', 904.00, 135.01, '21758719', '954607923747', '5294121812', '6563243497984053', '0', 904.00, '001');
INSERT INTO `f_t` VALUES (105, '00075595498870171696329', '5u6zm9itwkjcr', '00030003', '00030003', '320060072928', '236533', '00', '02', '07', 953.00, 953.00, '20221017', '223300', '20221017', '062', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017223300', '01', '0', '00000000', '34717383', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 953.00, '001', 953.00, 142.33, '74581152', '324568687886', '0899330860', '2738013690537118', '0', 953.00, '001');
INSERT INTO `f_t` VALUES (106, '00076789814592169926008', '5u6zm9itwkjcr', '00030003', '00030003', '357005178584', '147174', '00', '02', '01', 982.00, 982.00, '20221017', '225300', '20221017', '152', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017225300', '01', '0', '00000000', '76779470', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 982.00, '001', 982.00, 146.66, '93139859', '908552006709', '2505089854', '9245868746982551', '0', 982.00, '001');
INSERT INTO `f_t` VALUES (107, '00025359943325395855413', '5u6zm9itwkjcr', '00030003', '00030003', '593695173729', '945219', '00', '02', '03', 993.00, 993.00, '20221017', '230100', '20221017', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017230100', '01', '0', '00000000', '67031251', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 993.00, '001', 993.00, 148.30, '20813754', '770558156546', '0221448085', '0580019359544818', '0', 993.00, '001');
INSERT INTO `f_t` VALUES (108, '00096188050407935372817', '5u6zm9itwkjcr', '00030003', '00030003', '841127606967', '723146', '00', '02', '01', 964.00, 964.00, '20221017', '232100', '20221017', '022', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017232100', '01', '0', '00000000', '07271717', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 964.00, '001', 964.00, 143.97, '83936733', '719978271937', '3590194020', '4349604014279662', '0', 964.00, '001');
INSERT INTO `f_t` VALUES (109, '00007421529842374096157', '1e574fvqxzawj', '00030001', '00030001', '807810654444', '278017', '00', '02', '01', 70.00, 70.00, '20221018', '003300', '20221018', '150', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018003300', '01', '0', '00000000', '75936650', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 70.00, '001', 70.00, 10.45, '14039695', '444749737362', '5289229810', '1518056163503142', '0', 70.00, '001');
INSERT INTO `f_t` VALUES (110, '00016064812961442312554', '1e574fvqxzawj', '00030001', '00030001', '282520878270', '725878', '00', '02', '01', 997.00, 997.00, '20221018', '003900', '20221018', '071', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018003900', '01', '0', '00000000', '50078619', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 997.00, '001', 997.00, 148.90, '40635144', '153557654139', '2052260200', '5886124586400450', '0', 997.00, '001');
INSERT INTO `f_t` VALUES (111, '00038525141610391042878', '1e574fvqxzawj', '00030001', '00030001', '342803138259', '718860', '00', '02', '07', 963.00, 963.00, '20221018', '004600', '20221018', '022', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018004600', '01', '0', '00000000', '46287071', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 963.00, '001', 963.00, 143.82, '30181669', '197516748958', '5807111121', '1197385469318035', '0', 963.00, '001');
INSERT INTO `f_t` VALUES (112, '00066050495906371441460', '1e574fvqxzawj', '00030001', '00030001', '461009375824', '446395', '00', '02', '01', 994.00, 994.00, '20221018', '005000', '20221018', '040', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018005000', '01', '0', '00000000', '77354910', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 994.00, '001', 994.00, 148.45, '96189276', '062357793015', '4641703939', '5828343292356188', '0', 994.00, '001');
INSERT INTO `f_t` VALUES (113, '00049065896103810495924', '1e574fvqxzawj', '00030001', '00030001', '497682871652', '476214', '00', '02', '07', 928.00, 928.00, '20221018', '005200', '20221018', '010', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018005200', '01', '0', '00000000', '29793367', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 928.00, '001', 928.00, 138.59, '39795240', '869831256530', '7374141096', '7434311015572925', '0', 928.00, '001');
INSERT INTO `f_t` VALUES (114, '00027837456456347347633', '1e574fvqxzawj', '00030001', '00030001', '151122702324', '160168', '00', '02', '03', 942.00, 942.00, '20221018', '011100', '20221018', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018011100', '01', '0', '00000000', '49254101', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 942.00, '001', 942.00, 140.69, '50446796', '881003211349', '7388446613', '4266210836628391', '0', 942.00, '001');
INSERT INTO `f_t` VALUES (115, '00077126729636554039975', 'zn03t2slvcpd5', '00030003', '00030003', '167955480056', '003919', '00', '02', '03', 24.00, 24.00, '20221017', '230000', '20221017', '111', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017230000', '01', '0', '00000000', '10826935', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 24.00, '001', 24.00, 3.58, '17384660', '207504561089', '5339574752', '6061621111049187', '0', 24.00, '001');
INSERT INTO `f_t` VALUES (116, '00080748490544807432885', 'zn03t2slvcpd5', '00030003', '00030003', '986845810452', '522628', '00', '02', '07', 964.00, 964.00, '20221017', '230400', '20221017', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017230400', '01', '0', '00000000', '26424931', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 964.00, '001', 964.00, 143.97, '07913862', '479633078238', '0872207132', '3964984176528681', '0', 964.00, '001');
INSERT INTO `f_t` VALUES (117, '00016458037546628487405', 'zn03t2slvcpd5', '00030003', '00030003', '016631273179', '488779', '00', '02', '07', 971.00, 971.00, '20221017', '231300', '20221017', '111', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017231300', '01', '0', '00000000', '64832996', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 971.00, '001', 971.00, 145.02, '99270359', '023981786451', '7496116965', '1966433155561199', '0', 971.00, '001');
INSERT INTO `f_t` VALUES (118, '00084362660183119927402', 'zn03t2slvcpd5', '00030003', '00030003', '441602893811', '685890', '00', '02', '03', 928.00, 928.00, '20221017', '231500', '20221017', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017231500', '01', '0', '00000000', '01991449', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 928.00, '001', 928.00, 138.59, '48826717', '690802642574', '4724046651', '3785098862081802', '0', 928.00, '001');
INSERT INTO `f_t` VALUES (119, '00050926889587445943386', 'zn03t2slvcpd5', '00030003', '00030003', '471997530925', '816157', '00', '02', '01', 902.00, 902.00, '20221017', '232700', '20221017', '142', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017232700', '01', '0', '00000000', '28566504', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 902.00, '001', 902.00, 134.71, '34317897', '626033109087', '5293635792', '7702694803316964', '0', 902.00, '001');
INSERT INTO `f_t` VALUES (120, '00050920436294493558001', 'zn03t2slvcpd5', '00030003', '00030003', '341898308556', '606803', '00', '02', '01', 902.00, 902.00, '20221017', '234600', '20221017', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017234600', '01', '0', '00000000', '00636533', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 902.00, '001', 902.00, 134.71, '79447087', '413470368697', '3119430930', '4295956971578068', '0', 902.00, '001');
INSERT INTO `f_t` VALUES (121, '00030510988047616716172', 'g0ua2mc859x4b', '00030001', '00030001', '372180375090', '666070', '00', '02', '07', 70.00, 70.00, '20221018', '025100', '20221018', '122', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018025100', '01', '0', '00000000', '14791443', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 70.00, '001', 70.00, 10.45, '55674899', '258255645871', '4874936323', '9698826383970286', '0', 70.00, '001');
INSERT INTO `f_t` VALUES (122, '00002633505013381613542', 'g0ua2mc859x4b', '00030001', '00030001', '822481454521', '827258', '00', '02', '03', 950.00, 950.00, '20221018', '030800', '20221018', '131', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018030800', '01', '0', '00000000', '14183989', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 950.00, '001', 950.00, 141.88, '63126210', '502726670300', '6050764584', '6560542430471497', '0', 950.00, '001');
INSERT INTO `f_t` VALUES (123, '00059158558389503581764', 'g0ua2mc859x4b', '00030001', '00030001', '929799188277', '410876', '00', '02', '03', 983.00, 983.00, '20221018', '032100', '20221018', '130', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018032100', '01', '0', '00000000', '89499285', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 983.00, '001', 983.00, 146.81, '73536619', '611407921146', '7292494874', '1525517046965638', '0', 983.00, '001');
INSERT INTO `f_t` VALUES (124, '00033717657058694843262', 'g0ua2mc859x4b', '00030001', '00030001', '494159087315', '943930', '00', '02', '07', 922.00, 922.00, '20221018', '034000', '20221018', '060', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018034000', '01', '0', '00000000', '49738883', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 922.00, '001', 922.00, 137.70, '51683327', '301571370446', '6800996144', '0082420093660651', '0', 922.00, '001');
INSERT INTO `f_t` VALUES (125, '00003461982685118361144', 'g0ua2mc859x4b', '00030001', '00030001', '929720076866', '004916', '00', '02', '01', 902.00, 902.00, '20221018', '035400', '20221018', '022', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018035400', '01', '0', '00000000', '26167747', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 902.00, '001', 902.00, 134.71, '77587894', '934876434538', '3840624748', '7693043436901977', '0', 902.00, '001');
INSERT INTO `f_t` VALUES (126, '00078171434828514899640', 'g0ua2mc859x4b', '00030001', '00030001', '776362722016', '220928', '00', '02', '01', 928.00, 928.00, '20221018', '040300', '20221018', '070', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018040300', '01', '0', '00000000', '00246148', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 928.00, '001', 928.00, 138.59, '46491602', '733658745088', '7504774484', '6795058008699401', '0', 928.00, '001');
INSERT INTO `f_t` VALUES (127, '00043511273033041298311', 'qaf1wu0cr8z54', '00010000', '00010000', '148811553264', '225803', '00', '02', '07', 77.00, 77.00, '20221017', '021000', '20221017', '071', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017021000', '01', '0', '00000000', '25132510', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 77.00, '001', 77.00, 11.50, '74915842', '713284475559', '3663760395', '9616907830093429', '0', 77.00, '001');
INSERT INTO `f_t` VALUES (128, '00006809435304786786604', 'qaf1wu0cr8z54', '00010000', '00010000', '876206656082', '325629', '00', '02', '07', 948.00, 948.00, '20221017', '021600', '20221017', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017021600', '01', '0', '00000000', '51050139', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 948.00, '001', 948.00, 141.58, '59989527', '763638329346', '2267713027', '9559245797956440', '0', 948.00, '001');
INSERT INTO `f_t` VALUES (129, '00021558632380675636794', 'qaf1wu0cr8z54', '00010000', '00010000', '527550685754', '840602', '00', '02', '01', 911.00, 911.00, '20221017', '022700', '20221017', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017022700', '01', '0', '00000000', '21135736', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 911.00, '001', 911.00, 136.06, '31214872', '812932154472', '7741674058', '9905820257309869', '0', 911.00, '001');
INSERT INTO `f_t` VALUES (130, '00077841360583832831922', 'qaf1wu0cr8z54', '00010000', '00010000', '615319864814', '011853', '00', '02', '07', 993.00, 993.00, '20221017', '024300', '20221017', '060', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017024300', '01', '0', '00000000', '04734110', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 993.00, '001', 993.00, 148.30, '97769971', '352520662555', '4120424170', '0144468256652572', '0', 993.00, '001');
INSERT INTO `f_t` VALUES (131, '00069113204949748465215', 'qaf1wu0cr8z54', '00010000', '00010000', '800736209716', '829505', '00', '02', '03', 945.00, 945.00, '20221017', '025700', '20221017', '112', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017025700', '01', '0', '00000000', '39604507', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 945.00, '001', 945.00, 141.13, '75900526', '631508164097', '1872224635', '0805088804174553', '0', 945.00, '001');
INSERT INTO `f_t` VALUES (132, '00026447155844556628958', 'qaf1wu0cr8z54', '00010000', '00010000', '428971687998', '676549', '00', '02', '01', 960.00, 960.00, '20221017', '025800', '20221017', '041', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221017', '1017025800', '01', '0', '00000000', '97800197', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 960.00, '001', 960.00, 143.37, '62640144', '049727345459', '5087333903', '6182973712228285', '0', 960.00, '001');
INSERT INTO `f_t` VALUES (133, '00000877440638570736663', 'j52rnp1oygcbq', '00010001', '00010001', '990774542631', '190440', '00', '02', '07', 13.00, 13.00, '20221017', '043700', '20221017', '110', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017043700', '01', '0', '00000000', '25973841', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 13.00, '001', 13.00, 1.94, '03647223', '907831002602', '5719068993', '4094096752770615', '0', 13.00, '001');
INSERT INTO `f_t` VALUES (134, '00000495924715047415524', 'j52rnp1oygcbq', '00010001', '00010001', '143690534691', '022324', '00', '02', '03', 958.00, 958.00, '20221017', '045500', '20221017', '112', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017045500', '01', '0', '00000000', '81861203', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 958.00, '001', 958.00, 143.07, '39581267', '324149242235', '1502546905', '0487569115583565', '0', 958.00, '001');
INSERT INTO `f_t` VALUES (135, '00069666859139067469769', 'j52rnp1oygcbq', '00010001', '00010001', '007913882592', '249755', '00', '02', '07', 905.00, 905.00, '20221017', '051500', '20221017', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017051500', '01', '0', '00000000', '27044880', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 905.00, '001', 905.00, 135.16, '55127160', '815712420925', '8228616675', '3813117515817616', '0', 905.00, '001');
INSERT INTO `f_t` VALUES (136, '00030104200032780688596', 'j52rnp1oygcbq', '00010001', '00010001', '521345846511', '687820', '00', '02', '07', 943.00, 943.00, '20221017', '052800', '20221017', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017052800', '01', '0', '00000000', '45615186', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 943.00, '001', 943.00, 140.83, '88730156', '526613922803', '9529934161', '1157947248276290', '0', 943.00, '001');
INSERT INTO `f_t` VALUES (137, '00043079020367611393191', 'j52rnp1oygcbq', '00010001', '00010001', '317042364016', '867796', '00', '02', '03', 956.00, 956.00, '20221017', '054800', '20221017', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017054800', '01', '0', '00000000', '76787386', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 956.00, '001', 956.00, 142.78, '90312758', '995645076683', '9025282642', '5111250980343724', '0', 956.00, '001');
INSERT INTO `f_t` VALUES (138, '00097046779906481348815', 'j52rnp1oygcbq', '00010001', '00010001', '462849953047', '762733', '00', '02', '07', 989.00, 989.00, '20221017', '055900', '20221017', '140', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221017', '1017055900', '01', '0', '00000000', '78078440', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 989.00, '001', 989.00, 147.70, '59627206', '818428101779', '2709898842', '8633775359745112', '0', 989.00, '001');
INSERT INTO `f_t` VALUES (139, '00044800388915177487111', '5brn9uf1le80y', '00010002', '00010002', '944956343401', '989048', '00', '02', '03', 40.00, 40.00, '20221018', '043900', '20221018', '020', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018043900', '01', '0', '00000000', '39389720', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 40.00, '001', 40.00, 5.97, '46458194', '411650554158', '4174341180', '8338015018945228', '0', 40.00, '001');
INSERT INTO `f_t` VALUES (140, '00092752634828119547835', '5brn9uf1le80y', '00010002', '00010002', '328786452172', '023329', '00', '02', '03', 922.00, 922.00, '20221018', '044100', '20221018', '020', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018044100', '01', '0', '00000000', '28896683', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 922.00, '001', 922.00, 137.70, '99125624', '306620944674', '6286466744', '8015725050949278', '0', 922.00, '001');
INSERT INTO `f_t` VALUES (141, '00081708040959504346357', '5brn9uf1le80y', '00010002', '00010002', '155608133926', '883823', '00', '02', '03', 975.00, 975.00, '20221018', '045700', '20221018', '100', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018045700', '01', '0', '00000000', '13757090', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 975.00, '001', 975.00, 145.61, '45995572', '477761385321', '1217534496', '9308676543614408', '0', 975.00, '001');
INSERT INTO `f_t` VALUES (142, '00099976879122477973255', '5brn9uf1le80y', '00010002', '00010002', '744189356495', '218141', '00', '02', '07', 941.00, 941.00, '20221018', '051500', '20221018', '052', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018051500', '01', '0', '00000000', '35409925', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 941.00, '001', 941.00, 140.54, '04045298', '109763566040', '5496627658', '5219608937815626', '0', 941.00, '001');
INSERT INTO `f_t` VALUES (143, '00094058098751345083960', '5brn9uf1le80y', '00010002', '00010002', '245825054517', '624359', '00', '02', '01', 972.00, 972.00, '20221018', '051600', '20221018', '062', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018051600', '01', '0', '00000000', '34963885', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 972.00, '001', 972.00, 145.17, '40087188', '927534529817', '5802675733', '0699191851455130', '0', 972.00, '001');
INSERT INTO `f_t` VALUES (144, '00033568107241985639110', '5brn9uf1le80y', '00010002', '00010002', '529735322095', '531045', '00', '02', '07', 925.00, 925.00, '20221018', '053400', '20221018', '122', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0002', '000', '84', '06', '20221018', '1018053400', '01', '0', '00000000', '13347941', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 925.00, '001', 925.00, 138.15, '53858552', '715176931402', '6867133010', '4632573088123755', '0', 925.00, '001');
INSERT INTO `f_t` VALUES (145, '00048380081357115543341', 'ca13ieuto6mrb', '00010000', '00010000', '834566180515', '129665', '00', '02', '03', 23.00, 23.00, '20221018', '045000', '20221018', '121', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018045000', '01', '0', '00000000', '75503022', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 23.00, '001', 23.00, 3.43, '18385278', '289898248544', '6070243196', '0903460471047238', '0', 23.00, '001');
INSERT INTO `f_t` VALUES (146, '00010791739191501867652', 'ca13ieuto6mrb', '00010000', '00010000', '192581607288', '032827', '00', '02', '03', 943.00, 943.00, '20221018', '045600', '20221018', '151', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018045600', '01', '0', '00000000', '53604970', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 943.00, '001', 943.00, 140.83, '33520424', '872146736428', '2384293519', '2959921138107771', '0', 943.00, '001');
INSERT INTO `f_t` VALUES (147, '00090972378673615898021', 'ca13ieuto6mrb', '00010000', '00010000', '744712241226', '986507', '00', '02', '03', 936.00, 936.00, '20221018', '050800', '20221018', '000', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018050800', '01', '0', '00000000', '69002732', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 936.00, '001', 936.00, 139.79, '85307636', '380319193236', '7317491273', '0272502839535165', '0', 936.00, '001');
INSERT INTO `f_t` VALUES (148, '00082934516632045463058', 'ca13ieuto6mrb', '00010000', '00010000', '158743108705', '253970', '00', '02', '07', 968.00, 968.00, '20221018', '051700', '20221018', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018051700', '01', '0', '00000000', '43294520', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 968.00, '001', 968.00, 144.57, '51305315', '824328145178', '6173899124', '8218610635339729', '0', 968.00, '001');
INSERT INTO `f_t` VALUES (149, '00044073419835127775178', 'ca13ieuto6mrb', '00010000', '00010000', '573906178617', '633936', '00', '02', '07', 960.00, 960.00, '20221018', '053700', '20221018', '040', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018053700', '01', '0', '00000000', '77491236', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 960.00, '001', 960.00, 143.37, '53126162', '079738179252', '2814005184', '1355425344822568', '0', 960.00, '001');
INSERT INTO `f_t` VALUES (150, '00035190986124864989569', 'ca13ieuto6mrb', '00010000', '00010000', '758777286503', '670765', '00', '02', '07', 933.00, 933.00, '20221018', '054500', '20221018', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0000', '000', '84', '06', '20221018', '1018054500', '01', '0', '00000000', '04216023', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 933.00, '001', 933.00, 139.34, '51388290', '070636544233', '8055806432', '3191727911763031', '0', 933.00, '001');
INSERT INTO `f_t` VALUES (151, '00044181672486316232117', 'a9myep3fxsw26', '00010001', '00010001', '841309227209', '602316', '00', '02', '01', 25.00, 25.00, '20221018', '002600', '20221018', '152', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018002600', '01', '0', '00000000', '90246232', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 25.00, '001', 25.00, 3.73, '23688970', '870799133102', '3990357671', '0156501104984395', '0', 25.00, '001');
INSERT INTO `f_t` VALUES (152, '00012255835538917087958', 'a9myep3fxsw26', '00010001', '00010001', '688876325511', '917203', '00', '02', '03', 935.00, 935.00, '20221018', '004500', '20221018', '151', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018004500', '01', '0', '00000000', '54105362', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 935.00, '001', 935.00, 139.64, '28993871', '164104667430', '1200708799', '8798523749559712', '0', 935.00, '001');
INSERT INTO `f_t` VALUES (153, '00017177806745973458478', 'a9myep3fxsw26', '00010001', '00010001', '608312939043', '982913', '00', '02', '01', 931.00, 931.00, '20221018', '010200', '20221018', '111', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018010200', '01', '0', '00000000', '47726545', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 931.00, '001', 931.00, 139.04, '02490310', '427008640367', '0934782472', '6852179127207947', '0', 931.00, '001');
INSERT INTO `f_t` VALUES (154, '00006271039629096068480', 'a9myep3fxsw26', '00010001', '00010001', '817987855305', '854974', '00', '02', '01', 962.00, 962.00, '20221018', '010600', '20221018', '102', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018010600', '01', '0', '00000000', '27431434', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 962.00, '001', 962.00, 143.67, '56303853', '067806964021', '7645139615', '2482820642458270', '0', 962.00, '001');
INSERT INTO `f_t` VALUES (155, '00095779697919773176361', 'a9myep3fxsw26', '00010001', '00010001', '322691878277', '867321', '00', '02', '01', 957.00, 957.00, '20221018', '011800', '20221018', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018011800', '01', '0', '00000000', '43677141', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 957.00, '001', 957.00, 142.93, '88225703', '468778652610', '8548740045', '3014447867260475', '0', 957.00, '001');
INSERT INTO `f_t` VALUES (156, '00037809622794668248069', 'a9myep3fxsw26', '00010001', '00010001', '396125459564', '502634', '00', '02', '01', 996.00, 996.00, '20221018', '013300', '20221018', '000', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0001', '000', '84', '06', '20221018', '1018013300', '01', '0', '00000000', '43697293', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 996.00, '001', 996.00, 148.75, '38591398', '671291932217', '4180292675', '3943270367989532', '0', 996.00, '001');
INSERT INTO `f_t` VALUES (157, '00068953972963300286959', 'stvwybmx5hnj6', '00010003', '00010003', '173388074472', '097935', '00', '02', '07', 88.00, 88.00, '20221017', '235800', '20221017', '010', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221017', '1017235800', '01', '0', '00000000', '76180707', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 88.00, '001', 88.00, 13.14, '48637800', '825040651234', '2466480818', '2568329994285501', '0', 88.00, '001');
INSERT INTO `f_t` VALUES (158, '00044799467324185255348', 'stvwybmx5hnj6', '00010003', '00010003', '638830087247', '755966', '00', '02', '07', 907.00, 907.00, '20221018', '001500', '20221018', '141', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221018', '1018001500', '01', '0', '00000000', '15122418', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 907.00, '001', 907.00, 135.46, '03824073', '331846109647', '3830695383', '9565556454732460', '0', 907.00, '001');
INSERT INTO `f_t` VALUES (159, '00055489558421204331164', 'stvwybmx5hnj6', '00010003', '00010003', '860487085432', '192917', '00', '02', '07', 951.00, 951.00, '20221018', '003100', '20221018', '001', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221018', '1018003100', '01', '0', '00000000', '03709671', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 951.00, '001', 951.00, 142.03, '34631433', '473629199485', '4966732658', '6688922942830228', '0', 951.00, '001');
INSERT INTO `f_t` VALUES (160, '00052490116595856567146', 'stvwybmx5hnj6', '00010003', '00010003', '032571485258', '476488', '00', '02', '01', 924.00, 924.00, '20221018', '005100', '20221018', '061', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221018', '1018005100', '01', '0', '00000000', '15952817', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 924.00, '001', 924.00, 138.00, '23731785', '608828285439', '9778571524', '5209334299901769', '0', 924.00, '001');
INSERT INTO `f_t` VALUES (161, '00091389721040680178514', 'stvwybmx5hnj6', '00010003', '00010003', '441051451702', '811337', '00', '02', '01', 911.00, 911.00, '20221018', '005600', '20221018', '131', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221018', '1018005600', '01', '0', '00000000', '89075941', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 911.00, '001', 911.00, 136.06, '42173773', '076378948964', '9137047204', '1919880047601373', '0', 911.00, '001');
INSERT INTO `f_t` VALUES (162, '00072493956538682864921', 'stvwybmx5hnj6', '00010003', '00010003', '303814856957', '622250', '00', '02', '01', 999.00, 999.00, '20221018', '010400', '20221018', '021', '00000000', '000000000000000', 'XXXX', '0000', '0000', '0003', '000', '84', '06', '20221018', '1018010400', '01', '0', '00000000', '93974579', '2022-11-15 09:19:16', '2022-11-15 09:19:16', '0', '001', 999.00, '001', 999.00, 149.20, '88842037', '719653498711', '4883745532', '7051555201171683', '0', 999.00, '001');

-- ----------------------------
-- Table structure for gambling_card
-- ----------------------------
DROP TABLE IF EXISTS `gambling_card`;
CREATE TABLE `gambling_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_card
-- ----------------------------

-- ----------------------------
-- Table structure for gambling_f_t
-- ----------------------------
DROP TABLE IF EXISTS `gambling_f_t`;
CREATE TABLE `gambling_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for gambling_relative
-- ----------------------------
DROP TABLE IF EXISTS `gambling_relative`;
CREATE TABLE `gambling_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_relative
-- ----------------------------

-- ----------------------------
-- Table structure for gambling_store
-- ----------------------------
DROP TABLE IF EXISTS `gambling_store`;
CREATE TABLE `gambling_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_store
-- ----------------------------

-- ----------------------------
-- Table structure for gambling_trans
-- ----------------------------
DROP TABLE IF EXISTS `gambling_trans`;
CREATE TABLE `gambling_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_trans
-- ----------------------------

-- ----------------------------
-- Table structure for gambling_user
-- ----------------------------
DROP TABLE IF EXISTS `gambling_user`;
CREATE TABLE `gambling_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gambling_user
-- ----------------------------

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login`  (
  `role` int NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`username`, `password`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES (1, 'admin', 'pbkdf2_sha256$390000$zYuxTpLZ5c01BRIo5Tbld0$ti7eIbkfqP9BdkvszIb75V5Ox7ZmZ2qpqZG0kzMOGH4=');
INSERT INTO `login` VALUES (0, 'editor', 'pbkdf2_sha256$390000$srmZ3r0AaUFsDDuNR0Ece3$wh0WhcVcM2g5+zIr4rBPP91hJqK9rZs8CYIsZSP3Bik=');

-- ----------------------------
-- Table structure for marketing_card
-- ----------------------------
DROP TABLE IF EXISTS `marketing_card`;
CREATE TABLE `marketing_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_card
-- ----------------------------

-- ----------------------------
-- Table structure for marketing_f_t
-- ----------------------------
DROP TABLE IF EXISTS `marketing_f_t`;
CREATE TABLE `marketing_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for marketing_relative
-- ----------------------------
DROP TABLE IF EXISTS `marketing_relative`;
CREATE TABLE `marketing_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_relative
-- ----------------------------

-- ----------------------------
-- Table structure for marketing_store
-- ----------------------------
DROP TABLE IF EXISTS `marketing_store`;
CREATE TABLE `marketing_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_store
-- ----------------------------

-- ----------------------------
-- Table structure for marketing_trans
-- ----------------------------
DROP TABLE IF EXISTS `marketing_trans`;
CREATE TABLE `marketing_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_trans
-- ----------------------------

-- ----------------------------
-- Table structure for marketing_user
-- ----------------------------
DROP TABLE IF EXISTS `marketing_user`;
CREATE TABLE `marketing_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of marketing_user
-- ----------------------------

-- ----------------------------
-- Table structure for register_card
-- ----------------------------
DROP TABLE IF EXISTS `register_card`;
CREATE TABLE `register_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_card
-- ----------------------------

-- ----------------------------
-- Table structure for register_f_t
-- ----------------------------
DROP TABLE IF EXISTS `register_f_t`;
CREATE TABLE `register_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for register_relative
-- ----------------------------
DROP TABLE IF EXISTS `register_relative`;
CREATE TABLE `register_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_relative
-- ----------------------------

-- ----------------------------
-- Table structure for register_store
-- ----------------------------
DROP TABLE IF EXISTS `register_store`;
CREATE TABLE `register_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_store
-- ----------------------------

-- ----------------------------
-- Table structure for register_trans
-- ----------------------------
DROP TABLE IF EXISTS `register_trans`;
CREATE TABLE `register_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_trans
-- ----------------------------

-- ----------------------------
-- Table structure for register_user
-- ----------------------------
DROP TABLE IF EXISTS `register_user`;
CREATE TABLE `register_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of register_user
-- ----------------------------

-- ----------------------------
-- Table structure for relative
-- ----------------------------
DROP TABLE IF EXISTS `relative`;
CREATE TABLE `relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'gender',
  `age` int NULL DEFAULT NULL COMMENT 'age',
  `childList` json NULL COMMENT 'child set',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of relative
-- ----------------------------

-- ----------------------------
-- Table structure for store
-- ----------------------------
DROP TABLE IF EXISTS `store`;
CREATE TABLE `store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id_key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'level',
  `consumption_range` json NULL COMMENT 'consumption_range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'opening_hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'is_abnormal',
  `abnormal_state` json NULL COMMENT 'abnormal_type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 124 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for store_card
-- ----------------------------
DROP TABLE IF EXISTS `store_card`;
CREATE TABLE `store_card`  (
  `card_id` int NOT NULL AUTO_INCREMENT COMMENT 'Card id',
  `owner_type` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Owner type',
  `owner_id` int NULL DEFAULT NULL COMMENT 'Owner ID',
  `C4` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C4',
  `C5` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C5',
  `C6` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C6',
  `C7` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C7',
  `C8` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C8',
  `C9` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C9',
  `C10` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C10',
  `C11` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'C11',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`card_id`) USING BTREE,
  UNIQUE INDEX `C4`(`C4` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_card
-- ----------------------------

-- ----------------------------
-- Table structure for store_f_t
-- ----------------------------
DROP TABLE IF EXISTS `store_f_t`;
CREATE TABLE `store_f_t`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `F1` varchar(26) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F2` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F3` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F4` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F5` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F6` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F7` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F8` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F9` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F10` decimal(12, 2) NULL DEFAULT NULL,
  `F11` decimal(12, 2) NULL DEFAULT NULL,
  `F12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F16` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F18` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F20` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F21` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F22` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F23` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F24` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F25` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F26` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F27` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F28` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F29` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F31` timestamp NULL DEFAULT NULL,
  `F32` timestamp NULL DEFAULT NULL,
  `F33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F34` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F35` decimal(12, 2) NULL DEFAULT NULL,
  `F36` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F37` decimal(12, 2) NULL DEFAULT NULL,
  `F38` decimal(12, 2) NULL DEFAULT NULL,
  `F39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F40` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F41` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F42` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F43` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `F44` decimal(12, 2) NULL DEFAULT NULL,
  `F45` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_f_t
-- ----------------------------

-- ----------------------------
-- Table structure for store_relative
-- ----------------------------
DROP TABLE IF EXISTS `store_relative`;
CREATE TABLE `store_relative`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `user_id` int NOT NULL COMMENT 'user id',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `childList` json NULL COMMENT 'Children collection',
  `f_id` int NULL DEFAULT NULL COMMENT 'father id',
  `m_id` int NULL DEFAULT NULL COMMENT 'mather id',
  `c_id` int NULL DEFAULT NULL COMMENT 'couple id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_relative
-- ----------------------------

-- ----------------------------
-- Table structure for store_store
-- ----------------------------
DROP TABLE IF EXISTS `store_store`;
CREATE TABLE `store_store`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `industry` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Industry',
  `name_` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT 'Store name',
  `rank_` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Level',
  `consumption_range` json NULL COMMENT 'Spending range',
  `opening_hours` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Business hours',
  `S1` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S2` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S5` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S6` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S7` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S8` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S9` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S10` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S11` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S12` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S14` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S15` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S16` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S17` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S18` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `S19` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S20` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S21` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S22` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S23` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S24` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S26` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S27` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S28` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `S30` json NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_store
-- ----------------------------

-- ----------------------------
-- Table structure for store_trans
-- ----------------------------
DROP TABLE IF EXISTS `store_trans`;
CREATE TABLE `store_trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_trans
-- ----------------------------

-- ----------------------------
-- Table structure for store_user
-- ----------------------------
DROP TABLE IF EXISTS `store_user`;
CREATE TABLE `store_user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'ID primary key',
  `age` int NULL DEFAULT NULL COMMENT 'Age',
  `gender` int NULL DEFAULT NULL COMMENT 'Gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'Salary',
  `card` json NULL COMMENT 'Bank cards held',
  `abnormal` int NULL DEFAULT 0 COMMENT 'Is abnormal',
  `abnormal_state` json NULL COMMENT 'Abnormal type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Randomly generated encrypted user ID',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'Region field',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of store_user
-- ----------------------------

-- ----------------------------
-- Table structure for system_log
-- ----------------------------
DROP TABLE IF EXISTS `system_log`;
CREATE TABLE `system_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `change` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `time` datetime NOT NULL,
  `result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 193 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for trans
-- ----------------------------
DROP TABLE IF EXISTS `trans`;
CREATE TABLE `trans`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id_key',
  `T1` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T2` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T3` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T4` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T5` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T6` varchar(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `T7` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T8` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T9` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T10` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T11` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T12` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T13` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T14` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T15` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T16` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T17` decimal(12, 2) NULL DEFAULT NULL,
  `T18` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T19` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T20` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T21` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T22` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T23` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T24` varchar(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T25` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T26` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T27` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T28` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T29` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T30` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T31` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T32` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T33` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T34` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T35` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T36` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T37` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T38` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `T39` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `abnormal` int NULL DEFAULT 0 COMMENT 'is_abnormal',
  `abnormal_state` json NULL COMMENT 'abnormal_type',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15096 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;
-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id_key',
  `age` int NULL DEFAULT NULL COMMENT 'age',
  `gender` int NULL DEFAULT NULL COMMENT 'gender',
  `job` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `wage` int NULL DEFAULT NULL COMMENT 'wage',
  `card` json NULL COMMENT 'card',
  `abnormal` int NULL DEFAULT 0 COMMENT 'is_abnormal',
  `abnormal_state` json NULL COMMENT 'abnormal_type',
  `user_no` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'user_no',
  `loc_id` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT 'loc_id',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_no`(`user_no` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 201 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
