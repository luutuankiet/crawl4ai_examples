# Creating Looker expressions  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/creating-looker-expressions

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Looker expressions
  * Creating Looker expressions
    * Seeing all suggestions
    * Adding operators
    * Adding functions
    * Using error hints and the information pane
    * Including comments




Was this helpful?
Send feedback 
#  Creating Looker expressions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker expressions
  * Creating Looker expressions
    * Seeing all suggestions
    * Adding operators
    * Adding functions
    * Using error hints and the information pane
    * Including comments


## Looker expressions
Looker expressions (sometimes referred to as _Lexp_) are used to perform calculations for:
  * Table calculations


A Looker expression is built from a combination of these elements:
  * **NULL:** The value `NULL` indicates there is no data, and can be useful when you want to check that something is empty or doesn't exist.
  * **A constant:** A constant is an unchanging value that you provide. A number such as `7` or a string such as `Completed` are constants.
  * **A Looker field:** A reference to a Looker field, which includes dimensions, measures, and table calculations.
  * **A Looker operator:** There are several types of operators (which are listed on the Looker functions and operators documentation page):
    * Mathematical operators (such as `+`, `-`, `*`, and `/`)
    * Comparison operators (such as `=`, , and `<=`)
    * Logical operators (such as `AND`, `OR`, and `NOT`)
  * **A Looker function:** These are similar in nature to Excel functions. Functions let you transform your data or reference data in complex ways. All available functions are listed on the Looker functions and operators documentation page.


## Creating Looker expressions
Table calculations, custom fields, and custom filters use the Looker expression editor. As you type your expression, Looker prompts you with functions, operators, and field names that you might want to use.
### Seeing all suggestions
Access the Looker expression editor in an Explore by creating a table calculations, custom field, or custom filter.
Type a space to see a list of all fields, functions, and operators that you can choose from. If a field is currently selected in the Explore, Looker displays a black dot to the left of the field and displays the field at the top of the list.
Start typing in the Looker expression editor to shorten the list to items that you are interested in.
The editor for custom fields displays Explore fields that are currently in use, if they are compatible with the custom field's function.
### Adding a field
To include a Looker field in your expression, start typing the field's name. As you type, the editor narrows your search to a list of fields and functions that contain what you've typed. You can type the name of the field as it appears on the Explore page, or you can use its LookML name if you know it.
When you select a field from the list, Looker adds it to your expression using the LookML name in the form `${view_name.field_name}`. This ensures that all of your fields have unique names in your expression.
### Adding totals
If you are creating an expression that is based on an Explore where you displayed totals, you can also include column and row totals in your expression. Column totals appear in the editor with the word **Total** in front of the LookML iteration of the field name. For example, for a field named **Count** , Looker will give the column total for that field the name `Count - Total`.
The _LookML name_ for totals is in the form `${view_name.field_name:total}`, where `:total` is added to the end of the field name.
For row totals, the words **Row Totals** appear in front of the field name in the editor; and, in the _LookML name_ of the field, `:row_total` is added to the end of the field name, like `${view_name.field_name:row_total}`.
### Adding operators
You can add logical operators like `AND`, `OR`, and `NOT` to your expression if needed. Ordinarily `AND` operators are evaluated before `OR` operators, but you can override this behavior by using parentheses. You also can use comparison operators (such as , `=`, and `<=`) and mathematical operators (such as `+` and `*`).
When you hover your cursor over an operator, notes for proper use display in the information pane.
### Adding functions
To include a Looker function in your expression, start typing the function's name. As you type, the editor narrows your search to a list of fields and functions that contain what you've typed.
Functions may be constructed of arguments (or variables) that require a certain type, such as a field, a number, or yes/no. When you hover your cursor over a function, you can check the notes that display next to your expression in the information pane to understand which arguments you need to provide, and what type they need to be.
You can reference the full list of functions that Looker offers on the Looker functions and operators documentation page.
### Using error hints and the information pane
Looker displays an information pane next to the Looker expression editor. This pane provides documentation and suggestions, especially if you have an error in your expression.
The information pane next to the expression editor provides the following information:
  * **Error highlighting:** Looker underlines in red any parts of the expression that are not yet correct.
  * **Suggestions and error Details:** Looker gives suggestions about what to add next in your expression. If there's an error, it explains why the error is occurring. If there are multiple errors, the error that it shows to you is based on the location of your cursor.
  * **Documentation:** Looker displays documentation about the function or operator you're working with, based on your cursor position. For example, while you type the first argument of an `if()` function, Looker provides the information that the first argument should evaluate as true or false. You can click on the function name to navigate to the documentation for that function.


