/*#Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
#Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
#Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
#Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
#Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
*/



var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
