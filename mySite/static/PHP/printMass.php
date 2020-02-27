<?php
massPrint();

function massPrint() {
    echo '$_GET()<br>';
    foreach ($_GET as $value1 => $value2) {
        echo $value1.' : '.$value2.'<br>';
    }
    echo '$_POST()<br>';
    foreach ($_POST as $value1 => $value2) {
        echo $value1.' : '.$value2.'<br>';
    }
    echo '$_COOKIE()<br>';
    foreach ($_COOKIE as $value1 => $value2) {
        echo $value1.' : '.$value2.'<br>';
    }
}