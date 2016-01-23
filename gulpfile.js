'use strict';

//Imports
var gulp = require('gulp');
var stylus = require('gulp-stylus');
var autoprefixer = require('gulp-autoprefixer');
var minifyCSS = require('gulp-minify-css');
var gulp-rename = require('gulp-rename');

//compile stylus to css
gulp.task('css', function () {
    gulp.src('./static/stylus/index.styl')
        .pipe(stylus({compress: false, paths: ['static/stylus']}))
        .pipe(autoprefixer())
        .pipe(minifyCSS())
        .pipe(rename('index.css'))
        .pipe(gulp.dest('./static/css'));
});

//keep watch on stylus files to compile
gulp.task('comp', function () {
  gulp.watch('**/*.styl', ['css']);
});
