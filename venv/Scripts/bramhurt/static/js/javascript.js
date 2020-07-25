  $(document).ready(function(){
    $("#sendMessage").click(function(){
  var data = $("#newMessageForm").serialize();
  $.ajax({
        url:  $("#newMessageForm").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
        $("#newMessageForm")[0].reset();
            if(response.state == "failed"){
            $("#successMessage").removeClass("show");
                $("#failedMessage").addClass("show");

            }else{

                $("#failedMessage").removeClass("show");
                 $("#successMessage").addClass("show");
            }

        }});
  })

  $('img[data-enlargable]').addClass('img-enlargable').click(function(){
    var src = $(this).attr('src');
    var modal;
    function removeModal(){ modal.remove(); $('body').off('keyup.modal-close'); }
    modal = $('<div>').css({
        background: 'RGBA(0,0,0,.5) url('+src+') no-repeat center',
        backgroundSize: 'contain',
        width:'100%', height:'100%',
        position:'fixed',
        zIndex:'10000',
        top:'0', left:'0',
        cursor: 'zoom-out'
    }).click(function(){
        removeModal();
    }).appendTo('body');
    //handling ESC
    $('body').on('keyup.modal-close', function(e){
      if(e.key==='Escape'){ removeModal(); }
    });
});
   $(".showMore").click(function(){
     $(this).text($(this).text() == 'Pokaż mniej' ? 'Pokaż więcej' : 'Pokaż mniej');

   $(".comment-row").slice(3,$(".comment-row").length).toggleClass("hide");
      $(".comment-row").slice(3,$(".comment-row").length).toggleClass("active-2");

  })
    $("#submitRate").click(function(){
    var data = $("form").serialize();
    $.ajax({
        url: $("form").attr("action"),
        data: data,
        type: 'post',
        success: function(response){
           $("#addOpinionForm").trigger("reset");

         var element = ' <div class="d-flex hide flex-row comment-row m-t-0"><div class="comment-text w-100"><h6 class="font-medium">' + response.response.FirstName +" "+ response.response.LastName + '<span class="float-right">'+ '<i class="fa fa-star checked"></i>'.repeat(response.response.Rate) + '<i class="fa fa-star"></i>'.repeat(5-response.response.Rate) +'</span></h6> <span class="m-b-15 d-block">'+ response.response.Text+'</span><div class="comment-footer"> <span class="text-muted float-right">'+ "Teraz"+' </span> </div></div></div> ';
         $(".comment-widgets").prepend(element);
        $(".comment-row").first().removeClass("hide");
        $("#avarage").html(response.avarage)
         $(".comment-row").first().addClass("active-2");
         setTimeout(function(){
         $("html, body").animate({
        scrollTop : $(".comment-row").first().offset().top
        }, 1000 );
         },1000)

    }});
    });
    $(".comment-row").slice(0,3).removeClass("hide",2000,"easeInBack");
      $(".comment-row").slice(0,3).addClass("active");
    $( "label" ).tooltip({placement: "top",html: true});
       setTimeout( function(){$('.count').countTo();}, 2000)
   var inFunction = false
   $(window).bind('mousewheel', function(event) {
   var vHeight = $( window ).height();
    if (event.originalEvent.wheelDelta >= 0) {
        console.log('Scroll up');
    }
    else if( vHeight > 600 && $("html").scrollTop() > 374 && $("html").scrollTop() < 550 && inFunction == false) {
        inFunction = true
                 $("html, body").animate({
        scrollTop : $("#myCarousel").offset().top
        }, 1000 );
         setTimeout( function(){inFunction = false}, 1000)
        }

});

   });
var zoomImg = function () {
  // Create evil image clone
  var clone = this.cloneNode();
  clone.classList.remove("zoomD");

  // Put evil clone into lightbox
  var lb = document.getElementById("lb-img");
  lb.innerHTML = "";
  lb.appendChild(clone);

  // Show lightbox
  lb = document.getElementById("lb-back");
  lb.classList.add("show");
};

window.addEventListener("load", function(){
  // Attach on click events to all .zoomD images
  var images = document.getElementsByClassName("zoomD");
  if (images.length>0) {
    for (var img of images) {
      img.addEventListener("click", zoomImg);
    }
  }
  // Click event to hide the lightbox
  document.getElementById("lb-back").addEventListener("click", function(){
    this.classList.remove("show");
  })
});