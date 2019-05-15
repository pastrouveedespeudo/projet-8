{% include "navbarre.html" %}

{% block content %}
{% endblock %}

  <header class="masthead text-center d-flex">
    <div class="container my-auto">
      <div class="row">
        <div class="col-lg-5 mx-auto">
          <h1 id="ya">
            <div style='color:white;font-size:4vw;'><strong>ALOY !</strong></div>
          </h1>
          <hr>
        </div>


        
        <div class="col-lg-8 mx-auto">
          <div class="text-faded mb-5">
              <div style="font-size:3.5vw; color:red;">{% if user.is_authenticated %}ALOY ! {{user.username}}{%endif%}</div>
              
          </div>
        </div>
      </div>
    </div>
  </header>




  <section class="bg-primary" id="about">
  
    <div class="container">
    
      <div class="row">
      
        <div class="col-lg-12 mx-auto text-center">
        
          <h2 class="section-heading text-white" id="yo" style="font-size:3vw;">Information du compte</h2>
          <hr class="light my-4">
          
          <p class="text-faded mb-4" id="coletteTexte">
           <div style="font-size:2.5vw;"><strong>Info sur toi</strong></div>
           {% if user.is_authenticated %}
           <p style='font-size:2vw;'> Nom du compte :  {{user.username}}</p>
           <br>
           <p style="font-size:2vw;">Adresse Mail : {{user.email}}</p>
           <br>

           {%endif%}
          </p>


          
        </div>
      </div>
    </div>
  </section>





{% include "bottom_page.html" %}

{% block content2 %}
{% endblock content2%}

</body>

</html>
