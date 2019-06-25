<html>
<head>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="css/demo.css">
	<link rel="stylesheet" href="css/footer-distributed-with-address-and-phones.css">
	
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">

	<link href="http://fonts.googleapis.com/css?family=Cookie" rel="stylesheet" type="text/css">
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>

</head>
<body  style="background-image:url('a.jpg'); ">
<h1 style="font-size:50px; color:white; text-align:center; margin-top:100px;">RESULT</h1>
<?php
require('connect.php');
$result=0;
if(isset($_POST['submit'])){
$i=1;
$fname = $_POST['fname'];                                                                                            
$lname = $_POST['lname'];
   for($i=1;$i<=10;$i++){
	$str = strval($i);
	if(isset($_POST[strval($i)])){
	$selected=$_POST[strval($i)]; 
    $q="select * from ans where id='$i'";
	$query=mysqli_query($connection,$q);
	while($rows=mysqli_fetch_array($query)){
		$checked=($rows['answer']==$_POST[strval($i)]);
		if($checked){
			$result++;
		    }
	}
	}
   }
	     $a="SELECT * FROM `user`";
		 $b=mysqli_query($connection,$a);
	     while($row=mysqli_fetch_array($b)){
		 if($row['fname']==$_POST['fname'] && $row['lname']==$_POST['lname']){
			 $c = "UPDATE `user` set score='$result' where fname='".$_POST['fname']."' and lname='".$_POST['lname']."'";
			 $d=mysqli_query($connection,$c);
		 }
		    }
		 
		 $query = "INSERT INTO `user` (fname,lname,score) VALUES ('$fname' ,'$lname','$result')";
         $res = mysqli_query($connection, $query);
		 ?>

	   
	 
    <div class="card" style="width:130px; height:120px; display:inline-block; margin-left:500px; margin-top:100px;">
     <div class="card-header bg-primary" style="font-size:15px;text-align:center;">First Name</div>
	 <div class="card-body" style="text-align:center;">
     <?php echo $_POST['fname'];?>
	 </div>
	 </div>
	 <div class="card" style="width:130px; height:120px; display:inline-block;">
     <div class="card-header bg-primary" style="font-size:15px;text-align:center;">Last Name</div>
	 <div class="card-body" style="text-align:center;">
     <?php echo $_POST['lname'];?>
	 </div>
	 </div>
	 <div class="card" style="width:130px; height:120px; display:inline-block;">
     <div class="card-header bg-primary" style="font-size:15px;text-align:center;">Score</div>
	 <div class="card-body" style="text-align:center;">
     <?php echo $result;?>
	 </div>
	 </div>
	 <div class="card" style="width:130px; height:120px; display:inline-block;">
     <div class="card-header bg-primary" style="font-size:15px;text-align:center;">Time</div>
	 <div class="card-body" style="text-align:center;">
     <span id="my"></span>
	 </div>
	 </div>

<?php } 
	   ?>
	   <script>
		var h,m,s;
	
function init(){
    d=new Date();
    h = d.getHours();
    m = d.getMinutes();
    s = d.getSeconds();
    clock();
	
};
function clock(){
s++;
    if(s==60){
        s=0;
        m++;
        if(m==60){
            m=0;
            h++;
            if(h==24){
                h=0;
            }
        }
    }
    animate=setTimeout(clock,1000);
	document.getElementById("my").innerHTML = h +":"+m+":"+s;
};

function $(id,val){
    if(val<10){
        val='0'+val;
    }
    document.getElementById(id).innerHTML=val;
};

window.onload=init;
</script>

	   </body>
	   </html>
	   
