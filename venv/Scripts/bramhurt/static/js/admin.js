  $(document).ready(function(){
  $(".deleteMessage").click(function(){
  var data = $("body > div.container-fluid > input[type=hidden]").serialize();
  $.ajax({
        url: window.location.href + "/delete/" + this.value,
        data: data,
        type:"post",
        success:function(response){
        var x = "#heading" + response.id
        var y = "#collapse" + response.id
        $(x).hide();
        $(y).hide();
        }});
  })
  $("b").click(function(){
  var data = $("body > div.container-fluid > input[type=hidden]").serialize();
  $.ajax({
        url: window.location.href + "/open/" + this.getAttribute('aria-valuenow'),
        data: data,
        type:"post",
        success:function(response){
        $('[aria-valuenow = "' + response.id + '"]').css('font-weight', 'normal')}});
  })

  $(".deleteOpinion").click(function(){
  var data = $("body > div > input[type=hidden]").serialize();
  $.ajax({
        url: window.location.href + "delete/" + this.value,
        data: data,
        type:"post",
        success:function(response){
        $('[aria-label = "' + response.id + '"]').remove();
        }});
  });


  $("#saveBrandDate").click(function(){
  var data = $("#updateBrand").serialize();
  $.ajax({
        url:  $("#updateBrand").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
            if(response.state == "failed"){
                alert("Niepowodzenie");
            }else{
                alert("Powodzenie");
            }

        }});
  })
  $("#saveStatistic").click(function(){
  var data = $("#updateStatistic").serialize();
  $.ajax({
        url:  $("#updateStatistic").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
            if(response.state == "failed"){
                alert("Niepowodzenie");
            }else{
                alert("Powodzenie");
            }

        }});
  })
    $("#saveMainCategory").click(function(){
     var data = new FormData($('#newMainCategoryForm').get(0));
  $.ajax({
        url:  $("#newMainCategoryForm").attr("action"),
        data: data,
        type:"POST",
        cache: false,
        processData: false,
         contentType: false,
        success:function(response){
        $("#newMainCategoryForm")[0].reset();
            if(response.state == "failed"){
            $("#successMessage").removeClass("show");
                $("#failedMessage").addClass("show");

            }else{

                $("#failedMessage").removeClass("show");
                 $("#successMessage").addClass("show");
            }

        }});
  })

 $("#saveCategory").click(function(){
     var data = new FormData($('#newCategoryForm').get(0));
  $.ajax({
        url:  $("#newCategoryForm").attr("action"),
        data: data,
        type:"POST",
        cache: false,
        processData: false,
         contentType: false,
        success:function(response){
        $("#newCategoryForm")[0].reset();
            if(response.state == "failed"){
            alert("niepowodzenie");

            }else{

               alert("powodzenie");
            }

        }});
  })

 $("#saveObject").click(function(){
     var data = new FormData($('#newObjectForm').get(0));
  $.ajax({
        url:  $("#newObjectForm").attr("action"),
        data: data,
        type:"POST",
        cache: false,
        processData: false,
         contentType: false,
        success:function(response){
        $("#newObjectForm")[0].reset();
            if(response.state == "failed"){
            alert("niepowodzenie");

            }else{

                alert("powodzenie");
            }

        }});
  })

  $("#deleteMainCategory").click(function(){
     var data = $('#deleteMainCategoryForm').serialize();
  $.ajax({
        url:  $("#deleteMainCategoryForm").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
        $("#deleteMainCategoryForm")[0].reset();
            if(response.state == "failed"){
            alert("niepowodzenie");

            }else{

                alert("powodzenie");
            }

        }});
  })
   $("#deleteCategory").click(function(){
     var data = $('#deleteCategoryForm').serialize();
  $.ajax({
        url:  $("#deleteCategoryForm").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
        $("#deleteCategoryForm")[0].reset();
            if(response.state == "failed"){
            alert("niepowodzenie");

            }else{

                alert("powodzenie");
            }

        }});
  })
   $("#deleteObject").click(function(){
     var data = $('#deleteObjectForm').serialize();
  $.ajax({
        url:  $("#deleteObjectForm").attr("action"),
        data: data,
        type:"POST",
        success:function(response){
        $("#deleteObjectForm")[0].reset();
            if(response.state == "failed"){
            alert("niepowodzenie");

            }else{

                alert("powodzenie");
            }

        }});
  })

  });