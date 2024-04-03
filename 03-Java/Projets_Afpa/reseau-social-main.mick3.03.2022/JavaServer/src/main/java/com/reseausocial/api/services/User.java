package com.reseausocial.api.services;

import java.io.Serializable;

/**
 * <code>User</code><br>
 * Holds all information for one user.
 * @see java.lang.Object
 */
public class User implements Serializable {
    private int id;
    private String name;
    private String sex;
    private int age;

    public User(){}

    /**
     * <code>User(int, String, String, int)</code>
     * @param id <code>int</code> User's id
     * @param name <code>String</code> User's name
     * @param sex <code>String</code> User's sex ("M"/"F")
     * @param age <code>int</code> User's age
     */
    public User(final int id, final String name, final String sex, final int age){
        this.setId(id);
        this.setName(name);
        this.setSex(sex);
        this.setAge(age);
    }

    public int getId() {
        return id;
    }

    public void setId(final int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(final String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(final String sex) {
        this.sex = sex;
    }

    public int getAge() {
        return age;
    }

    public void setAge(final int age) {
        this.age = age;
    }
}
//public record User(int id, String name, String sex, int age){}


