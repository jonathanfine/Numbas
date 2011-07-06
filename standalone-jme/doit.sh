cat \
    standalone-jme/stub-numbas.js \
    runtime/scripts/math.js \
    runtime/scripts/util.js \
    runtime/scripts/jme.js \
    runtime/scripts/jme-display.js \
    > local/expr-to-latex.js

# Use -f to execute these two script files.
js -f local/expr-to-latex.js -f standalone-jme/testit.js