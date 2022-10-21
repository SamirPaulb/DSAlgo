<h2><a href="https://leetcode.com/problems/repeated-dna-sequences/">187. Repeated DNA Sequences</a></h2><h3>Medium</h3><hr><div><p>The <strong>DNA sequence</strong> is composed of a series of nucleotides abbreviated as <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.</p>

<ul>
	<li>For example, <code>"ACGAATTCCG"</code> is a <strong>DNA sequence</strong>.</li>
</ul>

<p>When studying <strong>DNA</strong>, it is useful to identify repeated sequences within the DNA.</p>

<p>Given a string <code>s</code> that represents a <strong>DNA sequence</strong>, return all the <strong><code>10</code>-letter-long</strong> sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>Output:</strong> ["AAAAACCCCC","CCCCCAAAAA"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "AAAAAAAAAAAAA"
<strong>Output:</strong> ["AAAAAAAAAA"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, or <code>'T'</code>.</li>
</ul>
</div>