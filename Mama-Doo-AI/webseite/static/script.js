document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Daten erfolgreich übermittelt!');
                window.location.href = "/confirmation";
            } else {
                alert('Fehler beim Übermitteln der Daten.');
            }
        });
    });
});
