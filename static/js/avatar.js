/* --- DARK MODE TOGGLE --- */
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// 1. Check if user already has a saved preference in their browser
const currentTheme = localStorage.getItem('theme');
if (currentTheme === 'dark') {
    body.classList.add('dark-mode');
    themeToggle.textContent = '☀️';
}

// 2. When the button is clicked
themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    // 3. Update the icon
    if (body.classList.contains('dark-mode')) {
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'dark'); // Save preference
    } else {
        themeToggle.textContent = '🌙';
        localStorage.setItem('theme', 'light'); // Save preference
    }
});