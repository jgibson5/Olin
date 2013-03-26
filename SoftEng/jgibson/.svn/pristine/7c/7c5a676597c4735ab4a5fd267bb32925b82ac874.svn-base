import java.util.ArrayList;
import java.util.Collections;

public class AnimalPack {
	private ArrayList<Animal> animals = new ArrayList<Animal>();
	
	public AnimalPack() {
		/*
		 * Animal Pack Constructor.
		 */
	}
	
	public AnimalPack(int size) {
		/*
		 * Animal Pack Constructor.
		 */
		this();
		makeArray(size);
	}
	
	public void makeArray(int size) {
		/** Does nothing.
		  * Here for maintaining spec.
		  * @param int size
		  */
		
	}
	
	public void addAnimal(int index, Animal a) {
		/** Sets the animal at the last index of arrayList animals to a.
		  * @param int index
		  * @param Animal a 
		  */
		animals.add(a);
	}
	
	public Animal biggestAnimal() {
		/** Returns the Animal in the array dogs that has the largest size.
		  * Uses the Animal.isBigger method. 
		  * @return Animal
		  */
		Animal biggest = new Dog();
		biggest.setSize(0);
		for (Animal a : animals) {
			if (a.isBigger(biggest)) {
				biggest = a;
			}
		}
		return biggest;
	}
	
	public void makeNoise() {
		/** Makes an animal noise.
		  */
		for (Animal a : animals) {
			a.makeNoise();
		}
	}
	
	public double geoMean() {
		/*
		 * Returns the geometric mean of the Animals arrayList.
		 * @return double
		 */
		int product = 1;
		for (Animal a : animals) {
			product *= a.getSize();
		}
		return Math.pow(product, 1.0 / animals.size());
	}
	
	/**
	 * Sorts ArrayList animals by size of Animals.
	 */
	public void sortBySize() {
		Collections.sort(animals);
	}
	
	/**
	 * Sorts ArrayList animals by String breed of Animals.
	 */
	public void sortByBreed() {
		AnimalCompare animalCompare = new AnimalCompare();
		Collections.sort(animals, animalCompare);
	}
	
	public String toString() {
		return animals.toString();
	}
}
