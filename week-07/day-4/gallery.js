'use strict';

var imagecount = 1
var total = 10

function slide (x) {
  var Image = document.getElementById('img');
  imagecount = imagecount + x;
  if (imagecount > total) { imagecount =1;}
  if (imagecount < 1) { imagecount = total;}
  Image.src = "Images/img" + imagecount +".jpg";
}

function step (y) {
  var little_images = document.querySelectorAll('.little_pictures');
  imagecount = imagecount + y;
  Image.src = "Images/img" + imagecount +".jpg";
}

function highlight (y) {
  var Image = document.getElementById('img');
  var little_image = document.querySelectorAll('.little_pictures')[y];
  Image = little_image;
}
