package com.reseausocial.api.services;

import com.reseausocial.sql.entities.EntitiesManager;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <code>UserService</code><br>
 * Initiates, finds, creates or updates users from a users HashMap.
 * @see Object
 */
public final class UserService {
    /**
     * @see HashMap
     */
    private static final Map<Integer, User> users = new HashMap<>();
    /**
     * <code>UserService()</code> Constructor
     * @see #initUsers()
     */
    public UserService(){
        initUsers();
    }
    /**
     * <code>initUsers()</code> Users Initialization
     * @see #add(User...)
     * @see User
     */
    private void initUsers(){
        this.add(
                new User(0, "Fred", "F", 38),
                new User(1, "Chad", "M", 26),
                new User(2, "Cédric", "M", 23),
                new User(3, "Guillaume", "M", 23),
                new User(4, "Allaye", "M", 28),
                new User(5, "Javier", "M", 32),
                new User(6, "Tito", "M", 38),
                new User(7, "Mickaël", "M", 32),
                new User(8,"Labib","M",27),
                new User(9,"Thomas","M",39)
        );
    }
    /**
     * <code>findAll()</code> : Find all Users
     * @return <code>List</code> of Users
     * @see List
     * @see User
     * @see HashMap
     * @see java.util.stream.Stream
     */
    public List<User> findAll() {
        return users.values().stream().toList();
    }
    /**
     * <code>findById(id)</code> : Find a User by its id
     * @param id <code>int</code> : User id
     * @return <code>User</code>
     * @see User
     * @see HashMap
     */
    public User findById(final int id) {
        return users.get(id);
    }
    /**
     * <code>update(User)</code> : Update user info
     * @param user <code>User</code> : User to update
     * @see User
     * @see HashMap
     */
    public void update(final User user){
        users.replace(user.getId(), user);
    }
    /**
     * <code>remove(id)</code> : Remove user at id from hash
     * @param id <code>int</code> : User's id
     * @see HashMap
     */
    public void remove(final int id){
        users.remove(id);
    }
    /**
     * <code>add(User Array)</code> Add users to hash
     * @param tUsers <code>Array</code> : Array of User Objects
     * @see #add(User)
     * @see User
     * @see java.util.Arrays
     */
    public void add(final User... tUsers){
        for (User user : tUsers) {
            this.add(user);
        }
    }
    /**
     * <code>add(User)</code> Add user to hash
     * @param user User object
     * @see User
     * @see HashMap
     */
    public void add(final User user){
        users.put(user.getId(), user);
    }
}
