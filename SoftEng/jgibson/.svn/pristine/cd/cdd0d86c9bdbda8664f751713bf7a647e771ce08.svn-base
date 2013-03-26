public abstract class Animal implements Comparable<Animal> {
	
	private int size;
	private String name;
	private String breed;
	
	public Animal() {
		/*
		 * Animal Constructor.
		 */
	}
	
	public Animal(int size) {
		/*
		 * Animal Constructor.
		 */
		this();
		this.size = size;
	}
	
	public Animal(int size, String name) {
		/*
		 * Animal Constructor.
		 */
		this();
		this.size = size;
		this.name = name;
	}
	
	/**
	 * @return the size
	 */
	public int getSize() {
		return size;
	}
	/**
	 * @param size the size to set
	 */
	public void setSize(int size) {
		this.size = Math.abs(size);
	}
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	/**
	 * @return the breed
	 */
	public String getBreed() {
		return breed;
	}

	/**
	 * @param breed the breed to set
	 */
	public void setBreed(String breed) {
		this.breed = breed;
	}

	public abstract void makeNoise();
	
	public boolean isBigger(Animal that) {
		return this.size > that.size;
	}
	
	/**
	 * Overrides the compareTo function for the Collections.sort method to
	 * sort by Animal.size
	 * @param Animal that
	 * @return int
	 */
	public int compareTo(Animal that) {
		return this.size - that.size;
	}
	
	public String toString() {
		return getName()+ "<" + getSize() + "," + getBreed() + ">";
	}

	
}
