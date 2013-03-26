package com.allendowney.btree;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Iterator;
import org.junit.Test;

public class BTreeTest {

	@Test
	public void testAdd() {
		BTree btree = new BTree();
		btree.add(7);
		btree.add(16);
		
		btree.setNode(9, new BTree());
		btree.add(12);
		
		System.out.println(btree);
		
		// NOTE: add actually works; this test fails because contains is broken
		assertTrue(btree.contains(12));
	}

	@Test
	public void testAddAll() {
		BTree btree = makeTestTree();
		int[] array = {8, 20};
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int x: array) {
			list.add(x);
		}
		btree.addAll(list);

		// NOTE: addAll actually works; this test fails because contains is broken
		assertTrue(btree.containsAll(list));
	}

	@Test
	public void testClear() {
		BTree btree = makeTestTree();
		btree.clear();
		assertFalse(btree.contains(16));
	}

	@Test
	public void testContains() {
		BTree btree = makeTestTree();
		System.out.println(btree);
		assertTrue(btree.contains(16));
		assertTrue(btree.contains(2));
		assertTrue(btree.contains(9));
		assertTrue(btree.contains(21));
		assertFalse(btree.contains(-1));
		assertFalse(btree.contains(8));
		assertFalse(btree.contains(25));
	}

	@Test
	public void testContainsAll() {
		BTree btree = makeTestTree();
		int[] array = {1, 2, 7, 9, 18};
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int x: array) {
			list.add(x);
		}
		assertTrue(btree.containsAll(list));

		int[] array2 = {3, 5, 7, 8, 20};
		ArrayList<Integer> list2 = new ArrayList<Integer>();
		for (int x: array2) {
			list2.add(x);
		}
		assertFalse(btree.containsAll(list2));
	}

	@Test
	public void testIsEmpty() {
		BTree btree = makeTestTree();
		assertFalse(btree.isEmpty());
		btree.clear();
		assertTrue(btree.isEmpty());
	}

	@Test
	public void testIterator() {
		BTree btree = makeTestTree();
		Iterator<Integer> it = btree.iterator();
		assertTrue(it.hasNext());
		assertTrue(it.next() == 1);
		assertTrue(it.hasNext());
	}

	@Test
	public void testSize() {
		BTree btree = makeTestTree();
		assertTrue(btree.size() == 10);
	}

	@Test
	public void testToArray() {
		BTree btree = makeTestTree();
		Object[] array = btree.toArray();
		assertTrue(array.length == 10);
		assertTrue((Integer) array[2] == 5);
	}

	@Test
	public void testToArrayTArray() {
		BTree btree = makeTestTree();
		Integer[] array = btree.toArray(new Integer[10]);
		assertTrue(array.length == 10);
		assertTrue(array[2] == 5);
	}


	private BTree makeTestTree() {
		BTree btree = new BTree();
		int[] array = {7, 16};
		for (int x: array) {
			btree.add(x);
		}
		
		BTree btree2 = new BTree();
		int[] array2 = {1, 2, 5, 6};
		for (int x: array2) {
			btree2.add(x);
		}
		
		btree.setNode(1, btree2);
		
		BTree btree3 = new BTree();
		int[] array3 = {9, 12};
		for (int x: array3) {
			btree3.add(x);
		}
		
		btree.setNode(9, btree3);
		
		BTree btree4 = new BTree();
		int[] array4 = {18, 21};
		for (int x: array4) {
			btree4.add(x);
		}
		
		btree.setNode(18, btree4);
		return btree;
	}

}
