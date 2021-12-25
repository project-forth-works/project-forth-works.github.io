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

Now an overview of all the words from **Minimal Forth** & the words we have selected to form **Generic Forth**, please note it is a living list. With good arguments it can be extended. Lines starting with a red dot ![#c53050](https://via.placeholder.com/15/c53050/000000?text=+) are words from Minimal Forth, lines starting with a green dot ![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) are the wordset extension for **Generic Forth**.

**String (Device):**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    KEY  EMIT  KEY?  CR  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    BL  SPACE  SPACES  S"  ."  CHAR  [CHAR]  CMOVE  MOVE  TYPE  `  
**Stack:**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    DUP  DROP  SWAP  OVER  ROT  >R  R>  R@  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    2DROP  2DUP  2OVER  2SWAP  DEPTH  `  
**Flow control:**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    IF  ELSE  THEN  BEGIN  WHILE  REPEAT  AGAIN  UNTIL  DO  I  J  LOOP  EXECUTE  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    +LOOP  UNLOOP  LEAVE  EXIT  `  
**Number to string conversion:**  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    <#  #  #S  #>  HOLD  SIGN  BASE  HEX  DECIMAL  .  U.  .R  U.R  `  
**Definitions:**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    :  ;  CONSTANT  VARIABLE  CREATE  DOES>  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    VALUE  TO  `  
**Compiling:**  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    POSTPONE  IMMEDIATE  STATE  RECURSE  [  ]  [']  [CHAR]  `  
**Memory:**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    !  C!  @  C@  ,  C,  ALLIGN  CELL+  CHAR+  CELLS  CHARS  CALLIGN  CALLIGNED  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    2!  2@  ALLIGNED  HERE  CHERE  ALLOT  FILL  ROM!  +!  COUNT  FILL  `  
**Error recovery:**  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    CATCH  THROW  ABORT"  ABORT  `  
**Arithmetic:**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    +  -  *  /  2*  2/  */MOD  MOD  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    UM*  UM/MOD  S>D  ABS  */  /MOD  1+  1-  FM/MOD  M*  MAX  MIN  NEGATE  FM/REM  `  
**Comparision (Logic):**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    0=  =  <  >  AND  OR  XOR  INVERT  TRUE  FALSE  LSHIFT  RSHIFT  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    U<  0<  `  
**Parsing:**  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    WORD  PARSE  '  `  
**Miscellaneous (Tools):**  
![#c53050](https://via.placeholder.com/15/c53050/000000?text=+)
`    (  \  .S  WORDS  `  
![c5f015](https://via.placeholder.com/15/c5f015/000000?text=+)
`    MS  EVALUATE  ACCEPT  FIND  QUIT  SOURCE  >NUMBER  >BODY  >IN  `  
