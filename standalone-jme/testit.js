// TODO: Provide for self and multiple arguments (not needed here).
var try_call = function(fn, arg){
    var value = null;
    var exception = null;

    try{
	value = fn(arg);
    } catch (x) {
	exception = x;
    }

    return {
	value: value,
	exception: exception
	};
};

// See: https://developer.mozilla.org/en/Rhino_Shell
var test_data = eval(readFile('local/test-data.json'));
var test_fn = Numbas.jme.display.exprToLaTeX;

var i = 0;
var n = test_data.length;
var actual;
var expect;

for (i=0; i < n; i++){
    
    expect = test_data[i];
    actual = try_call(test_fn, expect.input);

    if (expect.error === null || expect.error === undefined){
	// Not expecting an error.

	if (actual.exception !== null){
	    print('Got error, expecting value');
	    
	} else if (expect.output !== actual.value){
	    	    print('Got wrong value');
	    print('input: ' + expect.input);
	    print('expect: ' + expect.output);
	    print('actual: ' + actual.value);
	}
	
    } else {

	// We are expecting an error.	
    }
}


var actual = Numbas.jme.display.exprToLaTeX('2^(3+4)');
var expect = '2^{ 3 + 4 }';

if (actual === expect)
    print('ok');
else
    print('error');
