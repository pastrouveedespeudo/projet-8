var LISTE = ["a"];
var LISTE_NAME = [];
var USER = ["b"];

$("#product1,#product2,#product3,#product4,#product5,#product6").on("click", function(e){
   e.preventDefault();
    $.ajax({
        data:{
            'data[]':LISTE[LISTE.length - 1],
            'username':USER[USER.length - 1],
        },
        type:"POST",
        url:"/mes_aliments/recherche/"
    })
    .done(function(data){
        if (data.error){
            $("#monCadreAlert").text(data.error);
            $("#is_save");   
        }
        else{
            $("#is_save").html(data.data);
            $("#monCadreAlert");
        };
    });
});


function pushlist(id_product, user, stock, is_save){
  var a = document.getElementById(id_product).value;
  var b = document.getElementById(id_product).name;
  var c = document.getElementById(user).innerHTML;
  USER.push(c)
  LISTE.push(a)
  LISTE_NAME.push(b)
  d = document.getElementById(stock).innerHTML;
  console.log(d)
  if (d == "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"){
      console.log("trop d\'aliment pour ce compte")
      document.getElementById(is_save).innerHTML = "";
      document.getElementById(is_save).innerHTML = '<img style="width:15%;" src="/static/img/portfolio/recherche/croix.jpg" />'
      +'  <i>Vous avez trop d\'alement</i>';
    }
    else{
        document.getElementById(is_save).innerHTML = "";
        document.getElementById(is_save).innerHTML = '<img style="width:15%;" src="/static/img/portfolio/recherche/validate.jpg" />'
        +'  <i>Enregistrement effectué</i>';
    };
  };
  


var c = document.getElementById("user").innerHTML;
USER.push(c)
console.log(USER)

$.ajax({
    data:{
        'username':USER[USER.length - 1],
    },
    type:"POST",
    url:"/mes_aliments/recherche/"
})
.done(function(data){
    if (data.error){
        $("#monCadreAlert").text(data.error);
        $("#stock");
    }
    else{
        $("#stock").html(data.data);
        $("#monCadreAlert"); 
    }; 
});


