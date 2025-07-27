# Admin settings - Localization  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-general-localization

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Admin settings - Localization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Admins can set the default locale and number format for a Looker instance on the **Localization** page in the **General** section of the **Admin** panel.
Admins can set locales or number formats at the user or user group levels as well. Settings at the user or user group levels supersede settings for the instance.
## Locale
Certain Looker user interface text can be displayed in the following languages:
Language | Locale Code and Strings Filename  
---|---  
English  
Czech | `cs_CZ`  
German | `de_DE`  
Spanish (Spain) | `es_ES`  
Finnish | `fi_FI`  
French (France) | `fr_FR`  
Hindi | `hi_IN`  
Italian | `it_IT`  
Japanese | `ja_JP`  
Korean | `ko_KR`  
Lithuanian | `lt_LT`  
Norwegian (Bokmål) | `nb_NO`  
Dutch | `nl_NL`  
Polish | `pl_PL`  
Brazilian Portuguese | `pt_BR`  
Portuguese | `pt_PT`  
Russian | `ru_RU`  
Swedish | `sv_SE`  
Thai | `th_TH`  
Turkish | `tr_TR`  
Ukrainian | `uk_UA`  
Simplified Chinese | `zh_CN`  
Traditional Chinese | `zh_TW`  
It is helpful if Looker developers who are localizing data models set the models' `default_locale` parameters and the titles of their associated strings files to match the default locale for the instance.
If no locale is set on this page, Looker defaults to `en`.
For more information about localizing the Looker user interface, see the Supported user-interface languages documentation page.
## Number format
Looker's default number format setting for numbers that appear in data tables and visualizations is **1,234.56**. However, the number format can be set to any of the following:
  * **1,234.56** : Thousands separated with commas; decimals separated with a period
  * **1.234,56** : Thousands separated with periods; decimals separated with a comma
  * **1 234,56** : Thousands separated with spaces; decimals separated with a comma


For more information about localizing number formatting, see the Localizing number formatting documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


