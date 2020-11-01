<?php

session_start();

$server = "localhost";
$username = "root";
$password = "";
// make sure the db does exist on your machine
$database = 'details';

$con = mysqli_connect($server, $username, $password);
mysqli_select_db($con, $database) or die("Unable to select database");

if (!$con) {
    die("Connection to this databse failed due to " . mysqli_connect_error());
}

$sql_query = "SELECT `name`, `age`, `phoneNo` FROM `user_details`";
$result = mysqli_query($con, $sql_query)  or die(mysqli_error($link));
if ($result == false) {
    echo 'Unable to fetch';
    exit();
}

?>

<!DOCTYPE html>
<html>

<head>
    <title>Rooze q7</title>
    <style>
        table,
        td,
        th {
            border: 1px solid black;
        }
    </style>
</head>

<body>
    <table>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Phone number</th>
        </tr>
        <?php while ($row = mysqli_fetch_array($result)) {

            $name = $row['name'];
            $age = $row['age'];
            $phoneNo = $row['phoneNo'];
        ?>
            <tr>
                <td><?php echo $name; ?></td>
                <td><?php echo $age; ?></td>
                <td><?php echo $phoneNo; ?></td>
            </tr>
        <?php
        }
        ?>
    </table>
</body>

</html>