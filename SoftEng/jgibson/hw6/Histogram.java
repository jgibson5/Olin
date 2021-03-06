package net.joegibson.huffman;
import java.io.*;
import java.util.HashMap;
import java.util.PriorityQueue;
/**
 * @author jgibson, lpark
 *
 */
public class Histogram {

	private HashMap<String, Integer> charCount;
	private PriorityQueue<Node> priorityQueue;

	/**
	 * @param args
	 */
	
	public Histogram() {
		charCount = new HashMap<String, Integer>();
		priorityQueue = new PriorityQueue<Node>();
	}
	
	public PriorityQueue<Node> getPriorityQueue() {
		return priorityQueue;
	}
	
	public String toString() {
		return charCount.toString();
	}
	
	public void count(String s) {
		for (int i=0; i<s.length(); i++) {
			count(s.charAt(i));
		}
		
	}
	
	public void count(Character c) {
		if (charCount.containsKey(c.toString())) {
			charCount.put(c.toString(), charCount.get(c.toString()) + 1);
		} else {
			charCount.put(c.toString(), 1);
		}
	}
	
	public int freq(Character c) {
		if (charCount.get(c.toString()) != null) {
			return charCount.get(c.toString());
		} else {
			return 0;
		}
	}
	
	public void readTest(String filePath) {
		try {
			File myFile = new File(filePath);
			FileReader fileReader = new FileReader(myFile);
			
			BufferedReader reader = new BufferedReader(fileReader);
			
			String line = null;
			
			while ((line = reader.readLine()) != null) {
				count(line);
			}
			
			reader.close();
			fillQueue();
			
		} catch(Exception ex) {
			ex.printStackTrace();
		}
	}
	
	private void fillQueue() {
		for (String k:charCount.keySet()) {
			priorityQueue.add(new Node(k, charCount.get(k)));
		}
	}
	
	public void addToQueue(Node n) {
		priorityQueue.add(n);
	}
	
	public Node poll(){
		return priorityQueue.poll();
	}
}
