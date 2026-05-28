(function($) {
    "use strict";

    //===== Preloader
    $(window).on('load', function(event) {
        $('.preloader').delay(500).fadeOut(500);
        $('#preloader_two').fadeOut();
        $(".techwix_image_preloader").fadeOut("slow");
    });

      //===== Header Sticky & Headroom.js
    jQuery(function ($) {
        var header = $(".header-get-sticky");
        var topHeader = $(".tpc-header-top-bar");
        var topHeaderHeight = topHeader.length ? topHeader.outerHeight() : 0;
        var topHeaderHidden = false;

        var stickyMode = typeof techwix_sticky_data !== 'undefined' ? techwix_sticky_data.mode : 'smart';

        if (header.length) {
            if (stickyMode === 'always') {
                $(window).on("scroll", function () {
                    var scrollTop = $(this).scrollTop();

                    if (scrollTop > 100) {
                        header.addClass("top-header-removed");
                    } else {
                        header.removeClass("top-header-removed");
                    }

                    if (scrollTop > topHeaderHeight && !topHeaderHidden) {
                        topHeader.slideUp(200);
                        topHeaderHidden = true;
                    } else if (scrollTop === 0 && topHeaderHidden) {
                        topHeader.slideDown(200);
                        topHeaderHidden = false;
                    }
                });
            } else if (stickyMode === 'smart') {
                var options = {
                    offset: {
                        up: 100,
                        down: 200
                    },
                    tolerance: {
                        up: 5,
                        down: 0
                    },
                    classes: {
                        pinned: "headroom--pinned",
                        unpinned: "headroom--unpinned",
                        top: "headroom--top",
                        notTop: "headroom--not-top"
                    }
                };
                var myElement = document.querySelector(".header-get-sticky");
                var headroom = new Headroom(myElement, options);
                headroom.init();
            }
        }
    });


    //===== Login/Register Popup Modal
    $('.tpc-login-register-popup-trigger').on('click', function(e) {
        e.preventDefault();
        $('.techwix-login-form-popup').toggleClass('login-popup-visible');
        $('.techwix-login-popup-overlay').toggleClass('active');
    });

    const login_btn = document.querySelector(".login-item");
    const register_btn = document.querySelector(".register-item");
    $(".register-form").css("display", "none");

    $(function() {
        $('.login-item, #techwix-login-form-trigger').on(function() {
            login_btn.classList.add("active");
            $(".register-form").css("display", "none");
            if (register_btn.classList.contains("active")) {
                register_btn.classList.remove("active");
                $(".login-form").removeAttr("style");
            }
        });

        $('.register-item, #techwix-register-form-trigger').on(function() {
            register_btn.classList.add("active");
            $(".login-form").css("display", "none");
            if (login_btn.classList.contains("active")) {
                login_btn.classList.remove("active");
                $(".register-form").removeAttr("style");
            }
        });
    });

   //===== Close Login/Register Modal on Click Outside
    $('.techwix-custom-login-wrapper').on('click', function() {
        console.log("clicked");
    });

    //===== Close Login Modal on Close Button Click
    $('.techwix-login-popup-close .close-trigger').on('click', function() {
        $('.techwix-login-form-popup').removeClass('login-popup-visible');
        $('.techwix-login-popup-overlay').removeClass('active');
    });

    //===== Mobile Menu
    $('.techwix-mobile-hamburger-menu').on('click', function() {
        $(".techwix-mobile-hamburger-menu > a").toggleClass('techwix-mobile-menu-close--active');
        $(".techwix-mobile-menu-nav-wrapper").toggleClass('techwix-mobile-menu-visible');
        $('body').toggleClass('techwix-mobile-menu-active');
    });

    $('.techwix-mobile-menu-close > a').on('click', function() {
        $('.techwix-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
        $('.techwix-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
        $('body').removeClass('techwix-mobile-menu-active');
    });

    $('.techwix-mobile-menu-overlay').on('click', function() {
        $('.techwix-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
        $('.techwix-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
        $('body').removeClass('techwix-mobile-menu-active');
    });

    //===== Accordion Menu for Mobile
    $.fn.extend({
        accordionMenu: function(options) {
            var defaults = {
                speed: 400
            }
            var options = $.extend(defaults, options);

            return this.each(function() {
                $(this).addClass('techwix-mobile-menu-item');
                var menuItems = $(this).children('li');
                menuItems.find('.techwix-mobile-menu-item > .techwix-dropdown-menu').parent().addClass('menu-item-has-children');
                $('.techwix-mobile-menu-item .menu-item-has-children .techwix-dropdown-menu').hide();
                $('.techwix-mobile-menu-item .menu-item-has-children > a .techwix-menu-icon').on('click', function(event) {
                    event.stopPropagation();
                    event.preventDefault();
                    $(this).parent().siblings('.techwix-dropdown-menu').slideToggle(options.speed);
                    $(this).parent().siblings('.techwix-mega-menu').slideToggle(options.speed);
                });
            });
        }
    });
    $('#techwix-mobile-menu-item').accordionMenu();

    
    //===== Elementor Mobile Menu
    $('.techwix-elementor-mobile-hamburger-menu').on('click', function() {
        $(".techwix-elementor-mobile-hamburger-menu > a").toggleClass('techwix-mobile-menu-close--active');
        $(".techwix-elementor-mobile-menu-nav-wrapper").toggleClass('techwix-mobile-menu-visible');
        $('body').toggleClass('techwix-mobile-menu-active');
    });

    $('.techwix-elementor-mobile-menu-close > a').on('click', function() {
        $('.techwix-elementor-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
        $('.techwix-elementor-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
        $('body').removeClass('techwix-mobile-menu-active');
    });

    $('.techwix-elementor-mobile-menu-overlay').on('click', function() {
        $('.techwix-elementor-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
        $('.techwix-elementor-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
        $('body').removeClass('techwix-mobile-menu-active');
    });

    //===== Accordion Menu for Elementor Mobile
    $.fn.extend({
        accordionMenu: function(options) {
            var defaults = {
                speed: 400
            }
            var options = $.extend(defaults, options);

            return this.each(function() {
                $(this).addClass('techwix-elementor-mobile-menu-item');
                var menuItems = $(this).children('li');
                menuItems.find('.techwix-elementor-mobile-menu-item > .techwix-dropdown-menu').parent().addClass('menu-item-has-children');
                $('.techwix-elementor-mobile-menu-item .menu-item-has-children .techwix-dropdown-menu').hide();
                $('.techwix-elementor-mobile-menu-item .menu-item-has-children > a .techwix-menu-icon').on('click', function(event) {
                    event.stopPropagation();
                    event.preventDefault();
                    $(this).parent().siblings().slideToggle(options.speed);
                    $(this).parent().siblings('.techwix-mega-menu').slideToggle(options.speed);
                });
            });
        }
    });
    $('#techwix-elementor-mobile-menu-item').accordionMenu();

    //===== WooCommerce Helper
    function techwix_woocommerce_helper() {
        $('.product-over-info ul li.add-to-cart a.add_to_cart_button.ajax_add_to_cart').on("click", function() {
            $(this).closest('li').addClass('added_to_cart_item');
        });
    }

    //===== Swiper Carousel
    const swiper = new Swiper('.tpc-swiper-carousel-activator', {
        slidesPerView: 1,
        spaceBetween: 10,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            '@0.75': {
                slidesPerView: 2,
                spaceBetween: 20,
            },
            '@1.00': {
                slidesPerView: 3,
                spaceBetween: 40,
            },
            '@1.50': {
                slidesPerView: 4,
                spaceBetween: 1,
            },
        }
    });

    //===== SAL Animation
    sal();

    //===== Video Popup
    $(function() {
        $("a.bla-1").YouTubePopUp();
        $("a.bla-2").YouTubePopUp({ autoplay: 0 });
    });

    //===== Search
    $('#search').on('click', function() {
        $(".techwix-search-box").fadeIn(600);
    });
    
    $('.top-search').on('click', function() {
        $(".techwix-search-box").fadeIn(600);
    });

    $('.techwix-closebtn').on('click', function() {
        $(".techwix-search-box").fadeOut(600);
    });      


})(jQuery);
