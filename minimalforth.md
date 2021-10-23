# minimal Forth & extensions

## Minimal Forth [(Bennett/Knaggs)](http://www.euroforth.org/ef15/papers/knaggs.pdf) has the following words:

```
ALIGNED CELL+ CHAR+ ROT 2/ LSHIFT XOR OR > = 0= TRUE FALSE MOD 2* / * + VARIABLE CONSTANT DUP 
WORDS INCLUDE bye \ .S ( CR KEY? EMIT KEY DOES> ; CREATE : EXECUTE J LOOP UNTIL AGAIN BEGIN ELSE ' I DO 
REPEAT WHILE THEN IF R> OVER DROP R@ >R SWAP RSHIFT INVERT AND < - */MOD CHARS CALIGNED CALIGN C@ C, C! 
CELLS ALIGN @ , ! 
48 primitives, 69 words
```

## Minimal Forth extensions (Bitter/Hoffmann/Hoekstra/Ouwerkerk)

As we are working on this *Embedding Forth* project, we became aware that minimal Forth is just too minimal to provide even simple examples. So we defined a prototype of a word set extension. Words marked with stars like this `*MOVE*` are still under discussion, so only the words without stars are in this first expansion word set of 39 words! With another 15 words in the waiting room :)

String:
```
    BL  SPACE  SPACES  S"  ."  CHAR  [CHAR]
    CMOVE  *CMOVE>*  *MOVE*
```
Stack:
```
    2DROP  2DUP  *BOUNDS*  *-ROT*  *TUCK*
```
Number to string conversion:
```
    <#  #  #S  #>  HOLD  SIGN  .R  U.R  .  BASE  HEX  DECIMAL
```
Compiling:
``` 
    POSTPONE  IMMEDIATE  STATE  *[UNDEFINED]*  *[IF]*  *[THEN]*
```
Memory:
```
    HERE  CHERE  ALLOT  FILL  ROM!  *+!*  *CELLS*  *CELL-*
```
Error recovery:
```
    CATCH  THROW  ABORT"  *ABORT*
```
Arithmetic:
```
    UM*  UM/MOD  *ABS*
```
Miscellaneous:
```
    LEAVE  VALUE  TO  S>D  *MS*  *WITHIN*
```

