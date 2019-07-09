(function () {
    "use strict";

    //Remove loading-wrapper class before window load
    setTimeout(function () {
        $('.loading-wrapper').removeClass('loading-wrapper-hide');
        return false;
    }, 10);

    //Page Loader 
    setTimeout(function () {
        $('#loader-name').addClass('loader-up');
        $('#loader-animation').addClass('loader-up');
        return false;
    }, 100);

    setTimeout(function () {
        $('#page-loader').addClass('loader-out');
        return false;
    }, 300);

    $('#page-loader').delay(800).fadeOut(10);

    //Owl Carousel
    // >> Project Single
    $("#project-single-carousel").owlCarousel({
        navigation: false, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        responsiveRefreshRate: 200,
        responsiveBaseWidth: window,
        pagination: true,
        singleItem: true,
        navigationText: ["<span class='fa fa-chevron-left'></span>", "<span class='fa fa-chevron-right'></span>"],
    });

    //back-to-top button
    $('.header').waypoint(function (direction) {
        if (direction === 'down') {
            $('#back-to-top').removeClass('back-to-top-hide');
        }
        else {
            $('#back-to-top').addClass('back-to-top-hide');
        }
    },
        {
            offset: '-400px'
        });

    function backToTop() {
        $('html, body').animate({
            scrollTop: 0
        }, 200);
    }

    $('.back-to-top').on('click', function () {
        backToTop();
        return false;
    });

    //Isotope
    var $container = $('#isotope-filter'),
        $optionContainer = $('#options'),
        $options = $optionContainer.find('a[href^="#"]').not('a[href="#"]'),
        isOptionLinkClicked = false;

    $container.imagesLoaded(function () {
        $container.isotope({
            itemSelector: '.element',
            resizable: false,
            transitionDuration: '0.3s',
            layoutMode: 'packery'
        });
    });

    function isotopeGO() {
        var thisThing = $(this),
            href = thisThing.attr('href');

        if (thisThing.hasClass('selected')) {
            return;
        } else {
            $options.removeClass('selected');
            thisThing.addClass('selected');
        }

        jQuery.bbq.pushState('#' + href);
        isOptionLinkClicked = true;
        return false;
    }

    $options.on('click', function () {
        isotopeGO();
    });

    $('.isotope-link').on('click', function () {
        backToTop();
        isotopeGO();
    });

    $(window).on('hashchange', function (event) {
        var theFilter = window.location.hash.replace(/^#/, '');

        if (theFilter == false)
            theFilter = 'home';

        $container.imagesLoaded(function () {
            $container.isotope({
                filter: '.' + theFilter
            });
        });

        if (isOptionLinkClicked == false) {
            $options.removeClass('selected');
            $optionContainer.find('a[href="#' + theFilter + '"]').addClass('selected');
        }

        isOptionLinkClicked = false;
    }).trigger('hashchange');

    //Viewport
    var windowHeight = $(window).height();

    function adjustViewport() {
        $('.viewport').css('min-height', windowHeight);
        return false;
    }
    adjustViewport();

    let mainNav = document.getElementById('js-menu');
    let navBarToggle = document.getElementById('js-navbar-toggle');

    navBarToggle.addEventListener('click', function () {
        mainNav.classList.toggle('active');
    });

    //Services-hover
    var thisBox = null;
    $('.element-box-interative').on('mouseenter', function () {

        thisBox = $(this);
        thisBox.addClass('element-box-hover1');

        var intervalBox1 = setTimeout(function () {
            thisBox.addClass('element-box-hover2');
        }, 400);

        var intervalBox2 = setTimeout(function () {
            thisBox.find('.element-box-ico').addClass('element-box-ico-hover');
        }, 800);

        return false;
    });

    $('.element-box-interative').on('mouseleave', function () {
        thisBox = $(this);

        $('.element-box-ico').removeClass('element-box-ico-hover');
        var intervalBox3 = setTimeout(function () {
            $('.element-box-interative').removeClass('element-box-hover2');
        }, 400);

        var intervalBox4 = setTimeout(function () {
            $('.element-box-interative').removeClass('element-box-hover1');
            $('.element-box-ico').removeClass('element-box-ico-hover');
        }, 800);

        return false;
    });


    // Fancybox
    // $(".fancybox-iframe-btn").fancybox({
    //     type: 'iframe',
    //     fitToView: true
    // });

    // $(".fancybox").fancybox({
    // });

    // $(".image-gallery a").fancybox({

    // });


    //Form Validator and Ajax Sender
    // $("#contactForm").validate({
    //     submitHandler: function (form) {
    //         $.ajax({
    //             type: "POST",
    //             url: "php/contact-form.php",
    //             data: {
    //                 "name": $("#contactForm #name").val(),
    //                 "email": $("#contactForm #email").val(),
    //                 "subject": $("#contactForm #subject").val(),
    //                 "message": $("#contactForm #message").val()
    //             },
    //             dataType: "json",
    //             success: function (data) {
    //                 if (data.response == "success") {
    //                     $("#contactSuccess").fadeIn(300).addClass('modal-show');
    //                     $("#contactError").addClass("hidden");
    //                     $("#contactForm #name, #contactForm #email, #contactForm #subject, #contactForm #message")
    //                         .val("")
    //                         .blur();
    //                 } else {
    //                     $("#contactError").fadeIn(300).addClass('modal-show');
    //                     $("#contactSuccess").addClass("hidden");
    //                 }
    //             }
    //         });
    //     }
    // });


    //Modal for Contact Form
    $('.modal-wrap').click(function () {
        $('.modal-wrap').fadeOut(300);
    });

    //Modal for Forms
    function hideModal() {
        $('.modal-wrap').fadeOut(300);
        return false;
    }

    $('.modal-wrap').on('click', function () {
        hideModal();
    });

    $('.modal-bg').on('click', function () {
        hideModal();
    });

    //bootstrap tooltips
    // $('[data-toggle="tooltip"]').tooltip();

    //End - Document Ready
})();
