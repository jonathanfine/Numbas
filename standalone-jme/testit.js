var Numbas = require('expr-to-latex').Numbas;
require('qunit-cli');
var QUnit = require('qunit').QUnit;

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

QUnit.test("JME expression to LaTeX conversion",function() {
    var test_data = eval(readFile('local/tests/expr-to-latex.json'));
    var exprToLaTeX = Numbas.jme.display.exprToLaTeX;


    var i = 0;
    var n = test_data.length;
    var data;

    QUnit.expect(n);

    for (i=0; i < n; i++)
    {
        
        data = test_data[i];
        
        if(data.error)
        {
            QUnit.raises(function() {
                    exprToLaTeX(data.input)
                },
                data.input
            );
        }
        else 
        {
            QUnit.equals(exprToLaTeX(data.input), data.output, data.input);
        }
    }
});

QUnit.begin(); // hacked b/c currently QUnit.begin is normally called on document.load
QUnit.start();
