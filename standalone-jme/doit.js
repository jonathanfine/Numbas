load('local/expr-to-latex.js');

var actual = Numbas.jme.display.exprToLaTeX('2^(3+4)');
var expect = '2^{ 3 + 4 }';

if (actual === expect)
    print('ok');
else
    print('error');
