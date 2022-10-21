<h2><a href="https://leetcode.com/problems/match-substring-after-replacement/">2301. Match Substring After Replacement</a></h2><h3>Hard</h3><hr><div><p>You are given two strings <code>s</code> and <code>sub</code>. You are also given a 2D character array <code>mappings</code> where <code>mappings[i] = [old<sub>i</sub>, new<sub>i</sub>]</code> indicates that you may <strong>replace</strong> any number of <code>old<sub>i</sub></code> characters of <code>sub</code> with <code>new<sub>i</sub></code>. Each character in <code>sub</code> <strong>cannot</strong> be replaced more than once.</p>

<p>Return <code>true</code><em> if it is possible to make </em><code>sub</code><em> a substring of </em><code>s</code><em> by replacing zero or more characters according to </em><code>mappings</code>. Otherwise, return <code>false</code>.</p>

<p>A <strong>substring</strong> is a contiguous non-empty sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
<strong>Output:</strong> true
<strong>Explanation:</strong> Replace the first 'e' in sub with '3' and 't' in sub with '7'.
Now sub = "l3e7" is a substring of s, so we return true.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The string "f00l" is not a substring of s and no replacements can be made.
Note that we cannot replace '0' with 'o'.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
<strong>Output:</strong> true
<strong>Explanation:</strong> Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'.
Now sub = "l33tb" is a substring of s, so we return true.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sub.length &lt;= s.length &lt;= 5000</code></li>
	<li><code>0 &lt;= mappings.length &lt;= 1000</code></li>
	<li><code>mappings[i].length == 2</code></li>
	<li><code>old<sub>i</sub> != new<sub>i</sub></code></li>
	<li><code>s</code> and <code>sub</code> consist of uppercase and lowercase English letters and digits.</li>
	<li><code>old<sub>i</sub></code> and <code>new<sub>i</sub></code> are either uppercase or lowercase English letters or digits.</li>
</ul>
</div>