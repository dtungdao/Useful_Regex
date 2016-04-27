import re

HTML_CODE = '''
<html>
	<head>
		<title>Sample "Hello, World" Application</title>
	</head>
	
	<body bgcolor=white>
	<table border="0" cellpadding="10">
	<tr>
		<td>
			<img src="images/springsource.png">
		</td>
		<td>
			<h1>Sample "Hello, World" Application</h1>
		</td>
	</tr>
	</table>

	<p>This is the home page for the HelloWorld Web application. </p>
	<p>To prove that they work, you can execute either of the following links:</p>
	<ul>
		<li>To a <a href="hello.jsp">JSP page</a></li>
		<li>To a <a href="hello">servlet</a>.</li>
	</ul>
	</body>
</html>
'''

def GetHtmlTag(HTML_TAG, text):
	'''
	regex = <HTML-TAG\b[^>]*>([\s\S]*?)<\/HTML-TAG>
	'''
	blocks = re.findall(r"<" + HTML_TAG + r"\b[^>]*>([\s\S]*?)<\/" + HTML_TAG + r">", text)
	return blocks
	
if __name__ == '__main__':
	html_blocks = GetHtmlTag("td", HTML_CODE)
	
	for block in html_blocks:
		print(block)
		print("=" * 20)
