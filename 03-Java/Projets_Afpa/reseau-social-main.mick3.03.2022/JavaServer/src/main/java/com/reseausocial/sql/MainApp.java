package com.reseausocial.sql;

import com.reseausocial.sql.entities.Infos;
import com.reseausocial.sql.entities.EntitiesManager;
import java.util.Date;

public class MainApp {


    /*
      INSERT INTO passwords(hash, type) VALUES ("","MD5");
      INSERT INTO infos_personnelles(email, nom, prenom, date_de_naissance, telephone, photo) VALUES ("","","","","","")
      INSERT INTO utilisateurs(password, login) VALUES ((SELECT id FROM passwords WHERE hash = ""),
      (SELECT email FROM infos_personnelles WHERE email = ""));
     */

    public static void main(String[] args) {
        EntitiesManager.insertInfos(
                new Infos("mail@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto"),
                new Infos("mail1@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto"),
                new Infos("mail2@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto"),
                new Infos("mail3@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto"),
                new Infos("mail4@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto"),
                new Infos("mail5@mail.com", "nom", "prénom", new Date(), "tel", "urlPhoto")
        );
        System.out.println(EntitiesManager.getAllInfos());
    }
}
