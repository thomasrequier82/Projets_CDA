package com.reseausocial.api.vertx;

import java.util.List;

import com.reseausocial.api.services.User;
import com.reseausocial.api.services.UserService;
import io.vertx.core.Vertx;
import io.vertx.core.impl.logging.Logger;
import io.vertx.core.impl.logging.LoggerFactory;
import io.vertx.core.json.Json;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;

/**
 * <code>UserResource</code><br>
 * Handles users api router.
 * @see Object
 */
public final class UserResource {
    /**
     * <code><b>CONSTANTS</b></code><br>
     * <code>LOGGER</code> – Logger to use to show info, error, ... for the application<br>
     * <code>APPJSON</code> – "application/json"<br>
     * <code>CONTENTTYPE</code> – "content-type"<br>
     * <code>userService</code> – UserService
     * @see Logger
     * @see LoggerFactory
     * @see UserService
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(UserResource.class);
    private static final String APPJSON = "application/json";
    private static final String CONTENTTYPE = "content-type";
    private static final UserService userService = new UserService();

    /**
     * <code>getSubRouter(Vertx)</code>
     *
     * @param vertx Vertx used in main Router
     * @return Sub Router
     * @see Vertx
     * @see Router
     * @see BodyHandler
     */
    public Router getSubRouter(final Vertx vertx) {
        final Router subRouter = Router.router(vertx);
        // Body handler (permet de récupérer des données quand on fait un POST/PUT)
        subRouter.route("/*").handler(BodyHandler.create());
        // Routes
        subRouter.get("/").handler(this::getAllUsers);
        subRouter.get("/:id").handler(this::getOneUser);
        subRouter.post("/").handler(this::createOneUser);
        subRouter.post("/:id").handler(this::createOneUser);
        subRouter.put("/:id").handler(this::updateOneUser);
        subRouter.delete("/:id").handler(this::deleteOneUser);
        return subRouter;
    }

    /**
     * <code>getAllUsers(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @see RoutingContext
     * @see List
     * @see User
     * @see UserService#findAll()
     * @see JsonObject
     * @see Json
     * @see #routingResponse(RoutingContext, int, String)
     */
    private void getAllUsers(final RoutingContext routingContext) {
        LOGGER.info("In getAllUsers");
        final List<User> users = userService.findAll();
        final JsonObject jsonObject = new JsonObject();
        jsonObject.put("users", users);
        routingResponse(routingContext, 200, Json.encode(jsonObject));
    }

    /**
     * <code>getOneUser(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @see RoutingContext
     * @see Integer
     * @see User
     * @see JsonObject
     * @see Json
     * @see #bodyGetId(RoutingContext)
     * @see #createJsonError(String)
     * @see #routingResponse(RoutingContext, int, String)
     */
    private void getOneUser(final RoutingContext routingContext) {
        LOGGER.info("In getOneUser...");
        final Integer id = this.bodyGetId(routingContext);
        if (id == null) {
            return;
        }
        final User user = userService.findById(id);
        if (user == null) {
            JsonObject jsonObject = this.createJsonError("No user can be found for the specified id:" + id);
            routingResponse(routingContext, 404, Json.encode(jsonObject));
            return;
        }
        routingResponse(routingContext, 200, Json.encode(user));
    }

    /**
     * <code>createOneUser(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @see RoutingContext
     * @see JsonObject
     * @see Integer
     * @see User
     * @see Json
     * @see #bodyGetId(RoutingContext, JsonObject)
     * @see UserService#findById(int)
     * @see #routingResponse(RoutingContext, int, String)
     * @see #createJsonError(String)
     */
    private void createOneUser(final RoutingContext routingContext) {
        LOGGER.info("In createOneUser");
        final JsonObject body = routingContext.getBodyAsJson();
        final Integer id = this.bodyGetId(routingContext, body);
        if (id == null) {
            return;
        }
        if (userService.findById(id) == null) {
            final String name = body.getString("name");
            final String sex = body.getString("sex");
            final int age = body.getInteger("age");
            final User user = new User(id, name, sex, age);
            userService.add(user);
            routingResponse(routingContext, 201, Json.encode(user));
        } else {
            final JsonObject jsonObject = this.createJsonError(
                    "User with this id already exists. Use PUT instead to update.");
            jsonObject.put("user:", userService.findById(id));
            routingResponse(routingContext, 405, Json.encode(jsonObject));
        }
    }

