var slideIndex = 0;
let timeout;

function showSlides(dir) {
  let slides = Array.from(document.querySelector(".slides").children);
  for (let i = 0; i < slides.length; i++) {
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
  timeout = setTimeout(showSlides, 6000);
}

let images = document.querySelectorAll("img");
let parent = document.querySelector(".slideshow-container");

images.forEach(img => {
  img.style.width = `${parent.offsetWidth}px`;
  img.style.height = `${parent.offsetHeight}px`;
});

document.addEventListener('DOMContentLoaded', function() {
  var back = document.querySelector('.back');
  var forward = document.querySelector('.forward');
  var slides = Array.from(document.querySelector(".slides").children);

  back.addEventListener('click', function() {
    clearTimeout(timeout);
    showSlides("back");
  });

  forward.addEventListener('click', function() {
    clearTimeout(timeout);
    showSlides("forward");
  });
});
