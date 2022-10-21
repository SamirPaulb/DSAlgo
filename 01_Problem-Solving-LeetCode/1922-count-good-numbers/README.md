<h2><a href="https://leetcode.com/problems/count-good-numbers/">1922. Count Good Numbers</a></h2><h3>Medium</h3><hr><div><p>A digit string is <strong>good</strong> if the digits <strong>(0-indexed)</strong> at <strong>even</strong> indices are <strong>even</strong> and the digits at <strong>odd</strong> indices are <strong>prime</strong> (<code>2</code>, <code>3</code>, <code>5</code>, or <code>7</code>).</p>

<ul>
	<li>For example, <code>"2582"</code> is good because the digits (<code>2</code> and <code>8</code>) at even positions are even and the digits (<code>5</code> and <code>2</code>) at odd positions are prime. However, <code>"3245"</code> is <strong>not</strong> good because <code>3</code> is at an even index but is not even.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the <strong>total</strong> number of good digit strings of length </em><code>n</code>. Since the answer may be large, <strong>return it modulo </strong><code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>digit string</strong> is a string consisting of digits <code>0</code> through <code>9</code> that may contain leading zeros.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> The good numbers of length 1 are "0", "2", "4", "6", "8".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 400
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 50
<strong>Output:</strong> 564908303
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>
</div>