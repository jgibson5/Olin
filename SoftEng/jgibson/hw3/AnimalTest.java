/**
 * Homework 3. Exploring the use of interfaces and abstract classes in Java.
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
		
		System.out.println(d.fetch("Lisa"));
	}

}
