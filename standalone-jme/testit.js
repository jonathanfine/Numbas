// TODO: Provide for self and multiple arguments (not needed here).
var try_call = function(fn, arg){
    var value = null;
    var exception = null;

    try{
	value = fn(arg);
	// TODO: Resolve this hack for input "[".
	if (value === undefined)
	    value = null;
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

    // Fix up numbas strangeness - discard 'Expression was: ...'.
    // TODO: Better for numbas to add expression attribute to exception.
    if (actual.exception){
	actual.exception.message = actual.exception.message.split('\n')[0];
    }

    if (expect.error === null || expect.error === undefined){

	// Not expecting an error.
	if (actual.exception !== null){
	    print('Expecting value, got error');
	    print('input: ' + expect.input);
	    print('expect: ' + expect.output);
	    print('actual: ' + actual.exception.message);
	} 
	else if (expect.output !== actual.value)
	{
	    print('Wrong value');
	    print('input: ' + expect.input);
	    print('expect: ' + expect.output);
	    print('actual: ' + actual.value);
	}
	
    } else {
	
	// We are expecting an error.
	if (actual.exception === null){
	    print('Expecting error, got value');
	    print('input: ' + expect.input);
	    print('expect: ' + expect.error);
	    print('actual: ' + actual.value);
	} 
	else if (expect.error !== actual.exception.message)
	{
	    print('Wrong exception');
	    print('input: ' + expect.input);
	    print('expect: ' + expect.error);
	    print('actual: ' + actual.exception.message);	    
	}
    }
}


var actual = Numbas.jme.display.exprToLaTeX('2^(3+4)');
var expect = '2^{ 3 + 4 }';

if (actual === expect)
    print('ok');
else
    print('error');
