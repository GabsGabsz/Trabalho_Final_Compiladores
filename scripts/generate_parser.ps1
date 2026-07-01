java -jar tools\antlr-4.13.2-complete.jar `
    -Dlanguage=Python3 `
    -visitor `
    -listener `
    -Xexact-output-dir `
    -o generated `
    grammar\JSSLexer.g4 `
    grammar\JSSParser.g4