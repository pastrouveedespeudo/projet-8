{% include "navbarre.html" %}
{% block content %}
{% endblock %}

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<link href="/static/css/recherche1.css" rel="stylesheet">
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

section class="bg-primary" id="about">
    {% if user.is_authenticated %}
    <div id="user" value={{user.username}} style="display:none;">{{user.username}}</div>    
    <div id="stock">{{stock_depassé}}</div>    
    {% else %}
    <div style="text-align:center;">
      Connecte-toi afin de pouvoir les <strong>enregistrer</strong>
      et visualise les depuis <strong>"Mon compte"</strong>
    </div> 
    {% endif %}
    <div class="container-fluid" id="conteneurCarre">
      <div class="row" id="row3">
        <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
          <div id="rond"><img src={{aaaa}} ></div>
          <form action="/mes_aliments/recherche/aliment_det" method="post">
          {% csrf_token %}
          <input type="HIDDEN" value={{aaa}} id="produit" name="produit">
          <div id="im1"><input type="image" id="im11" class="fit-picture" src="{{a}}"/></div>
          <div id="nomAliment1" style="font-size:1.5em;"><strong>{{aa}}</strong></div>
        <br>
      </form>
    <form action="/mes_aliments/remplacement" method="post" >
      {% csrf_token %}
    <input type="hidden" name="remplace_food" value="{{titre}},{{aa}}" >
    <center><input type="submit" value="Remplacer"></center>
    <div id="is_save1"></div>
  </form>
  </div> 
  <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
  <div id="rond"><img src={{bbbb}}></div>
  <form action="/mes_aliments/recherche/aliment_det" method="post">
        {% csrf_token %}
  <input type="HIDDEN" value={{bbb}} name="produit">
  <div id="im2"><input type="image" id="im11" value={{aa}} class="fit-picture" src="{{b}}"/></a></div>
  </form>
  <div id="nomAliment2" style="font-size:1.5em;"><strong>{{bb}}</strong></div>
  <br>
  <form action="/mes_aliments/remplacement" method="post" >
    {% csrf_token %}
  <input type="hidden" name="remplace_food" value="{{titre}},{{bb}}" >
  <center><input type="submit" value="Remplacer"></center>
  <div id="is_save2"></div>
  </form>
  </div>
  <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
    <div id="rond"><img src={{cccc}}></div>
    <form action="/mes_aliments/recherche/aliment_det" method="post">
          {% csrf_token %}

      <input type="HIDDEN" value={{ccc}} name="produit">
      <div id="im3"><input type="image" id="im11" value={{cc}} class="fit-picture" src="{{c}}"/></a></div>
      </form>
      <div id="nomAliment2" style="font-size:1.5em;"><strong>{{cc}}</strong></div>
      <br>
      <form action="/mes_aliments/remplacement" method="post" >
        {% csrf_token %}
      <input type="hidden" name="remplace_food" value="{{titre}},{{cc}}" >
      <center><input type="submit" value="Remplacer"></center>
      <div id="is_save3"></div>
      </form>
    </form>
  </div>
  <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
    <div id="rond"><img src={{dddd}}></div>
      <form action="/mes_aliments/recherche/aliment_det" method="post">
            {% csrf_token %}
      <input type="HIDDEN" value={{ddd}} name="produit">
      <div id="im4"><input type="image" id="im11" value={{dd}} class="fit-picture" src="{{d}}"/></a></div>
      </form>
      <div id="nomAliment2" style="font-size:1.5em;"><strong>{{dd}}</strong></div>
      <br>
      <form action="/mes_aliments/remplacement" method="post" >
        {% csrf_token %}
      <input type="hidden" name="remplace_food" value="{{titre}},{{dd}}" >
      <center><input type="submit" value="Remplacer"></center>
      <div id="is_save4"></div>
      </form>
    </form>
  </div>
  <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
    <div id="rond"><img src={{eeee}}></div>
    <form action="/mes_aliments/recherche/aliment_det" method="post">
          {% csrf_token %}
      <input type="HIDDEN" value={{eee}} name="produit">
      <div id="im5"><input type="image" id="im11" value={{ee}} class="fit-picture" src="{{e}}"/></div>
      </form>
      <div id="nomAliment2" style="font-size:1.5em;"><strong>{{ee}}</strong></div>
      <br>
      <form action="/mes_aliments/remplacement" method="post" >
        {% csrf_token %}
      <input type="hidden" name="remplace_food" value="{{titre}},{{ee}}" >
      <center><input type="submit" value="Remplacer"></center>
      <div id="is_save5"></div>
    </form>
  </div>
  <div class="col-sm-12 col-md-12 col-lg-4" id="block4">
    <div id="rond">
        <img src={{ffff}}>
    </div>
    <form action="/mes_aliments/recherche/aliment_det" method="post">
        {% csrf_token %}
        <input type="HIDDEN" value={{fff}} name="produit">
        
        <div id="im6">
            <input type="image" id="im11" value={{ff}} class="fit-picture" src="{{f}}"/>
        </div>
    </form>
        <div id="nomAliment2" style="font-size:1.5em;">
            <strong>{{ff}}</strong>
        </div>
        <br>
      <form action="/mes_aliments/remplacement" method="post" >
      {% csrf_token %}

      <input type="hidden" name="remplace_food" value="{{titre}},{{ff}}" >
        <center><input type="submit" value="Remplacer" /></center>{% csrf_token %}
      </form>
        <div id="is_save6">
  </div>
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
{% endblock content2%}</body>




