### Including comments
You can include comments in Looker expressions by beginning the comment line with `#` in the expression editor.
## Using fields
Sometimes you'll want to use the value of a field (a dimension, measure, or table calculation) in an expression. You might want to add the value of the field to something else, check that it has a certain value, include it in a function, or many other possibilities.
As described previously on this page, you can type the name of the field into the expression editor, and Looker will help you find the correct way to reference the field. When you add a field to an expression, Looker uses the field's LookML identifier, which looks like `${view_name.field_name}`. Type the field name as it appears in the field picker and the expression editor will show you the field picker name and the LookML identifier together.
There are several ways to retrieve a value:
  * **Get a value from the same row:** The most basic way to use a field is to reference it directly. For example, your expression might use `${product.category}`. When you do this, you're saying "for any given row, grab the Product Category from that row."
  * **Get a value from a different row:** You can also get a field's value from a different row. For example, you might want the logic "for any given row, grab the Product Category from the _previous_ row." To do that, you can use an offset function (see this list of positional functions). The offset function might look like this: `offset(${product.category}, -1)`.
  * **Get a value from a pivoted column:** You can also get values from pivoted columns. For example, you might want the logic "for any given row, grab the Total Sales from the first pivoted column." To work with pivoted columns, you'll need to use pivot functions (see this list of pivot functions). The pivot function might look like this: `pivot_index(${order.total_sales}, 1)`.
  * **Get a total from a row or a column:** If you added totals to your Explore, you can get total values from the column or row by adding `:total` (for column totals) or `:row_total` (for row totals) to the field name, using the format `${field_name:total}`. For example, if you want a percentage of the total of an **Orders** count, you could create a table calculation like this: `${orders.count} / ${orders.count:total}`.


## Using operators
Looker expressions can include logical, comparison, and mathematical operators to create different conditions:
  * Logical operators (such as `AND`, `OR`, and `NOT`)
  * Comparison operators (such as and )
  * Mathematical operators (such as `+` and `-`)


Unless you specify otherwise with parentheses, `AND` logic is considered before `OR` logic. The following expression without additional parentheses:
```
if${order_items.days_to_process}>=4${order_items.shipping_time}>5${order_facts.is_first_purchase},
"review",
```

is evaluated as:
```
if${order_items.days_to_process}>=4${order_items.shipping_time}>5${order_facts.is_first_purchase}),
"review",
```

In Looker, you should use `yes` and `no` instead of `true` and `false`. These logical constants are _not_ the same thing as the words `"yes"` and `"no"`, which are enclosed in quotes. See the logical constants description for more detail.
## Using functions
Looker expressions often include one or more functions, which help you to retrieve certain data or calculate certain things. They are similar in nature to Excel functions.
Functions take the form of a name followed by two parentheses, like this: `my_function()`. You might need to provide information within those parentheses, separated by commas. These bits of information are called "arguments" and look like this: `my_function(argument_1, argument_2)`.
For example, the `now` function does not take any arguments, and gives you the current date and time. You use it like this: `now()`.
The `round` function _does_ take one argument, which is a number. You use it like this: `round(3.2)`. The result is `3`.
There are two ways to know which arguments you'll need to provide, if any:
  * The information pane that appears next to the expression editor provides some documentation about the function you are writing. You can click on the function's name to navigate to its documentation.
  * You can also navigate directly to the Looker functions and operators documentation page and look up the function you want to use.


Consider the `contains` function, which has documentation that looks like this:
Function | Syntax | Purpose  
---|---|---  
contains | `contains(string, search_string)` | Returns `Yes` if `string` contains `search_string`, and `No` otherwise  
You can see that two arguments are required. They have the names `string` and `search_string`, but that doesn't mean you need to type the exact word "string" and "search_string" into the function. These are just names for the arguments that you'll replace with something. Reading the purpose, we see that `string` should be a field or other value we want to search _in_ , while the `search_string` is the thing we want to search _for_. An example might be:
```
contains(${customer.feedback_text},
```

If the word "great" appears in the customer feedback, then this function gives a result of `Yes`. Otherwise, it gives a result of `No`.
You can put functions inside of other functions to handle complex logic. As long as the result of the inner function is appropriate for the arguments of the outer function, it will work. For example:
```
contains(
${customer.feedback_text}),
${customer.comment_text},
${customer.feedback_text}

```

The `is_null` function is nested inside of an function, which is itself inside a `contains` function. It works like this:
  1. The `is_null()` function checks for customer feedback text.
  2. Next, the `if()` function uses that result and returns the customer feedback text if any, or otherwise returns the customer comment text.
  3. Finally, the `contains()` function uses the text returned by the `if()` function and searches it for the word "great".


Logically, this expression means: "If there is customer feedback, then search in that. If not, then search in customer comments instead. In both cases, look for the word 'great' ".
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


