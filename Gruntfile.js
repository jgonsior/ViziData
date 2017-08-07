module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    //pkg: grunt.file.readJSON('package.json'),
    ///////////
    // UGLIFY
    uglify: {
      dev: {
        options: {
          mangle: false,//true,
          beautify: false,
          compress: false,//true,
          preserveComments: true//false
        },
        files: {
          'js/main.js': 'js/*/*.js'
        }
      }
    },

    includeFiles: {
      options: {
        basePath: '',
        baseUrl: '',
        templates: {
          html: {
            js: '<script src="{filePath}"></script>'
          }
        }
      },
      myTarget: {
        files: {
          'index.html' : 'index.tpl'
        }
      }
    },


    ////////////
    // COMPASS
    compass: {
      dist: {
        options: {
          sassDir: 'sass',
          cssDir: 'stylesheets',
          outputStyle: 'compressed',
          environment: 'production'
        }
      }
    },
    ///////////////
    // AUTOPREFIX
    autoprefixer: {
      screen: {
        src: 'stylesheets/screen.css',
        dest: 'stylesheets/screen.css'
      }
    },
    //////////
    // WATCH
    watch: {
      compass: {
        files: 'sass/*.scss',
        tasks: ['compass','autoprefixer:screen']
      },
      includeFiles : {
        files: 'js/modular/*.js',
        tasks: ['includeFiles']
      }
     /* uglify: {
        files: 'js/modular/*.js',
        tasks: ['uglify']
      }*/
    }
  });


  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-autoprefixer');
  grunt.loadNpmTasks('grunt-include-files')

  // Default task(s).
  grunt.registerTask('default', ['includeFiles', 'watch']);

};
