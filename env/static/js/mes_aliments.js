CHOISEN = []



function choice(im, image, detail, remplacement, nan, gabarit){
    var a = "<center><img src=" + gabarit + " style='padding:10px;width:60%;height:90px;'></center>"
    document.getElementById(im).style.display = "none";
    document.getElementById(image).innerHTML = a
    document.getElementById(detail).innerHTML = "<center><input type='submit'" +
                                                    "style='color:black;' value='Détails aliment' />" +
                                                    "</center><br>";
    document.getElementById(remplacement).innerHTML = "<center><input type='submit' style='color:black;" + 
                                                        "'value='Remplacer cette aliment' /></center><br>";

 
    var a =  "nanrien(" + "'" + im + "'" + ",'" + image + "','" + detail + "','" + remplacement + "','" + nan + "')" + '"'

   document.getElementById(nan).innerHTML = "<center><input type='button' onclick=" + '"' + a +
                                                "style='color:black;' value='Enfete non rien'/></center>";

   

};




function nanrien(im, image, detail, remplacement, nan){
    
    document.getElementById(im).style.display = "block";
    document.getElementById(image).innerHTML = "";
    document.getElementById(detail).innerHTML = "";    
    document.getElementById(remplacement).innerHTML = "";
    document.getElementById(nan).innerHTML = "";
    CHOISEN = []

    };


