package com.reseausocial.api.vertx;
import io.vertx.core.Vertx;
import io.vertx.core.impl.logging.Logger;
import io.vertx.core.impl.logging.LoggerFactory;

/**
 * <code>VertxApp</code><br>
 * Main Java Class of the app.
 * @see java.lang.Object
 * @author Mick
 */
public class VertxApp {
    /**
     * <code><b>CONSTANTS</b></code><br>
     * <code>LOGGER</code> – Logger to use to show info, error, ... for the application<br>
     * <code>PORT</code> – Port to use<br>
     * <code>API_DIRECTORY</code> – Main directory to use
     * @see Logger
     * @see LoggerFactory
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(VertxApp.class);
    /**
     * <code>main</code>
     * @param args <code>String[]</code>
     */
    public static void main(String[] args) {
        LOGGER.info("App...");
        // Initialisation de Vertx
        final Vertx vertx = Vertx.vertx();
        // Déploiement du Verticle
        vertx.deployVerticle(new ApiVerticle());
    }
}
