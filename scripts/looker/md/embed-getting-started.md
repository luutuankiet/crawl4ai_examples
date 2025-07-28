# Get started with embedding Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embed-getting-started

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Your iframe embedding options
    * Private embedding
    * Signed embedding
    * Signed embedding with Embed SDK (Recommended)
  * Suggested learning path




Was this helpful?
Send feedback 
#  Get started with embedding Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Your iframe embedding options
    * Private embedding
    * Signed embedding
    * Signed embedding with Embed SDK (Recommended)
  * Suggested learning path


We provide options for you to embed Looker content in your host application using iframes. Each option differs in how you manage and interact with your iframe and authorize or authenticate your user. If you are not sure which option to start with, check out the suggested learning path at the end of this page.
## Your iframe embedding options
Every option supports theming and can embed dashboards, LookML dashboards, Explores, Looks, query visualizations, and extensions.
### Private embedding
  * You manage your iframe directly.
  * You may use window.postMessage() to interact with your iframe.
  * Your user must authenticate or authorize with Looker directly or with Looker using signed embedding with an identity provider.


Get started with private embedding
### Signed embedding
  * You manage your iframe directly.
  * You may use window.postMessage() to interact with your iframe.
  * You generate a unique iframe src url for every embed user session. This one-time-use URL creates a new Looker embed user or updates an existing one.
  * You must authenticate or authorize the user outside of Looker, for example, through your host application's identity provider using signed embedding.


Get started with signed embedding
### Signed embedding with Embed SDK (Recommended)
  * You use the Embed SDK's convenient Javascript API to **manage** and **interact** with your iframe.
  * You generate a unique URL for every embed user session. This one-time-use URL creates a new Looker embed user or updates an existing one. The Embed SDK helps automate part of the URL generation.
  * You must authenticate or authorize the user outside of Looker, for example, through your host application's identity provider using signed embedding.


Get started with signed embedding with the Embed SDK
## Suggested learning path
We suggest you get started in this order:
1. Get started with private embedding
Private embedding will provide a basic understanding of Looker embedding.
2. Get started with signed embedding with Embed SDK
Signed Embedding and the Embed SDK are more advanced concepts.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


