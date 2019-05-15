{% include "navbarre.html" %}

{% block content %}
{% endblock %}


<style>
  .titreUn{
    color: rgba(51, 51, 0);
    background-color: rgba(255, 153, 102);
  }
  </style>

  <header class="masthead text-center d-flex">
    <div class="container my-auto">
      <div class="row">
        <div class="col-lg-10 mx-auto">
          <h1 class="titreUn">
            <strong>Deviens un AS de la bonne nourriture !</strong>
          </h1>
          <hr>
        </div>


        
        <div class="col-lg-8 mx-auto">
          <div class="text-faded mb-5" id="texteMilieu">
              <h2>Trouve le produit le plus sain parmis les autres</h2><br>
              <h2>Gagne l'icone Cuisinier Modèle</h2><br>
              <h2>Et gagne des bons d'achat !</h2>
          </div>
      
    
            <form action="/jeux/jeux/" method="POST">
            {% csrf_token %}
                <input type="hidden" id="hid">
                <input type="button" onclick="lvl1()" value="Niveau 1" name="niveau1" id="niveau1">
                <input type="button" onclick="lvl2()" value="Niveau 2" name="niveau2" id="niveau2">
                <input type="button" onclick="lvl3()" value="Niveau 3" name="niveau3" id="niveau3">
            </form>
            
        </div>
      </div>
    </div>
  </header>



  
  <div id='score'></div>


</div>
  <section class="bg-primary" id="about">
    <center><p>Selon toi, lequels de ces articles à un nutriscore de A</p></center>
   
    <div id="jeux">
    
                                                     
  

    </div>
          <br><br><br><br>
          <form action="/jeux/jeux/" methode='POST' id='validation'>
          {% csrf_token %}
          <div id='cont1' style='display:none'>
            "<center><input type='button' value='valider1' id='valider1' name='valider'></center>"
          </div>
          <div id='cont2' style='display:none'>
          "<center><input type='button' value='valider2' id='valider2' name='valider'></center>"
          </div>
          </form>
          
        </div>
      </div>
    </div>
  </section>
 





{% include "bottom_page.html" %}

{% block content2 %}
{% endblock content2%}


</body>

</html>





