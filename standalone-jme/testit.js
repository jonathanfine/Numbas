
// See: https://developer.mozilla.org/en/Rhino_Shell
var test_data = eval(readFile('local/test-data.json'));

var i = 0;
var n = test_data.length;
var item;

for (i=0; i < n; i++){
    
    item = test_data[i];
    print(item);
}


var actual = Numbas.jme.display.exprToLaTeX('2^(3+4)');
var expect = '2^{ 3 + 4 }';

if (actual === expect)
    print('ok');
else
    print('error');
