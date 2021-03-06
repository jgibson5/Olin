/**
 * 
 */
package net.joegibson.huffman;

/**
 * @author jgibson, lpark
 *
 */
public class HuffmanTree{
	public Node bigTree;
	
	/**encodes string to binary string
	 * @param string
	 * @return
	 */
	public String encode(String string){
		String encodedString = "";
		for (Character c: string.toCharArray()){
			String s = c.toString();
			encodedString = encodedString + bigTree.encode(s, "");
		}
		return encodedString;
	}
	
	/**constructs Huffman tree based on histogram of characters in file
	 * @param h
	 * @param filePath
	 */
	public void construct(Histogram h, String filePath){
		h.readTest(filePath);
		while (h.getPriorityQueue().size() >1){
			Node childNode1 = h.poll();
			Node childNode2 = h.poll();
			Node parent = new Node(childNode1, childNode2);
			h.addToQueue(parent);
		}
		bigTree = h.poll();
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		return bigTree.toString();
	}
	/**decodes binary String into String of characters
	 * @param encodedString
	 * @return
	 */
	public String decode(String encodedString){
		String decodedString = "";
		while (encodedString.length() > 0){
			Node node = bigTree;
			String nodeCharacter = node.getCharacter();
			while (nodeCharacter == null){
				Character c = encodedString.charAt(0);
				Integer b = Integer.parseInt(c.toString());
				node = node.getChildren()[b];
				encodedString = encodedString.substring(1);
				nodeCharacter = node.getCharacter();
			}
			decodedString = decodedString + node.getCharacter();
			node = bigTree;
		}
		return decodedString;
	}

}
