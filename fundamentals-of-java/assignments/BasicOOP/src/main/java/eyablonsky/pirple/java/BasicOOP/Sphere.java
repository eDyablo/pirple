package eyablonsky.pirple.java.BasicOOP;

import java.lang.Math;

public class Sphere {
    private float radius;

    public Sphere(float radius) {
        this.radius = radius;
    }

    public float radius() {
        return this.radius;
    }

    public float diameter() {
        return radius * 2.0f;
    }

    public float circumference() {
        return 2f * (float)Math.PI * radius;
    }

    public float surfaceArea() {
        return 4f * (float)Math.PI * (float)Math.pow(radius, 2);
    }

    public float volume() {
        return 4f/3f * (float)Math.PI * (float)Math.pow(radius, 3);
    }
}