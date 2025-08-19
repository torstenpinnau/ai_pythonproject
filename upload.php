<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
$name = $_POST['name'];
$website = $_POST['email'];

}
echo $name .'Welcome '. $website;
?>