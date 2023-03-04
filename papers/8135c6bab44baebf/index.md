vim: filetype=markdown :

 - [Engineering a Compiler](./engineering_a_compiler.pdf)
 - [Crafting Interpreter](./crafting-interpreters.pdf)
 - [Modern Compiler Implementation in C](./modern_compiler_implementation.pdf)
 - [Types and Programming Languages](types_and_programming_languages.pdf)
 - [An Incremental Approach to Compiler Construction](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf)
 - Friendman series [The little schemer](./the_little_schemer.pdf), the reasoned schemer the little typer
 - [Art of Intel x86 Assembly](https://archive.org/details/ArtOfIntelX86Assembly)
 - https://github.com/pfalcon/ssabook
 - More links: https://github.com/MattPD/cpplinks/blob/master/compilers.md#books, https://gist.github.com/MattPD/00573ee14bf85ccac6bed3c0678ddbef#program-analysis-resources
 - Architecture: [computer architecture books](https://github.com/MattPD/cpplinks/blob/master/comparch.md#books)
 - Cornell CS 6120: Advanced Compilers - The Self-Guided Online Course - Adrian Sampson (great lecturer, interesting selection of topics--including LLVM, dynamic compilers, and program synthesis--not frequently seen together in a single course)
 - IU P423/P523: Compilers (Programming Language Implementation) - Jeremy Siek, with the course book "Essentials of Compilation: An Incremental Approach" (pretty interesting approach, with programming language features developed incrementally having a fully working compiler at each step, cf. <http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf>; implementation language Racket),
 - KAIST CS420: Compiler Design - Jeehoon Kang (good modern treatment of SSA representation itself, including the use of block arguments, <https://mlir.llvm.org/docs/Rationale/Rationale/#block-arguments-vs-phi-nodes>, as well as SSA-based analysis and optimization; Rust as an implementation language),
 - UFMG DCC888: Static Program Analysis - Fernando Magno Quintão Pereira (a more advanced course particularly relevant for the middle-end optimizations as well select backend topics: really good SSA coverage--the lecturer has done some great research in this area--and even includes modern topics relevant for SIMD optimizations or GPU compilers like divergence analysis)
 - UCSD CSE 131: Compiler Construction - Joseph Gibbs Politz, Ranjit Jhala (great lecturers, both Haskell and OCaml edition were interesting; fun extra: one of the Fall 2019 lectures (11/26) has an interesting discussion of the trade-offs between traditional OOP and FP compiler implementation),
 - UCSD CSE 231: Advanced Compiler Design - Sorin Lerner (after UCSD CSE 131: for more on analysis & optimization--data flow analysis, lattice theory, SSA, optimization; fun extra: the final Winter 2018 lecture highlighted one of my favorite papers, <https://pldi15.sigplan.org/details/pldi2015-papers/31/Provably-Correct-Peephole-Optimizations-with-Alive>),
 - UW CSE CSEP 501: Compilers - Hal Perkins (nice balanced introduction, including x86-64 assembly code generation, with the aforementioned "Engineering a Compiler" used as the course textbook).
 - Dragon Book - Compilers: Principles, Techniques, and Tools

# Book recommendations after reading “crafting interpreters”

[Discussion](http://old.reddit.com/r/ProgrammingLanguages/search?q=flair_name%3A%22Discussion%22&restrict_sr=1)

Hello, I finished the book crafting interpreters by Robert Nystrom. The book
has helped me alot and felt like an amazing introduction to the field of
language design and implementation.

 > Crafting interpreters has a very nice cover, I should read it at some point
 > Perhaps looking for the author Robert Nystrom also makes sense

My question however is: what next to read? I know of the dragon book and have
read the first couple of chapters. But maybe there are better alternatives.
Also, after crafting interpreters, i have a basic understanding of interpreted
language design. However, I have the urge to study compiler design.

So are there any books you would recommend me for my level of knowledge?


From what I remember, the book "Engineering a Compiler" goes over pretty much
every part of a compiler (and you can probably skip the lexer/parser chapters
since they'll probably duplicate much of "Crafting Interpreters"). There are
some books specific to type theory if you want to learn more about that as
well, "Types and Programming Languages", and the "advanced" sequel. If you're
looking for something more like "Crafting an Interpreter", there may be other
books (I think "Modern Compiler Implementation in Java" or "in C" or "in ML"
by Appel). I wasn't a huge fan of the Appel book in Java when I first read it
though, but I can't remember why.

Excellent, thank you! I had my eye on "Engineering a Compiler" I saw a third
edition will be released. So I think I'm gonna wait for that.

The lexing/parsing is actually super different between the two books, so I
think even that section would be an interesting dive into theory that isn’t in
“Crafting Interpreters”. I agree good recommendation!

There are the writing an interpreter/compiler in go books by Thorsten Ball

I’ve been curious to read this books, but I would like to know how it differs
from crafting interpreters.

You can also read through [An Incremental Approach to Compiler Construction](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf) to learn about compiling an AST to assembly.

 > agumonkey

I only skimmed through some but there's:

  * brown edu PLAI (online)

  * anatomy of lisp, allen

  * lisp in small pieces, queinnec

  * appel, modern compiler in ml (exists also in C and Java but people say the ports are not as great)

ps: if I may add, Friendman series The little schemer, the reasoned schemer,
the little typer are also very enlightening (if you can fathom the socratic
discourse style)

Thank you for the suggestions, I will look into them. I have never used lisp
but see it talked about often. Why did you recommend lisp sources?

Also would you recommend "Engineering a Compiler" by Keith Cooper?

 _Engineering a Compiler_ is a good choice for the next step in my view, it includes SSA and other foundations for code improvement. And if you want to know more about the Type System or programming theory, a good choice may be is [Software Foundations](https://softwarefoundations.cis.upenn.edu/). And, I think you need to read the [LLVM tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html) if possible.

If you already did, nevermind, look at other comments :) but make a bunch of
tiny languages, maybe all unfonished, not working, it doesnt really matter!
you will learn _a lot_ just with that :)

Types and Programming Languages. Not directly related to compiler design, but
having solid fundamentals of type systems will make your life easier!

One important thing to realize is that if you've built out the CLox
interpreter in _Crafting Interpreters_ , **you 've built a compiler**.

From the outside, this looks like an interpreter because it's compiling to a
bytecode which is only runnable via the virtual machine you build from the
book, and then the bytecode is lost after you finish running, because it's
only stored in memory. But if instead of running the bytecode, you stored it
to a file (similar to a .jar, for example) and then separated out the VM and
made it load bytecode from the file, that would make it visible that you're
actually compiling, without fundamentally changing much of the implementation.

The biggest difference between this and a more common conception of a compiler
is actually **what is generated** ; this compiler generates CLox bytecode,
whereas a more common conception of a compiler would generate something like
x64 assembly or LLVM assembly.

So the biggest gap in your knowledge after reading _Crafting Interpreters_ is probably assembly. As such, I'd point you to [My First Language Frontend with LLVM](https://www.llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html) (skip to chapter 3, you already know how to lex/parse from _Crafting Interpreters_ ) or [Art of Intel x86 Assembly](https://archive.org/details/ArtOfIntelX86Assembly) (avoid the "modernized" _Art of Assembly Language_ which teaches you "High Level Assembler", which is neither high level nor assembler). The LLVM route is probably more applicable to modern general-purpose language compilers, but the x86/x64 route is probably better for learning actual assembly, and techniques from that will be portable to other assemblies without relying on LLVM or similar tools.

Thank you! I guess assembly is really what I want to learn as well. The Clox
bytecode VM is also stack based, and while that has a very interesting way of
working, I guess I would also want to know how a register based CPU works (or
any other architecture for that matter).

I am running an AMD chip, so is the Art of interl x86 assembly book
recommended for that?

Compilers Books

I'd indeed start with "Engineering a Compiler" by Keith Cooper and Linda
Torczon. I also like "Modern Compiler Design" by Dick Grune, Kees van
Reeuwijk, Henri E. Bal, Ceriel J.H. Jacobs, and Koen G. Langendoen
(<https://dickgrune.com/Books/MCD_2nd_Edition/>). Some chapters are better in
one than the other, so you may read some of both to see if you like another
explanation.

For more on the analysis & compiler optimization side, "SSA-based Compiler
Design" is a good follow-up (original URL (inactive):
<http://ssabook.gforge.inria.fr/latest/>; GitHub Mirror:
<https://github.com/pfalcon/ssabook>, PDF:
<https://pfalcon.github.io/ssabook/latest/>; to be published in 2022:
<https://link.springer.com/book/9783030805142>).

Further readings: Book recommendations in
<https://github.com/MattPD/cpplinks/blob/master/compilers.md#books> as well as
program analysis resources (in particular lattice theory, type systems and
programming languages theory, related notation):
<https://gist.github.com/MattPD/00573ee14bf85ccac6bed3c0678ddbef#program-analysis-resources>

If you're interested in computer architecture background (relevant for the back-end optimizations), see [computer architecture books](https://github.com/MattPD/cpplinks/blob/master/comparch.md#books) & [computer architecture courses](https://github.com/MattPD/cpplinks/blob/master/comparch.md#courses). Personally I'd definitely recommend Prof. Onur Mutlu's Lecture Videos and Materials - <http://people.inf.ethz.ch/omutlu/lecture-videos.html> \- fantastic lecturer and more up-to-date than textbooks (e.g., branch prediction lectures discussed modern TAGE and neural network predictors a few years before they've been implemented in, say, <https://en.wikichip.org/wiki/amd/microarchitectures/zen_2#Branch_Prediction_Unit>; in contrast, most textbooks stop at the level of two-level / saturating bits BPs from the early 1990s).

The CS 6120 course (see below) blog is a great resource for writeups on
techniques and papers:
<https://www.cs.cornell.edu/courses/cs6120/2020fa/blog/>

Compilers Courses

I can recommend the following:
<https://github.com/MattPD/cpplinks/blob/master/compilers.md#courses>

Particularly (in alphabetical order--I think these are all great, so including
highlights of what I've liked about them):

  * Cornell CS 6120: Advanced Compilers - The Self-Guided Online Course - Adrian Sampson (great lecturer, interesting selection of topics--including LLVM, dynamic compilers, and program synthesis--not frequently seen together in a single course)

  * IU P423/P523: Compilers (Programming Language Implementation) - Jeremy Siek, with the course book "Essentials of Compilation: An Incremental Approach" (pretty interesting approach, with programming language features developed incrementally having a fully working compiler at each step, cf. <http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf>; implementation language Racket),

  * KAIST CS420: Compiler Design - Jeehoon Kang (good modern treatment of SSA representation itself, including the use of block arguments, <https://mlir.llvm.org/docs/Rationale/Rationale/#block-arguments-vs-phi-nodes>, as well as SSA-based analysis and optimization; Rust as an implementation language),

  * UFMG DCC888: Static Program Analysis - Fernando Magno Quintão Pereira (a more advanced course particularly relevant for the middle-end optimizations as well select backend topics: really good SSA coverage--the lecturer has done some great research in this area--and even includes modern topics relevant for SIMD optimizations or GPU compilers like divergence analysis)

  * UCSD CSE 131: Compiler Construction - Joseph Gibbs Politz, Ranjit Jhala (great lecturers, both Haskell and OCaml edition were interesting; fun extra: one of the Fall 2019 lectures (11/26) has an interesting discussion of the trade-offs between traditional OOP and FP compiler implementation),

  * UCSD CSE 231: Advanced Compiler Design - Sorin Lerner (after UCSD CSE 131: for more on analysis & optimization--data flow analysis, lattice theory, SSA, optimization; fun extra: the final Winter 2018 lecture highlighted one of my favorite papers, <https://pldi15.sigplan.org/details/pldi2015-papers/31/Provably-Correct-Peephole-Optimizations-with-Alive>),

  * UW CSE CSEP 501: Compilers - Hal Perkins (nice balanced introduction, including x86-64 assembly code generation, with the aforementioned "Engineering a Compiler" used as the course textbook).

Thank you so much! The amount of resources that you and others have
recommended will keep me busy for the next few years

I loved the dragon book. I’ve heard it’s a little bit outdated, but the
theoretical concepts are still true. The fundamental grammar and regex
structures are true, and the code gen and optimization stuff haven’t become
false.
