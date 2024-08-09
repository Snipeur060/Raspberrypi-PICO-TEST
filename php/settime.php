<?php

// Vérifier si le paramètre "time" est présent dans l'URL
if (isset($_GET['time'])) {
    $time = $_GET['time'];

    // Vérifier que le paramètre "time" est au format attendu (ajuster selon votre besoin)
    if (preg_match('/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/', $time)) {
        // Enregistrez le temps (ajustez cette partie pour l'enregistrement dans votre base de données ou autre)
        file_put_contents('time.txt', $time);
        echo "Heure enregistrée avec succès : $time";
    } else {
        echo "Format de 'time' invalide";
    }
} else {
    echo "Paramètre 'time' manquant dans l'URL";
}

?>
