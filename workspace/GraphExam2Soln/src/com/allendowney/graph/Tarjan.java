/**
 * 
 */
package com.allendowney.graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

/**
 * @author downey
 *
 */
public class Tarjan {
	// current index
	Integer index = 0;
			
	// map from node to index
	HashMap<Node, Integer> index_map = new HashMap<Node, Integer>();
			
	// map from node to low link
	HashMap<Node, Integer> low_link = new HashMap<Node, Integer>();
			
	// stack of nodes we are in the process of visiting
	Stack<Node> stack = new Stack<Node>();
	

	/** Returns true if the graph is strongly connected; false otherwise.
	 * 
	 * Uses Tarjan's algorithm to find all connected components.
	 * 
	 * If the graph is strongly connected, there is only one connected component,
	 * and it contains all nodes.
	 * 
	 * @return
	 */
	public boolean isStronglyConnected(Graph g) {
		
		for (Node node: g.getNodes()) {
			if (notIndexed(node)) {
				ArrayList<Node> component = strongConnect(node);

				// if the component contains all nodes, the graph is
				// completely connected
				if (component.size() == g.size()) {
					return true;
				}
			}
		}
		return false;
	}

	/** Returns true if this node has not been indexed yet.
	 * 
	 * @param node
	 * @return
	 */
	private boolean notIndexed(Node node) {
		return !index_map.containsKey(node);
	}

	/** Finds a connected component rooted at node.
	 * 
	 * @param node
	 * 
	 */
	private ArrayList<Node> strongConnect(Node node) {
		
		index_map.put(node, index);
		low_link.put(node, index);
		index++;
		stack.push(node);
		
		for (Node child: node.getChildren()) {
			if (notIndexed(child)) {
				strongConnect(child);
				low_link.put(node, 
							 minLowLink(node, child));
				
			} else if (stack.contains(child)) {
				low_link.put(node, 
						 	 minIndex(node, child));				
			}
		}
		
		if (isRoot(node)) {
			return popComponent(node);
		}
		return null;
	}

	/** Pops a connected component off the stack.
	 * 
	 * @param node
	 * @return
	 */
	private ArrayList<Node> popComponent(Node node) {
		ArrayList<Node> component = new ArrayList<Node>();
		
		Node w = null;
		while (!node.equals(w)) {
			w = stack.pop();
			component.add(w);
		}
		return component;
	}

	/** Returns true if this node is the root of a connected component.
	 * 
	 * @param node
	 * @return
	 */
	private boolean isRoot(Node node) {
		return index_map.get(node) == low_link.get(node);
	}

	/** Min of node.low_link and child.index 
	 * 
	 * @param node
	 * @param child
	 * @return
	 */
	private int minIndex(Node node, Node child) {
		return Math.min(low_link.get(node), 
				  		index_map.get(child));
	}

	/** Min of node.low_link and child.low_link
	 * 
	 * @param node
	 * @param child
	 * @return
	 */
	private int minLowLink(Node node, Node child) {
		return Math.min(low_link.get(node), 
				  		low_link.get(child));
	}
}
