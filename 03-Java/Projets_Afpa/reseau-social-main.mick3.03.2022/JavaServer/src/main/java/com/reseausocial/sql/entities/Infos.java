package com.reseausocial.sql.entities;

import javax.persistence.*;
import java.util.Date;



@Entity
@Table(name = "infos_personnelles")
public class Infos {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String email;
    private String nom;
    private String prenom;
    @Column(name = "date_de_naissance")
    private Date dateNaissance;
    private String telephone;
    private String photo;

    public Infos() {
    }

    public Infos(String email, String nom, String prenom, Date dateNaissance, String telephone, String photo){
        setEmail(email);
        setNom(nom);
        setPrenom(prenom);
        setDateNaissance(dateNaissance);
        setTelephone(telephone);
        setPhoto(photo);
    }

    public int getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public Date getDateNaissance() {
        return dateNaissance;
    }

    public void setDateNaissance(Date dateNaissance) {
        this.dateNaissance = dateNaissance;
    }

    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
}
