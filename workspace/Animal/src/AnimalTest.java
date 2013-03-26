/**
 * Homework 5. Exploring the use of Comparators and learning how to sort
 * in Java.
 * @author jgibson
 * @date 2-18-13
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
		Dog d = new Dog();
		Cat c = new Cat();
		
		d.setSize(20);
		d.setName("One");
		d.setBreed("lab");
		c.setSize(1);
		c.setName("Two");
		c.setBreed("saimese");
		
		AnimalPack animals = new AnimalPack();
		animals.makeArray(2);
		
		animals.addAnimal(1, d);
		animals.addAnimal(1, c);
		
		System.out.println(animals.geoMean());
		System.out.println(AnimalPack.geoMean(animals));
		
		System.out.println(animals.toString());
		
		animals.sortBySize();
		System.out.println(animals.toString());
		
		animals.sortByBreed();
		System.out.println(animals.toString());
		
	}

}
