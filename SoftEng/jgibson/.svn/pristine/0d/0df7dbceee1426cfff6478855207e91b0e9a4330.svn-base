package net.joegibson.huffman;

/**
 * @author jgibson, lpark
 *
 */
public class Node implements Comparable<Node>{
	private String character;
	private int freq;
	private Node [] children;

	/**
	 * Constructors
	 */
	public Node() {
		this.character = null;
		this.children = null;
	}
	
	public Node(String c, int freq) {
		this.character = c;
		this.freq = freq;
	}
	
	public Node(Node n1, Node n2) {
		this.character = null;
		this.freq = n1.getFreq() + n2.getFreq();
		this.children = new Node[2];
		this.children[0] = n1;
		this.children[1] = n2;
	}
	
	/**
	 * @return the character
	 */
	public String getCharacter() {
		return character;
	}
	
	/**
	 * @return children
	 */
	public Node[] getChildren(){
		return children;
	}

	/**
	 * @param character the character to set
	 */
	public void setCharacter(String character) {
		this.character = character;
	}
	/**
	 * @return the freq
	 */
	public int getFreq() {
		return freq;
	}
	/**
	 * @param freq the freq to set
	 */
	public void setFreq(int freq) {
		this.freq = freq;
	}
	
	/* (non-Javadoc)
	 * @see java.lang.Comparable#compareTo(java.lang.Object)
	 */
	public int compareTo(Node that) {
		return this.freq - that.getFreq();
	}
	
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString() {
		if (children == null){
			return "(" + this.character + ", " + this.freq + ", " + this.children+")";

		}
		else{
			return "(" + this.character + ", " + this.freq + ", " + "["+this.children[0] + this.children[1]+"])";

		}
	}
	/**encodes character string to binary string
	 * @param s
	 * @param encodedString
	 * @return
	 */
	public String encode(String s, String encodedString) {		
		if (s.equals(character)) {
			return encodedString;
		} else if (children == null) {
			return null;
		} else {
			String s1 = children[0].encode(s, encodedString + "0");
			String s2 = children[1].encode(s, encodedString + "1");
			if (s1 != null){
				return s1;
			}
			else{
				return s2;
			}
		}
	}
	
}
