import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

/**
 * Duplicates class has a static method for checking duplicate Strings.
 * @author jgibson
 * @date 2-11-13
 *
 */
public class Duplicates {

	/**
	 * Test code for Duplicates.
	 * @param args
	 * @author Joe Gibson
	 */
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>();
		list.add("One");
		list.add("Two");
		list.add("Three");
		System.out.println(Duplicates.hasDuplicates(list));
		list.add("Three");
		System.out.println(Duplicates.hasDuplicates(list));
		
	}
	
	/**
	 * Takes an ArrayList of Strings and returns true if there are any
	 * duplicate Strings.
	 * @param ArrayList list
	 * @return boolean
	 */
	public static boolean hasDuplicates (ArrayList<String> list) {
		Set<String> set = new HashSet<String>(list);
		
		return set.size() < list.size();
		
	}

}