<script>


    <!-- niveau 1 -->

    function choice1(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image1niveau1').src
      CHOICE.push('image1')
      CHOICE.push(a)
      
      
      };
    function choice2(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image1niveau1').src
      CHOICE.push('image2')
      CHOICE.push(a)
   
      };

    function choice3(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image1niveau1').src
      CHOICE.push('image3')
      CHOICE.push(a)
  
      };

    function choice4(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image1niveau1').src
      CHOICE.push('image4')
      CHOICE.push(a)
     
      };



    <!-- niveau 2 -->


    function choice2_1(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image1niveau2').src
      CHOICE.push('image1')
      CHOICE.push(a)
      
      
      };
    function choice2_2(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image2niveau2').src
      CHOICE.push('image2')
      CHOICE.push(a)
   
      };

    function choice2_3(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image3niveau2').src
      CHOICE.push('image3')
      CHOICE.push(a)
  
      };

    function choice2_4(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image4niveau2').src
      CHOICE.push('image4')
      CHOICE.push(a)
     
      };

    function choice2_5(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image5niveau2').src
      CHOICE.push('image5')
      CHOICE.push(a)
      
      
      };
    function choice2_6(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image6niveau2').src
      CHOICE.push('image6')
      CHOICE.push(a)
   
      };

    function choice2_7(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image7niveau2').src
      CHOICE.push('image7')
      CHOICE.push(a)
  
      };

    function choice2_8(){
      CHOICE = []
      document.getElementById('score').innerHTML = ""
      var a = document.getElementById('image8niveau2').src
      CHOICE.push('image8')
      CHOICE.push(a)
     
      };



  <!-- niveau 3 -->






  <!-- variables -->


      
    var LISTE = ["a"];
    var IMAGE = [];
    var IMAGE2 = [];
    function lvl1(){

        document.getElementById("jeux").innerHTML = "<div class='col-xs-12-mx-auto text-center'>" +
                                                        "<div class='row' id='row3'>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px; margin-left:auto;'>" +
                                                                "<input type='image' src='' id='image1niveau1' onclick='choice1()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image2niveau1' onclick='choice2()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image3niveau1' onclick='choice3()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;margin-right:auto;'>" +
                                                                "<input type='image' src='' id='image4niveau1' onclick='choice4()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                        "</div>" +
                                                     "</div>"

        var a = document.getElementById("niveau1").value;
        console.log(a);
        LISTE.push(a)


       
        };


  <!-- niveau 2 -->


  
    function lvl2(){

        
        
     document.getElementById("jeux").innerHTML =  "<div class='col-xs-12-mx-auto text-center'>" +
                                                        "<div class='row' id='row3'>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px; margin-left:auto;'>" +
                                                                "<input type='image' src='' id='image1niveau2' onclick='choice2_1()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image2niveau2' onclick='choice2_2()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image3niveau2' onclick='choice2_3()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;margin-right:auto;'>" +
                                                                "<input type='image' src='' id='image4niveau2' onclick='choice2_4()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                        "</div>" +
                                                     "</div>" +
                                                    "<br>" +
                                                    "<div class='col-xs-12-mx-auto text-center'>" +
                                                        "<div class='row' id='row3'>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px; margin-left:auto;'>" +
                                                                "<input type='image' src='' id='image5niveau2' onclick='choice2_5()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image6niveau2' onclick='choice2_6()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<input type='image' src='' id='image7niveau2' onclick='choice2_7()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;margin-right:auto;'>" +
                                                                "<input type='image' src='' id='image8niveau2' onclick='choice2_8()' style='width:250px; height:300px;'>" +
                                                            "</div>" +
                                                        "</div>" +
                                                     "</div>"


        var a = document.getElementById("niveau2").value;
        console.log(a);
        LISTE.push(a)


        };


    function lvl3(){
     document.getElementById("jeux").innerHTML =  "<div class='col-xs-12-mx-auto text-center'>" +
                                                        "<div class='row' id='row3'>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px; margin-left:auto;'>" +
                                                                "<img src='{{image1}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<img src='{{image2}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<img src='{{image3}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;margin-right:auto;'>" +
                                                                "<img src='{{image4}}'>" +
                                                            "</div>" +
                                                        "</div>" +
                                                     "</div>" +
                                                    "<br>" +
                                                    "<div class='col-xs-12-mx-auto text-center'>" +
                                                        "<div class='row' id='row3'>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px; margin-left:auto;'>" +
                                                                "<img src='{{image5}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<img src='{{image6}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;'>" +
                                                                "<img src='{{image7}}'>" +
                                                            "</div>" +
                                                            "<div style='width:20px;'></div>" +
                                                            "<div style='border:1px solid blue;width:250px; height:300px;margin-right:auto;'>" +
                                                                "<img src='{{image8}}'>" +
                                                            "</div>" +
                                                        "</div>" +
                                                     "</div>"

        };




    
    $("#niveau1").on("click", function(e){
         e.preventDefault();
          document.getElementById('cont2').style.display = 'none';
          $.ajax({
              data:{
                  'data':LISTE[LISTE.length - 1],
                  csrfmiddlewaretoken:'{{ csrf_token }}'
                  
           
              },
              type:"POST",
              url:"/jeux/jeux/"
          })
          .done(function(data){
              if (data.error){
                  $("#monCadreAlert").text(data.error);
                  $("#is_save");
                  
                  
              }
              else{
                  $("#is_save").html(data);
                  $("#monCadreAlert");
                  IMAGE.push(JSON.stringify(data['image1']))
                  IMAGE.push(JSON.stringify(data['image2']))
                  IMAGE.push(JSON.stringify(data['image3']))
                  IMAGE.push(JSON.stringify(data['image4']))
  
                  var i = IMAGE[0]
                  var j = i.slice(1,i.length-1)
                  
                  var k = IMAGE[1]
                  var l = k.slice(1,k.length-1)
                  
                  var m = IMAGE[2]
                  var n = m.slice(1,m.length-1)
                  
                  var o = IMAGE[3]
                  var p = o.slice(1,o.length-1)
                  
                  
                  document.getElementById('image1niveau1').src=j;
                  document.getElementById('image2niveau1').src=l;
                  document.getElementById('image3niveau1').src=n;
                  document.getElementById('image4niveau1').src=p;
                  document.getElementById('cont1').style.display ='block';

                  
              };
              
          });
    });



  
    $("#valider1").on("click", function(e){
         e.preventDefault();
       
         IMAGE = []
      
          $.ajax({
              data:{
                  'data':String(CHOICE),
                  'data1':'Niveau 1',
                  csrfmiddlewaretoken:'{{ csrf_token }}'
                  
           
              },
              type:"POST",
              url:"/jeux/jeux/"
          })
          .done(function(data){
              if (data.error){
                  $("#monCadreAlert").text(data.error);
                  $("#is_save");
                  
                  
              }
              else{
                  $("#is_save").html(data);
                  $("#monCadreAlert");
     
                  IMAGE.push(JSON.stringify(data['image1']))
                  IMAGE.push(JSON.stringify(data['image2']))
                  IMAGE.push(JSON.stringify(data['image3']))
                  IMAGE.push(JSON.stringify(data['image4']))
  
                  var i = IMAGE[0]
                  var j = i.slice(1,i.length-1)
                  
                  var k = IMAGE[1]
                  var l = k.slice(1,k.length-1)
                  
                  var m = IMAGE[2]
                  var n = m.slice(1,m.length-1)
                  
                  var o = IMAGE[3]
                  var p = o.slice(1,o.length-1)
                  

                  document.getElementById('image1niveau1').src=j;
                  document.getElementById('image2niveau1').src=l;
                  document.getElementById('image3niveau1').src=n;
                  document.getElementById('image4niveau1').src=p;
                  document.getElementById('score').innerHTML = "Tu as :" + String(JSON.stringify(data['score_actuel'])) +
                                                                "points &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                                                                String(JSON.stringify(data['message']))


              };
              
          });
    });





    $("#niveau2").on("click", function(e){
         e.preventDefault();
         document.getElementById('cont1').style.display = 'none';
          $.ajax({
              data:{
                  'data':LISTE[LISTE.length - 1],
                  csrfmiddlewaretoken:'{{ csrf_token }}'
                  
           
              },
              type:"POST",
              url:"/jeux/jeux/"
          })
          .done(function(data){
              if (data.error){
                  $("#monCadreAlert").text(data.error);
                  $("#is_save");
                  
                  
              }
              else{
                  $("#is_save").html(data);
                  $("#monCadreAlert");
             
                  
                  IMAGE2.push(JSON.stringify(data['image1']))
                  IMAGE2.push(JSON.stringify(data['image2']))
                  IMAGE2.push(JSON.stringify(data['image3']))
                  IMAGE2.push(JSON.stringify(data['image4']))
                  IMAGE2.push(JSON.stringify(data['image5']))
                  IMAGE2.push(JSON.stringify(data['image6']))
                  IMAGE2.push(JSON.stringify(data['image7']))
                  IMAGE2.push(JSON.stringify(data['image8']))
                  
              
                  
                  var i = IMAGE2[0]
                  var j = i.slice(1,i.length-1)
                  
                  var k = IMAGE2[1]
                  var l = k.slice(1,k.length-1)
                  
                  var m = IMAGE2[2]
                  var n = m.slice(1,m.length-1)
                  
                  var o = IMAGE2[3]
                  var p = o.slice(1,o.length-1)


                  var q = IMAGE2[4]
                  var r = p.slice(1,q.length-1)
               
                  
                  var s = IMAGE2[5]
                  var t = s.slice(1,s.length-1)
               
                  var u = IMAGE2[6]
                  var v = u.slice(1,u.length-1)
                
                  var w = IMAGE2[7]
                  var x = w.slice(1,w.length-1)
                  

                  
                  
                  document.getElementById('image1niveau2').src=j;
                  document.getElementById('image2niveau2').src=l;
                  document.getElementById('image3niveau2').src=n;
                  document.getElementById('image4niveau2').src=p;

                  document.getElementById('image5niveau2').src=r;
                  document.getElementById('image6niveau2').src=t;
                  document.getElementById('image7niveau2').src=v;
                  document.getElementById('image8niveau2').src=x;


                  document.getElementById('cont2').style.display ='block';

                  
              };
              
          });
    });


    <!-- niveau 2  validate-->

    $("#cont2").on("click", function(e){
    
         e.preventDefault();
         
         IMAGE2 = []
      
          $.ajax({
              data:{
                  'data':String(CHOICE),
                  'data1':'Niveau 2',
                  csrfmiddlewaretoken:'{{ csrf_token }}'
                  
           
              },
              type:"POST",
              url:"/jeux/jeux/"
          })
          .done(function(data){
              if (data.error){
                  $("#monCadreAlert").text(data.error);
                  $("#is_save");
                  
                  
              }
              else{
                  $("#is_save").html(data);
                  $("#monCadreAlert");
                  alert(JSON.stringify(data))
                  alert(IMAGE2)
                  IMAGE2.push(JSON.stringify(data['image1']))
                  IMAGE2.push(JSON.stringify(data['image2']))
                  IMAGE2.push(JSON.stringify(data['image3']))
                  IMAGE2.push(JSON.stringify(data['image4']))

                  IMAGE2.push(JSON.stringify(data['image5']))
                  IMAGE2.push(JSON.stringify(data['image6']))
                  IMAGE2.push(JSON.stringify(data['image7']))
                  IMAGE2.push(JSON.stringify(data['image8']))

                  
                  var i = IMAGE2[0]
                  var j = i.slice(1,i.length-1)
                  
                  var k = IMAGE2[1]
                  var l = k.slice(1,k.length-1)
                  
                  var m = IMAGE2[2]
                  var n = m.slice(1,m.length-1)
                  
                  var o = IMAGE2[3]
                  var p = o.slice(1,o.length-1)
                  

                  var q = IMAGE2[4]
                  var r = q.slice(1,q.length-1)
                  
                  var s = IMAGE2[5]
                  var t = s.slice(1,s.length-1)
                  
                  var u = IMAGE2[6]
                  var v = u.slice(1,u.length-1)
                  
                  var w = IMAGE2[7]
                  var x = w.slice(1,w.length-1)


                  document.getElementById('image1niveau2').src=j;
                  document.getElementById('image2niveau2').src=l;
                  document.getElementById('image3niveau2').src=n;
                  document.getElementById('image4niveau2').src=p;
                  
                  document.getElementById('image5niveau2').src=r;
                  document.getElementById('image6niveau2').src=t;
                  document.getElementById('image7niveau2').src=v;
                  document.getElementById('image8niveau2').src=x;
                  
                  document.getElementById('score').innerHTML = "Tu as :  " + String(JSON.stringify(data['score_actuel'])) +
                                                                "points &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                                                                String(JSON.stringify(data['message']))


              };
              
          });
    });


             
</script>







































