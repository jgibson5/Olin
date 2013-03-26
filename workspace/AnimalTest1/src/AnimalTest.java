/** Solution to Software Engineering Homework 03
 *
 * @author Allen B. Downey
 *
 */

import java.util.ArrayList;

/** Represents an animal.
 * @author downey
 *
 */
abstract class Animal {
	private int size;
    private String name;

    /** Constructor.
     * 
     * @param size
     * @param name
     */
    public Animal(int size, String name) {
    	this.size = size;
    	this.name = name;
    }
    
    /** Returns this animal's size. */
    int getSize() {
    	return size;
    }
    
    /** Sets this animal's size.
     * 
     * @param size
     */
    void setSize(int size) {
    	this.size = size;
    }

	/**
	 * @return
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name
	 */
	public void setName(String name) {
		this.name = name;
	}

	/** Returns true if this animal is bigger (in size) than that.
	 * 
	 * @param that
	 * @return
	 */
	boolean isBigger(Animal that) {
    	if (that == null) {
    		return true;
    	}
    	return this.size > that.size;
    }

    /** Makes an appropriate animal noise.
     * 
     * Child classes must provide an implementation.
     * 
     */
    abstract void makeNoise();

}

/** Defines the interface for animals that fetch.
 * 
 * @author downey
 *
 */
interface Fetchable {
	
	/** Returns a String representing the fetched item.
	 * 
	 * @param item
	 * @return
	 */
	abstract String fetch(String item);
}


/** Represents a dog.
 * 
 * @author downey
 *
 */
class Dog extends FeedableAnimal implements Fetchable {
	
	/**Constructor.
	 * 
	 * @param size
	 * @param name
	 */
	public Dog(int size, String name) {
		super(size, name);
	}

	/* (non-Javadoc)
	 * @see com.allendowney.hw03.Animal#makeNoise()
	 */
	@Override
	void makeNoise() {
		System.out.println("woof");
	}

	@Override
	public String fetch(String item) {
		return "damp " + item;
	}
	
	/** Implementing Feedable from FeedableAnimal.
	 * 
	 */
	@Override
	void feedFood(String food) {
		System.out.println("Dog food in dog bowl.");
		
	}
	
	/** Implementing Feedable from FeedableAnimal.
	 * 
	 */
	@Override
	void feedWater(String water) {
		System.out.println("Water in dog bowl.");
		
	}
}

/** Represents a Cat.
 * 
 * @author downey
 *
 */
class Cat extends Animal implements Feedable {
	
	public Cat(int size, String name) {
		super(size, name);
	}

	/* (non-Javadoc)
	 * @see com.allendowney.hw03.Animal#makeNoise()
	 */
	@Override
	void makeNoise() {
		System.out.println("meow");
	}
	
	/** Implementing Feedable.
	 * 
	 */
	@Override
	public void feed(String water, String food) {
		System.out.println("Fed the hungry cat.");
		
	}
}

/** Represents a collection of Animals.
 * @author downey
 *
 */
class AnimalPack {
    ArrayList<Animal> animals;

    /** Makes an empty array of animals.
     * 
     * @param capacity
     */
    void makeArray(int capacity) {
    	animals = new ArrayList<Animal>(capacity);
    }

    /** Adds an animal to the array at the given location.
     * 
     * @param index	 Where to put the animal
     * @param animal
     */
    void addAnimal(int index, Animal animal) {
    	animals.add(index, animal);
    }

    /** Returns the biggest animal in the pack.
     * 
     * @return	 Biggest animal
     */
    Animal biggestAnimal() {
    	Animal biggest = null;
    	for (Animal animal: animals) {
    		if (animal.isBigger(biggest)) {
    			biggest = animal;
    		}
    	}
    	return biggest;
    }
}

/** Interface to specify a feedable animal.
 * 
 * @author jgibson
 *
 */
interface Feedable {
	void feed(String water, String food);
}

/** Represents an animal that is feedable.
 * 
 * @author jgibson
 *
 */
abstract class FeedableAnimal extends Animal implements Feedable {

	public FeedableAnimal(int size, String name) {
		super(size, name);
	}
	
	/** Feed the hungry animal.
	 * 
	 */
	public void feed(String water, String food) {
		feedFood(food);
		feedWater(water);
	}
	
	abstract void feedFood(String food);
	abstract void feedWater(String water);
	
}

/** Test code for animal and animalPack.
 * @author downey
 *
 */
public class AnimalTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

    	AnimalPack pack = new AnimalPack();
    	pack.makeArray(10);

    	Dog rover = new Dog(20, "Rover");
    	rover.feed("water", "food");
    	System.out.println(rover.fetch("tennis ball"));
    	
    	pack.addAnimal(0, rover);
    	
		Animal biggest = pack.biggestAnimal();
		System.out.println(biggest.getSize());
    }
}
