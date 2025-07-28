# ColorCollection  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorCollection

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  ColorCollection
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
id
_lock_
string 
Unique Id
label
string 
Label of color collection
categoricalPalettes
Expand DiscretePalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
colors
string[] 
sequentialPalettes
ContinuousPalette[] 
Expand ContinuousPalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
stops
Expand ColorStop definition... 
color
string 
CSS color string
offset
integer 
Offset in continuous palette (0 to 100)
divergingPalettes
ContinuousPalette[] 
Expand ContinuousPalette definition... 
id
_lock_
string 
Unique identity string
label
string 
Label for palette
type
string 
Type of palette
stops
Expand ColorStop definition... 
color
string 
CSS color string
offset
integer 
Offset in continuous palette (0 to 100)
## Related Methods
  * ColorCollection/create_color_collection
  * ColorCollection/set_default_color_collection
  * ColorCollection/default_color_collection
  * ColorCollection/color_collection
  * ColorCollection/update_color_collection


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


