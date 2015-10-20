SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `DB_Tsyganov` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `DB_Tsyganov` ;

-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `about` TEXT NULL,
  `email` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NULL,
  `username` VARCHAR(255) NULL,
  `isAnonymous` TINYINT(1) NULL DEFAULT false,
  PRIMARY KEY (`email`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`Post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`Post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL,
  `message` TEXT NULL,
  `Forum_short_name` VARCHAR(255) NOT NULL,
  `thread` INT NOT NULL,
  `User_email` VARCHAR(255) NOT NULL,
  `isApproved` TINYINT(1) NULL DEFAULT false,
  `isDeleted` TINYINT(1) NULL DEFAULT false,
  `isEdited` TINYINT(1) NULL DEFAULT false,
  `isHighlighted` TINYINT(1) NULL DEFAULT false,
  `isSpam` TINYINT(1) NULL DEFAULT false,
  `likes` INT UNSIGNED NULL DEFAULT 0,
  `dislikes` INT UNSIGNED NULL DEFAULT 0,
  `mpath` VARCHAR(225) NOT NULL,
  PRIMARY KEY (`id`, `Forum_short_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`Thread`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`Thread` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL,
  `isClosed` TINYINT(1) NULL,
  `message` TEXT NULL,
  `slug` VARCHAR(255) NULL,
  `title` VARCHAR(255) NULL,
  `User_email` VARCHAR(255) NOT NULL,
  `Forum_short_name` VARCHAR(255) NOT NULL,
  `isDeleted` TINYINT(1) NULL DEFAULT false,
  `likes` INT UNSIGNED NULL DEFAULT 0,
  `dislikes` INT UNSIGNED NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uq_title_Forum` (`Forum_short_name` ASC, `title` ASC),
  UNIQUE INDEX `uq_slug_Forum` (`Forum_short_name` ASC, `slug` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`Forum`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`Forum` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `short_name` VARCHAR(255) NOT NULL,
  `User_email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`short_name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `short_name_UNIQUE` (`short_name` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`Followers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`Followers` (
  `Follower_email` VARCHAR(255) NOT NULL,
  `Followee_email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Follower_email`, `Followee_email`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_Tsyganov`.`Subscriptions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_Tsyganov`.`Subscriptions` (
  `User_email` VARCHAR(255) NOT NULL,
  `Thread_id` INT NOT NULL,
  PRIMARY KEY (`User_email`, `Thread_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
