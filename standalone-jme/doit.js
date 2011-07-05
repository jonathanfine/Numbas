var Numbas = {};
var type = {};

Numbas.queueScript = function(file, deps, callback){
    callback();
    };

load('runtime/scripts/math.js');
load('runtime/scripts/util.js');
load('runtime/scripts/jme.js');
load('runtime/scripts/jme-display.js');
