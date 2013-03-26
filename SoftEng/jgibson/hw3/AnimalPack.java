import java.util.ArrayList;

public class AnimalPack {
	private ArrayList<Animal> animals = new ArrayList<Animal>();
	
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
		Animal biggest = null;
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
}
