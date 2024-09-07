const icon = document.getElementById('search-icon');
const searchEngine = document.getElementById('searchEngine');

icon.addEventListener('click', () => {
    searchEngine.classList.toggle('active');
});