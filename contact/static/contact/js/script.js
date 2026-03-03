
    function openFilter() {
        document.getElementById('filterPanel').classList.add('active');
        document.getElementById('overlay').classList.add('active');
    }
    
    function closeFilter() {
        document.getElementById('filterPanel').classList.remove('active');
        document.getElementById('overlay').classList.remove('active');
    }
    
    // Закрываем фильтр если нажали Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeFilter();
        }
    });
