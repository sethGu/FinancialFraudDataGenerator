/*
 Navicat Premium Data Transfer

 Source Server         : bank
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : sf_web_001

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 05/07/2023 21:45:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for operator
-- ----------------------------
DROP TABLE IF EXISTS `operator`;
CREATE TABLE `operator`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `original_ID` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '原始ID',
  `contactor` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '触点',
  `contactor_ID` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '触点ID',
  `mobile_phone_brand` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机品牌',
  `mobile_operating_system` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机操作系统',
  `pv` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'pv',
  `terminal_type` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '终端类型',
  `video_website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '视频网站',
  `shopping_website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '购物网站',
  `overseas_taobao_shopping_channel` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '海淘购物渠道',
  `automotive_website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '汽车网站',
  `real_estate_website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '房产网站',
  `travel_website` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '旅游网站',
  `highest_calling` decimal(18, 0) NULL DEFAULT 0 COMMENT '当月内用户日最高主叫通话次数',
  `city_number` decimal(18, 0) NULL DEFAULT 0 COMMENT '当月与该号码通话的对端所属城市数量',
  `day_calling` decimal(18, 0) NULL DEFAULT 0 COMMENT '工作日白天主叫通话次数',
  `night_calling` decimal(18, 0) NULL DEFAULT 0 COMMENT '工作日夜间通话天数',
  `three_month_calling` decimal(18, 0) NULL DEFAULT 0 COMMENT '近三月月均主叫通话次数',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
