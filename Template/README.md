# Template for a new idea called «name»

## «name» idea

*Explain in a few words what the idea of this description is.*
*The reader should understand what this is about so that s/he can decide whether or not it is worthwhile to continue reading.*

*What is the problem. How is the problem solved?*

*Continue also to explain background information and the idea proper. Is there a trick?* 

## Implementation

*Discuss a typical (possibly naïve) implementation that best allows to understand the implementation.* 
*More sophisticated/optimized implementations can be presented later. Most system specific implementations will be optimized.*

## Implementation in pseudo code

*Use pseudo code following this style:
```
Function: «name» ( input parameters -- results )
  «prose text descripting operations in this function»
 
  Set «variable» to «description of value»
  «imperative subject object ...»
  
  IF «condition»:
     ...
  ELSE:
     ...
  
  WHILE «condition»:
     ...
```
*For defining words use:*
```
Function  
	Define: ( u -- )
		Reserve RAM space 
		allocate ROM space 
	Action: ( -- a )
		Leave start address of this 
```

## Minimal Forth implementation:

*Try to implement the pseudo code using the words in [Minimal Forth](http://www.euroforth.org/ef15/papers/knaggs.pdf) mentioning and explaining all additional words that
your implementation requires*

*Also show how your implementation is used by giving some examples.*


## Various other Implementations

*Present additional (possibly more sophisticated) implementations, e.g for a specific microcontroller boards, a specific Forth system or in Standard Forth.*
*Try to state precisely what implementations you present and what requirements they have. No need to be portable here: Embrace the difference*

## Background information and possible Pitfalls

*Please give references to data sheets, background articles or articles for follow up reading.*

*Please also describe any problems that can occur related to the idea that you describe.*  
*What were stumbling stones, what issues are important for others to know?*


--- 

For a simple example idea have a look at [The DUMP utility](https://github.com/embeddingforth/embeddingForth/tree/main/System-Software/dump).