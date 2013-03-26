package com.allendowney.graph;
import java.util.Comparator;

/**
 * Compares two Nodes based off of the Node value.
 * @author jgibson
 *
 */
public class NodeComparator implements Comparator<Node>{

	@Override
	public int compare(Node n1, Node n2) {
		
		return n1.toString().compareTo(n2.toString());
	}
	
}
