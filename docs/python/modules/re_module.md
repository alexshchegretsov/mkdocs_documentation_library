`re`
==


raw strings(сырые строки) - строки, в которых не работает экранирование
при помощи `\` и сам символ `\` интерпретируется как символ в строке.

```
>>> print("\tTab")
        Tab
>>> print(r"\tTab")
\tTab
>>>
```
This module exports the following functions:

- `match` - Match a regular expression pattern to the beginning of a string.
```
# start strig with 3 character
>>> re.match(r"\w{3}", "wre ty")
<_sre.SRE_Match object; span=(0, 3), match='wre'>

# start string with 2 character
>>> re.match(r"\w{3}", "wr ty")

```
- `fullmatch` - Match a regular expression pattern to all of a string.
```
# only full occurence
>>> re.fullmatch("\w{4}\s\d{2}", "sAaq 22")
<_sre.SRE_Match object; span=(0, 7), match='sAaq 22'>

# remove whitespace from string
>>> re.fullmatch("\w{4}\s\d{2}", "sAaq22")
```
- `search` - Search a string for the presence of a pattern.
```
>>> re.search(r"spam", "some spamming today")
<_sre.SRE_Match object; span=(5, 9), match='spam'>
```
- `sub` - Substitute occurrences of a pattern found in a string.
```
>>> re.sub(r"spam", "x", "spamspamspamn")
'xxxn'
```
- `subn` - Same as sub, but also return the number of substitutions made.
```
>>> re.subn(r"spam", "x", "spamspamspamn")
('xxxn', 3)
````
- `split` - Split a string by the occurrences of a pattern.
```
# split by "so", "me", "fo", "12"
>>> re.split("\w{2}", "some ( foo [124")
['', '', ' ( ', 'o [', '4']
```
- `findall` - Find all occurrences of a pattern in a string.
```
>>> re.findall("\w{2}", "some ( foo [124")
['so', 'me', 'fo', '12']
```
- `finditer` - Return an iterator yielding a match object for each match.
```
>>> a = re.finditer("\w{2}", "some ( foo [124")
>>> a
<callable_iterator object at 0x7f3ac9493b70>
>>> next(a)
<_sre.SRE_Match object; span=(0, 2), match='so'>
>>> next(a)
<_sre.SRE_Match object; span=(2, 4), match='me'>
>>> next(a)
<_sre.SRE_Match object; span=(7, 9), match='fo'>
>>> next(a)
<_sre.SRE_Match object; span=(12, 14), match='12'>
>>> next(a)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    next(a)
StopIteration
```
- `compile` - Compile a pattern into a RegexObject.
```
>>> p=re.compile("^\w{2}\.")
>>> p.findall("23. err. er.")
['23.']

```
- `purge` - Clear the regular expression cache.
- `escape` - Backslash all non-alphanumerics in a string.



special characters:

- `.` - any character except new line
- `^` - matches beginning of string and after each line break
- `$` 0 matches end of string and before each line break
- `[5ab]` - matches either "5" or "a" or "b"
- `[0-9a-z]` - matches any from "0" to "9" and from "a" to "z"
- `[^abc]` - matches EXCEPT "a", "b", "c"
- `R|S` - matches either `R` or `S` regex pattern
- `()` - create a capture group

special sequences:

- `\d` - any digit (0-9)
- `\D` - not a digit (0-9)
- `\w` - any alphabetically symbol  [A-Za-z]
- `\W` - any non alphabetically symbol
- `\s` - whitespace
- `\S` - non whitespace
- `\A` - matches only at the start of the string
- `\Z` - matches the end of the string
- `\b` - matches the empty string at the beginning or at the end of the word
- `\B` - matches characters inside word, not at word boundary

```
# \b
>>> re.findall(r"\b\w{3}\b", "And a day will be light and productive")
['And', 'day', 'and']

>>> re.findall(r"\bpython\b", "python")
['python']
>>> re.findall(r"\bpython\b", "python3")
[]
>>>

# \B
>>> re.findall(r"\Bth\B", "python")
['th']
>>>
```

quantifiers:

- `*` - 0 or more (append ? for non-greedy)
- `+` - 1 or more (append ? for non-greedy)
- `?` - 0 or 1 (append ? for non-greedy)
- `{10}` - 10 occurences
- `{1,4}` - from 1 to 4 occurences
- `{,4}` - from 0 to 4 occurences
- `{4,}` - from 4 to infinity occurences


groups:

- (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
- (?:...)  Non-grouping version of regular parentheses.
- (?P<name>...) The substring matched by the group is accessible by name.
- (?P=name)     Matches the text matched earlier by the group named name.
- (?#...)  A comment; ignored.
- (?=...)  Matches if ... matches next, but doesn't consume the string.
- (?!...)  Matches if ... doesn't match next.
- (?<=...) Matches if preceded by ... (must be fixed length).
- (?<!...) Matches if not preceded by ... (must be fixed length).
- (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.

lazy vs greedy
=

```
# greedy
>>> re.findall(r"<.+>", "<i>Hello world</i>")
['<i>Hello world</i>']

# lazy
>>> re.findall(r"<.+?>", "<i>Hello world</i>")
['<i>', '</i>']
>>>

You may think that <.+> (. means any non newline character 
and + means one or more) would only match the <em> and the </em>, 
when in reality it will be very greedy, 
and go from the first < to the last >. 
This means it will match <em>Hello World</em> instead of what you wanted.
Making it lazy (<.+?>) will prevent this. By adding the ? after the +, 
we tell it to repeat as few times as possible, 
so the first > it comes across, is where we want to stop the matching.
```

