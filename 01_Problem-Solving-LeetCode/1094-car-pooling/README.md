<h2><a href="https://leetcode.com/problems/car-pooling/">1094. Car Pooling</a></h2><h3>Medium</h3><hr><div><p>There is a car with <code>capacity</code> empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).</p>

<p>You are given the integer <code>capacity</code> and an array <code>trips</code> where <code>trips[i] = [numPassengers<sub>i</sub>, from<sub>i</sub>, to<sub>i</sub>]</code> indicates that the <code>i<sup>th</sup></code> trip has <code>numPassengers<sub>i</sub></code> passengers and the locations to pick them up and drop them off are <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> respectively. The locations are given as the number of kilometers due east from the car's initial location.</p>

<p>Return <code>true</code><em> if it is possible to pick up and drop off all passengers for all the given trips, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 4
<strong>Output:</strong> false
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 5
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= trips.length &lt;= 1000</code></li>
	<li><code>trips[i].length == 3</code></li>
	<li><code>1 &lt;= numPassengers<sub>i</sub> &lt;= 100</code></li>
	<li><code>0 &lt;= from<sub>i</sub> &lt; to<sub>i</sub> &lt;= 1000</code></li>
	<li><code>1 &lt;= capacity &lt;= 10<sup>5</sup></code></li>
</ul>
</div>