{% include "navbarre.html" %}
{% block content %}
{% endblock %}

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<link href="/static/css/recherche1.css" rel="stylesheet">
<script type="text/javascript" src="/static/js/la_recherche1_js.js"></script>

<body id="page-top">
  <style>
    header.masthead {
          background-image: url({{image}});
    }
  </style>
  
  <header class="masthead text-center d-flex">
    <div class="container my-auto">
      <div class="row">
        <div class="col-lg-10 mx-auto">
          <h1 class="titreUn">
            <strong>{{titre}}</strong>
          </h1>
          <hr>
        </div>
        </div>
      </div>
    </div>
  </header>

  <section class="bg-primary" id="about">
  {% if user.is_authenticated %}
    <div id="user" value={{user.username}} style='display:none;'>{{user.username}}</div>
    <div id="stock"><center><strong>{{stock_depassé}}</strong></center></div>   
  {% else %}
  <div style="text-align:center;">
    Connecte-toi afin de pouvoir les <strong>enregistrer</strong>
    et visualise les depuis <strong>"Mon compte"</strong>
  </div> 
  {% endif %}
  <div class="container-fluid" id="conteneurCarre">
    <div class="row" id="row3">
      <div class="col-sm-12 col-md-4" id="block4">
        <div id="rond"><img src={{aaaa}} ></div>
          <form action="aliment_det" method="post">
            {% csrf_token %}
            <input type="HIDDEN" value={{aaa}} id="produit" name="produit">
              <div id="im1">
                <input type="image" id="im11" class="fit-picture" src="{{a}}"/>
              </div>    
              <div id="nomAliment1">
                {{aa}}
              </div>
              <br>
          </form>
          {% if user.is_authenticated %}
          <form action="/mes_aliments/recherche/" method="POST">          
            <div>
              <input type="checkbox" style="width: 20px; height: 20px;"\
                "name="is_save1" id="product1" onclick='pushlist("product1", "user", "stock", "is_save1")' value="{{aa}}"/>
                Sauvegarder   
                <div id="is_save1"></div>          
            </div>
          </form>
          {% endif %}
          </div>
          <div class="col-sm-12 col-md-4" id="block4">
            <div id="rond"><img src={{bbbb}}></div>
              <form action="aliment_det" method="post">
                {% csrf_token %}
                <input type="HIDDEN" value={{bbb}} name="produit">
                <div id="im2">
                  <input type="image" id="im11" value={{aa}} class="fit-picture" src="{{b}}"/>
                </div>
                <div id="nomAliment2">
                  {{bb}}
                </div>
                <br>
                {% if user.is_authenticated %}
                <input type="checkbox" style="width: 20px; height: 20px;"
                id="product2" onclick='pushlist("product2", "user", "stock", "is_save2")' name="is_save2" value="{{bb}}" /> Sauvegarder
                <div id="is_save2"></div>
                {% endif %}
             </form>
           </div>
           <div class="col-sm-12 col-md-4" id="block4">
              <div id="rond">
                <img src={{cccc}}>
              </div>
              <form action="aliment_det" method="post">
                {% csrf_token %}
                <input type="HIDDEN" value={{ccc}} name="produit">
                <div id="im3">
                  <input type="image" id="im11" value={{cc}} class="fit-picture" src="{{c}}"/>
                </div>
                <div id="nomAliment2">
                  {{cc}}
                </div>
                <br>
                {% if user.is_authenticated %}
                <input type="checkbox" style="width: 20px; height: 20px;"
                id="product3" onclick='pushlist("product3", "user", "stock", "is_save3")' value="{{cc}}" name="is_save3"> Sauvegarder
               <div id="is_save3"></div>
               {% endif %}
             </form> 
           </div>
           <div class="col-sm-12 col-md-4" id="block4">
              <div id="rond"><img src={{dddd}}></div>
                <form action="aliment_det" method="post">
                  {% csrf_token %}

                  <input type="HIDDEN" value={{ddd}} name="produit">
                  <div id="im4">
                    <input type="image" id="im11" value={{dd}} class="fit-picture" src="{{d}}"/>
                  </div>
                  <div id="nomAliment2">{{dd}}</div>
                  <br>
                  {% if user.is_authenticated %}
                  <input type="checkbox" style="width: 20px; height: 20px;"
                  id="product4" onclick='pushlist("product4", "user", "stock", "is_save4")' value="{{dd}}" name="is_save4"> Sauvegarder
                  <div id="is_save4"></div>
                  {% endif %}
                </form>
              </div>
           <div class="col-sm-12 col-md-4" id="block4">
              <div id="rond"><img src={{eeee}}></div>
                <form action="aliment_det" method="post">
                  {% csrf_token %}
                  <input type="HIDDEN" value={{eee}} name="produit">
                  <div id="im5">
                  <input type="image" id="im11" value={{ee}} class="fit-picture" src="{{e}}"/></a></div>
                  <div id="nomAliment2">{{ee}}</div>
                  <br>
                  {% if user.is_authenticated %}
                    <input type="checkbox" style="width: 20px; height: 20px;"
                  id="product5" onclick='pushlist("product5", "user", "stock", "is_save5")' value="{{ee}}"name="is_save5"> Sauvegarder
                  <div id="is_save5"></div>
                  {% endif %}
                </form>
              </div>
           <div class="col-sm-12 col-md-4" id="block4">
             <div id="rond"><img src={{ffff}}></div>
              <form action="aliment_det" method="post">
                {% csrf_token %}
               <input type="HIDDEN" value={{fff}} name="produit">
               <div id="im6"><input type="image" id="im11" value={{ff}} class="fit-picture" src="{{f}}"/></a></div>
               <div id="nomAliment2">{{ff}}</div>
               <br>
               {% if user.is_authenticated %}
                <input type="checkbox" style="width: 20px; height: 20px;"
               id="product6" onclick='pushlist("product6", "user", "stock", "is_save6")' name="is_save6" value='{{ff}}'/> Sauvegarder
               <div id="is_save6"></div>
               {% endif %}
             </form>
         </div>
         <div style="text-align:center;">
        </div>
       </div>
    </div>
    <div id="a"></div>
    <br><br><br>
 </section>

<br><br>

{% include "bottom_page.html" %}
{% block content2 %}
{% endblock content2%}


<script type="text/javascript" src="/static/js/la_recherche1_js.js"></script>




