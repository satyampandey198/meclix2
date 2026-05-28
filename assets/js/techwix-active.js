(function($) {
    "use strict";

    // ==== Testimonial ====
    var WidgetTestimonialCarouselHandler = function($scope, $) {
        var $carouselElem = $scope.find('.tpc-testimonial_wrapper').eq(0);
        var settings = $carouselElem.data('settings');

        if (settings !== undefined) {
            var autoPlay = settings['autoplay'];
            var autoplaySpeed = parseInt(settings['autoplay_speed']) || 3000;
            var infiniteLoop = settings['infinite_loop'];
            var centerSlides = settings['center_slides'];
            var displayColumns = settings['display_columns'] || 2;
            var itemGap = parseInt(settings['item_gap']) || 20;
            var pauseOnHover = settings['pause_on_hover'];
            var pauseOnInteraction = settings['pause_on_interaction'];
        
            var displayColumnsTablet = settings['display_columns_tablet'] || 2;
            var tabletItemGap = parseInt(settings['tablet_item_gap']) || 20;
            var centerSlidesTab = settings['center_slides_tablet'];
        
            var displayColumnsMobile = settings['display_columns_mobile'] || 1;
            var mobileItemGap = parseInt(settings['mobile_item_gap']) || 0;
            var centerSlidesMobile = settings['center_slides_mobile'];
        
            var autoplayOptions = autoPlay ? {
                delay: autoplaySpeed,
                pauseOnMouseEnter: pauseOnHover,
                disableOnInteraction: pauseOnInteraction,
            } : false;
        
            var swiperParams = {
                spaceBetween: itemGap,
                slidesPerView: displayColumns,
                loop: infiniteLoop,
                centeredSlides: centerSlides,
                pagination: {
                    el: $carouselElem.find('.testi-pagination')[0], // Using [0] to get the DOM element
                    clickable: true,
                },
                navigation: {
                    nextEl: $carouselElem.find('.testi-button-next')[0],
                    prevEl: $carouselElem.find('.testi-button-prev')[0],
                },
                autoplay: autoplayOptions,
                breakpoints: {
                    0: {
                        slidesPerView: displayColumnsMobile,
                        spaceBetween: mobileItemGap,
                        centeredSlides: centerSlidesMobile,
                    },
                    575: {
                        slidesPerView: displayColumnsTablet,
                        spaceBetween: tabletItemGap,
                        centeredSlides: centerSlidesTab,
                    },
                    992: {
                        slidesPerView: displayColumns,
                        centeredSlides: centerSlides,
                    },
                }
            };
        
            // Generate a unique selector for the Swiper container
            var $swiperContainer = $carouselElem.find('.tpc_testimonial');
            var uniqueId = 'swiper-container-' + Math.random().toString(36).substr(2, 9);
            $swiperContainer.addClass(uniqueId);
        
            new Swiper('.' + uniqueId, swiperParams);
        }
       
    };

    // ==== Accordion ====

    var WidgetAccordionsMapHandler = function($scope, $) {
        // Getting Accordion id
        var accordion_element = $scope.find('.accordion').eq(0);
        var settings = accordion_element.data('settings');
        var close_all = accordion_element.data('close-all');
        var open_item = accordion_element.data('open-item');
        var elem_id = settings['accordion_id'];
 
        // Define scoped selectors
        var header_class = ".techwix-accordion-header" + elem_id;
        var content_class = ".accordion-body" + elem_id;
        var icon_class = ".techwix-icon" + elem_id;
        var speed = 400;
    
        // Scoped selection of elements within the current accordion
        const questions = $scope.find(header_class);
        const acc_content = $scope.find(content_class);
    

        if(close_all === true){
            // Initially close all accordion bodies and remove 'active' class from headers
            acc_content.hide();  // Hide all accordion bodies
            questions.removeClass('active'); // Remove 'active' class from all headers
        }else{
            // Initially close all accordion bodies except the n one
            acc_content.hide().eq(open_item).show();  // Hide all, then show the n
            questions.removeClass('active').eq(open_item).addClass('active'); // Remove 'active' class from all, then add it to the n
        }
 
    
        questions.each(function(index, element) {
            $(element).on("click", function() {
                var $this = $(this);
                var nextBox = $this.next();
    
                // Toggle the clicked accordion
                $this.toggleClass('active');
                nextBox.slideToggle(speed);
    
                // Close all other accordion bodies and remove 'active' class from other headers
                acc_content.not(nextBox).slideUp(speed);
                questions.not($this).removeClass('active');
            });
        });
    };

    //===== Counter =====
    var WidgetCounterHandler = function($scope, $) {
        var count_elem = $scope.find('.eb_counting').eq(0);
        count_elem.counterUp({
            delay: 10,
            time: 1000,
        });
    }

    // ====== Countdown =====
    var WidgetCountdown = function($scope, $) {
       
        var accordion_element = $scope.find('.techwix-countdown-timer-widget').eq(0);
        var settings = accordion_element.data('settings');
        var elem_id = settings['countdown_id'];
        
        //date id with id prefix for multiple elementor element in same page
        var days_id = "days"+elem_id;
        var hours_id = "hours"+elem_id;
        var minutes_id = "minutes"+elem_id;
        var seconds_id = "seconds"+elem_id;
        var countdown_id = "countdown"+elem_id;
        var label_id = "ctw-label"+elem_id;

        var date = settings['countdown_date'];

        const second = 1000,
                minute = second * 60,
                hour = minute * 60,
                day = hour * 24;

            var d = date;
            d = d.split(' ')[0];
        const countDown = new Date(d).getTime(),
            x = setInterval(function() {    


                const now = new Date().getTime(),
                    distance = countDown - now;

                document.getElementById(days_id).innerText = Math.floor(distance / (day)),
                document.getElementById(hours_id).innerText = Math.floor((distance % (day)) / (hour)),
                document.getElementById(minutes_id).innerText = Math.floor((distance % (hour)) / (minute)),
                document.getElementById(seconds_id).innerText = Math.floor((distance % (minute)) / second);

                //do something later when date is reached
                if (distance < 0) {
                document.getElementById(countdown_id).style.display = "none";
                document.getElementById(label_id).style.display = "block";
                clearInterval(x);
                }
                //seconds
            }, 0)
           

    }

     // ==== Service Box addon ====
     var WidgetServiceCarouselHandler = function($scope, $) {
        var serviceCarouselElem = $scope.find('.tpc-service-carousel-wrapper').eq(0);
        var settings = serviceCarouselElem.data('settings');

        if (settings !== undefined) {
            var autoPlay = settings['autoplay'];
            var autoplay_speed = parseInt(settings['autoplay_speed']) || 3000;
            var infiniteLoop = settings['infinite_loop'];
            var centerSlides = settings['center_slides'];
            var display_columns = settings['display_columns'] || 3;
            var item_gap = parseInt(settings['item_gap']) || 20;
            var pauseOnHover = settings['pause_on_hover'];
            var pauseOnInteraction = settings['pause_on_interaction'];
        
            var display_columns_tablet = settings['display_columns_tablet'] || 2;
            var tablet_item_gap = parseInt(settings['tablet_item_gap']) || 20;
            var centerSlidesTab = settings['center_slides_tablet'];
        
            var display_columns_mobile = settings['display_columns_mobile'] || 1;
            var mobile_item_gap = parseInt(settings['mobile_item_gap']) || 0;
            var centerSlidesMobile = settings['center_slides_mobile'];
        
            var autoplayOptions = autoPlay ? {
                delay: autoplay_speed,
                pauseOnMouseEnter: pauseOnHover,
                disableOnInteraction: pauseOnInteraction,
            } : false;
        
            var mySwiperParamsService = {
                spaceBetween: item_gap,
                slidesPerView: display_columns,
                loop: infiniteLoop,
                centeredSlides: centerSlides,
                pagination: {
                    el: serviceCarouselElem.find('.service-pagination')[0], // Scoped pagination
                    clickable: true,
                },
                navigation: {
                    nextEl: serviceCarouselElem.find('.service-pg-next')[0], // Scoped navigation next
                    prevEl: serviceCarouselElem.find('.service-pg-prev')[0], // Scoped navigation prev
                },
                autoplay: autoplayOptions,
                breakpoints: {
                    0: {
                        slidesPerView: display_columns_mobile,
                        spaceBetween: mobile_item_gap,
                        centeredSlides: centerSlidesMobile,
                    },
                    575: {
                        slidesPerView: display_columns_tablet,
                        spaceBetween: tablet_item_gap,
                        centeredSlides: centerSlidesTab,
                    },
                    992: {
                        slidesPerView: display_columns,
                        centeredSlides: centerSlides,
                    },
                }
            };
        
            // Generate a unique class for each Swiper container
            var uniqueClass = 'swiper-container-' + Math.random().toString(36).substr(2, 9);
            serviceCarouselElem.addClass(uniqueClass);
        
            new Swiper('.' + uniqueClass + ' .techwix-service-activation', mySwiperParamsService);
        }
        
    };

    // ==== Animation Addon ====
    var WidgetAnimationHandler = function($scope, $) {

        var dept_selector = $( ".techwix-animation-widget" ).attr( "id" );

        var value =  $( dept_selector  ).attr("data-depth");

        $( ".techwix-mouse-track-item" ).each( function () {
            var parallaxInstance = new Parallax(this);
    
            parallaxInstance.scalar(value, value);
        });
        
    }

     // ==== Nav menu addon ====
    var WidgetNavMenuHandler = function($scope, $) {
        //===== Mobile Menu
        $('.techwix-elementor-mobile-hamburger-menu').click(function() {
            $(".techwix-elementor-mobile-hamburger-menu > a").toggleClass('techwix-mobile-menu-close--active');
            $(".techwix-elementor-mobile-menu-nav-wrapper").toggleClass('techwix-mobile-menu-visible');
            $('body').toggleClass('techwix-mobile-menu-active');
        });
        //===== Mobile Menu Close Button
        $('.techwix-elementor-mobile-menu-close > a').click(function() {
            $('.techwix-elementor-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
            $('.techwix-elementor-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
            $('body').removeClass('techwix-mobile-menu-active');
        });
        //===== Mobile menu close while click outside
        $('.techwix-elementor-mobile-menu-overlay').click(function() {
            $('.techwix-elementor-mobile-hamburger-menu > a').removeClass('techwix-mobile-menu-close--active');
            $('.techwix-elementor-mobile-menu-nav-wrapper').removeClass('techwix-mobile-menu-visible');
            $('body').removeClass('techwix-mobile-menu-active');
        });

        // mav menu and submenu show/hide 
        $.fn.extend({
            accordionMenu: function(options){
                
                // Set the default options
                var defaults = {
                speed: 400
                }
                var options =  $.extend(defaults, options);

                return this.each(function(){
                
                    $(this).addClass('techwix-elementor-mobile-menu-item');
                    var menuItems = $(this).children('li');
                    menuItems.find('.techwix-elementor-mobile-menu-item > .techwix-dropdown-menu').parent().addClass('menu-item-has-children');
                    $('.techwix-elementor-mobile-menu-item .menu-item-has-children .techwix-dropdown-menu').hide();
                    $('.techwix-elementor-mobile-menu-item .menu-item-has-children > a').on('click', function(event) {
                        event.stopPropagation();
                        event.preventDefault();
                        $(this).siblings().slideToggle(options.speed);
                    });
                
                });
            }
        });
        $('#techwix-elementor-mobile-menu-item').accordionMenu();
    }


    var WidgetWooProductHandler = function($scope, $) {
        var wooProductWrapper = $scope.find('.woocommerce-addons-wrapper').eq(0);
        var settings = wooProductWrapper.data('settings');

        if (settings !== undefined) {
            var infiniteLoop = settings['infiniteLoop'] === "true";
            var autoPlay = settings['autoplay'] === 'true';
            var autoplay_speed = parseInt(settings['autoplaySpeed']) || 3000;
            var display_columns = parseInt(settings['displayColumns']) || 3;
            var item_gap = parseInt(settings['itemGap']) || 20;
            var pauseOnHover = settings['pauseOnHover'] === "true";
            var pauseOnInteraction = settings['pauseOnInteraction'] === "true";
        
            var display_columns_tablet = parseInt(settings['displayColumnsTablet']) || 2;
            var tablet_item_gap = parseInt(settings['tabletItemGap']) || 20;
        
            var display_columns_mobile = parseInt(settings['displayColumnsMobile']) || 1;
            var mobile_item_gap = parseInt(settings['mobileItemGap']) || 0;
        
            var autoplayOptions = autoPlay ? {
                delay: autoplay_speed,
                pauseOnMouseEnter: pauseOnHover,
                disableOnInteraction: pauseOnInteraction,
            } : false;
        
            var mySwiperParamsWoo = {
                spaceBetween: item_gap,
                slidesPerView: display_columns,
                loop: infiniteLoop,
                pagination: {
                    el: wooProductWrapper.find('.woo-pagination')[0], // Scoped pagination
                    clickable: true,
                },
                navigation: {
                    nextEl: wooProductWrapper.find('.woo-next')[0], // Scoped navigation next
                    prevEl: wooProductWrapper.find('.woo-prev')[0], // Scoped navigation prev
                },
                autoplay: autoplayOptions,
                breakpoints: {
                    0: {
                        slidesPerView: display_columns_mobile,
                        spaceBetween: mobile_item_gap,
                    },
                    575: {
                        slidesPerView: display_columns_tablet,
                        spaceBetween: tablet_item_gap,
                    },
                    992: {
                        slidesPerView: display_columns,
                    },
                }
            };
        
            // Generate a unique class for each Swiper container
            var uniqueClass = 'swiper-container-' + Math.random().toString(36).substr(2, 9);
            wooProductWrapper.addClass(uniqueClass);
        
            new Swiper('.' + uniqueClass + ' .woocommerce-addons-wrapper-active', mySwiperParamsWoo);
        }
        
    };

    // ===== Category Carousel =====
   var WidgetTeamCarouselHandler = function($scope, $) {
        var teamWrapper = $scope.find('.techwix_team_wrapper').eq(0);
        var settings = teamWrapper.data('settings');
        
        if (settings !== undefined) {
            var autoPlay = settings['autoplay'];
            var autoplay_speed = parseInt(settings['autoplay_speed']) || 3000;
            var infiniteLoop = settings['infinite_loop'];
            var centerSlides = settings['center_slides'];
            var display_columns = parseInt(settings['display_columns']) || 3;
            var item_gap = parseInt(settings['item_gap']) || 0;
            var pauseOnHover = settings['pause_on_hover'];
            var pauseOnInteraction = settings['pause_on_interaction'];

            var display_columns_tablet = parseInt(settings['display_columns_tablet']) || 2;
            var tablet_item_gap = parseInt(settings['tablet_item_gap']) || 0;
            var centerSlidesTab = settings['center_slides_tablet'];

            var display_columns_mobile = parseInt(settings['display_columns_mobile']) || 1;
            var mobile_item_gap = parseInt(settings['mobile_item_gap']) || 0;
            var centerSlidesMobile = settings['center_slides_mobile'];

            var autoplayOptions = autoPlay ? {
                delay: autoplay_speed,
                pauseOnMouseEnter: pauseOnHover,
                disableOnInteraction: pauseOnInteraction,
            } : false;

            var teamParams = {
                spaceBetween: item_gap,
                slidesPerView: display_columns,
                loop: infiniteLoop,
                centeredSlides: centerSlides,
                pagination: {
                    el: teamWrapper.find('.team-pagination')[0], // Scoped pagination
                    clickable: true,
                },
                navigation: {
                    nextEl: teamWrapper.find('.team-next')[0], // Scoped navigation next
                    prevEl: teamWrapper.find('.team-prev')[0], // Scoped navigation prev
                },
                autoplay: autoplayOptions,
                breakpoints: {
                    0: {
                        slidesPerView: display_columns_mobile,
                        spaceBetween: mobile_item_gap,
                        centeredSlides: centerSlidesMobile,
                    },
                    575: {
                        slidesPerView: display_columns_tablet,
                        spaceBetween: tablet_item_gap,
                        centeredSlides: centerSlidesTab,
                    },
                    992: {
                        slidesPerView: display_columns,
                        centeredSlides: centerSlides,
                    },
                }
            };

            // Generate a unique class for each Swiper container
            var uniqueClass = 'swiper-container-' + Math.random().toString(36).substr(2, 9);
            teamWrapper.addClass(uniqueClass);

            new Swiper('.' + uniqueClass + ' .techwix-team-item', teamParams);
        }
        
    };
    // ===== Case Studies Carousel =====
    var WidgetCaseStudyCarouselHandler = function($scope, $) {
        var caseStudyWrapper = $scope.find('.techwix_case_study_wrapper').eq(0);
        var settings = caseStudyWrapper.data('settings');
    
        if (settings !== undefined) {
            var autoPlay = settings['autoplay'];
            var autoplaySpeed = parseInt(settings['autoplay_speed']) || 3000;
            var infiniteLoop = settings['infinite_loop'];
            var centerSlides = settings['center_slides'];
            var display_columns = parseInt(settings['display_columns']) || 3;
            var item_gap = parseInt(settings['item_gap']) || 0;
            var pauseOnHover = settings['pause_on_hover'];
            var pauseOnInteraction = settings['pause_on_interaction'];
        
            var display_columns_tablet = parseInt(settings['display_columns_tablet']) || 2;
            var tablet_item_gap = parseInt(settings['tablet_item_gap']) || 0;
            var centerSlidesTab = settings['center_slides_tablet'];
        
            var display_columns_mobile = parseInt(settings['display_columns_mobile']) || 1;
            var mobile_item_gap = parseInt(settings['mobile_item_gap']) || 0;
            var centerSlidesMobile = settings['center_slides_mobile'];
        
            var autoplayOptions = autoPlay ? {
                delay: autoplaySpeed,
                pauseOnMouseEnter: pauseOnHover,
                disableOnInteraction: pauseOnInteraction,
            } : false;
        
            var caseStudyParams = {
                spaceBetween: item_gap,
                slidesPerView: display_columns,
                loop: infiniteLoop,
                centeredSlides: centerSlides,
                pagination: {
                    el: caseStudyWrapper.find('.case-study-pagination')[0], // Scoped pagination
                    clickable: true,
                },
                navigation: {
                    nextEl: caseStudyWrapper.find('.case-study-next')[0], // Scoped navigation next
                    prevEl: caseStudyWrapper.find('.case-study-prev')[0], // Scoped navigation prev
                },
                autoplay: autoplayOptions,
                breakpoints: {
                    0: {
                        slidesPerView: display_columns_mobile,
                        spaceBetween: mobile_item_gap,
                        centeredSlides: centerSlidesMobile,
                    },
                    575: {
                        slidesPerView: display_columns_tablet,
                        spaceBetween: tablet_item_gap,
                        centeredSlides: centerSlidesTab,
                    },
                    992: {
                        slidesPerView: display_columns,
                        centeredSlides: centerSlides,
                    },
                }
            };
        
            // Generate a unique class for each Swiper container
            var uniqueClass = 'swiper-container-' + Math.random().toString(36).substr(2, 9);
            caseStudyWrapper.addClass(uniqueClass);
        
            new Swiper('.' + uniqueClass + ' .techwix-case-study-item', caseStudyParams);
        }
        
    };

 // === Add JavaScript to Widgets ====
    $(window).on('elementor/frontend/init', function() {

        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-testimonial-addons.default', WidgetTestimonialCarouselHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-counter.default', WidgetCounterHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-countdown.default', WidgetCountdown);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-accordion.default', WidgetAccordionsMapHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-services-box.default', WidgetServiceCarouselHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-nav-menu.default', WidgetNavMenuHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-animation.default', WidgetAnimationHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-woo-product-addons.default', WidgetWooProductHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-team-addons.default', WidgetTeamCarouselHandler);
        elementorFrontend.hooks.addAction('frontend/element_ready/techwix-case-study-addons.default', WidgetCaseStudyCarouselHandler);

    });

})(jQuery);