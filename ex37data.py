keyword_list = [
    ('and',         "Boolean operator for AND",     ("",)),
    ('del',         "Deletes an item from memory",          ("del foo[4]",)),
    ('from',        "Keyword used in import statements",    ("from sys import argv",)),
    ('not',         "Boolean operator for NOT",          ("",)),
    ('while',       "Indicates the beginning of a while-loop",      ("",)),
    ('as',          "Designate new names for imported modules",         ("from sys import argv as argument_variables",)),
    ('elif',        "Else-if instruction, for branching more than one option in an if statement.",       ("",)),
    ('global',      "Allows you to set a variable to be global from inside a function (or anywhere that the variable would not normally be global)",         ("(i.e. global me = \"locally defined\" )",)),
    ('or',          "Boolean operator for OR",      ("",)),
    ('with',        "Creates an object from an unmanaged resource, and iterated against it.  It's a special kind of loop that opens and closes the file automagically",        ("with A() as a:","\tdo something",)),
    ('assert',      "Used to verify the state of the variables in the program, essentially if the assert statement is False it will throw an AssertionError",       ("max = 0","if a < b:","\tmax = b","if b > a:","\tmax = a","assert (max == a or max ==b) and max >= a and max >= b",)),
    ('else',        "Final statement in an if-statement, acting as a catch-all for anything didn't find a True condition in one of the if or elif branches.",       ("",)),
    ('if',          "Indicates an if statement.",       ("if a == b:", "\tdo something",)),
    ('pass',        "Does nothing. Is useful to put in code blocks where something is required syntactically, but no actions need to be performed.  Is also useful as a placeholder while writing code allowing for structure without requiring content.",      ("",)),
    ('yield',       "Is used to return a generator statement (that is, an iterable object which can only be used once and is not stored in memory, so the list can be exceptionally long.  There is a great explanation on StackOverflow of what it is and how to use it.",     ("",)),
    ('break',       "Is used to end a loop.",       ("while True:","\tbreak",)),
    ('except',      "Deals gracefully with error messages.  Instead of crashing the program immediately, \"except\" allows for catching the Exception, and returning an error message to the user.",        ("(i.e. while True:","\ttry:","\t\tx = int(raw_input(\"Please enter a number: \"))","\t\tbreak","\texcept (ValueError, TypeError):","\t\tprint \"Oops!  That was not a valid number.  Try again...\"",)),
    ('import',      "Used when importing other modules for use in a particular piece of code.",     ("from sys import argv as argument_variables",)) ,
    ('print',       "Prints whatever.",     ("",)),
    ('class',      "Begins the definition of a class ",         ("",)),
    ('exec',      "Allows python code to be run from a string",        ("exec \"x=23\"",)) ,
    ('in',      "Part of a for loop",        ("For line in file:","\tdo something",)) ,
    ('raise',      "Can manually raise exceptions with custom error messages",        ("try","\traise NameError('HiThere')","except NameError:","\tprint \'an exception flew by!\'","\traise",)) ,
    ('continue',      "Returns to the top of the loop and runs with the next iteration.  It's kind of like pass, except that it can only be used in loops, and it will not execute the remainder of the loop, while pass will.",        ("",)),
    ('finally',      "Adds \'footer code\' to the bottom of a try block, so no matter what happens this code gets run at the end",        ("try:","\tf = file(\'poem.txt\')","\tprint f.readline()","finally:","\tf.close()",)),
    ('is',      "Tests for IDENTITY, not equality of two objects.  Essentailly it says \"Do I have two names for the same object?\"",        ("a is b",)),
    ('return',      "Specifies the statement to be returned by a function",        ("x = 15","return x",)),
    ('def',      "Indicates the definition of a function",        ("def my_function(**args):",)),
    ('for',      "Indicates the start of a for loop",        ("for line in file:","\tdo something",)),
    ('lambda',      "A shortcut for creating anonymous, one-time, single-expression functions which return a value.  It's a kind of shorthand for the \'def\' statement",        ("sum = lambda x ,y : x + y",)) ,
    ('try',      "Starts a try/except/finally statement",        ("try:","\tdo something","except TypeError:","\tprint \"Oops, something hs gone wrong\"","finally:","\tdo something else",)) ,
]   

