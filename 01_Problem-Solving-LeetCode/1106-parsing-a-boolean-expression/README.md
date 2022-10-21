<h2><a href="https://leetcode.com/problems/parsing-a-boolean-expression/">1106. Parsing A Boolean Expression</a></h2><h3>Hard</h3><hr><div><p>A <strong>boolean expression</strong> is an expression that evaluates to either <code>true</code> or <code>false</code>. It can be in one of the following shapes:</p>

<ul>
	<li><code>'t'</code> that evaluates to <code>true</code>.</li>
	<li><code>'f'</code> that evaluates to <code>false</code>.</li>
	<li><code>'!(subExpr)'</code> that evaluates to <strong>the logical NOT</strong> of the inner expression <code>subExpr</code>.</li>
	<li><code>'&amp;(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code> that evaluates to <strong>the logical AND</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.</li>
	<li><code>'|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code> that evaluates to <strong>the logical OR</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.</li>
</ul>

<p>Given a string <code>expression</code> that represents a <strong>boolean expression</strong>, return <em>the evaluation of that expression</em>.</p>

<p>It is <strong>guaranteed</strong> that the given expression is valid and follows the given rules.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> expression = "&amp;(|(f))"
<strong>Output:</strong> false
<strong>Explanation:</strong> 
First, evaluate |(f) --&gt; f. The expression is now "&amp;(f)".
Then, evaluate &amp;(f) --&gt; f. The expression is now "f".
Finally, return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> expression = "|(f,f,f,t)"
<strong>Output:</strong> true
<strong>Explanation:</strong> The evaluation of (false OR false OR false OR true) is true.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> expression = "!(&amp;(f,t))"
<strong>Output:</strong> true
<strong>Explanation:</strong> 
First, evaluate &amp;(f,t) --&gt; (false AND true) --&gt; false --&gt; f. The expression is now "!(f)".
Then, evaluate !(f) --&gt; NOT false --&gt; true. We return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li>expression[i] is one following characters: <code>'('</code>, <code>')'</code>, <code>'&amp;'</code>, <code>'|'</code>, <code>'!'</code>, <code>'t'</code>, <code>'f'</code>, and <code>','</code>.</li>
</ul>
</div>