# Regular expressions in Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/regular-expressions-in-looker-studio

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Alternatives to using regular expressions
  * Regular expression examples
  * Metacharacters
    * Character classes
  * Tips
    * Use simple expressions
    * Case-sensitivity
    * Escaping a backslash character




Was this helpful?
Send feedback 
#  Regular expressions in Looker Studio
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Alternatives to using regular expressions
  * Regular expression examples
  * Metacharacters
    * Character classes
  * Tips
    * Use simple expressions
    * Case-sensitivity
    * Escaping a backslash character


A regular expression (regexp) is a specific sequence of characters that broadly or narrowly matches patterns in your data. You can use regular expressions to create more flexible filters in charts and controls. You can also use the following regular expression functions in calculated field formulas:
Function | Description  
---|---  
`REGEXP_CONTAINS` |  Returns true if the input value contains the regular expression pattern, otherwise returns false.  Learn more about `REGEXP_CONTAINS`.  
`REGEXP_EXTRACT` |  Returns the first matching substring in the input value that matches the regular expression pattern.  Learn more about `REGEXP_EXTRACT`.  
`REGEXP_MATCH` |  Returns true if the input value matches the regular expression pattern, otherwise returns false.  Learn more about `REGEXP_MATCH`.  
`REGEXP_REPLACE` |  Replaces all occurrences of text that match the regular expression pattern in the input value with the _replacement_ string.  Learn more about `REGEXP_REPLACE`.  
## Alternatives to using regular expressions
Constructing regular expressions can be complex. Before using a regexp function, consider whether using a simpler text function will achieve your goal. The following functions provide regular expression-like functionality without requiring you to know regexp syntax.
Function  |  Description   
---|---  
Returns true if the specified text is found in the field or expression, otherwise returns false.   
Returns true if the field or expression ends with the specified text, otherwise returns false.   
Returns a number of characters from the beginning of a specified string.   
Returns a copy of the original text with all occurrences of the search text substituted with the replacement text.   
Returns a number of characters from the end of a specified string.   
Returns true if the field or expression begins with the specified text, otherwise returns false.   
Returns text with leading and trailing spaces removed.   
## Regular expression examples
**Matches if MyField contains space characters:**
`REGEXP_CONTAINS(MyField, "\\s+")`
**Extracts the top-level directory in a URL:**
`REGEXP_EXTRACT(URL, `^https://[^/]+/([^/]+)/`)`
For example, if the `URL` field contained this page's address, the previous function would return `looker-studio`.
Categorize ad campaigns by language:
```
CASE
WHENREGEXP_MATCH(Campaign2,R".*\|\s*en\s*\|.*")then"English"
WHENREGEXP_MATCH(Campaign2,R".*\|\s*es\s*\|.*")then"Spanish"
ELSE"Other language"
END

```

For example, applying this regular expression to the _Campaign_ dimension in the Google Analytics Demo account gives these results:
Campaign  |  Language   
---|---  
Campaign #1  |  Other language   
1000549 | Google Analytics Demo | DR | apontes | NA | US | en | Hybrid | AW SEM | BKWS | ~ AW - Google Brand (US)  |  English   
1000549 | Google Analytics Demo | DR | apontes | NA | CA | es | Hybrid | AW SEM | BKWS | ~ AW - YouTube (CA)  |  Spanish   
**Swap the order of sections in a string:**
`REGEXP_REPLACE(Campaign, R'(.*):(.*)', R'\2 \1')`
In the previous example, the sections are separated by a colon (:).
## Metacharacters
Metacharacters are characters that have special meaning in a regular expression. Following are some of the more common metacharacters you can use. Note that these examples will open in the Google Analytics Help Center, but the information presented there applies equally to Looker Studio.
### Wildcards
Character | Description | Example  
---|---|---  
.  |  Matches any single character (letter, number, or symbol).  |  1. matches 10, 1A  Examples   
?  |  Matches the preceding character 0 or 1 times.  |  10? matches 1, 10  Examples   
+  |  Matches the preceding character 1 or more times.  |  10+ matches 10, 100  Examples   
*  |  Matches the preceding character 0 or more times.  |  1* matches 1, 10  Examples   
|  |  Creates an OR match.  |  1|10 matches 1, 10  Examples   
### Anchors
Character | Description | Example  
---|---|---  
^  |  Matches the adjacent characters at the beginning of a string.  |  ^10 matches **10** , **10** 0, **10** x **10** , 1 **10** x  Examples   
$  |  Matches the adjacent characters at the end of a string.  |  10$ matches 1 **10** , 10 **10** **10** 0, **10** x  Examples   
### Groups
Character | Description | Example  
---|---|---  
( )  |  Matches the enclosed characters in exact order anywhere in a string.  |  (10) matches **10** , **10** 1, **10** 11  Examples   
[ ]  |  Matches the enclosed characters in any order anywhere in a string.  |  [10] matches **01** 2, **1** 20, 2 **10** Examples   
-  |  Creates a range of characters within brackets to match anywhere in a string.  |  [0-9] matches any number 0 through 9  Examples   
### Escape
Character | Description | Example  
---|---|---  
\\\  |  Indicates that the adjacent character should be interpreted literally rather than as a regex metacharacter.  |  \\\ indicates that the adjacent dot should be interpreted as a period or decimal rather than as a wildcard  Examples   
### Character classes
Class | Characters  
---|---  
\d  |  digits (≡ [0-9])   
\D  |  not digits (≡ [^0-9])   
\s  |  whitespace (≡ [\t\n\f\r ])   
\S  |  not whitespace (≡ [^\t\n\f\r ])   
\w  |  word characters (≡ [0-9A-Za-z_])   
\W  |  not word characters (≡ [^0-9A-Za-z_])   
## Tips
### Use simple expressions
Keep your regular expressions simple. Simple expressions are easier for another user to interpret and modify.
### Case-sensitivity
Regular expressions are case-sensitive by default. You can make the match case-insensitive by using the `(?i)` flag. For example, this expression extracts both "abc123" and "ABC123":
`REGEXP_EXTRACT(MyField, '(?i)(a.*)')`
### Escaping a backslash character
If you want to write a filter condition that includes a backslash character, you need to escape the backslash character with a second backslash character.
For example, the following expression checks whether a field contains the string `green\yellow`:
`REGEXP_CONTAINS(field_name, "green\\yellow")`
You can also prepend an expression with the Raw string literal prefix, **R**. If you do this, then you don't need to escape special characters like the backslash character. The preceding example could be equivalently rewritten as follows:
`REGEXP_CONTAINS(field_name, R"green\yellow")`
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


