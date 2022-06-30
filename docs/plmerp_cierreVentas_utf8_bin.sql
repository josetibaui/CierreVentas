-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: plmerp_cierreVentas
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ba_bancos`
--

DROP TABLE IF EXISTS `ba_bancos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ba_bancos` (
  `idBanco` int unsigned NOT NULL AUTO_INCREMENT,
  `banco` varchar(255) NOT NULL,
  `cuentaContabilidad` varchar(16) DEFAULT NULL,
  `estado` smallint NOT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idBanco`),
  UNIQUE KEY `banBanco_UK` (`banco`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ig_locales`
--

DROP TABLE IF EXISTS `ig_locales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ig_locales` (
  `idLocal` int unsigned NOT NULL AUTO_INCREMENT,
  `codLocal` smallint unsigned NOT NULL,
  `local` varchar(64) NOT NULL,
  `alias` varchar(64) DEFAULT NULL,
  `tipo` varchar(1) NOT NULL DEFAULT 'V',
  `ciudad` varchar(64) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `referencia` varchar(255) DEFAULT NULL,
  `codigoArea` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) NOT NULL,
  `codigoPostal` varchar(6) DEFAULT NULL,
  `estado` smallint unsigned NOT NULL DEFAULT '1',
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idLocal`),
  UNIQUE KEY `igLocal_codLocal_UK` (`codLocal`),
  UNIQUE KEY `igLocal_local_UK` (`local`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ig_log`
--

DROP TABLE IF EXISTS `ig_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ig_log` (
  `idLog` int unsigned NOT NULL AUTO_INCREMENT,
  `tabla` varchar(45) NOT NULL,
  `idPersona` int unsigned NOT NULL COMMENT 'id de la persona que realizó la acción',
  `fechaHora` varchar(45) NOT NULL,
  `preCondicion` json DEFAULT NULL COMMENT 'Estado del resgistro anrtes de realizar la acción',
  `postCondicion` json DEFAULT NULL,
  PRIMARY KEY (`idLog`),
  KEY `igLog_persona_FK_idx` (`idPersona`),
  KEY `igLog_tablafechaHora_IDX` (`tabla`,`fechaHora`),
  KEY `igLog_tablaPersonaFecha_IDX` (`tabla`,`idPersona`,`fechaHora`),
  CONSTRAINT `igLog_persona_FK` FOREIGN KEY (`idPersona`) REFERENCES `pe_personas` (`idPersona`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_cierreVentas`
--

DROP TABLE IF EXISTS `loc_cierreVentas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_cierreVentas` (
  `idCierreVentas` int unsigned NOT NULL AUTO_INCREMENT,
  `idLocal` int unsigned NOT NULL,
  `fecha` date NOT NULL,
  `ventaTotal` decimal(14,4) NOT NULL DEFAULT '0.0000',
  `diferencia` decimal(14,4) NOT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idCierreVentas`),
  UNIQUE KEY `locCierreVentas_locFecha_UK` (`idLocal`,`fecha`),
  CONSTRAINT `locCierreVentas_idLocal_FK` FOREIGN KEY (`idLocal`) REFERENCES `ig_locales` (`idLocal`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_cierreVentas_depositos`
--

DROP TABLE IF EXISTS `loc_cierreVentas_depositos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_cierreVentas_depositos` (
  `idCierreVentasDepositos` int unsigned NOT NULL AUTO_INCREMENT,
  `idCierreVentas` int unsigned NOT NULL,
  `idBanco` int unsigned NOT NULL,
  `valor` decimal(14,4) NOT NULL DEFAULT '0.0000',
  `observaciones` varchar(255) DEFAULT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idCierreVentasDepositos`),
  KEY `locCVDepositos_FK_idx` (`idCierreVentas`),
  KEY `locCV_Depositos_Banco_FK_idx` (`idBanco`),
  CONSTRAINT `locCV_Depositos_Banco_FK` FOREIGN KEY (`idBanco`) REFERENCES `ba_bancos` (`idBanco`) ON UPDATE CASCADE,
  CONSTRAINT `locCV_Depositos_CierreVentas_FK` FOREIGN KEY (`idCierreVentas`) REFERENCES `loc_cierreVentas` (`idCierreVentas`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_cierreVentas_egresos`
--

DROP TABLE IF EXISTS `loc_cierreVentas_egresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_cierreVentas_egresos` (
  `idcve` int unsigned NOT NULL AUTO_INCREMENT,
  `idCierreVentas` int unsigned NOT NULL,
  `idlocEgreso` int unsigned NOT NULL,
  `valor` decimal(14,4) NOT NULL DEFAULT '0.0000',
  `descripcion` varchar(45) DEFAULT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idcve`),
  KEY `locCVE_idCierreVentas_FK_idx` (`idCierreVentas`),
  KEY `locCVE_idEgresos_FK_idx` (`idlocEgreso`),
  CONSTRAINT `locCVE_idCierreVentas_FK` FOREIGN KEY (`idCierreVentas`) REFERENCES `loc_cierreVentas` (`idCierreVentas`) ON UPDATE CASCADE,
  CONSTRAINT `locCVE_idEgresos_FK` FOREIGN KEY (`idlocEgreso`) REFERENCES `loc_egresos` (`idLocEgreso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_cierreVentas_formaPagos`
--

DROP TABLE IF EXISTS `loc_cierreVentas_formaPagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_cierreVentas_formaPagos` (
  `idcvfp` int unsigned NOT NULL AUTO_INCREMENT,
  `idCierreVentas` int unsigned NOT NULL,
  `idFormaPago` int unsigned NOT NULL,
  `valor` decimal(14,4) NOT NULL DEFAULT '0.0000',
  `descripcion` varchar(255) DEFAULT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idcvfp`),
  KEY `locCVFP_idcv_FK_idx` (`idCierreVentas`),
  KEY `locCVFP_formapago_FK_idx` (`idFormaPago`),
  CONSTRAINT `locCVFP_formapago_FK` FOREIGN KEY (`idFormaPago`) REFERENCES `loc_formaPagos` (`idFormaPagos`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `locCVFP_idcv_FK` FOREIGN KEY (`idCierreVentas`) REFERENCES `loc_cierreVentas` (`idCierreVentas`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_cierreVentas_pagosPersonal`
--

DROP TABLE IF EXISTS `loc_cierreVentas_pagosPersonal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_cierreVentas_pagosPersonal` (
  `idCVPP` int unsigned NOT NULL AUTO_INCREMENT,
  `idCierreVentas` int unsigned NOT NULL,
  `idPagosPersonal` int unsigned NOT NULL,
  `idPersona` int unsigned NOT NULL,
  `valor` decimal(14,4) NOT NULL DEFAULT '0.0000',
  `descripcion` varchar(255) DEFAULT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idCVPP`),
  UNIQUE KEY `loc_cvpp_idCierrePagoPersona_UK` (`idCierreVentas`,`idPagosPersonal`,`idPersona`),
  KEY `loc_cvpp_pagoPersonal_FK_idx` (`idPagosPersonal`),
  KEY `loc_cvpp_persona_FK_idx` (`idPersona`),
  CONSTRAINT `loc_cvpp_cierreVentas_FK` FOREIGN KEY (`idCierreVentas`) REFERENCES `loc_cierreVentas` (`idCierreVentas`) ON UPDATE CASCADE,
  CONSTRAINT `loc_cvpp_pagoPersonal_FK` FOREIGN KEY (`idPagosPersonal`) REFERENCES `loc_pagosPersonal` (`idPagosPersonal`) ON UPDATE CASCADE,
  CONSTRAINT `loc_cvpp_persona_FK` FOREIGN KEY (`idPersona`) REFERENCES `pe_personas` (`idPersona`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_egresos`
--

DROP TABLE IF EXISTS `loc_egresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_egresos` (
  `idLocEgreso` int unsigned NOT NULL AUTO_INCREMENT,
  `egreso` varchar(255) NOT NULL,
  `cuentaContabilidad` varchar(8) DEFAULT NULL,
  `estado` varchar(45) NOT NULL DEFAULT '1',
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idLocEgreso`),
  UNIQUE KEY `locEgresos_UK` (`egreso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_egresos_no_locales`
--

DROP TABLE IF EXISTS `loc_egresos_no_locales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_egresos_no_locales` (
  `idEgresoNoLocal` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Cuenta de egreso que no sea aplicable en algún local',
  `idEgreso` int unsigned NOT NULL,
  `idLocal` int unsigned NOT NULL,
  `estado` smallint NOT NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idEgresoNoLocal`),
  UNIQUE KEY `loc_egresoNoLocal_UK` (`idLocal`,`idEgreso`),
  KEY `locEgresoNoLocal_idEgreso_FK_idx` (`idEgreso`),
  CONSTRAINT `locEgresoNoLocal_idEgreso_FK` FOREIGN KEY (`idEgreso`) REFERENCES `loc_egresos` (`idLocEgreso`) ON UPDATE CASCADE,
  CONSTRAINT `locEgresoNoLocal_idLocal_FK` FOREIGN KEY (`idLocal`) REFERENCES `ig_locales` (`idLocal`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='Lo normal es que todos los egresos sean aplicables en todos los locales. En esta tabla se registran las cuentas de egresos que no se deben aplicar a un local. Esta lista siempre será más corta, o quizás nula, que la de los cuentas que se usan en cada local.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_formaPagos`
--

DROP TABLE IF EXISTS `loc_formaPagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_formaPagos` (
  `idFormaPagos` int unsigned NOT NULL AUTO_INCREMENT,
  `formaPago` varchar(255) NOT NULL,
  `cuentaContabilidad` varchar(16) DEFAULT NULL,
  `estado` varchar(45) NOT NULL DEFAULT '1',
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idFormaPagos`),
  UNIQUE KEY `locFormaPagos_UK` (`formaPago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loc_pagosPersonal`
--

DROP TABLE IF EXISTS `loc_pagosPersonal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc_pagosPersonal` (
  `idPagosPersonal` int unsigned NOT NULL AUTO_INCREMENT,
  `tipoPago` varchar(255) NOT NULL,
  `cuentaContabilidad` varchar(8) DEFAULT NULL,
  `estado` varchar(45) NOT NULL DEFAULT '1',
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idPagosPersonal`),
  UNIQUE KEY `locPagosPersoanl_UK` (`tipoPago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pe_historia`
--

DROP TABLE IF EXISTS `pe_historia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pe_historia` (
  `idPeHistoria` int unsigned NOT NULL AUTO_INCREMENT,
  `idPersona` int unsigned NOT NULL,
  `fecha` date NOT NULL,
  `idLocal` int unsigned DEFAULT NULL COMMENT 'Para registrar un ingreso o un cambio de local se pone el local, para registrar una salida, se deja el local en blanco(nulo)',
  `descripcion` varchar(255) NULL,
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idPeHistoria`),
  KEY `peHistoria_Idlocal_FK_idx` (`idLocal`),
  KEY `peHistoria_idPersona_FK_idx` (`idPersona`),
  CONSTRAINT `peHistoria_Idlocal_FK` FOREIGN KEY (`idLocal`) REFERENCES `ig_locales` (`idLocal`) ON UPDATE CASCADE,
  CONSTRAINT `peHistoria_idPersona_FK` FOREIGN KEY (`idPersona`) REFERENCES `pe_personas` (`idPersona`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pe_personas`
--

DROP TABLE IF EXISTS `pe_personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pe_personas` (
  `idPersona` int unsigned NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `tipoIdentificacion` char(2) NOT NULL,
  `identificacion` varchar(45) NOT NULL,
  `codigoNomina` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `estado` varchar(45) NOT NULL DEFAULT '1',
  `idPor` INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY (`idPersona`),
  UNIQUE KEY `pePersona_nombreApellido_UK` (`nombres`,`apellidos`),
  UNIQUE KEY `pePersoana_identificacion_IK` (`tipoIdentificacion`,`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'plmerp_cierreVentas'
--

--
-- Dumping routines for database 'plmerp_cierreVentas'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-16 15:13:28
