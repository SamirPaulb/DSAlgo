<h2><a href="https://leetcode.com/problems/split-a-string-in-balanced-strings/">1221. Split a String in Balanced Strings</a></h2><h3>Easy</h3><hr><div><p><strong>Balanced</strong> strings are those that have an equal quantity of <code>'L'</code> and <code>'R'</code> characters.</p>

<p>Given a <strong>balanced</strong> string <code>s</code>, split it in the maximum amount of balanced strings.</p>

<p>Return <em>the maximum amount of split <strong>balanced</strong> strings</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "RLRRLLRLRL"
<strong>Output:</strong> 4
<strong>Explanation:</strong> s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "RLLLLRRRLR"
<strong>Output:</strong> 3
<strong>Explanation:</strong> s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "LLLLRRRR"
<strong>Output:</strong> 1
<strong>Explanation:</strong> s can be split into "LLLLRRRR".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>'L'</code> or <code>'R'</code>.</li>
	<li><code>s</code> is a <strong>balanced</strong> string.</li>
</ul>
</div>