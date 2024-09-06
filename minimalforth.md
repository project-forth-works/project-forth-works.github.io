# Minimal Forth & Generic Forth

## Minimal Forth [(Bennett/Knaggs)](http://www.euroforth.org/ef15/papers/knaggs.pdf) has the following words:
 
```
ALIGNED CELL+ CHAR+ ROT 2/ LSHIFT XOR OR > = 0= TRUE FALSE MOD 2* / * + VARIABLE CONSTANT DUP 
WORDS INCLUDE bye \ .S ( CR KEY? EMIT KEY DOES> ; CREATE : EXECUTE J LOOP UNTIL AGAIN BEGIN ELSE 
' I DO REPEAT WHILE THEN IF R> OVER DROP R@ >R SWAP RSHIFT INVERT AND < - */MOD CHARS CALIGNED 
CALIGN C@ C, C! CELLS ALIGN @ , ! 
48 primitives, 69 words
```

## Generic Forth (Bitter/Hoffmann/Hoekstra/Ouwerkerk/Nijhof)

As we are working on this *Project Forth Works*, we became aware that Minimal Forth is just too minimal to provide even simple examples. So we defined a prototype of a word set extension based mainly on the [core wordset](https://www.taygeta.com/forth/dpans6.htm#6.1) of [dpANS94](http://www.openfirmware.info/data/docs/dpans94.pdf). We call this baby **Generic Forth**, as it is a Forth that most Forthers and Forth systems can easily understand.
In this **Generic Forth** word set there are a total of 153 words!

Now an overview of all the words we have selected to form **Generic Forth**, please note it is a living list. With good arguments it can be extended.

**String (Device):**  
`    KEY  EMIT  KEY?  CR  BL  SPACE  SPACES  S"  ."  CHAR  [CHAR]  CMOVE  MOVE  TYPE  `  

**Stack:**  
`    ?DUP  DUP  DROP  SWAP  OVER  ROT  >R  R>  R@  2DROP  2DUP  2OVER  2SWAP  DEPTH  `  

**Flow control:**  
`    IF  ELSE  THEN  BEGIN  WHILE  REPEAT  AGAIN  UNTIL  DO  I  J  LOOP  EXECUTE  +LOOP  UNLOOP  LEAVE  EXIT  `  

**Number to string conversion:**  
`    <#  #  #S  #>  HOLD  SIGN  BASE  HEX  DECIMAL  .  U.  .R  U.R  `  

**Definitions:**  
`    :  ;  CONSTANT  VARIABLE  CREATE  DOES>  VALUE  TO  `  

**Compiling:**  
`    POSTPONE  IMMEDIATE  STATE  RECURSE  [  ]  [']  [CHAR]  LITERAL  `  

**Memory:**  
`    !  C!  @  C@  ,  C,  ALIGN  CELL+  CELLS  2!  2@  ALIGNED  HERE  CHERE  ALLOT  FILL  ROM!  +!  COUNT  FILL  `  
**Error recovery:**  
`    CATCH  THROW  ABORT"  ABORT  `  

**Arithmetic:**  
`    +  -  *  /  2*  2/  */MOD  MOD  UM*  UM/MOD  S>D  ABS  */  /MOD  1+  1-  FM/MOD  M*  MAX  MIN  NEGATE  FM/REM  `  

**Comparision (Logic):**  
`    0=  =  <  >  AND  OR  XOR  INVERT  TRUE  FALSE  LSHIFT  RSHIFT  U<  0<  WITHIN `  

**Parsing:**  
`    WORD  PARSE  '  REFILL`  

**Miscellaneous (Tools):**  
`    (  \  .S  WORDS  MS  EVALUATE  ACCEPT  FIND  QUIT  SOURCE  >NUMBER  >BODY  >IN  `  
