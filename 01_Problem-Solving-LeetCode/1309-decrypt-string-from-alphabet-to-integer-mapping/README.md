<h2><a href="https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/">1309. Decrypt String from Alphabet to Integer Mapping</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code>s</code> formed by digits and <code>'#'</code>. We want to map <code>s</code> to English lowercase characters as follows:</p>

<ul>
	<li>Characters (<code>'a'</code> to <code>'i')</code> are represented by (<code>'1'</code> to <code>'9'</code>) respectively.</li>
	<li>Characters (<code>'j'</code> to <code>'z')</code> are represented by (<code>'10#'</code> to <code>'26#'</code>) respectively.</li>
</ul>

<p>Return <em>the string formed after mapping</em>.</p>

<p>The test cases are generated so that a unique mapping will always exist.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "10#11#12"
<strong>Output:</strong> "jkab"
<strong>Explanation:</strong> "j" -&gt; "10#" , "k" -&gt; "11#" , "a" -&gt; "1" , "b" -&gt; "2".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "1326#"
<strong>Output:</strong> "acz"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of digits and the <code>'#'</code> letter.</li>
	<li><code>s</code> will be a valid string such that mapping is always possible.</li>
</ul>
</div>