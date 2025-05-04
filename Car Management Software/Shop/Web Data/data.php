<?php 

$conn = mysqli_connect($host='localhost',$user='root',$password='',$dbname='shopping');

$devicename = gethostname();
$data = mysqli_query($conn,"select * from logindata where device_name = '$devicename' ");
$total = mysqli_num_rows($data);
$result = mysqli_fetch_array($data);

if($total == 1)
{

}
else{
	echo "<script>alert('Please Login First')</script>";
}

 ?>
 <!DOCTYPE html>
 <html>
 <head>
 	<title>Cars Data</title>
 	<style type="text/css">
 		*{
 			text-decoration: none;
 			color: white;
 		}
 		table{
 			border-color: white;
 			text-align: center;
 		}
 	</style>
 </head>
 <body bgcolor="#5453a6">
 	<h3 align="center">All Cars Data</h3>
 <table border="1" width="100%" cellspacing="10">
 	<?php 
 	echo "<tr>

 	<td>Car Id</td>
 	<td>Car Name</td>
 	<td>Car Price</td>
 	<td>Model Date</td>
 	<td>Car Type</td>
 	<td>Car Capicity</td>
 	<td>Car Brand</td>
 	<td>Car Features</td>
 	<td>Update</td>
 	<td>Delete</td>

 	</tr>";

	$devicename = gethostname();
	$data = mysqli_query($conn,"select * from cars_data where device_name = '$devicename' ");

 	while($res = mysqli_fetch_array($data))
 	{
 	echo "<tr>

 	<td>$res[0]</td>
 	<td>$res[1]</td>
 	<td>$res[2]</td>
 	<td>$res[3]</td>
 	<td>$res[4]</td>
 	<td>$res[5]</td>
 	<td>$res[6]</td>
 	<td>$res[7]</td>
 	<td><a href='' style='color: yellow;'>Update</td>
 	<td><a href='' style='color: red;'>Delete</td>

 	</tr>";

 }

 	 ?>
 </table>
 </body>
 </html>