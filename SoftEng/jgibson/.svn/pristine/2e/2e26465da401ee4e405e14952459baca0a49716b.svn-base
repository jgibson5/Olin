
public abstract class Animal {
	
	private int size;
	private String name;
	
	public Animal() {
		/*
		 * Animal Constructor.
		 */
		System.out.println("Animal Constructor.");
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

	public abstract void makeNoise();
	
	public boolean isBigger(Animal that) {
		return this.size > that.size;
	}
}
