package eyablonsky.pirple.java.AdvanceOOP;

public abstract class Vehicle {
    private String make;
    private String model;
    private int year;
    private float weight;
    protected boolean needsMaintenance;
    protected int tripsSinceMaintenance;

    protected Vehicle() {
        make = "unknown";
        model = "unknown";
    }

    public void setMake(String value) {
        make = value;
    }

    public void setModel(String value) {
        model = value;
    }

    public void setYear(int value) {
        year = value;
    }

    public void setWeight(float value) {
        weight = value;
    }
    
    public void Print() {
        System.out.println("Make:   " + make);
        System.out.println("Model:  " + model);
        System.out.println("Year:   " + year);
        System.out.println("Weight: " + weight);
        System.out.println("Trips:  " + tripsSinceMaintenance);
        if (needsMaintenance) {
            System.out.println("Needs maintenance");
        } else {
            System.out.println("No maintenance needed");
        }
    }

    public void repair() {
        needsMaintenance = false;
        tripsSinceMaintenance = 0;
    }
}
