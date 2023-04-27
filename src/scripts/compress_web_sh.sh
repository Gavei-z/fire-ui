#! /bin/bash

JS_PATH=D:/GaveiFile/Fire_UI_dj/src/web/static/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/

find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}web.js
