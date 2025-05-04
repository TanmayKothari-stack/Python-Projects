<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<script src="jquery.js">
	$(document).ready(function(){
		refresh();
	});
	function refresh(){
		setTimeout(function(){
			$("#body").load('data.php');
			refresh();
		},1000);
	}
</script>
</body>
</html>