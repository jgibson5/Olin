
public class Cat extends Animal {
	/** Cat class that inherits from Animal.
	  * Changes the makeNoise() method.
	  */
	
	public Cat() {
		/*
		 * Cat Constructor.
		 */
		System.out.println("Cat Constructor.");
	}
	
	public Cat(int size) {
		/*
		 * Cat Constructor.
		 */
		super(size);
	}
	
	public void makeNoise() {
		/** Makes a cat noise.
		  */
		System.out.println("Meow.");
	}
}
