{% include "navbarre.html" %}

{% block content %}
{% endblock %}




  <header class="masthead text-center d-flex"></header>


  


  <section class="bg-primary" id="about">
      <div style="text-align:center">
        <form method="POST">
            {% csrf_token%}
            
             &nbsp;&nbsp;&nbsp;&nbsp;<strong>Ton pseudo :</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
             &nbsp;{{form.username}}

             <br><br>
             
            &nbsp;&nbsp;&nbsp;&nbsp<strong>Ton email : </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{form.email}}
            
            <br><br>
            
            &nbsp;&nbsp;&nbsp;&nbsp<strong>Confirme le : </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp
            &nbsp;{{form.email2}}
            
            <br><br>
            
            
            <strong>Et ton password </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {{form.password}}

            <br><br><br>
            
            &nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp<input type="submit" style="color:black;"/>
        </form>
        </div>
  </section>


{% include "bottom_page.html" %}

{% block content2 %}
{% endblock content2%}



</body>

</html>

  
  
  <script type = "text/javascript">



</script>




























