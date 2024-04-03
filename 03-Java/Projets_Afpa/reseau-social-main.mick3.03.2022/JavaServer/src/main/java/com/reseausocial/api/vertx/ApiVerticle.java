package com.reseausocial.api.vertx;
import io.vertx.core.AbstractVerticle;
import io.vertx.core.Vertx;
import io.vertx.core.impl.logging.Logger;
import io.vertx.core.impl.logging.LoggerFactory;
import io.vertx.ext.web.Router;

/**
 * <code>ApiVerticle</code><br>
 * Handles connection to server and main router creation
 * @see AbstractVerticle
 */
public final class ApiVerticle extends AbstractVerticle {
    /**
     * <code>LOGGER</code> – Logger to use to show info, error, ... for the application<br>
     * @see Logger
     * @see LoggerFactory
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(ApiVerticle.class);
    /**
     * <code>start()</code>
     * @see io.vertx.core.Vertx
     * @see Router
     * @see UserResource
     * @see UserResource#getSubRouter(Vertx)
     * @see Override
     * @throws Exception If there's a problem during connection to server
     */
    @Override
    public void start() throws Exception {
        LOGGER.info("In start...");
        // Création du router
        final Router router = Router.router(vertx);
        // Création du serveur
        vertx.createHttpServer()
                .requestHandler(router)
                .listen(8080);
        // Création du subrouter qui s'occupera de toutes les routes se trouvant dans "/users/v1"
        final UserResource userResource = new UserResource();
        final Router userSubRouter = userResource.getSubRouter(vertx);
        router.mountSubRouter("/users", userSubRouter);
    }
}
