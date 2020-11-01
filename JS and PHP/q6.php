<?php
if (isset($_POST['name'])) {
    $server = "localhost";
    $username = "root";
    $password = "";

    $con = mysqli_connect($server, $username, $password);

    if (!$con) {
        die("connection to this databse failed due to " . mysqli_connect_error());
    }
    // echo "Success connecting to the db";
    // before implementing this code, create a database "details" in phpMyAdmin, and then a table "user_details" with sno as primary key (auto_incremented), name (as varchar(25)), age(as tinyint(3)) and phoneNo (as bigint(10)). 

    $name = $_POST['name'];
    $age = $_POST['age'];
    $phoneNo = $_POST['phoneNo'];
    $sql = "INSERT INTO `details`.`user_details` (`name`, `age`, `phoneNo`) VALUES ('$name', '$age', '$phoneNo');";

    if ($con->query($sql) == true) {
        //echo "Successfully inserted";
    } else {
        echo "ECHO: $sql <br> $con->error";
    }
    $con->close();
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Rooze q6</title>
</head>

<body>
    Add your info:
    <form action="q6.php" method="POST">
        <table>
            <tr>
                <td>
                    Name:
                </td>
                <td>
                    <input type="text" name="name" placeholder="Rooze">
                </td>
            </tr>
            <tr>
                <td>
                    Age:
                </td>
                <td>
                    <input type="number" name="age" placeholder="19">
                </td>
            </tr>
            <tr>
                <td>
                    Phone Number:
                </td>
                <td>
                    <input type="number" name="phoneNo" placeholder="7983553007">
                </td>
            </tr>
        </table>
        <input type="submit">
    </form>
</body>

</html>