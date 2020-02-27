<?php
setCurrentPage();

function getCurrentPage() {

    // Подключение к MySQL
    $servername = "localhost"; // локалхост
    $username = "root"; // имя пользователя
    $password = ""; // пароль если существует
    $dbname = "raz_db"; // база данных

    // Создание соединения
    $connSelect = new mysqli($servername, $username, $password, $dbname);
    // Проверка соединения
    if ($connSelect->connect_error) {
        die("Ошибка подключения: " . $connSelect->connect_error);
    }

    $sqlSelect = "SELECT `page` FROM `current_page` LIMIT 1";
    $result = $connSelect->query($sqlSelect);

    if ($result->num_rows > 0) {
        // Выводим данные каждой строки
        $count = 0;
        while($row = $result->fetch_assoc()) {
            $str = $count.': '.$row["page"].'<br>';
            $mass[$count] = $str;
            $count++;
        }
    } else {
        $str = "0 results";
        $mass[0] = $str;
    }
    $connSelect->close();
    for ($i = 0; $i <= $count; $i++) {
        echo $mass[$i];
    }
}

function setCurrentPage() {

    // Подключение к MySQL
    $servername = "localhost"; // локалхост
    $username = "root"; // имя пользователя
    $password = ""; // пароль если существует
    $dbname = "raz_db"; // база данных

    // Создание соединения
    $connSelect = new mysqli($servername, $username, $password, $dbname);
    // Проверка соединения
    if ($connSelect->connect_error) {
        die("Ошибка подключения: " . $connSelect->connect_error);
    }

    $page = $_COOKIE['currPage'];
    $text = "UPDATE `current_page` SET `page`='".$page."' LIMIT 1";
    $result = $connSelect->query($text);
    $connSelect->close();

}