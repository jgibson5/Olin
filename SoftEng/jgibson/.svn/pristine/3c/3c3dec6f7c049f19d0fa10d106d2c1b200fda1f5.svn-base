package com.allendowney.graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;


/** Represents a graph.
 * 
 * @author downey
 *
 */
public class Graph {
	private ArrayList<Node> nodes = new ArrayList<Node>();

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "Graph [nodes=" + nodes + "]";
	}

	/** Adds a node to the graph.
	 * 
	 * @param node
	 */
	public void addNode(Node node) {
		nodes.add(node);
	}
	
	/** Returns true if this graph is a tree; false otherwise.
	 * 
	 * @return
	 */
	public boolean isTree() {
		// make a map from each Node to the number of times it is referenced
		Map<Node, Integer> map = new HashMap<Node, Integer>();
		
		for (Node node: nodes) {
			map.put(node, 0);
		}
		
		for (Node node: nodes) {			
			for (Node child: node.getChildren()) {
				map.put(child, map.get(child)+1);
			}
		}
				
		// check that there is only one node with zero references,
		// and all other nodes have one.
		int zeros = 0;
		for (Integer value : map.values()) {
			if (value > 1) return false;
			if (value == 0) {
				zeros++;
			} 
		}
		return (zeros == 1);
	}
	
	/** Checks whether the graph is strongly connected.
	 * 
	 * @return
	 */
	public boolean isStronglyConnected() {
		Map<Node, HashSet<Node>> map = reachabilityMap();
		for (Node node: nodes) {
			Set<Node> set = map.get(node);
			if (set.size() != nodes.size()) {
				return false;
			}
		}
		return true;
	}
	
	/** Makes a map from each node to the set of nodes it can reach.
	 * 
	 * @return
	 */
	public Map<Node, HashSet<Node>> reachabilityMap() {
		Map<Node, HashSet<Node>> map = 
				new HashMap<Node, HashSet<Node>>();
		
		for (Node node: nodes) {
			HashSet<Node> set = reachableFrom(node);
			map.put(node, set);
		}
		
		return map;
	}
	
	/** Returns the set of nodes that can be reached from node.
	 * 
	 * @param node
	 * @return
	 */
	private HashSet<Node> reachableFrom(Node node) {
		
		HashSet<Node> set = new HashSet<Node>();
		LinkedList<Node> queue = new LinkedList<Node>();
				
		queue.add(node);
		while (!queue.isEmpty()) {
			Node child = queue.poll();
			if (!set.contains(child)) {
				set.add(child);
				queue.addAll(child.getChildren());
			}	
		}
		return set;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Graph g = new Graph();
		Node node1 = new Node("A");
		
		g.addNode(node1);
		System.out.println(g.isTree());

		Node node2 = new Node("B");
		node1.addChild(node2);
		g.addNode(node2);
		
		System.out.println(g.isTree());
		
		node1.addChild(node1);
		System.out.println(g.isTree());
	}

	/** Returns true if the graph is strongly connected; false otherwise.
	 * 
	 * Uses Tarjan's algorithm to find all connected components.
	 * 
	 * If the graph is strongly connected, there is only one connected component,
	 * and it contains all nodes.
	 * 
	 * @return
	 */
	public boolean tarjan() {
		// current index
		Integer index = 0;
		
		// map from node to index
		HashMap<Node, Integer> index_map = new HashMap<Node, Integer>();
		
		// map from node to low link
		HashMap<Node, Integer> low_link = new HashMap<Node, Integer>();
		
		// stack of nodes we are in the process of visiting
		Stack<Node> stack = new Stack<Node>();
		
		// call strongConnect on all unvisited nodes
		for (Node node: nodes) {
			if (!index_map.containsKey(node)) {
				ArrayList<Node> component = strongConnect(node,
						index, index_map, low_link, stack);

				// if the component contains all nodes, the graph is
				// completely connected
				if (component.size() == nodes.size()) {
					return true;
				}
			}
		}
		return false;
	}

	/** Finds a connected component rooted at node.
	 * 
	 * Modifies index, index_map, low_link and stack.
	 * 
	 * @param node
	 * @param index
	 * @param index_map
	 * @param low_link
	 * @param stack
	 * @return
	 */
	private ArrayList<Node> strongConnect(
				Node node,
				Integer index, 
				HashMap<Node, Integer> index_map,
				HashMap<Node, Integer> low_link, 
				Stack<Node> stack) {
		
		index_map.put(node, index);
		low_link.put(node, index);
		index++;
		stack.push(node);
		
		for (Node child: node.getChildren()) {
			if (!index_map.containsKey(child)) {
				strongConnect(child, index, index_map, low_link, stack);
				low_link.put(node, 
							 Math.min(low_link.get(node), 
									  low_link.get(child)));
			} else if (stack.contains(child)) {
				low_link.put(node, 
						 	 Math.min(low_link.get(node), 
						 			  index_map.get(child)));				
			}
		}
		
		if (index_map.get(node) == low_link.get(node)) {
			ArrayList<Node> component = new ArrayList<Node>();
			
			Node w = null;
			while (!node.equals(w)) {
				w = stack.pop();
				component.add(w);
			}
			return component;
		}
		return null;
	}

	public List<Node> getNodes() {
		return nodes;
	}

	public int size() {
		return nodes.size();
	}
}
