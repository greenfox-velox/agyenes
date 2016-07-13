'use strict';

var express = require('express');
var http = require('http');
var app = express();
var bodyParser = require('body-parser');
var id = 0;
var mysql = require("mysql");

var con = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "12345",
  database: "todos"
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.get('/todos', function(req, res) {
  con.query('SELECT * FROM todos;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
      console.log(rows);
      res.send(rows);
  })
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM todos WHERE todo_id = ?;', req.params.id, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
      console.log(rows);
      res.send(rows);
  })
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

app.delete('/todos/:id', function(req, res) {
  for (var i = 0; i < todos.length; i++) {
    if (todos[i].id === +req.params.id) {
      todos[i]["destroyed"] = true;
      res.json(todos[i]);
      todos.splice(i, 1);
    }
  }
});

app.listen(3000);
