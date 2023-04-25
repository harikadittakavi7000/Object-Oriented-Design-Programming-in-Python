## Object Oriented WordProcessor/Text Editor

- This  word processor uses objects to represent characters.
- One reason word processor represent characters as objects is that they use the Composite pattern to represent the contents of a document. 
- The goal is to use Flyweight Design Pattern to save space.
 
This implementation shows the use of following Design Patterns:
 - ***Flyweight Design Pattern***
      - The Flyweight is used to save space. Here, Flyweights are characters. 
      
 - ***Factory Design Pattern***
     - Flyweight factory is implemented which takes an unicode code point (a char in Java) returns the Flyweight character object for the character. 
     - In this factory the input will be a triple:
          - The font name (Times, Courier, etc), point size (12, 13, etc) and style (bold, italic, underline etc). 
                  
 - ***Composite Design Pattern***
     - To represent the contents of a document.
 
 ### Run Array
 
    - For the Character Flyweight to work we store the extrinsic state of the character objects, that is the font information. For this RunArray is used. 
    - A RunArray keeps track of runs in a sequence. 
    - For example :
            - If we have a document that starts with 250 characters in font A, then has 10 characters in font B and finally 320 characters in font A. The RunArray store the runs: 250, 10 and 320. It also store the font i.e associated with each run. Given any index (0 to 579 or 1 to 580) the run array will return the font used by the character in that location of the document. So give index 12 the RunArray will return Font A,  given the index 255 will return Font B. When adding runs to the RunArray one needs to indicate the index the run starts at, the length of the run and the value at the run array. 
            
            - So for the current example we might have:
                   RunArray test = new RunArray();
                   test.addRun(0, 250, fontA);
                   test.addRun(250, 10, fontB);
                   test.appendRun(320, fontA);
                   
            - If the run is appended the run array can determine the start index of the run.
            