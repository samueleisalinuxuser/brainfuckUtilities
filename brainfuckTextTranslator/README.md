# brainfuckTextTranslator

brainfuckTextTranslator is a small program that can traslate texts in brainfuck

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
python brainfuckTextTranslator.py -t "I program in brainfuck"
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
-----------------------------------------.>++++++++++++++++[<+++++>-]<.++.
---.--------.+++++++++++.-----------------.>++++[<+++>-]<.
>-----------[<------->+]<.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++.
>-------------[<------>+]<.
>+++++++++++[<++++++>-]<.
++++++++++++++++.
-----------------.++++++++.+++++.--------.>+++++[<+++>-]<.>---------[<-->+]<.++++++++.
```

### Memory usage
The resulting brainfuck program uses only two cells of memory, one for storing and printing charactersand one for calculating and passing values to the first one.

### Program explanation

here I'll comment the code.
