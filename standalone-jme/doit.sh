cat \
    standalone-jme/stub-numbas.js \
    runtime/scripts/math.js \
    runtime/scripts/util.js \
    runtime/scripts/jme.js \
    runtime/scripts/jme-display.js \
    > local/expr-to-latex.js

js standalone-jme/doit.js