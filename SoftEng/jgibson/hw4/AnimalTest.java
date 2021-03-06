/**
 * Homework 4. Exploring the use of constructors and static variables, methods, 
 * and classes in Java.
 * @author jgibson
 * @date 2-6-13
 * @course Software Engineering
 * @professor Allen Downey
 *
 */
public class AnimalTest {

	/**
	 * Main method for Animal package.
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println("TEST");
		
		Dog d = new Dog();
		Cat c = new Cat();
		
		d.makeNoise();
		c.makeNoise();
		
		d.setSize(20);
		c.setSize(1);
		System.out.println(d.isBigger(c));
		
		AnimalPack animals = new AnimalPack();
		animals.makeArray(2);
		
		animals.addAnimal(1, c);
		animals.addAnimal(1, d);
		
		animals.makeNoise();
		
		System.out.println(animals.biggestAnimal());
		System.out.println(animals.geoMean());
		System.out.println(AnimalPack.geoMean(animals));

		System.out.println(d.fetch("Test"));
	}

}
