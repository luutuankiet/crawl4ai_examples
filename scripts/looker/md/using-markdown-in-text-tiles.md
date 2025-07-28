# Using Markdown in Markdown tiles  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/using-markdown-in-text-tiles

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Markdown syntax supported in Markdown tiles
    * Code highlighting
  * Unsupported Markdown syntax




Was this helpful?
Send feedback 
#  Using Markdown in Markdown tiles
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Markdown syntax supported in Markdown tiles
    * Code highlighting
  * Unsupported Markdown syntax


> To use Markdown in a text tile, select **Markdown** from the dashboard's **Add** menu when you create the tile. **Text** tiles are a new type of Looker text tile that do not use Markdown but instead provide a visual editing experience.
You can use text tiles on a dashboard to describe the other tiles and to help viewers understand the information that those tiles present. Looker's **Markdown** tiles support a limited version of the Markdown markup language in text tiles, which gives you options for formatting your text or adding links and images that can make your dashboards pop.
## Markdown syntax supported in Markdown tiles
This page lists the Markdown syntax that is supported for **Markdown** tiles, with each example shown first in a code block and then as the result.
The styles in which the Markdown elements render on your dashboard tiles may differ from the styles shown here.
### Headers
Dashboards support header levels 1-6:
```
## Header level 1

### Header level 2

#### Header level 3

##### Header level 4

###### Header level 5

####### Header level 6

```

### Tables
Table columns are sized to the widest data value. You can use `&nbsp;` to add width to columns.
```
| Tables        | Are           | Cool  |
| ------------- | ------------- | ----- |
| leopards      | have spots    | $1600 |
| zebras        | have stripes &nbsp;&nbsp;   | $12   |
| polar bears  &nbsp;&nbsp;&nbsp;&nbsp;  | are white     | $1    |

```

Only left justification is supported in table columns.
### Emphasis
```
Emphasis (italics) with *asterisks* or _underscores_.

Strong emphasis (bold) with **double asterisks** or __double underscores__.

Combined emphasis with **asterisks and _underscores_**.

```

### Numbered lists
```
1. First ordered list item
1. Another item
1. Actual numbers don't matter, just that it's a number
1. And another item

```

### Unordered lists
```
* Unordered lists can use asterisks
- or minuses
+ or pluses

```

### Links
Links can be added in several ways, as shown in the following Markdown:
```
[Inline-style link](https://www.looker.com)
[Reference-style link](Case-insensitive reference text)
[Relative reference to a public repository](../assets/images/dashboard-add-text.png)
[Number used for a reference-style link definition][1]

```

URLs in angled brackets are automatically turned into links. For example, `<looker.com>` as well as `looker.com`.
### Images
Images can be referenced by path or URL.
```
Here's our logo:

URL-style:

<img src="url/to/image.png">

Inline-style:

![alt text](path/to/image.png)

Reference-style:

![alt text][logo]



```

To control the size of the image in relation to the tile size, use HTML to call the image and add a percent size parameter. The following example changes the size using the `width="50%"` parameter:
```

<img src="path/to/image.png" width="50%">

```

Or, you can provide explicit height and width maximums like this:
```

<img src="path/to/image.png" width="500px" height="30px">

```

Height and width pixel parameters will NOT set the image to those exact dimensions; rather, the aspect ratio of the image will be "best fit" to those constraints. For example, if the dimensions "width=100px height=30px" were set on an image that is originally 200px x 20px the result would be 100px x 10px since the logic is roughly "image width exceeds maximum > scale down until width maximum is reached."
### Code highlighting
```
`<script>Some code</script>.`

```

### Horizontal rule
```
Three or more hyphens

---

Asterisks

***

Underscores

___


```

### Blockquotes
```
> Blockquotes are very handy.
> This line is part of the same quote.

```

### Quote break
```
> This is a very long line that will be quoted properly when it wraps. I will keep writing to make sure this is long enough to actually wrap for everyone. Also, you can *put* **Markdown** into a blockquote.

```

## Unsupported Markdown syntax
The following Markdown syntax is _not_ supported in dashboard **Markdown** tiles:
  * Math
  * Images with alt text
  * Links with alt text
  * Language-specific syntax highlighting
  * Strikethrough using two tildes
  * Sublists
  * Indentation


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


