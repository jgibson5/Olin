import java.net.URL;
import java.util.Comparator;

/**
 * Compares two URLs based off of the url string.
 * @author jgibson
 *
 */
public class UrlComparator implements Comparator<URL>{

	@Override
	public int compare(URL u1, URL u2) {
		
		return u1.toString().compareTo(u2.toString());
	}
	
}
