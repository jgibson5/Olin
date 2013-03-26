package com.allendowney.graph;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class GraphTest {

	public GraphTest() {
	}

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testIsTree() {
		Graph g = new Graph();
		Node node1 = new Node("A");
		
		g.addNode(node1);
		assertTrue(g.isTree());

		Node node2 = new Node("B");
		node1.addChild(node2);
		g.addNode(node2);
		
		assertTrue(g.isTree());
		
		node1.addChild(node1);
		assertFalse(g.isTree());
	}

}
