let slideIndex = 0;
let timeout;

function showSlides(dir) {
  const slides = Array.from(document.querySelector(".slides").children);
  for (let i = 0; i < slides.length; i++) {
    slides[i].classList.remove("fade");
    slides[i].style.display = "none";
  }
  
  if (dir === "back") {
    slideIndex--;
    if (slideIndex < 0) {
      slideIndex = slides.length - 1;
    }
  } else if (dir === "forward") {
    slideIndex++;
    if (slideIndex === slides.length) {
      slideIndex = 0;
    }
  } else {
    slideIndex++;
    if (slideIndex === slides.length) {
      slideIndex = 0;
    }
  }
  
  slides[slideIndex].style.display = "block";
  slides[slideIndex].classList.add("fade");
  timeout = setTimeout(showSlides, 8000);
}

const images = document.querySelectorAll("img");
const parent = document.querySelector(".slideshow-container");

images.forEach(img => {
  img.style.width = `${parent.offsetWidth}px`;
  img.style.height = `${parent.offsetHeight}px`;
});

document.addEventListener('DOMContentLoaded', function() {
  const back = document.querySelector('.back');
  const forward = document.querySelector('.forward');
  const slides = Array.from(document.querySelector(".slides").children);

  back.addEventListener('click', function() {
    clearTimeout(timeout);
    showSlides("back");
  });

  forward.addEventListener('click', function() {
    clearTimeout(timeout);
    showSlides("forward");
  });
});
timeout = setTimeout(showSlides, 8000);


