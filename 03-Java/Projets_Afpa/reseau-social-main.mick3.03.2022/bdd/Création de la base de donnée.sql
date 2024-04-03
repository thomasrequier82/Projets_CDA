#supression la base de données dans le cas où elle éxiste
DROP DATABASE IF EXISTS `reseau_social`;
#création la base de données
CREATE DATABASE `reseau_social`;
#utilisation de la base de données
USE `reseau_social`;
#création de la table infos personnelles liées à la table utilisateurs
CREATE TABLE `infos_personnelles`
(
    `email`             VARCHAR(255) NOT NULL UNIQUE KEY,
    `nom`               VARCHAR(255),
    `prenom`            VARCHAR(255),
    `date_de_naissance` DATE,
    `telephone`         VARCHAR(255),
    `photo`             VARCHAR(255),
    PRIMARY KEY (`email`)
);
#création de la table password liée à la table utilisateurs
CREATE TABLE `passwords`
(
    `id`   INTEGER(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `hash` VARCHAR(255),
    `type` VARCHAR(255)
);
#création de la table utilisateurs
CREATE TABLE `utilisateurs`
(
    `id`       INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `password` INTEGER(5),
    `login`    VARCHAR(255),
    FOREIGN KEY (`password`) REFERENCES passwords (`id`),
    FOREIGN KEY (`login`) REFERENCES infos_personnelles (`email`)
);