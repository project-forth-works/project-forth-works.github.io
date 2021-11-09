# Minimal Forth & Generic Forth

## Minimal Forth [(Bennett/Knaggs)](http://www.euroforth.org/ef15/papers/knaggs.pdf) has the following words:

```
ALIGNED CELL+ CHAR+ ROT 2/ LSHIFT XOR OR > = 0= TRUE FALSE MOD 2* / * + VARIABLE CONSTANT DUP 
WORDS INCLUDE bye \ .S ( CR KEY? EMIT KEY DOES> ; CREATE : EXECUTE J LOOP UNTIL AGAIN BEGIN ELSE ' I DO 
REPEAT WHILE THEN IF R> OVER DROP R@ >R SWAP RSHIFT INVERT AND < - */MOD CHARS CALIGNED CALIGN C@ C, C! 
CELLS ALIGN @ , ! 
48 primitives, 69 words
```

## Generic Forth (Bitter/Hoffmann/Hoekstra/Ouwerkerk)

As we are working on this *Project Forth Works*, we became aware that Minimal Forth is just too minimal to provide even simple examples. So we defined a prototype of a word set extension, we call this baby **Generic Forth**, as it is a Forth that most Forthers can easily understand.
Words marked with stars like this `*MOVE*` are still under discussion, so only the words without stars are in this **Generic Forth** word set of 42 words! With another 19 words in the waiting room :)  

Now an overview of all the words from **Minimal Forth** & the word we have selected to form **Generic Forth**, please note it is a living list. With good arguments it can be extended.  

String (Device):
```
    KEY  EMIT  KEY?  CR
```
```
    BL  SPACE  SPACES  S"  ."  CHAR  [CHAR]
    CMOVE  *CMOVE>*  *MOVE*
```
Stack:
```
    DUP  DROP  SWAP  OVER  ROT  >R  R>  R@  
```
```
    2DROP  2DUP  *BOUNDS*  *-ROT*  *TUCK*
```
Flow control:
```
    IF  ELSE  THEN  BEGIN  WHILE  REPEAT  AGAIN  UNTIL  DO  I  J  LOOP  EXECUTE  '
```
```
    LEAVE  EXIT
```
Number to string conversion:
```
    <#  #  #S  #>  HOLD  SIGN  .R  U.R  .  U.  BASE  HEX  DECIMAL
```
Definitions:
```
    :  ;  CONSTANT  VARIABLE  CREATE  DOES>
```
```
    VALUE  TO
```
Compiling:
``` 
    POSTPONE  IMMEDIATE  STATE  *[UNDEFINED]*  *[IF]*  *[THEN]*  *[*  *]*  *LITERAL*
```
Memory:
```
    !  C!  @  C@  ,  C,  ALLIGN  CELL+  CHAR+  CELLS  CHARS  CALLIGN  CALLIGNED  
```
```
    HERE  CHERE  ALLOT  FILL  ROM!  *+!*  *CELLS*
```
Error recovery:
```
    CATCH  THROW  ABORT"  *ABORT*
```
Arithmetic:
```
    +  -  *  /  2*  2/  */MOD  MOD
```
```
    UM*  UM/MOD  S>D  *ABS*  *ARSHIFT*
```
Comparision (Logic):
```
    0=  =  <  >  AND  OR  XOR  INVERT  TRUE  FALSE  LSHIFT  RSHIFT
```
```
    U<  *0<*  *WITHIN*
```
Miscellaneous (Tools):
```
    (  \  .S
```
```
    *MS*
```
