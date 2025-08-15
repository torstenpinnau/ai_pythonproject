<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
$name = $_POST['vorname'];
$website = $_POST['aktion'];

}
echo $name .'Welcome '. $website;
?>