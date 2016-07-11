'use strict';

var express = require('express');
var http = require('http');
var app = express();
var bodyParser = require('body-parser');
var id = 0;

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

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

app.post('/todos', function(req, res) {
  var id = todos.length
  req.body["id"] = id + 1;
  todos.push(req.body);
  req.body["completed"] = false;
  res.json(todos[id-1]);
});

app.put('/todos/:id', function(req, res) {
  for (var i = 0; i < todos.length; i++) {
    if (todos[i].id === +req.params.id) {
      todos[i].text = req.body["text"];
      todos[i].completed = req.body["completed"];
      res.json(todos[i]);
    }
  }
});

// app.delete('/todos/:id', function(req, res) {
//   for (var i = 0; i < todos.length; i++) {
//     if (todos[i].id === +req.params.id) {
//       todos[i].text = req.body["text"];
//       todos[i].completed = req.body["completed"];
//       res.json(todos[i]);
//     }
//   }
// });

app.listen(3000);
