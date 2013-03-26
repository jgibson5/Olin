import java.util.Comparator;

/**
 * Implementation of Comparator for Animal.breed.
 * @author jgibson
 *
 */
public class AnimalCompare implements Comparator<Animal>{

	/**
	 * Returns positive int of one.breed is alphabetically greater than
	 * two.breed, 0 if same, negative int otherwise.
	 * @param Animal one
	 * @param Animal two
	 * @return int
	 */
	@Override
	public int compare(Animal one, Animal two) {
		
		return one.getBreed().compareTo(two.getBreed());
	}

}
