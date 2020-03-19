//функции аккордеона
/*
$(document).ready(function(){
    initMenu();
})
*/


function initMenu() {
    //$('.active_l').hide();
    str = 'Элементы: ';    
    let elements = document.getElementsByClassName('vertmenu_l');   
    document.write(elements.length);
    let element = elements.item(0);
    //document.write(element + '<br>');
    //element.outerHTML = '111';
    document.write(element.id);
    //elements.forEach((x) => document.write(x));
    //str = elements.item(0).outerHTML;
    document.write(element);

    $('.vertmenu_l a').click(         
        function() {    
            document.write('0');        
            var iselemnt = $(this).next();
            if((iselemnt.is('ul')) && (iselemnt.is(':visible'))) {
                return false;
                document.write('1');
            }

            if((iselemnt.is('ul')) && (!iselemnt.is(':visible'))) {
                $('.vertmenu_l ul:visible').slideUp('normal');
                iselemnt.slideDown('normal');
                return false;
                document.write('2');
            }
        }
    ); 
}


//функции загрузки содержимого
function changeFunction(str) {
    var url = 'static/pages/' + str + '.html';

    var xhr = new XMLHttpRequest();
    xhr.responseType = "text";
    xhr.open("POST", url, true);
    xhr.onload = function(e) {
        if (this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText;
        } else {
            document.getElementById("content").innerHTML = 'НЕТ ЗНАЧЕНИЯ' 
                                                            + '<br>'
                                                            + 'Статус: ' + this.status 
                                                            + '<br>' 
                                                            + 'ID элемента: ' + str
                                                            + '<br>' 
                                                            + 'URL элемента: ' + url
        }
    };
    xhr.send();

    //getCurrentPage(str);
    //test(str);
    window.scrollTo(0, 0);
}

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

}

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

function myOnclick(str) {
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'change/', true);
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
    alert('Функция myOnclick - выполнена!');
}
