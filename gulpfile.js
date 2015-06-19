'use strict';

var gulp = require('gulp'),
    jade = require('gulp-jade'),
    rigger = require('gulp-rigger'),
    sourcemaps = require('gulp-sourcemaps'),
    sass = require('gulp-sass'),
    prefixer = require('gulp-autoprefixer'),
    cssmin = require('gulp-minify-css'),
    watch = require('gulp-watch'),
    rimraf = require('rimraf'),
    uglify = require('gulp-uglify');

var path = {
    build: {
        templates: 'templates/',
        js: 'static/js/'
    },
    src: {
        jade: 'src/jade/**/*.jade',
        js: 'src/js/**/*.js'
    },
    watch: {
        jade: 'src/jade/**/*.jade',
        js: 'src/js/**/*.js'
    },
    clean: {
        templates: 'templates/'
    }
};

gulp.task('templates:clean', function (cb) {
    rimraf(path.clean.templates, cb);
});

gulp.task('jade:build' , function () {
    gulp.src(path.src.jade)
        .pipe(jade({
            pretty: true
        }))
        .on('error', console.log)
        .pipe(rigger())
        .pipe(gulp.dest(path.build.templates));
});

gulp.task('js:build', function () {
    gulp.src(path.src.js)
        .pipe(rigger())
        .pipe(sourcemaps.init())
        .pipe(uglify())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.build.js));
});

gulp.task('clean', [
    'templates:clean',
]);

gulp.task('build', [
    'jade:build',
    'js:build',
]);

gulp.task('watch', function(){
    watch([path.watch.jade], function(event, cb) {
        gulp.start('jade:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('js:build');
    });
});

gulp.task('default', ['build', 'watch']);