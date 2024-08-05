<?php

// Vérifier si le paramètre temp existe dans l'URL
if(isset($_GET['temp'])) {
    // Récupérer la température depuis l'URL
    $temperature = $_GET['temp'];

    // Vérifier si la température est un nombre décimal
    if(is_numeric($temperature)) {
        // Vérifier si la température est dans une plage raisonnable (par exemple, entre -50 et 50 degrés Celsius)
        if($temperature >= -50 && $temperature <= 50) {
            // Échapper la température pour éviter les injections
            $temperature = htmlspecialchars($temperature);

            // Enregistrer la température dans le fichier temp.txt
            file_put_contents('temp.txt', $temperature);

            echo 'Température enregistrée avec succès : ' . $temperature . ' degrés Celsius';
        } else {
            echo 'Erreur : La température doit être comprise entre -50 et 50 degrés Celsius';
        }
    } else {
        echo 'Erreur : La température doit être un nombre décimal';
    }
} else {
    echo 'Erreur : Paramètre temp manquant dans l\'URL';
}

?>
