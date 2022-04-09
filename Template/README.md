# Template for a new idea called «name»

## «name» idea

Explain in a few words what the idea of this description is.
The reader should understand what this is about so that s/he can decide whether or not it is worthwhile to continue reading.

What is the problem. How is the problem solved?

Continue also to explain background information and the idea proper. Is there a trick? 

## Implementation

Discuss a typical (possibly naïve) implementation that best allows to understand the implementation. 
More sophisticated/optimized implementations can be presented later. Most system specific implementations will be optimized.

## Implementation in pseudo code

*Use pseudo code following this style:*
```
Function: «name» ( input parameters -- results )
  «prose text descripting operations in this function»
 
  Set «variable» to «description of value»
  «imperative subject object ...»
  
  IF: «condition»:
     ...
  ELSE:
     ...
  
  WHILE: «condition»:
     ...
```
*For defining words use:*
```
Function:  
	Define: ( u -- )
		Reserve RAM space 
		allocate ROM space 
	Action: ( -- a )
		Leave start address of this 
```

## Generic Forth implementation:

Try to implement the pseudo code using the words in [Generic Forth](https://github.com/project-forth-works/project-forth-works.github.io/blob/main/minimalforth.md) and the words listed in the file [well-known-words](https://github.com/project-forth-works/project-forth-works.github.io/blob/main/well-known-words.txt), 
mentioning and explaining all other additional words that your implementation requires.  
Hardware details may come to the surface, but minimise them!

*Also show how your implementation is used by giving some examples.*


## Various other Implementations

Present additional (possibly more sophisticated) implementations, e.g for a specific microcontroller board, a specific Forth system or in Standard Forth.
Try to state precisely what implementations you present and what requirements they have. No need to be portable here: *Embrace the difference*

## Background information and possible Pitfalls

Please give references to data sheets, background articles or articles for follow up reading.
Also describe any problems that may arise in connection with the idea you are describing.  
What were stumbling blocks, what things are important for others to know?

--- 

For a simple example idea have a look at [The DUMP utility](https://github.com/project-forth-works/project-forth-works/tree/main/Programming-Tools/dump).
