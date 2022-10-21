<h2><a href="https://leetcode.com/problems/count-number-of-ways-to-place-houses/">2320. Count Number of Ways to Place Houses</a></h2><h3>Medium</h3><hr><div><p>There is a street with <code>n * 2</code> <strong>plots</strong>, where there are <code>n</code> plots on each side of the street. The plots on each side are numbered from <code>1</code> to <code>n</code>. On each plot, a house can be placed.</p>

<p>Return <em>the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street</em>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>Note that if a house is placed on the <code>i<sup>th</sup></code> plot on one side of the street, a house can also be placed on the <code>i<sup>th</sup></code> plot on the other side of the street.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/12/arrangements.png" style="width: 500px; height: 500px;">
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 9
<strong>Explanation:</strong> The 9 possible arrangements are shown in the diagram above.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>
</div>