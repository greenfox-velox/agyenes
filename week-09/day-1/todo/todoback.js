'use strict';

var express = require('express');
var http = require('http');
var app = express();
var bodyParser = require('body-parser')

var urlencodedparser = bodyParser.urlencoded({extended: false});

var todos = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
];

app.get('/todos', function(req, res) {
  res.send(todos);
});

function getOneTodo(todoItem) {
  for (var i = 0; i < todos.length; i++) {
    if (todos[i].id === todoItem) {
      return todos[i];
    }
  }
}

app.get('/todos/:id', function(req, res) {
  res.json(getOneTodo(+req.params.id));
});

app.post('/todos', urlencodedparser, function(req, res) {
  todo_list.push(req.body);
});

app.listen(3000);
