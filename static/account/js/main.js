$(document).ready(function () {
    $('.nav-link').click(function(e){
        e.preventDefault();
        $('.nav-link').removeClass('nav-link_active');
        $(this).addClass('nav-link_active');
    })
    
    $('.aside-title').click(function(){
        $('.table-body').slideToggle(300);
        $(this).toggleClass('aside-active');
    })
    
    $(function(){
        $(window).bind("resize",function(){
         if($(this).width() < 1199){
            $('.table-body').css('display', 'none');
            $('.aside-active').removeClass('aside-active');
         } else {
            $('.table-body').css('display', 'block');
         }
        }).resize();
    });
    

    
    
    
    
});
