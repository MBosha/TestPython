function changeFunction(str) {
    var url = 'static/templates/' + str + '.html';

    var xhr = new XMLHttpRequest();
    xhr.responseType = "text";
    xhr.open("POST", url, true);
    xhr.onload = function(e) {
        if (this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText;
        } else {
            document.getElementById("content").innerHTML = 'НЕТ ЗНАЧЕНИЯ' + '<br>' + 'Статус: ' + this.status;
        }
    };
    xhr.send();

    //getCurrentPage(str);
    test(str);
    window.scrollTo(0, 0);
};

function getCurrentPage(str) {
    document.cookie = "currPage=" + str;
    var url = 'static/PHP/functionPHP.php';

    var xhr = new XMLHttpRequest();
    xhr.responseType = "text";
    xhr.open("POST", url, true);
    xhr.setRequestHeader('123', '123');
    xhr.onload = function(e) {
        if (this.status == 200) {
            document.getElementById("rightDiv").innerHTML = this.responseText;
        } else {
            document.getElementById("rightDiv").innerHTML = 'НЕТ ЗНАЧЕНИЯ';
        }
    };
    xhr.send();

};

function test(str) {
    document.cookie = "user=John";    
    for (let i = 0; i < 23; i++) {
        document.cookie = str + "_" + i + "=" + str;
     }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'static/left.php', true);
    //Передает правильный заголовок в запросе
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        //Вызывает функцию при смене состояния.
        if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            // Запрос завершен. Здесь можно обрабатывать результат.
            /*document.getElementById("asideRight").innerHTML = this.responseText + document.cookie;*/
            document.getElementById("asideRight").innerHTML = "Это куки:<br> " + document.cookie
        }
    }
    xhr.send(str);
}
