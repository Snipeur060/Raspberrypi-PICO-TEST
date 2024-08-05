<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affichage de la Température et de l'Heure</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            text-align: center;
        }

        h2 {
            color: #333;
        }

        p {
            margin: 0;
            color: #4caf50;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Affichage de la Température et de l'Heure</h2>
    <div id="dataResult"></div>

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
</div>

</body>
</html>
