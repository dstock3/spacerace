let slideIndex = 0;
let timeout;

const showSlides = () => {
  let i;
  let slides = Array.from(document.querySelector(".slides").children);
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  
  if (slideIndex >= slides.length - 1) {
    slideIndex = 0;
  }
  
  slides[slideIndex].style.display = "block";
  timeout = setTimeout(showSlides, 6000);
  return timeout
}

let images = document.querySelectorAll("img");
let parent = document.querySelector(".slideshow-container");

images.forEach(img => {
  img.style.width = `${parent.offsetWidth}px`;
  img.style.height = `${parent.offsetHeight}px`;
});

document.addEventListener('DOMContentLoaded', function() {
  let back = document.querySelector('.back');
  let forward = document.querySelector('.forward');
  let slides = Array.from(document.querySelector(".slides").children);

  back.addEventListener('click', function() {
    
    if (slideIndex < 0) {
      slideIndex = slides.length - 1;

    }
    let timeout = showSlides();
    clearTimeout(timeout);
  });

  forward.addEventListener('click', function() {

    slideIndex++;
    if (slideIndex >= slides.length) {
      slideIndex = 0;
    }
    let timeout = showSlides();
    clearTimeout(timeout);
  });
});
