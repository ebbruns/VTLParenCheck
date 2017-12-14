----------------
|Run it Online!|
----------------

https://repl.it/@ebbruns/VTL-ParenCheck

---------------
|VTLParenCheck|
---------------
Written by Evan Bruns

Helps fix typos in the Velocity Template Language by telling the user where parenthesis, curly brackets and square brackets do not match.
Currently looks at number of opens/closes per line and order within to look at the order of matches rather than just the number of opening and closing symbols.
Also "fails fast" on a given line if a closing symbol is noticed before any opening symbols of the same type.

Potential future improvements include looking for problems like this one: {(}) , which would currently not be detected.
I also hope to better support people who choose to put enclosures across multiple lines (although this is rarely done in production-quality Velocity code).
Additionally, I'd like to add slightly more verbose descriptions of errors.
