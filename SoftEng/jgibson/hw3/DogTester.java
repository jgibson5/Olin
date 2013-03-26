/** Practice with methods and arrays in Java using Dog and DogPack classes.
  * <p>
  *	@author Joe Gibson
  * @course Software Engineering
  * @date 1-30-13
  */

import java.util.ArrayList;

class DogTest {
	/** Tester class for the Dog and Cat classes.
	  */
	public static void main (String[] args) {
		/** Main method for the app.
		  * 
		  * Creates 3 Dog objects and puts them into an array.
		  * Loops through the array, invoking the bark() method on each dog.
		  * Loops through the array, printing the attributes of the biggest dog.
		  */
		
		Dog d1 = new Dog();
		d1.setSize(5);
		int size = d1.getSize();
		System.out.println(size);
		
		Dog d2 = new Dog();
		d2.setSize(10);
		
		boolean bigger = d1.isBigger(d2);
		System.out.println(bigger);
		
		DogPack dogs = new DogPack();
		int[] sizes = {1, 2, 3, 4, 5};
		dogs.makeArray(sizes.length);
		for(int i=0; i<sizes.length; i++) {
			Dog d = new Dog();
			d.setSize(sizes[i]);
			dogs.addDog(i, d);
		}
		
		Dog d3 = dogs.biggestDog();
		System.out.println(d3.getSize());
		

	}
}

class Dog {
	/** Dog class used in the exercise.
	  */

	private int size;
	
	public int getSize() {
		/** Gets size.
		  * @return int
		  */
		return size;
	}
	
	public void setSize(int s) {
		/** Sets size to s.
  		  * @param int s
  		  */
		size = s;
	}
	
	public boolean isBigger(Dog d) {
		/** Returns boolean value of this.size > d.size.
		  * @param Dog d 
		  * @return boolean
		  */
		if (this.getSize() > d.getSize()) {
			return true;
		}
		return false;
	}
}

class DogPack {
	/** DogPack class used in this exercise.
	  * Contains an array of Dogs.
	  */
	private ArrayList<Dog> dogs;
	
	public void makeArray(int size) {
		/** Sets the size of the dogs array to size.
		  * @param int size
		  */
		dogs = new ArrayList<Dog>(size);
	}
	
	public void addDog(int index, Dog d) {
		/** Sets the dog at the index index of array dogs to d.
		  * @param int index
		  * @param Dog d 
		  */
		dogs.add(index, d);
	}
	
	public Dog biggestDog() {
		/** Returns the Dog in the array dogs that has the largest size.
		  * Uses the Dog.isBigger method. 
		  * @return Dog
		  */
		Dog biggest = new Dog();
		biggest.setSize(0);
		for (Dog d:dogs) {
			if (d.isBigger(biggest)) {
				biggest = d;
			}
		}
		return biggest;
	}
}
