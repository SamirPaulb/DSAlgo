<h2><a href="https://leetcode.com/problems/design-a-text-editor/">2296. Design a Text Editor</a></h2><h3>Hard</h3><hr><div><p>Design a text editor with a cursor that can do the following:</p>

<ul>
	<li><strong>Add</strong> text to where the cursor is.</li>
	<li><strong>Delete</strong> text from where the cursor is (simulating the backspace key).</li>
	<li><strong>Move</strong> the cursor either left or right.</li>
</ul>

<p>When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that <code>0 &lt;= cursor.position &lt;= currentText.length</code> always holds.</p>

<p>Implement the <code>TextEditor</code> class:</p>

<ul>
	<li><code>TextEditor()</code> Initializes the object with empty text.</li>
	<li><code>void addText(string text)</code> Appends <code>text</code> to where the cursor is. The cursor ends to the right of <code>text</code>.</li>
	<li><code>int deleteText(int k)</code> Deletes <code>k</code> characters to the left of the cursor. Returns the number of characters actually deleted.</li>
	<li><code>string cursorLeft(int k)</code> Moves the cursor to the left <code>k</code> times. Returns the last <code>min(10, len)</code> characters to the left of the cursor, where <code>len</code> is the number of characters to the left of the cursor.</li>
	<li><code>string cursorRight(int k)</code> Moves the cursor to the right <code>k</code> times. Returns the last <code>min(10, len)</code> characters to the left of the cursor, where <code>len</code> is the number of characters to the left of the cursor.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
<strong>Output</strong>
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

<strong>Explanation</strong>
TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
                          // The current text is "leet|". 
                          // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
                           // The current text is "leetpractice|". 
                           // The cursor cannot be moved beyond the actual text and thus did not move.
                           // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
                          // The current text is "leet|practice".
                          // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
                           // The current text is "|practice".
                           // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
                          // The current text is "|practice".
                          // The cursor cannot be moved beyond the actual text and thus did not move. 
                          // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
                           // The current text is "practi|ce".
                           // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length, k &lt;= 40</code></li>
	<li><code>text</code> consists of lowercase English letters.</li>
	<li>At most <code>2 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>addText</code>, <code>deleteText</code>, <code>cursorLeft</code> and <code>cursorRight</code>.</li>
</ul>
</div>