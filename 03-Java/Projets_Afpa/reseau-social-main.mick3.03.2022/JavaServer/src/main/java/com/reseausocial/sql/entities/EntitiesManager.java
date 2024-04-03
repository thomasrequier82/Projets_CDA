package com.reseausocial.sql.entities;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;

public class EntitiesManager {
    private static final EntityManagerFactory emf = Persistence.createEntityManagerFactory("connect");
    private static final EntityManager em = emf.createEntityManager();
    private static final List<Infos> infosList = new ArrayList<>();
    private static final List<Utilisateurs> utilisateursList = new ArrayList<>();
    private static final List<Passwords> passwordsList = new ArrayList<>();

    public EntitiesManager() {
        throw new IllegalStateException("Utility class");
    }

    @Transactional
    public static void insertInfos(final Infos... infos) {
        em.getTransaction().begin();
        for (Infos info : infos) {
            infosList.add(info);
            em.persist(info);
        }
        em.getTransaction().commit();
    }
    @Transactional
    public static void insertUtilisateurs(final Utilisateurs... utilisateurs) {
        em.getTransaction().begin();
        for (Utilisateurs utilisateur : utilisateurs) {
            utilisateursList.add(utilisateur);
            em.persist(utilisateur);
        }
        em.getTransaction().commit();
    }
    @Transactional
    public static void insertPassword(final Passwords... passwords) {
        em.getTransaction().begin();
        for (final Passwords password : passwords) {
            passwordsList.add(password);
            em.persist(password);
        }
        em.getTransaction().commit();
    }

    public static List<Infos> getAllInfos(){
        final List<Infos> list = new ArrayList<>();
        for (Infos infos : infosList) {
            list.add(em.getReference(Infos.class, infos.getId()));
        }
        return list;
    }

    public static List<Utilisateurs> getAllUtilisateurs(){
        final List<Utilisateurs> list = new ArrayList<>();
        for (Utilisateurs utilisateurs : utilisateursList) {
            list.add(em.getReference(Utilisateurs.class, utilisateurs.getId()));
        }
        return list;
    }

    public static List<Passwords> getAllPasswords(){
        final List<Passwords> list = new ArrayList<>();
        for (Passwords passwords : passwordsList) {
            list.add(em.getReference(Passwords.class, passwords.getId()));
        }
        return list;
    }
}
