package com.allendowney.btree;

import java.util.ArrayList;
import java.util.Collections;

/** Represents a node in a B-tree.
 * 
 * @author downey
 *
 */
public class Node {
	/** values is a List of the values in this node.
	 *  nodes is a List of references to child nodes.
	 */
	ArrayList<Integer> values = new ArrayList<Integer>();
	ArrayList<Node> nodes = new ArrayList<Node>();
	
	/** No-arg constructor.
	 * 
	 */
	public Node() {
		// nodes always has one more element than values
		nodes.add(null);
	}
	
	@Override
	public String toString() {
		return "values" + values.toString() + "nodes" + nodes.toString();
	}
	
	/** Adds the given element to this node or a child node.
	 * 
	 * @param e
	 * @return boolean whether the new key was added
	 */
	public boolean addKey(Integer e) {
		int i = Collections.binarySearch(values, e);
		if (i >= 0) {
			// it's already there
			return false;
		}
		
		int pos = -(i + 1);
		Node node = nodes.get(pos);
		
		if (node == null) {
			values.add(pos, e);
			nodes.add(null);
			return true;
		} else {
			return node.addKey(e);
		}
	}

	/** Stores the given node at the location where the given integer would go.
	 * 
	 * @param e
	 * @param node
	 * @return boolean, whether the given integer was not in the node.
	 */
	public boolean setNode(Integer e, Node node) {
		int i = Collections.binarySearch(values, e);
		if (i >= 0) {
			return false;
		}
		int pos = -(i + 1);
		nodes.set(pos, node);
		return true;
	}

	/** Checks whether the node is empty.
	 * 
	 * Note: doesn't check the children, so this will not work correctly
	 * with an improper B-tree.
	 * 
	 * @return boolean, whether the tree is empty.
	 */
	public boolean isEmpty() {
		return values.isEmpty();
	}
	
	public boolean contains(Object o) {
		Integer e = (Integer) o;
		/*
		for (int i=0; i<values.size(); i++) {
			if (values.get(i) == e) {
				return true;
			} else if (values.get(i) > e) {
				return nodes.get(i).contains(e);
			}
		}*/
		System.out.println("Contains?" + o);
		System.out.println("Values:" + values);
		System.out.println("Nodes:" + nodes);
		if (values.contains(o)) {
			System.out.println("Found " + o);
			return true;
		} else if (nodes.get(0) == null) {
			return false;
		} else {
			for (int i=0; i<values.size(); i++) {
				if (values.get(i) > e) {
					return nodes.get(i).contains(o);
				}
			}
			return nodes.get(nodes.size() - 1).contains(e);
		}
	}
}
