jQuery(document).ready(function ($) {
  "use strict";
  jQuery(window).scroll(function () {
    if (jQuery(this).scrollTop() > 170) {
      jQuery("body").addClass("wm-sticky");
    } else {
      jQuery("body").removeClass("wm-sticky");
    }
  });
  jQuery(".wm-service-slider").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    prevArrow:
      "<span class='slick-arrow slick-arrow-left'><i class='flaticon-arrows-1'></i></span>",
    nextArrow:
      "<span class='slick-arrow slick-arrow-right'><i class='flaticon-arrows-1'></i></span>",
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 2, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 2, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-banner-for").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: ".wm-banner-nav",
  });
  jQuery(".wm-banner-nav").slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: ".wm-banner-for",
    dots: false,
    vertical: true,
    prevArrow:
      "<span class='slick-arrow-left'><img src='/static/snippet/img_index/banner-arrow-1.png' alt=''></span>",
    nextArrow:
      "<span class='slick-arrow-right'><img src='/static/snippet/img_index/banner-arrow-2.png' alt=''></span>",
    centerMode: true,
    focusOnSelect: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          vertical: true,
        },
      },
      {
        breakpoint: 800,
        settings: { slidesToShow: 4, slidesToScroll: 1, vertical: false },
      },
      {
        breakpoint: 1440,
        settings: { slidesToShow: 4, slidesToScroll: 1, vertical: true },
      },
      {
        breakpoint: 400,
        settings: { slidesToShow: 3, slidesToScroll: 1, vertical: false },
      },
    ],
  });
  jQuery(".wm-banner-two").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: false,
    fade: true,
    prevArrow:
      "<span class='slick-arrow-left'><i class='flaticon-arrows-1'></i></span>",
    nextArrow:
      "<span class='slick-arrow-right'><i class='flaticon-arrows-1'></i></span>",
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-testimonial-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: true,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-qoute-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: false,
    prevArrow:
      "<span class='slick-arrow-left'><i class='flaticon-arrows-1'></i></span>",
    nextArrow:
      "<span class='slick-arrow-right'><i class='flaticon-arrows-1'></i></span>",
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-banner-three").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: true,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-testimonial-for").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    asNavFor: ".wm-testimonial-nav",
    autoplay: true,
    autoplaySpeed: 2000,
  });
  jQuery(".wm-testimonial-nav").slick({
    slidesToShow: 9,
    slidesToScroll: 1,
    asNavFor: ".wm-testimonial-for",
    dots: false,
    arrows: false,
    centerMode: true,
    focusOnSelect: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 1,
          infinite: true,
          vertical: false,
        },
      },
      {
        breakpoint: 800,
        settings: { slidesToShow: 3, slidesToScroll: 1, vertical: false },
      },
      {
        breakpoint: 400,
        settings: { slidesToShow: 2, slidesToScroll: 1, vertical: false },
      },
    ],
  });
  jQuery(".wm-gallery-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    centerMode: true,
    focusOnSelect: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-bannerfour-for").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    asNavFor: ".wm-bannerfour-nav",
    autoplay: true,
    autoplaySpeed: 2000,
  });
  jQuery(".wm-bannerfour-nav").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: ".wm-bannerfour-for",
    dots: false,
    arrows: false,
    centerMode: true,
    focusOnSelect: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          vertical: false,
        },
      },
      {
        breakpoint: 800,
        settings: { slidesToShow: 2, slidesToScroll: 1, vertical: false },
      },
      {
        breakpoint: 400,
        settings: { slidesToShow: 1, slidesToScroll: 1, vertical: false },
      },
    ],
  });
  jQuery(".wm-latest-case-slider").slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    focusOnSelect: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 2, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 2, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-blogpost-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    focusOnSelect: true,
    autoplay: true,
    fade: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-client-slide").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: true,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".wm-company-timeline-slide").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: true,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: { slidesToShow: 1, slidesToScroll: 1, infinite: true },
      },
      { breakpoint: 800, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      { breakpoint: 400, settings: { slidesToShow: 1, slidesToScroll: 1 } },
    ],
  });
  jQuery(".backtop-btn").on("click", function () {
    jQuery("html, body").animate({ scrollTop: 0 }, 800);
    return false;
  });
  jQuery(function () {
    var austDay = new Date();
    austDay = new Date(austDay.getFullYear() + 1, 1 - 1, 26);
    jQuery("#wm-countdown").countdown({ until: austDay });
    jQuery("#year").text(austDay.getFullYear());
  });
  jQuery(".word-count").counterUp({ delay: 10, time: 1000 });
  jQuery("area[data-rel^='prettyPhoto']").prettyPhoto();
  jQuery(".gallery:first a[data-rel^='prettyPhoto']").prettyPhoto({
    animation_speed: "normal",
    theme: "facebook",
    social_tools: "",
    slideshow: 3000,
    autoplay_slideshow: false,
  });
  jQuery(".gallery:gt(0) a[data-rel^='prettyPhoto']").prettyPhoto({
    animation_speed: "fast",
    slideshow: 10000,
    hideflash: true,
  });
  jQuery("#custom_content a[data-rel^='prettyPhoto']:first").prettyPhoto({
    custom_markup:
      '<div id="map_canvas" style="width:260px; height:265px"></div>',
    changepicturecallback: function () {
      initialize();
    },
  });
  jQuery("#custom_content a[data-rel^='prettyPhoto']:last").prettyPhoto({
    custom_markup:
      '<div id="bsap_1259344" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div><div id="bsap_1237859" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6" style="height:260px"></div><div id="bsap_1251710" class="bsarocks bsap_d49a0984d0f377271ccbf01a33f2b6d6"></div>',
    changepicturecallback: function () {
      _bsap.exec();
    },
  });
  jQuery(".wm-main-section").fitVids();
  jQuery(".skillbar").each(function () {
    jQuery(this).appear(function () {
      jQuery(this)
        .find(".count-bar")
        .animate({ width: jQuery(this).attr("data-percent") }, 3000);
      var percent = jQuery(this).attr("data-percent");
      jQuery(this)
        .find(".count")
        .html("<span>" + percent + "</span>");
    });
  });
  jQuery('[data-toggle="tooltip"]').tooltip();
  jQuery("a.wm-cartbtn").on("click", function () {
    jQuery(".wm-cart-box").slideToggle("slow");
    return false;
  });
  jQuery("html").on("click", function () {
    jQuery(".wm-cart-box").fadeOut();
  });
  jQuery(".wm-navicons,.wm-cartsection").on("click", function (event) {
    event.stopPropagation();
  });
  jQuery(".wm-navicons a.fa-search,.wm-search a.fa-search").on(
    "click",
    function () {
      jQuery(".wm-search-popup").fadeToggle("");
      return false;
    }
  );
  jQuery("a.wm-header-button").on("click", function () {
    jQuery(".wm-main-header").toggleClass("wm-header-slider");
    return false;
  });
  jQuery("video").mediaelementplayer({
    success: function (player, node) {
      jQuery("#" + node.id + "-mode").html("mode: " + player.pluginType);
    },
  });
  jQuery("#slider-range").slider({
    range: true,
    min: 0,
    max: 500,
    values: [75, 300],
    slide: function (event, ui) {
      jQuery("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
    },
  });
  jQuery("#amount").val(
    "$" +
      jQuery("#slider-range").slider("values", 0) +
      " - $" +
      jQuery("#slider-range").slider("values", 1)
  );
  jQuery(function () {
    jQuery("#slider-range-min").slider({
      range: "min",
      value: 37,
      min: 1,
      max: 700,
      slide: function (event, ui) {
        jQuery("#amount").val("$" + ui.value);
      },
    });
    jQuery("#amount").val("$" + $("#slider-range-min").slider("value"));
  });
  jQuery(".wm-testimonails-info").niceScroll("", {
    cursorcolor: "#26a4de",
    cursoropacitymax: 1,
    boxzoom: true,
    touchbehavior: false,
    autohidemode: false,
    background: "#e6e6e6",
    cursorborderradius: "20px 20px 0px 0px",
    cursorminheight: 20,
    cursorwidth: 6,
    cursorborder: 5,
    touchbehavior: true,
    railoffset: { top: 21, left: -19 },
    railpadding: { top: 0, right: 0, left: 0, bottom: 31 },
  });
});
jQuery(function ($) {
  $(".wm-filterable li").on("click", function (event) {
    event.preventDefault();
    var target = $(this).find(">a").prop("hash");
    $("html, body").animate({ scrollTop: $(target).offset().top }, 500);
  });
  $("a.preview").prettyPhoto({ social_tools: false });
  $(window).load(function () {
    $portfolio = $(".wm-case-filter");
    $portfolio.isotope({ itemSelector: "li", layoutMode: "fitRows" });
    $portfolio_selectors = $(".wm-filterable li a");
    $portfolio_selectors.on("click", function () {
      $portfolio_selectors.removeClass("active");
      $(this).addClass("active");
      var selector = $(this).attr("data-filter");
      $portfolio.isotope({ filter: selector });
      return false;
    });
  });
});
