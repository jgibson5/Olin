/**
 * HW6
 * Joe Gibson, Lisa Park
 * Homework assignment exploring object oriented design and file reading 
 * with Huffman Codes.
 * 
 * @author jgibson, lpark
 * @date 2-24-13
 * @course Software Engineering, Olin College
 * @professor Allen Downey
 */
package net.joegibson.huffman;

import static org.junit.Assert.*;

import org.junit.Test;

/**
 * @author jgibson, lpark
 *
 */
public class HistogramTest {
	
	//Histogram tests
	
	@Test
	public void testReadHistogram() {
		Histogram h = new Histogram();
		h.readTest("/home/jgibson/Documents/test.py");
		//System.out.println(h.getPriorityQueue());
		while (h.getPriorityQueue().peek() != null) {
			h.getPriorityQueue().poll();
		}
		assertEquals("{D=1, E=1, A=1, M=1, 	=29, N=1, O=1, R=2, ]=5, Y=1, [=5, \"=2, f=6, g=2,  =41, d=8, e=14, c=3, a=2559, n=25, +=3, o=9, l=17, (=13, m=10, )=13, j=3, .=1, ,=2, h=1, -=1, i=13, w=1, 2=1, u=10, 1=6, t=7, 0=3, s=13, r=16, p=5, :=11, >=1, y=3, ==10, <=1}", h.toString());
	}

	@Test
	public void testCount() {
		Histogram h = new Histogram();
		h.count("moose");
		assertEquals("{e=1, s=1, o=2, m=1}", h.toString());
	}

	@Test
	public void testCountChar() {
		Histogram h = new Histogram();
		h.count('a');
		assertEquals("{a=1}", h.toString());
	}
	
	@Test
	public void testFreq() {
		Histogram h = new Histogram();
		h.count("moose");
		assertEquals(2, h.freq('o'));
	}
	
	
	//Node tests
	@Test
	public void testNodeCompare() {
		Node n1 = new Node("a", 2);
		Node n2 = new Node("b", 5);
		assertEquals(true, n1.compareTo(n2) < 0);
	}
	
	
	//Tree tests
	@Test
	public void testConstruct() {
		HuffmanTree tree = new HuffmanTree();
		Histogram h = new Histogram();
		tree.construct(h, "/home/jgibson/Documents/test.py");
		assertEquals("(null, 2882, [(null, 323, [(null, 134, [(null, 61, [(	, 29, null)(null, 32, [(null, 16, [(null, 8, [(null, 4, [(null, 2, [(D, 1, null)(E, 1, null)])(null, 2, [(O, 1, null)(., 1, null)])])(null, 4, [(\", 2, null)(g, 2, null)])])(null, 8, [(null, 4, [(null, 2, [(h, 1, null)(-, 1, null)])(null, 2, [(2, 1, null)(Y, 1, null)])])(null, 4, [(null, 2, [(A, 1, null)(N, 1, null)])(null, 2, [(>, 1, null)(<, 1, null)])])])])(r, 16, null)])])(null, 73, [(null, 34, [(null, 17, [(d, 8, null)(null, 9, [(null, 4, [(R, 2, null)(null, 2, [(M, 1, null)(w, 1, null)])])(null, 5, [(,, 2, null)(c, 3, null)])])])(l, 17, null)])(null, 39, [(null, 19, [(o, 9, null)(u, 10, null)])(null, 20, [(=, 10, null)(m, 10, null)])])])])(null, 189, [(null, 85, [( , 41, null)(null, 44, [(null, 21, [(null, 10, [([, 5, null)(], 5, null)])(:, 11, null)])(null, 23, [(null, 11, [(p, 5, null)(null, 6, [(0, 3, null)(y, 3, null)])])(null, 12, [(1, 6, null)(f, 6, null)])])])])(null, 104, [(null, 51, [(n, 25, null)(null, 26, [((, 13, null)(i, 13, null)])])(null, 53, [(null, 26, [(), 13, null)(s, 13, null)])(null, 27, [(null, 13, [(null, 6, [(j, 3, null)(+, 3, null)])(t, 7, null)])(e, 14, null)])])])])])(a, 2559, null)])", tree.toString());
	}
	
	@Test
	public void testEncode() {
		HuffmanTree tree = new HuffmanTree();
		Histogram h = new Histogram();
		tree.construct(h, "/home/jgibson/Documents/test.py");
		assertEquals("110001100100100011010011100", tree.encode("aarR()"));
	}
	
	@Test
	public void testDecode() {
		HuffmanTree tree = new HuffmanTree();
		Histogram h = new Histogram();
		tree.construct(h, "/home/jgibson/Documents/test.py");
		assertEquals("aaa", tree.decode("111"));
	}
	
	
}
