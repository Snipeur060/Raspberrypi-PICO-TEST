<?php

// Récupérer la température depuis le fichier temp.txt
$temperature = file_get_contents('temp.txt');
$time = file_get_contents("time.txt");
// Vérifier si la température a été enregistrée
$response = array('success' => true, 'temperature' => $temperature,'time' => $time);

// Retourner la réponse au format JSON
header('Content-Type: application/json');
echo json_encode($response);
