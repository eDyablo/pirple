package eyablonsky.pirple.java.AdvanceOOP;

public class Cars extends Vehicle {
    private boolean isDriving;

    public void Drive() {
        isDriving = true;
    }

    public void Stop() {
        if (isDriving) {
            tripsSinceMaintenance++;
            if (tripsSinceMaintenance > 100) {
                needsMaintenance = true;
            }
        }
        isDriving = false;
    }
}
