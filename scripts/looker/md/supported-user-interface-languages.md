# Supported user-interface languages  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/supported-user-interface-languages

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Supported user-interface languages
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Looker admins can set Looker to display certain user interface (UI) text in the following languages:
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
To display the Looker UI in specific languages for particular users, set the locale for users, user groups, or instances through one of the following methods:
  * **To set a locale for individual users:** Use one of the codes from the supported user-interface languages table in the **Locale** field on the **Edit User** page in the **Admin** panel.
  * **To set a locale for a user group:** Assign one of the codes from the supported user-interface languages table to the `locale` user attribute for a particular user group. If users within a group have set a custom value using the **Locale** setting, the custom value will override any value assigned to the group. To prevent that from happening, ensure that the **User Access** setting for the `locale` user attribute is not set to **Edit**.
  * **To set a locale for an instance:** Assign one of the codes from the supported user-interface languages table to the **Locale** field on the **Localization** page of the **Admin** panel.


For users with no **Locale** set, Looker uses the locale chosen on the **Localization** page of the **Admin** panel as the default locale; and, if no locale is set there, Looker defaults to `en`.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


