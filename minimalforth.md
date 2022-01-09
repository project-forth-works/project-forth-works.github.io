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

As we are working on this *Project Forth Works*, we became aware that Minimal Forth is just too minimal to provide even simple examples. So we defined a prototype of a word set extension based mainly on the [core wordset](http://forth.sourceforge.net/std/dpans/dpans6.htm) of [dpANS94](http://www.openfirmware.info/data/docs/dpans94.pdf). We call this baby **Generic Forth**, as it is a Forth that most Forthers and Forth systems can easily understand.
In this **Generic Forth** word set there are a total of 152 words!

Now an overview of all the words we have selected to form **Generic Forth**, please note it is a living list. With good arguments it can be extended.

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **String (Device):**  
`    KEY  EMIT  KEY?  CR  BL  SPACE  SPACES  S"  ."  CHAR  [CHAR]  CMOVE  MOVE  TYPE  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Stack:**  
`    DUP  DROP  SWAP  OVER  ROT  >R  R>  R@  2DROP  2DUP  2OVER  2SWAP  DEPTH  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Flow control:**  
`    IF  ELSE  THEN  BEGIN  WHILE  REPEAT  AGAIN  UNTIL  DO  I  J  LOOP  EXECUTE  +LOOP  UNLOOP  LEAVE  EXIT  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Number to string conversion:**  
`    <#  #  #S  #>  HOLD  SIGN  BASE  HEX  DECIMAL  .  U.  .R  U.R  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Definitions:**  
`    :  ;  CONSTANT  VARIABLE  CREATE  DOES>  VALUE  TO  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Compiling:**  
`    POSTPONE  IMMEDIATE  STATE  RECURSE  [  ]  [']  [CHAR]  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Memory:**  
`    !  C!  @  C@  ,  C,  ALLIGN  CELL+  CHAR+  CELLS  CHARS  CALLIGN  CALLIGNED  2!  2@  ALLIGNED  HERE  CHERE  ALLOT  FILL  ROM!  +!  COUNT  FILL  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Error recovery:**  
`    CATCH  THROW  ABORT"  ABORT  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Arithmetic:**  
`    +  -  *  /  2*  2/  */MOD  MOD  UM*  UM/MOD  S>D  ABS  */  /MOD  1+  1-  FM/MOD  M*  MAX  MIN  NEGATE  FM/REM  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Comparision (Logic):**  
`    0=  =  <  >  AND  OR  XOR  INVERT  TRUE  FALSE  LSHIFT  RSHIFT  U<  0<  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Parsing:**  
`    WORD  PARSE  '  `  

![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Miscellaneous (Tools):**  
`    (  \  .S  WORDS  MS  EVALUATE  ACCEPT  FIND  QUIT  SOURCE  >NUMBER  >BODY  >IN  `  
