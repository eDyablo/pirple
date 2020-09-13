package eyablonsky.pirple.java.AdvanceOOP;

import java.util.ArrayList;

public class Program {
    public static void main(final String[] args) {
        ArrayList<Vehicle> vehicles = new ArrayList<Vehicle>();

        Cars car = new Cars();
        vehicles.add(car);
        car.setMake("Heavy Motors");
        car.setModel("Bull");
        car.setYear(1999);
        car.setWeight(3f);
        for (int i = 0; i < 50; i++) {
            car.Drive();
            car.Stop();
        }

        car = new Cars();
        vehicles.add(car);
        car.setMake("LuxurZ");
        car.setModel("Silver");
        car.setYear(2001);
        car.setWeight(1.5f);
        for (int i = 0; i < 110; i++) {
            car.Drive();
            car.Stop();
        }

        car = new Cars();
        vehicles.add(car);
        car.setMake("Nebula");
        car.setModel("Model Y");
        car.setYear(2020);
        car.setWeight(1.35f);
        for (int i = 0; i < 110; i++) {
            car.Drive();
            car.Stop();
        }
        car.repair();
        for (int i = 0; i < 20; i++) {
            car.Drive();
            car.Stop();
        }

        for (Vehicle vehicle: vehicles) {
            vehicle.Print();
        }

        Planes plane = new Planes();
        plane.setMake("EveryoneCanFly");
        plane.setModel("Sparrow");
        plane.setYear(2000);
        plane.setWeight(1.0f);
        for (int i = 0; i < 102; i++) {
            plane.Fly();
            plane.Land();
        }
        plane.Print();
    }
}