data_type_list = [
    ('True',       "Boolean value for True.  Everything that isn't False is True.",       ("",)),
    ('False',       "Boolean value for False.  Other possible things that evaluate to False are: None, any 0 (i.e. 0, 0.00, 0L, 0j), any empty sequence (i.e. [],(),""), any empty mapping {}, instances of user-designed classes.",       ("",)),
    ('None',       "False",       ("",)),
    ('strings',       "Strings are arrays of characters, indicated by sets of \"quotation marks\" or 'like this'",       ("",)),
    ('numbers',       "Numbers are integer numbers.",       ("",)),
    ('floats',       "Floats are degimal numbers",       ("",)),
    ('lists',       "Lists are arrays, and are indicated by []",       ("",)),
]

escape_sequence_list = [
    ('\\\\',       "Allows a \\ Character to appear inside a string instead of being an escape character",       ("",)),
    ('\\\'',       "Allows a ' within a string that's closed by \'s if necessary",       ("",)),
    ('\\\"',       "Allows a \" within a sthing that slosed by \"s if necessary",       ("",)),
    ('\\a',       "ASCII Bell (BEL)",       ("",)),
    ('\\b',       "ASCII Backspace (BS)",       ("",)),
    ('\\f',       "ASCII Formfeed (FF)",       ("",)),
    ('\\n',       "Inserts a newline character",       ("",)),
    ('\\r',       "ASCII Carriage Return (CR)",       ("",)),
    ('\\t',       "Inserts a tab character",       ("",)),
    ('\\v',       "ASCII Vertical Tab (VT)",       ("",)),
]

string_format_list = [
    ('%d',       "Allows for an integer to be inserted into the string. Signed integer decimal.",       ("",)),
    ('%i',       "Signed integer decimal.",       ("",)),
    ('%o',       "Unsigned octal.",       ("",)),
    ('%u',       "Unsigned decimal.",       ("",)),
    ('%x',       "Unsigned hexadecimal, lowercase.",       ("",)),
    ('%X',       "Unsigned hexadecimal, uppercase.",       ("",)),
    ('%e',       "Floating point eponential, lowercase.",       ("",)),
    ('%f',       "Floating point exponential, uppercase.",       ("",)),
    ('%g',       "Floating point, varying display.",       ("",)),
    ('%G',       "Floating point, varying display.",       ("",)),
    ('%c',       "Singel character.",       ("",)),
    ('%r',       "Uses repr() to turn any object into a sthing to embed in the output stream as a string encapsulated by 's",("",)),
    ('%s',       "Allows for a string to be inserted into the string.",       ("",)),
    ('%%',       "Nothing.  This allows for a % sign to show up in text",       ("",)),
]

