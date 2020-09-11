package eyablonsky.pirple.java.BasicOOP;

public class Program {
    public static void main(final String[] args) {
        Sphere sphere = new Sphere(3.1415926f);
        System.out.println("radius:        " + sphere.radius());
        System.out.println("diameter:      " + sphere.diameter());
        System.out.println("circumference: " + sphere.circumference());
        System.out.println("surface area:  " + sphere.surfaceArea());
        System.out.println("volume:        " + sphere.volume());
    }
}
