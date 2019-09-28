(function( $ ) {

    'use strict';

    $('#menu-toggle').on('click', function(e) {
        e.preventDefault();
        $('#wrapper').toggleClass('toggled');
    });

    $('.sidebar-nav li.parent a').on('click', function(e) {
        e.preventDefault();
        $(this).toggleClass('rotate');
        $(this).parent().find('.children').toggleClass('active');
    })

})( jQuery );