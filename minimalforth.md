# minimal Forth v2.0

## (Minimal Forth (Bennett/Knaggs))[http://www.euroforth.org/ef15/papers/knaggs.pdf] has the following words:

```
ALIGNED CELL+ CHAR+ ROT 2/ LSHIFT XOR OR > = 0= TRUE FALSE MOD 2* / * + VARIABLE CONSTANT DUP 
WORDS INCLUDE bye \ .S ( CR KEY? EMIT KEY DOES> ; CREATE : EXECUTE J LOOP UNTIL AGAIN BEGIN ELSE ' I DO 
REPEAT WHILE THEN IF R> OVER DROP R@ >R SWAP RSHIFT INVERT AND < - */MOD CHARS CALIGNED CALIGN C@ C, C! 
CELLS ALIGN @ , ! 
48 primitives, 69 words
```

## Limitations

- no allocation of memory: ALLOT HERE 
- no number output only .S: . .R 
- no pictured numeric output: <# #S # HOLD SIGN #> 

