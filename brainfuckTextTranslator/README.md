# brainfuckTextTranslator

brainfuckTextTranslator is a small programm that can traslate texts in brainfuck

### Usage
```
python brainfuckTextTranslator.py -h
usage: brainfuckTextTranslator.py [-h] [-t T]

A small utility that translates texts in brainfuck.

optional arguments:
  -h, --help  show this help message and exit
  -t T        text to be translated

```
#### Example
```
python brainfuckTextTranslator.py -t "Hello World!"
>+++++++++[<++++++++>-]<.+++++++++++++++++++++++++++++.+++++++..+++.-------------------------------------------------------------------------------.>+++++++++++[<+++++>-]<.>++++++++[<+++>-]<.+++.>---[<-->+]<.--------.-------------------------------------------------------------------.
```

### How the program works
The aim of the program is to create a fast and light brainfuck program by reducing the used cells to only 2:
- cell 0 that will store datas
- cell 1 that will do calculations and that will move datas into the cell 0 from where they will be printed

This makes the program very fast and light as it is only necessary to update the value of a single cell a little as to get all the ascii values of all the characters the program have to print.
