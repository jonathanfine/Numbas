/*
 Run exprToLaTeX on examples.txt and write JSON output to console.

jonathanfine-Numbas$ js -f local/JSON-js/json2.js -f local/expr-to-latex.js standalone-jme/run-examples.js
[
    {
        "input": "2 + 2",
        "value": "undefined"
    },
    {
        "input": "a + b",
        "value": "2 + 2"
    },
    {
        "input": "2 + + + 2",
        "value": "a + b"
    },
    {
        "input": "3 * * * 4",
        "value": "2 + 2"
    }
]

 */


// TODO: Copied from testit.js.
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


var data;
var input;
var result;
var results;
var results_as_json;
var actual;
var i;

data = readFile('standalone-jme/examples.txt').split('\n');
results = [];

for(i=0; i<data.length; i++){
    
    input = data[i];

    // A line that begins with a '#' is a comment line.
    if (input.charAt(0) === '#')
	continue;

    // Trim leading and trailing white space.
    // http://stackoverflow.com/questions/498970/how-to-trim-a-string-in-javascript
    input = input.replace(/^\s+|\s+$/g, '');

    // Skip empty lines (such as at end of file).
    if (input === '')
	continue;

    // Make the function call, partially form the result.
    actual = try_call(Numbas.jme.display.exprToLaTeX, result.input);
    result = {};
    result.input = input;

    // Complete formation of the result.
    if (actual.exception){
	result.error = actual.exception.message.split('\n')[0];
    } else {
	result.value = actual.value;
    }

    // Append result to the array of results.
    results.push(result);
}

// Echo results, as JSON, to the console.
results_as_json = JSON.stringify(results, null, '    ');
print(results_as_json);
