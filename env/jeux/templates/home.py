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
            <strong>Du gras, oui mais de qualité !</strong>
          </h1>
          <hr>
        </div>


        
        <div class="col-lg-8 mx-auto">
          <div class="text-faded mb-5" id="texteMilieu">
              <h2>Trouvez un produit de substitution</h2><br>
              <h2>pour ceux que vous consommez</h2><br>
              <h2>tous les jours.</h2>
          </div>
    

            <form action ="/mes_aliments/recherche/" method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="ZpPGYe4an9kbhNTmpXYQUBxfWbFxQnWq20X3SVmFrLBYDz1HyQacjnVhPE8nfBY7">
            <input type="hidden" name="csrfmiddlewaretoken" value="EamjY5jhJJz2DK6tRyzNuimbCmgWR39MDQ8h0gSiKiGjLb0OABbO443CiSMNOeH4">
              <input name="cool" class="input_top_haut_droit" type="text" size:"30" placeholder="Produit"/>
              <input class="input_desous_h2" type="submit" value="Chercher"/>
            </form>
            
        </div>
      </div>
    </div>
  </header>





  <section class="bg-primary" id="about">
  
    <div class="container">
    
      <div class="row">
      
        <div class="col-lg-8 mx-auto text-center">
        
          <h2 class="section-heading text-white">Colette et Remy</h2>
          <hr class="light my-4">
          
          <p class="text-faded mb-4" id="coletteTexte">
           <strong>Colette Tatou : </strong>" Nous aimons tous manger, surtout en France! Personnellement,
           une baguette fraîche, du bon fromage de chèvre et un bon vin rouge me suffisent amplement.
           Comme tout le monde, je fais mes courses au supermarché woulah je me fais pas livrer sur la tete de oim.
           Mais petit à petit je me suis rendue compte,
           quand nous avons ouvert le restaurant,
           que je te les REMPLACER pouvais aseptisés Que Produits l'habitus d'je avais acheter par de bons produits du terroir
           Et versez le same Souvent prix!" 
          </p>

          <p class="text-faded mb-4" id="remTexte">
           <strong>Remy : </strong>"Pour ma part je me rendais déjà bien dans les magasins car j'aime beaucoup me balader
           a dos de mamouth, surtout dans les caves et les cuisines.
           Je ne sais pas ce que c'est le contenu des boutiques bio (dont je raffole) ainsi que les ingrédients
           de tous les aliments vendus. Quand on m'a demandé de remplacer son Nutella par un aliment plus sain,
           je savais tout de suite. L'idée de pur beurre était née! "
          </p>



          <div class="rem">
            <img class="img-fluid1" src="/static/img/portfolio/mid/Rem.jpg" alt="">
            <p class ="remi_sous_picture"><strong>Chef Remy</strong></p>
          </div>

          
          <div class="colette">
            <img class="img-fluid2" src="/static/img/portfolio/mid/Coco.png" alt="">
            <p class="colette_sous_picture"><strong>Chef Colette Tatou</strong></p>
          </div>
          
        </div>
      </div>
    </div>
  </section>



{% include "bottom_page.html" %}

{% block content2 %}
{% endblock content2%}




</body>

</html>





