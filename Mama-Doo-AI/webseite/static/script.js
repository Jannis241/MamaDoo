// Formularvalidierung für Lebensmittel-Eingabe
document.addEventListener('DOMContentLoaded', function() {
    // Eventlistener für Formularabsenden hinzufügen
    document.getElementById('foodForm').addEventListener('submit', function(event) {
        // Lebensmittel-Eingabefeld abrufen
        let foodInput = document.getElementById('food');
        // Überprüfen, ob das Feld leer ist
        if (foodInput.value.trim() === '') {
            // Absenden des Formulars verhindern
            event.preventDefault();
            // Benutzer benachrichtigen
            alert('Bitte geben Sie ein Lebensmittel ein.');
        }
    });
});
