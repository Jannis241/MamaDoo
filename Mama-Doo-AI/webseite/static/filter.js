$(document).ready(function() {
    $('#filterSelect').change(function() {
        var sortBy = $(this).val();
        var container = $('#resultsContainer');

        if (sortBy === 'default') {
            return;
        }

        container.children().sort(function(a, b) {
            var aValue, bValue;

            if (sortBy === 'rating' || sortBy === 'satt' || sortBy === 'difficulty') {
                aValue = parseFloat($(a).find('p strong:contains(' + sortBy + ')').next().text().trim());
                bValue = parseFloat($(b).find('p strong:contains(' + sortBy + ')').next().text().trim());
            }

            if (sortBy === 'rating' || sortBy === 'satt') {
                return sortBy === 'rating' || sortBy === 'satt' ? bValue - aValue : aValue - bValue;
            } else {
                if (aValue < bValue) {
                    return -1;
                }
                if (aValue > bValue) {
                    return 1;
                }
                return 0;
            }
        }).appendTo(container);
    });
});
