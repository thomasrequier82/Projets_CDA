package com.reseausocial.sql.entities;

import javax.persistence.*;

@Entity
@Table(name = "passwords")
public class Passwords {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String hash;
    private String type;


    public Passwords(){

    }

    public Passwords(String hash, String type) {
        setHash(hash);
        setType(type);
    }

    public int getId() {
        return id;
    }

    public String getHash() {
        return hash;
    }

    public void setHash(String hash) {
        this.hash = hash;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}
