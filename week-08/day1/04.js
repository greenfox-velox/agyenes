'use strict';

var property = 1
var price = 40

function Car(type, color, balance) {
    this.type = type;
    this.color = color;
    this.balance = balance;
}

Car.prototype.enter = function(enterDate) {
  this.enterDate = enterDate;
  this.property = property;
  property++;
}

Car.prototype.getEnterDate = function() {
  console.log(this.enterDate) ;
}

Car.prototype.leave = function(leaveDate) {
  this.balance -= (leaveDate - this.enterDate) * price
}

Car.prototype.getStats = function() {
  console.log('Type: ' + this.type + ' Color: ' + this.color + ' Balance: ' + this.balance)
}

var Car1 = new Car('Buick', 'red', 300);
var Car2 = new Car('Datsun', 'green', 650);
var Car3 = new Car('NSU', 'white', 700);

Car1.enter(12)
Car2.enter(15)
Car3.enter(18)
Car1.getEnterDate()
Car2.getEnterDate()
Car3.getEnterDate()
Car1.leave(18)
Car2.leave(21)
Car3.leave(22)
Car1.getStats()
Car2.getStats()
Car3.getStats()

var number_of_cars = 0;
var parkingCarsSince = 0;
var cars_in_park = []
var elapsed_time = 0

function CarPark(income, startTime) {
  this.income = income;
  this.startTime = startTime;
  this.elapsed_time = elapsed_time;
  this.number_of_cars = number_of_cars
}

CarPark.prototype.carEnter = function(car) {
  car.startTime = startTime;
  this.number_of_cars += 1;
  cars_in_park.push(car)
  cars_in_park++;
}

CarPark.prototype.carLeave = function(car) {
  car.leaveTime = leaveTime;
  this.number_of_cars -= 1;
  cars_in_park.pop(car);
}

CarPark.prototype.elapseTime = function(hours) {
  this.elapsed_time += car.leaveTime - car.startTime;
  this.income += car.balance
}

CarPark.prototype.getStats = function() {
  console.log('Cars: ' + this.number_of_cars + ' Time: ' + this.color + ' Income: ' + this.income)
}

CarPark.prototype.getParkingCarsSince = function(hour) {
  cars_in_park.forEach(function(e) {
    if (e.this.elapsed_time > hour) {
      parkingCarsSince ++;
      }
    })
  };

var CarPark1 = new CarPark(50000, 0);
CarPark1.getStats()
