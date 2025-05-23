// GSAP Animations 
gsap.fromTo(".panto", 
  { opacity: 1, y: -50 }, 
  { opacity: 1, y: 0, duration: 1, delay: 0.5 }
);

gsap.to("nav", { opacity: 1, duration: 1, delay: 1 });
gsap.from("nav a", { opacity: 1, x: -50, duration: 1, stagger: 0.2, delay: 1.5 });
gsap.from(".cart", { opacity: 1, x: 100, duration: 1, delay: 1.5 });

// Dropdown Animation
const dropdown = document.querySelector('.dropdown');
const dropdownMenu = document.querySelector('.dropdown-menu');

dropdown.addEventListener('mouseenter', () => {
  gsap.to(dropdownMenu, { opacity: 1, y: 10, duration: 0.3, display: 'block' });
});

dropdown.addEventListener('mouseleave', () => {
  gsap.to(dropdownMenu, { opacity: 0, y: -10, duration: 0.3, autoAlpha: 0 });

});

// Shake effect for the cart count when hovered over the cart icon
const cartIcon = document.querySelector('.cart-icon');
const cartCount = document.querySelector('.cart-count');

cartIcon.addEventListener('mouseenter', () => {
  gsap.to(cartCount, {
    x: 10, 
    duration: 0.1, 
    repeat: 10, 
    yoyo: true, 
    ease: "linear",
    onComplete: () => {
      gsap.to(cartCount, {
        x: 0, 
        duration: 0.3,
        ease: "power2.out"
      });
    }
  });
});

// GSAP Animations for Hero Text
gsap.from(".hedh1s", { opacity: 1, y: -50, duration: 1, delay: 1, ease: "power4.out" });
gsap.from(".hedps", { opacity: 1, y: 50, duration: 1, delay: 1.5, ease: "power4.out" });

// GSAP Animations for Search Bar Section
gsap.from(".search-bar-container", { opacity: 0, y: 50, duration: 1, delay: 2, ease: "power4.out" });

// Массив фраз для placeholder
const placeholderTexts = [
  "Search for Amazon, IKEA, or eBay...",
  "Looking for Target, Walmart, or Nike?",
  "Search for electronics, furniture, or fashion..."
];

const searchBar = document.getElementById('search-bar');
let textIndex = 0; // Индекс текущей фразы
let charIndex = 0; // Индекс текущего символа в фразе
let isTyping = false; // Флаг для отслеживания ввода текста

// Функция для динамичного набора текста в placeholder
function typePlaceholder() {
  if (isTyping) return; // Останавливаем печатание, если пользователь уже начал вводить

  const currentText = placeholderTexts[textIndex];
  searchBar.setAttribute("placeholder", currentText.substring(0, charIndex));
  charIndex++;

  if (charIndex > currentText.length) {
    // Плавное исчезновение текста перед переключением
    gsap.to(searchBar, { opacity: 0, duration: 0.5, onComplete: () => {
      // Задержка перед сменой фразы
      setTimeout(() => {
        charIndex = 0;
        textIndex = (textIndex + 1) % placeholderTexts.length; // Следующий текст
        gsap.to(searchBar, { opacity: 1, duration: 0.5 }); // Плавное возвращение текста
        typePlaceholder(); // Начинаем печатать новый текст
      }, 200); // Задержка перед новым набором текста
    }});
  } else {
    setTimeout(typePlaceholder, 50); // Скорость печатания (мс)
  }
}

// Запуск эффекта печатания
typePlaceholder();

// Обработка фокуса (начало ввода)
searchBar.addEventListener("focus", () => {
  isTyping = true; // Пользователь начал вводить, остановить анимацию
});

// Обработка потери фокуса (завершение ввода)
searchBar.addEventListener("blur", () => {
  isTyping = false; // Пользователь ушел, начать анимацию снова
  typePlaceholder(); // Возобновить анимацию
});

// Маппинг сайтов
const searchMappings = {
  amazon: "https://www.amazon.com",
  ikea: "https://www.ikea.com",
  ebay: "https://www.ebay.com",
  walmart: "https://www.walmart.com",
  target: "https://www.target.com",
  nike: "https://www.nike.com",
  adidas: "https://www.adidas.com",
  samsung: "https://www.samsung.com",
  microsoft: "https://www.microsoft.com",
  apple: "https://www.apple.com",
  etsy: "https://www.etsy.com",
  zara: "https://www.zara.com",
  uniqlo: "https://www.uniqlo.com",
  hm: "https://www.hm.com",
  bestbuy: "https://www.bestbuy.com",
  flipkart: "https://www.flipkart.com",
  aliexpress: "https://www.aliexpress.com"
  // Добавляйте свои сайты
};

// Обработка Enter
searchBar.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    const searchTerm = searchBar.value.trim().toLowerCase();
    const url = searchMappings[searchTerm];

    if (url) {
      window.location.href = url;
    } else {
      alert("Sorry, no results found. Try another keyword.");
    }
  }
});

// Лёгкое движение для заголовка
gsap.to(".hedh1s", {
y: "-10%", // Очень маленькое перемещение
duration: 2, // Плавное движение
repeat: -1, // Бесконечный повтор
yoyo: true, // Возврат в исходное положение
ease: "power1.inOut" // Лёгкое движение
});


// Ensure GSAP library is included in your project
gsap.registerPlugin(ScrollTrigger);

// Animating the features
gsap.utils.toArray('.gsap-feature').forEach(feature => {
gsap.from(feature, {
opacity: 0,
y: 50,
duration: 1.5,
delay: 0.2,
scrollTrigger: {
  trigger: feature,
  start: "top 80%",
  end: "top 50%",
  scrub: true,
  markers: false
}
});
});

document.addEventListener('DOMContentLoaded', function() {
  const slider = document.querySelector('.testimonial-cards');
  const cards = document.querySelectorAll('.testimonial-card');
  const prevBtn = document.querySelector('.slider-control--prev');
  const nextBtn = document.querySelector('.slider-control--next');
  
  let currentIndex = 0;
  const cardWidth = cards[0].offsetWidth;
  
  function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
  }
  
  nextBtn.addEventListener('click', () => {
    if (currentIndex < cards.length - 1) {
      currentIndex++;
      updateSlider();
    }
  });
  
  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateSlider();
    }
  });
});