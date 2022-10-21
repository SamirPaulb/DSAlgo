<h2><a href="https://leetcode.com/problems/minimum-cost-for-tickets/">983. Minimum Cost For Tickets</a></h2><h3>Medium</h3><hr><div><p>You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array <code>days</code>. Each day is an integer from <code>1</code> to <code>365</code>.</p>

<p>Train tickets are sold in <strong>three different ways</strong>:</p>

<ul>
	<li>a <strong>1-day</strong> pass is sold for <code>costs[0]</code> dollars,</li>
	<li>a <strong>7-day</strong> pass is sold for <code>costs[1]</code> dollars, and</li>
	<li>a <strong>30-day</strong> pass is sold for <code>costs[2]</code> dollars.</li>
</ul>

<p>The passes allow that many days of consecutive travel.</p>

<ul>
	<li>For example, if we get a <strong>7-day</strong> pass on day <code>2</code>, then we can travel for <code>7</code> days: <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, <code>6</code>, <code>7</code>, and <code>8</code>.</li>
</ul>

<p>Return <em>the minimum number of dollars you need to travel every day in the given list of days</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> days = [1,4,6,7,8,20], costs = [2,7,15]
<strong>Output:</strong> 11
<strong>Explanation:</strong> For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
<strong>Output:</strong> 17
<strong>Explanation:</strong> For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days.length &lt;= 365</code></li>
	<li><code>1 &lt;= days[i] &lt;= 365</code></li>
	<li><code>days</code> is in strictly increasing order.</li>
	<li><code>costs.length == 3</code></li>
	<li><code>1 &lt;= costs[i] &lt;= 1000</code></li>
</ul>
</div>