(function( $ ) {

    'use strict';

    /* global jQuery */
    /* global toastr */

    // Sidebar Nav Toggler
    $('#menu-toggle').on('click', function(e) {
        e.preventDefault();
        $('#wrapper').toggleClass('toggled');
    });

    // Sidebar Nav Dropdown
    $('.sidebar-nav li.parent > a').on('click', function(e) {
        e.preventDefault();
        $(this).toggleClass('rotate');
        $(this).parent().find('.children').toggleClass('active');
    });

    $('.toastr').each(function() {
        var toastr_tag = $(this).attr('data-tag');
        var toastr_message = $(this).attr('data-message');

        if ( toastr_tag == 'success' ) {
            toastr.success(toastr_message);
        } else if ( toastr_tag == 'warning' ) {
            toastr.warning(toastr_message);
        } else if ( toastr_tag == 'error' ) {
            toastr.error(toastr_message);
        } else if ( toastr_tag == 'info' ) {
            toastr.info(toastr_message);
        } else {
            toastr.info(toastr_message);
        }

        toastr.options = {
            'progressBar' : true,
            'preventDuplicates' : true,
        };
    });

})( jQuery );