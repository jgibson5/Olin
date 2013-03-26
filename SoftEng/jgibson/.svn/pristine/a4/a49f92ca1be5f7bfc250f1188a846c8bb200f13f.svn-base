package com.allendowney.graph;

import java.util.ArrayList;

/** Represents a node in a graph.
 * 
 * @author downey
 *
 */
public class Node {
	private String name;
	private ArrayList<Node> children;

	public Node(String name) {
		this.name = name;
		this.children = new ArrayList<Node>();
	}
	
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "Node [name=" + name + "]";
	}

	/** Adds a child node.
	 * 
	 * @param node
	 */
	public void addChild(Node node) {
		this.children.add(node);
	}

	/** Returns this node's children.
	 * 
	 * @return
	 */
	public ArrayList<Node> getChildren() {
		return children;
	}
}
