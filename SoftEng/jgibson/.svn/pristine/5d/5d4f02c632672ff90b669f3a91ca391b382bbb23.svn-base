package com.allendowney.graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;

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
	    ArrayList<Node> visited = new ArrayList<Node>();
	    PriorityQueue<Node> q = new PriorityQueue<Node>();
	    Node current;
	    q.add(nodes.get(0));
	    while (q.peek() != null) {
	    	current = q.poll();
	    	visited.add(current);
	    	for (int i=0; i<current.getChildren().size(); i++) {
	    		if (visited.contains(current.getChildren().get(i))) {
	    			return false;
	    		}
	    		q.add(current.getChildren().get(i));
	    	}
	    }
		return true;
	}
	
	/**
	 * Checks if Graph is strongly connected.
	 * Loops through Nodes and checks if path exists to each other point.
	 * @return boolean of Graph being strongly connected
	 */
	public boolean isStronglyConnected() {
		for (Node node : nodes) {
			for (Node target : nodes) {
				if (!pathExists(node, target)) {
					return false;
				}
			}
		}
		return true;
	}
	
	/**
	 * Checks to see if there is a path between source and target using breadth
	 * first search over the nodes.
	 * @param Node source
	 * @param Node target
	 * @return boolean if path exists
	 */
	public boolean pathExists(Node source, Node target) {
		
		NodeComparator cmp = new NodeComparator();
		PriorityQueue<Node> q = new PriorityQueue<Node>(11, cmp);
		q.add(source);
		HashSet<Node> visited = new HashSet<Node>();
		Node current;
		
		while (q.peek() != null) {
			current = q.poll();
			if (current.equals(target)) {
				return true;
			}
			for (Node child : current.getChildren()) {
				if (!visited.contains(child)) {
					visited.add(child);
					q.add(child);
				}
			}
		}
		
		
		return false;
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
		
		Graph connectedGraph = new Graph();
		Node a = new Node("a");
		Node b = new Node("b");
		Node c = new Node("c");
		a.addChild(b);
		b.addChild(c);
		c.addChild(a);
		connectedGraph.addNode(a);
		connectedGraph.addNode(b);
		connectedGraph.addNode(c);
		
		//true
		System.out.println(connectedGraph.isStronglyConnected());
		
		Node d = new Node("d");
		a.addChild(d);
		connectedGraph.addNode(d);
		
		//false
		System.out.println(connectedGraph.isStronglyConnected());
		
		d.addChild(c);
		
		//true
		System.out.println(connectedGraph.isStronglyConnected());
		
		Node e = new Node("e");
		connectedGraph.addNode(e);
		
		//false
		System.out.println(connectedGraph.isStronglyConnected());
		
		
	}
}
