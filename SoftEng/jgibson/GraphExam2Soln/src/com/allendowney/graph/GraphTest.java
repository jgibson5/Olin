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

	@Test
	public void testIsStronglyConnected() {
		Graph g = new Graph();
		Node node1 = new Node("A");
		
		g.addNode(node1);
		assertTrue(g.isStronglyConnected());

		Node node2 = new Node("B");
		node1.addChild(node2);
		g.addNode(node2);
		
		assertFalse(g.isStronglyConnected());
		
		node2.addChild(node1);
		assertTrue(g.isStronglyConnected());
	}

	@Test
	public void testTarjan() {
		Graph g = new Graph();
		Node node1 = new Node("A");
		
		g.addNode(node1);
		assertTrue(g.tarjan());

		Node node2 = new Node("B");
		node1.addChild(node2);
		g.addNode(node2);
		
		assertFalse(g.tarjan());
		
		node2.addChild(node1);
		assertTrue(g.tarjan());
	}

	@Test
	public void testTarjan2() {
		Graph g = new Graph();
		Node node1 = new Node("A");
		
		g.addNode(node1);
		assertTrue(new Tarjan().isStronglyConnected(g));

		Node node2 = new Node("B");
		node1.addChild(node2);
		g.addNode(node2);
		
		assertFalse(new Tarjan().isStronglyConnected(g));
		
		node2.addChild(node1);
		assertTrue(new Tarjan().isStronglyConnected(g));
	}

}
