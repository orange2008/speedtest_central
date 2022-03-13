<?php
$name = $_POST['name'];
date_default_timezone_set("Asia/Shanghai");
$date = date('Y-m-d-H-i');
$uploaded = $_FILES['file']['tmp_name'];
$path = "./";
$filename = $date . ".json";
move_uploaded_file($uploaded, $path . $filename);
$output = shell_exec("python3 ./main.py '" . $name . "' " . $filename);
echo "python3 ./main.py '" . $name . "' " . $filename;
echo "<br />";
echo $output;
?>

