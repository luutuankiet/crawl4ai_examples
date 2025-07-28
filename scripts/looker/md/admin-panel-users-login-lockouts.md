# Admin settings - Login lockouts  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-users-login-lockouts

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Included information
  * Unlocking an account




Was this helpful?
Send feedback 
#  Admin settings - Login lockouts
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Included information
  * Unlocking an account


Looker automatically locks out user accounts for five minutes after someone has tried to log in to an account and failed to enter the proper credentials four times in a row from a single IP address. If an account is locked, that account is not allowed to login from that same IP address, even with the proper credentials, until the five-minute lockout period expires. Lockouts occur on a per-user credential and per-IP address basis, so a user credential that is locked out on an IP address can still attempt to log in from a different IP address, or a different user credential can attempt to log in from that same IP address.
> The lockout policy does not apply to signed embed users.
The **Login Lockouts** page in the **Users** section of the **Admin** menu shows a list of user credentials that are currently locked out because their owners exceeded the maximum number of failed login attempts.
## Included information
Column | Definition  
---|---  
User ID | The user ID associated with the locked account. If there is not an account associated with the credentials used for the unsuccessful login attempts, this column is empty.  
Name | The name associated with the locked account. If there is not an account associated with the credentials used for the unsuccessful login attempts, this column shows "No matching account."  
Email | The email address used with the unsuccessful login attempts.  
Time Remaining | The amount of time left before the account unlocks.  
Authentication Type | The authentication method through which the unsuccessful login attempts were made. Possible options are:
  * `email`: Invalid email address and password combination
  * `api`: Invalid Looker API credentials
  * `totp`: Invalid two-factor authentication codes
  * `ldap`: Invalid LDAP credentials

  
IP Address | The IP address from which the unsuccessful logins were attempted.  
Actions | Shows the **Unlock** button, which lets you unlock the user account.  
## Unlocking an account
Looker admins can unlock an account that is currently locked, letting that user attempt to log in again before the five-minute lockout period expires. Click the **Unlock** button next to the user account that you want to unlock. Looker will display a confirmation dialog box. Click **Unlock** on the dialog box to unlock the user account.
If there is a user account associated with the credentials used for the login attempts, the dialog box includes a link to that user account page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


