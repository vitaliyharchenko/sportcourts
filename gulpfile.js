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
        templates: 'templates/'
    },
    src: {
        jade: 'src/jade/**/*.jade'
    },
    watch: {
        jade: 'src/jade/**/*.jade'
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

gulp.task('clean', [
    'templates:clean',
]);

gulp.task('build', [
    'jade:build',
]);

gulp.task('watch', function(){
    watch([path.watch.jade], function(event, cb) {
        gulp.start('jade:build');
    });
});

gulp.task('default', ['clean', 'build', 'watch']);