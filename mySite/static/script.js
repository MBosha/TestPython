//функции аккордеона
/*
$(document).ready(function(){
    $("#vertmenu_l").css("background-color", "yellow"); 
    initMenu();
})


function initMenu() {
    //$('.active_l').hide();
    elements = document.getElementsByClassName('subCat_l');    
    element = elements[0];
    str = '';
    str = str + element.textContent;
    alert(str);
    //element.checked = true;
    

    $('.vertmenu_l').click(         
        function() {            
            var iselemnt = $(this).next();
            if((iselemnt.is('ul')) && (iselemnt.is(':visible'))) {
                return false;
            }

            if((iselemnt.is('ul')) && (!iselemnt.is(':visible'))) {
                $('.vertmenu_l ul:visible').slideUp('normal');
                iselemnt.slideDown('normal');
                return false;
            }
        }
    ); 
}
*/

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
                                                            + 'ID элетента: ' + str
                                                            + '<br>' 
                                                            + 'URL элетента: ' + url
                                                            + '<br>' 
                                                            + document.cookie;
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
