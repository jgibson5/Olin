
public class Dog extends Animal implements Fetcher {
	/** Dog class that inherits from Animal and implements Fetcher.
	  */
	public void makeNoise() {
		/** Makes a dog noise.
		  */
		System.out.println("Bark.");
	}

	@Override
	public String fetch(String thingToFetch) {
		/** Overrides the fetch method from Fetcher
		  */
		return "damp " + thingToFetch;
	}
}
