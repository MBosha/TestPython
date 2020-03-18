$(document).ready(function(){
    initMenu();
})

function initMenu() {

    $('#vertmenu_l ul').hide();
    $('#vertmenu_l ul li:eq(0)').show();

    $('#vertmenu_l li a').click(
        function() {
            var iselemnt = $(this).next();
            if((iselemnt.is('ul')) && (iselemnt.is(':visible'))) {
                return false;
            }

            if((iselemnt.is('ul')) && (!iselemnt.is(':visible'))) {
                $('#vertmenu_l ul:visible').slideUp('normal');
                iselemnt.slideDown('normal');
                return false;
            }
        }
    );
}