operator_list = [
    ('+',       "Addition",       ("",)),
    ('-',       "Subtraction",       ("",)),
    ('*',       "Multiplication",       ("",)),
    ('**',       "Exponents",       ("",)),
    ('/',       "Division",       ("",)),
    ('//',       "Floor division (integer division, done by dividing, then applying the Math.floor() method to the quotient.",       ("",)),
    ('\%',       "Modulo Division (returns remainder of equation)",       ("",)),
    ('<',       "Less Than",       ("",)),
    ('>',       "Greater Than",       ("",)),
    ('<=',       "Less Than or Equal To",       ("",)),
    ('>=',       "Greater Than or Equal To",       ("",)),
    ('==',       "Equals (checks for equality)",       ("",)),
    ('!=',       "Does not equal",       ("",)),
    ('<>',       "Does not equal",       ("",)),
    ('()',       "Many applications, commonly used in tuples, functions, and mathermatical operations",       ("",)),
    ('[]',       "Used in array creation and retrieval",       ("",)),
    ('{}',       "Creates an empty hash/dict",       ("",)),
    ('@',       "Decorator expression",       ("",)),
    (',',       "list separator",       ("",)),
    (':',       "Indicates the start of a definition, object, function, dict, etc..",       ("",)),
    ('.',       "Most often seen in dot notation of Object.methods",       ("",)),
    ('=',       "Equals (assigns object/value on right to object/variable on left)",       ("",)),
    (';',       "End of code line",       ("",)),
    ('+=',       "Increment variable",       ("",)),
    ('-=',       "Decrement variable",       ("",)),
    ('*=',       "Multiply variable",       ("",)),
    ('/=',       "Divide variable",       ("",)),
    ('//=',       "floor divide variable",       ("",)),
    ('%=',       "Modulo variable",       ("",)),
    ('**=',       "Variable to the power of...",       ("",)),
]
itertools_list = [
    # Infinite iterators
    ('count(start[, step])',       "Infinite counting upwards from start by multiples of step.",       ("",)),
    ('cycle(p)',       "Infinite repetition of p, character by character",       ("",)),
    ('repeat(p[,n])',       "Infinite repetition of p as a whole, or until n number of repetitions",       ("",)),
    # Finite Iterators
    ('chain(p, q, ...)',       "Lists contents of all items by character",       ("",)),
    ('compress(data, selectors)',       "Return sequence redced according to selectors.",       ("compress('ABCDEF',[1,0,1,0,1,1])",">> A C E F",)),
    ('dropwhile(pred, seq)',       "Display sequence starting when the predicate function (pred) fails",       ("dropwhile(lambda x: x<5, [1,4,6,4,1])",">> 6 4 1",)),
    ('groupby(iterable[keyfunction])',       "sub-iterators grouped by value of keyfunction(v)",       ("",)),
    ('ifilter(pred, seq)',       "Shows elements of seq where pred is True",       ("ifilter(lambda x: x%2, range(10))",">> 1 3 5 7 9",)),
    ('ifilterfalse(pred, seq)',       "elements of seq where pred is False",       ("ifilterfalse(lambda x: x%2, range(10))",">> 0 2 4 6 8",)),
    ('islice(seq, [start,] stop[, seq]),',       "Slices seq from start:stop by step.",       ("",)),
    ('imap(func, p, q, ...)',       "Maps a function to be repeated mutiple times, each p, q, is a new set of amounts for one variable fed into func",       ("imap(pow, (2,3,10), (5,2,3)",">> 32 9 1000",)),
    ('starmap(func, seq)',       "Maps a functions to be repeated multiple times, each p, q, is a new set of variables fed into func.",       ("starmap(pow, [(2,5),(3,2),(10,3)])",">> 32 9 1000",)),
    ('tee(it, n)',       "splits one iterator (it) into n",       ("",)),
    ('takewhile(pred, seq)',       "Opposite of dropwhile, returns seq until pred fails",       ("takewhile(lambda x: x<5, [1,4,6,4,1])",">> 1 4",)),
    ('izip(p, q, ...)',       "Crosses p, q, in a zipper fashion, as long as each set has items to use",       ("izip('ABCD','xy')",">> Ax By",)),
    ('izip_longest(p, q, ...[, fillvalue=\'-\'])',       "Crosses p, q, in a zipper fashion, filling in missing values with the fillvalue.",       ("izip_longest('ABCD','xy', fillvalue='-')",">> Ax By C- D-",)),
    # Combinatoric Generators
    ('product(p,q[,repeat])',       "cartesian procust, equivalent to a nested for-loop",       ("product('ABCD', repeat=2)",">> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD",)),
    ('permutations(p[, r])',       "r-length tuples of all possible orderings, no repeated elements",       ("permutations('ABCD', 2)",">> AB AC AD BA BC BD CA CB CD DA DB DC",)),
    ('combinations(p, r)',       "r-length tuples, in sorted order, no repeated elements",       ("combinations('ABCD', 2)",">> AB AC AD BC BD CD",)),
    ('combinations_with_replacement(p, r)',       "r-length tuples, sorted in order, with repeated elements",       ("combinations_with_replacement('ABCD', 2)",">> AA AB AC AD BB BC BD CC CD DD",)),
    ('del',         "Deletes an item from memory",          ("del foo[4]",)),
]

definition_list = [
    "Keyword",
    "Operator",
    "Data Type",
    "String Format",
    "Escape Sequence",
    "Itertools",
]
