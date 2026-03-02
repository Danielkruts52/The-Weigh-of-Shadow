(function() {
    const slidesWrapper = document.getElementById('slidesWrapper');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dots = document.querySelectorAll('.dot');
    
    const totalSlides = document.querySelectorAll('.slide').length;
    let currentIndex = 0;
    
    function updateCarousel() {
        slidesWrapper.style.transform = `translateX(-${currentIndex * 100}%)`;
        
        dots.forEach((dot, idx) => {
            if (idx === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }
    
    function nextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateCarousel();
    }
    
    function prevSlide() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateCarousel();
    }
    
    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);
    
    dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => {
            currentIndex = idx;
            updateCarousel();
        });
    });
    
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            e.preventDefault();
            prevSlide();
        } else if (e.key === 'ArrowRight') {
            e.preventDefault();
            nextSlide();
        }
    });
    
    updateCarousel();
})();


// Функция для обновления таймера
function updateCountdown() {
    // Устанавливаем целевую дату (12 марта 2026 года)
    // Месяцы в JS начинаются с 0, поэтому март - это 2
    const targetDate = new Date(2026, 2, 12, 0, 0, 0); // 12 марта 2026 00:00:00
    const currentDate = new Date();
    
    // Вычисляем разницу в миллисекундах
    const difference = targetDate - currentDate;
    
    // Получаем элемент для отображения таймера
    const timerElement = document.getElementById('countdown-timer');
    
    // Проверяем, не наступила ли уже целевая дата
    if (difference <= 0) {
        timerElement.textContent = "Акция закончилась!";
        clearInterval(timerInterval);
        return;
    }
    
    // Вычисляем дни, часы, минуты и секунды
    const days = Math.floor(difference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((difference % (1000 * 60)) / 1000);
    
    // Форматируем вывод (добавляем ведущие нули для красоты)
    const formattedHours = hours.toString().padStart(2, '0');
    const formattedMinutes = minutes.toString().padStart(2, '0');
    const formattedSeconds = seconds.toString().padStart(2, '0');
    
    // Обновляем текст
    timerElement.textContent = `${days}д ${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

// Запускаем таймер
updateCountdown(); // Запускаем сразу, чтобы не ждать первую секунду
const timerInterval = setInterval(updateCountdown, 1000); // Обновляем каждую секунду