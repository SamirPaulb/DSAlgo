<h2><a href="https://leetcode.com/problems/repeated-string-match/">686. Repeated String Match</a></h2><h3>Medium</h3><hr><div><p>Given two strings <code>a</code> and <code>b</code>, return <em>the minimum number of times you should repeat string </em><code>a</code><em> so that string</em> <code>b</code> <em>is a substring of it</em>. If it is impossible for <code>b</code>​​​​​​ to be a substring of <code>a</code> after repeating it, return <code>-1</code>.</p>

<p><strong>Notice:</strong> string <code>"abc"</code> repeated 0 times is <code>""</code>, repeated 1 time is <code>"abc"</code> and repeated 2 times is <code>"abcabc"</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> a = "abcd", b = "cdabcdab"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We return 3 because by repeating a three times "ab<strong>cdabcdab</strong>cd", b is a substring of it.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> a = "a", b = "aa"
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist of lowercase English letters.</li>
</ul>
</div>