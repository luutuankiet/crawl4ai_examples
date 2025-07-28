# Allowing Looker support to access a customer-hosted deployment  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/support-access-customer-hosted-deployment

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Contacting Looker Support to access your Looker instance
  * Contacting Looker Support to finish deploying your Looker instance




Was this helpful?
Send feedback 
#  Allowing Looker support to access a customer-hosted deployment
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Contacting Looker Support to access your Looker instance
  * Contacting Looker Support to finish deploying your Looker instance


If you are hosting your own Looker deployment, we **strongly** recommend that you provide a means for the Looker Support team to access your Looker application. This helps us answer questions and resolve issues as quickly as possible.
## Contacting Looker Support to access your Looker instance
You can enable support by adding to the allowlist the traffic from our secure gateway IP address, `54.209.194.236`, to your Looker application. Looker access to the secure gateway is strictly controlled and secured with multifactor authentication. The secure gateway IP to add to the allowlist is different than the IP addresses that Looker hosts customers on.
The destination will be your Looker application's host and HTTPS port, generally 9999. This hostname/IP needs to be publicly routable from the internet. See this American Registry for Internet Numbers page for more information on private addresses.
## Contacting Looker Support to finish deploying your Looker instance
After you have added Looker's secure gateway to the allowlist, the Looker Support team will need to do some further configuration. Open a support request and provide the following:
  * Your company's name.
  * The destination URL of your Looker instance.
  * The hostname of your Looker instance as seen from the public Internet, for example `looker.mycompany.com`.
  * The port on which Looker's web interface is listening. By default this is 9999, but many customers change it to 443 (the standard for HTTPS).


This support request lets the Looker Support team finish enabling access for Looker support or answer any additional questions you may have.
## Next steps
Once you have added Looker's secure gateway IP address to the allowlist, you can ensure the Support Access feature is enabled.
After that, you're ready to set up Looker monitoring.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


