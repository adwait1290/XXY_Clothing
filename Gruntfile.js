'use strict';
module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        exec : {
                run_collect_static: {
                    command: 'src/manage.py collectstatic --no-input',
                    stdout: false,
                    stderr: false
                },
        },
        // Task configuration goes here.
        concat: {
            options : { nonull: true, },
            app: {
                src: ['static/js/app/**/*.js'],
                dest: 'build/static/js/app.js'
                },
            vendor: {
                src: ['static/js/vendor/**/*.js'],
                dest: 'build/static/js/lib.js'
            }
        },
        uglify: {
            app: {
                files: {'build/static/js/app.min.js': ['static/js/app/**/*.js']}
            },
            vendor: {
                files: {'build/static/js/lib.min.js': ['static/js/vendor/**/*.js']}
            }
        },
        less: {
                dev: {
                    options: {
                        paths: ['/static/static/less/'],
                        plugins: [
                            new (require('less-plugin-autoprefix'))({browsers: ["last 2 versions"]}),
                            new (require('less-plugin-clean-css'))
                          ],
                    },
                    files: {
                        'static/static/css/theme.css': 'static/static/less/theme.less'
                    }
                }
            },
        watch: {
            options: {livereload: true},
            javascript: {
                    files: ['static/js/app/**/*.js'],
                    tasks: ['concat']
            },
            less: {
                    files: 'static/static/less/*.less',
                    tasks: ['less:dev']
            },
            css: {
                files: 'static/static/css/*.css',
                tasks: ['exec:run_collect_static']
            }
        }
    });

    // Load plugins here.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-exec');
    // Register tasks here.
    grunt.registerTask('default', ['grunt-contrib-concat','grunt-contrib-uglify','grunt-contrib-less','grunt-contrib-watch']);

};