    /**
     * <code>updateOneUser(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @see RoutingContext
     * @see JsonObject
     * @see Integer
     * @see User
     * @see Json
     * @see #bodyGetId(RoutingContext, JsonObject)
     * @see #createJsonError(String)
     * @see #routingResponse(RoutingContext, int, String)
     */
    private void updateOneUser(final RoutingContext routingContext) {
        LOGGER.info("In updateOneUser...");
        final JsonObject body = routingContext.getBodyAsJson();
        final Integer id = this.bodyGetId(routingContext, body);
        if (id == null) {
            return;
        }
        final User user = userService.findById(id);
        if (user == null) {
            final JsonObject jsonObject = this.createJsonError(
                    "User with this id doesn't exist. Use POST instead to create it.");
            routingResponse(routingContext, 405, Json.encode(jsonObject));
        } else {
            final String name = body.getString("name");
            final String sex = body.getString("sex");
            final int age = body.getInteger("age");
            final User newUser = new User(id, name, sex, age);
            userService.update(newUser);
            routingResponse(routingContext, 200, Json.encode(user));
        }
    }

    /**
     * <code>deleteOneUser(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @see RoutingContext
     * @see Integer
     * @see User
     * @see JsonObject
     * @see Json
     * @see UserService#findById(int)
     * @see #createJsonError(String)
     * @see #routingResponse(RoutingContext, int)
     */
    private void deleteOneUser(final RoutingContext routingContext) {
        LOGGER.info("In deleteOneUser");
        final int id = Integer.parseInt(routingContext.request().getParam("id"));
        final User user = userService.findById(id);
        if (user == null) {
            final JsonObject jsonObject = this.createJsonError(
                    "No user can be found for the specified id: " + id);
            routingResponse(routingContext, 404, Json.encode(jsonObject));
            return;
        }
        userService.remove(id);
        routingResponse(routingContext, 200);
    }

    /**
     * <code>bodyGetId(RoutingContext)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @return <code>Integer</code> or <code>null</code> if no id found
     * @see Integer
     * @see NumberFormatException
     * @see JsonObject
     * @see Json
     * @see #createJsonError(String)
     * @see #routingResponse(RoutingContext, int, String)
     */
    private Integer bodyGetId(final RoutingContext routingContext) {
        int id;
        try {
            id = Integer.parseInt(routingContext.request().getParam("id"));
            return id;
        } catch (NumberFormatException nfe) {
            final JsonObject jsonObject = this.createJsonError("Incorrect id");
            routingResponse(routingContext, 404, Json.encode(jsonObject));
            return null;
        }
    }

    /**
     * <code>bodyGetId(RoutingContext, jSonObject)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @param body           <code>JsonObject</code> Current body to check from, in Json format
     * @return <code>Integer</code> or <code>null</code> if no id found
     * @see Integer
     * @see NumberFormatException
     * @see JsonObject
     * @see Json
     * @see #routingResponse(RoutingContext, int, String)
     * @see #createJsonError(String)
     */
    private Integer bodyGetId(final RoutingContext routingContext, final JsonObject body) {
        int id;
        try {
            id = body.getInteger("id");
            return id;
        } catch (NumberFormatException nfe) {
            try {
                id = Integer.parseInt(routingContext.request().getParam("id"));
                return id;
            } catch (NumberFormatException nfe2) {
                final JsonObject jsonObject = this.createJsonError("Incorrect id");
                routingResponse(routingContext, 404, Json.encode(jsonObject));
                return null;
            }
        }
    }

    /**
     * <code>createJsonError(String)</code>
     *
     * @param value <code>String</code> Value of Json Object
     * @return <code>JsonObject</code> {"Error": value}
     * @see String
     * @see JsonObject
     */
    private JsonObject createJsonError(final String value) {
        final JsonObject jsonObject = new JsonObject();
        jsonObject.put("Error", value);
        return jsonObject;
    }

    /**
     * <code>routingResponse(RoutingContext, int)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @param statusCode     <code>int</code> Status Code (200 = OK, 404 = Not Found, ...)
     */
    private void routingResponse(final RoutingContext routingContext, final int statusCode) {
        routingContext.response()
                .setStatusCode(statusCode)
                .putHeader(CONTENTTYPE, APPJSON)
                .end();
    }

    /**
     * <code>routingResponse(RoutingContext, int, end)</code>
     *
     * @param routingContext <code>RoutingContext</code> to get request & response info
     * @param statusCode     <code>int</code> Status Code (200 = OK, 404 = Not Found, ...)
     * @param end            <code>String</code> to show once response is done
     */
    private void routingResponse(final RoutingContext routingContext, final int statusCode, final String end) {
        routingContext.response()
                .setStatusCode(statusCode)
                .putHeader(CONTENTTYPE, APPJSON)
                .end(end);
    }
}