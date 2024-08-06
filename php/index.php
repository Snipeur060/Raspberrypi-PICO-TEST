<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affichage de la Température et de l'Heure</title>
    <style>
        /* Google Font Import */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background-color: #0b0c10;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-image: linear-gradient(135deg, #0b0c10 25%, #1f2833 100%);
        }

        .container {
            background-color: #1f2833;
            border: 1px solid #66fcf1;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(102, 252, 241, 0.2);
            padding: 20px;
            width: 320px;
            text-align: center;
            animation: pulse 2s infinite;
        }

        h2 {
            color: #66fcf1;
            margin-bottom: 20px;
        }

        p {
            margin: 10px 0;
            color: #c5c6c7;
            animation: pulseText 2s infinite;
        }

        #dataResult p {
            font-weight: bold;
        }

        /* Model Viewer Styles */
        model-viewer {
            width: 100%;
            height: 300px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 0 10px rgba(102, 252, 241, 0.3);
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Affichage de la Température et de l'Heure</h2>
    <div id="dataResult"></div>
	<h3 style="color:white;">Votre station météo ressemble à :</h3>

    <!-- Intégration du modèle 3D -->
    <model-viewer alt="Modèle 3D du Raspberry Pi Pico" src="rppi.glb" ar shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer>

    <script>
        function getData() {
            var xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);

                    if (response.success) {
                        document.getElementById('dataResult').innerHTML =
                            '<p>Température actuelle : ' + response.temperature + ' degrés Celsius</p>' +
                            '<p>Heure actuelle : ' + response.time + '</p>';
                    } else {
                        document.getElementById('dataResult').innerHTML = '<p>Aucune donnée disponible pour le moment.</p>';
                    }
                }
            };

            xhr.open('GET', 'interaction', true);
            xhr.send();
        }

        // Appeler la fonction toutes les 5 secondes
        setInterval(getData, 2000);

        // Appeler la fonction une première fois au chargement de la page
        window.onload = getData;
    </script>

    <!-- Import the component -->
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.5.0/model-viewer.min.js"></script>

</div>

</body>
</html>
