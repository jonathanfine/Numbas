var Numbas = {};
var type = {};

Numbas.queueScript = function(file, deps, callback){
    callback();
    };

load('runtime/scripts/math.js');
load('runtime/scripts/util.js');
load('runtime/scripts/jme.js');
load('runtime/scripts/jme-display.js');

var actual = Numbas.jme.display.exprToLaTeX('2^(3+4)');
var expect = '2^{ 3 + 4 }';

if (actual === expect)
    print('ok');
else
    print('error');
