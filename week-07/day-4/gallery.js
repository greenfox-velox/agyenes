'use strict';

// buttons

var button_left = document.querySelector('.selected .left_holder');
var button_right = document.querySelector('.selected .right_holder');
var small_button_left = document.querySelector('.thumbnails .left_holder');
var small_button_right = document.querySelector('.thumbnails .right_holder');

button_left.addEventListener('click', countListItems);
button_right.addEventListener('click', countListItems);
small_button_left.addEventListener('click', countListItems);
small_button_right.addEventListener('click', countListItems);
