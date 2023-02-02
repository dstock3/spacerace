var slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = Array.from(document.querySelector(".slides").children);
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex >= slides.length) {
    slideIndex = 0;
  }
  slides[slideIndex].style.display = "block";
  setTimeout(showSlides, 6000);
}

let images = document.querySelectorAll("img");
let parent = document.querySelector(".slideshow-container");

images.forEach(img => {
  img.style.width = `${parent.offsetWidth}px`;
  img.style.height = `${parent.offsetHeight}px`;
});