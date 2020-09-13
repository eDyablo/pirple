package eyablonsky.pirple.java.AdvanceOOP;

public class Planes extends Vehicle {
    private boolean isFlying;

    public boolean Fly() {
        if (needsMaintenance) {
            isFlying = false;
            System.err.println("Can't fly until it's repaired");
        } else {
            isFlying = true;
        }
        return isFlying;
    }

    public void Land() {
        if (isFlying) {
            tripsSinceMaintenance++;
            if (tripsSinceMaintenance >= 100) {
                needsMaintenance = true;
            }
        }
        isFlying = false;
    }
}
