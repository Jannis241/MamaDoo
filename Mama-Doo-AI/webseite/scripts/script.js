document.getElementById('suche-habe-ich-nicht').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const ergebnisse = document.getElementById('ergebnisse-habe-ich-nicht');
    ergebnisse.innerHTML = '';

    if (query.length > 0) {
        const lebensmittel = ['Milch', 'Brot', 'Käse', 'Butter', 'Eier', 'Apfel'];
        const gefilterteErgebnisse = lebensmittel.filter(item => item.toLowerCase().includes(query));

        gefilterteErgebnisse.forEach(item => {
            const div = document.createElement('div');
            div.textContent = item;
            ergebnisse.appendChild(div);
        });
    }
});

document.getElementById('suche-habe-ich').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const ergebnisse = document.getElementById('ergebnisse-habe-ich');
    ergebnisse.innerHTML = '';

    if (query.length > 0) {
        const lebensmittel = ['Milch', 'Brot', 'Käse', 'Butter', 'Eier', 'Apfel'];
        const gefilterteErgebnisse = lebensmittel.filter(item => item.toLowerCase().includes(query));

        gefilterteErgebnisse.forEach(item => {
            const div = document.createElement('div');
            div.textContent = item;
            ergebnisse.appendChild(div);
        });
    }
});
