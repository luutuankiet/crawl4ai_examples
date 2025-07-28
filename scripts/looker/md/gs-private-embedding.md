# Get started with private embedding  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/gs-private-embedding

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * 1. Build the embed content URL
    * Part 1: Hostname
    * Part 3: Parameters
  * 2. Test your embed content URL
  * 3. Create your iframe
  * 4. Consider user access issues
    * User login options
    * User browser cookie policy
  * 5. Interact with your iframe




Was this helpful?
Send feedback 
#  Get started with private embedding
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * 1. Build the embed content URL
    * Part 1: Hostname
    * Part 3: Parameters
  * 2. Test your embed content URL
  * 3. Create your iframe
  * 4. Consider user access issues
    * User login options
    * User browser cookie policy
  * 5. Interact with your iframe


This page will walk you through how to set up private embedding. The private embedding option requires that you manage the <iframe> HTML element directly to embed your Looker content and requires that the user log in to Looker separately from the host application.
We will walk through this private embedding code example:
```
<iframe
    src="https://instance.looker.com/embed/dashboards/4?Timeframe=14+day"
    width="600"
    height="300"
    frameborder="0">
</iframe>

```

## 1. Build the embed content URL
Consider an example of Looker content at the URL `https://instance.looker.com/dashboards/4?theme=red&Timeframe=14+day`. From this Looker content URL, we will construct the **embed content URL** and set the iframe's `src` attribute to it. Feel free to use your own Looker content URL as you work through these steps.
The embed content URL from the preceding code sample is follows:
https://instance.looker.com/embed/dashboards/4?theme=red&Timeframe=14+day
The embed content URL consists of three parts:
  * Hostname: your Looker instance's hostname
  * Path: Looker content URL path prefixed with `/embed` (with extra steps for query visualizations)
  * Parameters: URL parameters that specify filters and theming


The protocol must always be `https://`. Let's build each part in detail.
### Part 1: Hostname
  1. Navigate to your Looker content. Following the example Looker content URL: `https://instance.looker.com/dashboards/4?theme=red&Timeframe=14+day`.
  2. Your embed content URL hostname is `instance.looker.com`.


### Part 2: Path
Your embed content URL path depends on the Looker content you embed.
#### Embedding all Looker content except query visualizations
  1. Navigate to your Looker content. Following the example Looker content URL: `https://instance.looker.com/dashboards/4?theme=red&Timeframe=14+day`
  2. Identify your Looker content URL's path: `/dashboards/4`.
  3. Prefix `/embed` onto your Looker content URL's path. Your embed content URL's path is `/embed/dashboards/4`.


#### Embedding a query visualization
  1. Navigate to your query visualization. Example URL: `instance.looker.com/explore/my_model/my_explore?qid=1234567890abcdefghij12`
  2. Identify your query client ID. The `qid` parameter: `1234567890abcdefghij12` is your query's client ID that represents the query and the visualizations settings.
  3. Your embed content URL path is `/embed/query-visualization/` appended with your query client ID. The example embed content URL's path is `/embed/query-visualization/1234567890abcdefghij12`


### Part 3: Parameters
Your embed content URL parameters control your embedded content's filters and theming.
#### Filters
  1. Navigate to your Looker content URL.
  2. Manually adjust the content's filters to what you want. For this example, your resulting Looker content URL is: `https://instance.looker.com/dashboards/4?Timeframe=14+day`
  3. Your embed content URL parameters are the Looker content URL parameters, for example, `Timeframe=14+day`


In this example, the parameter `Timeframe=14+day` sets the value of the dashboard's `Timeframe` filter.
#### Theming
Check out the theming guide to read about how to control the appearance of your embedded content.
## 2. Test your embed content URL
Open your embed content URL in your browser to preview your embed content's behavior and appearance.
## 3. Create your iframe
  1. Create your iframe element in your host application.
  2. Set the `src` attribute to your embed content URL.
  3. Define the `width`, `height`, and other attributes to what you need to best display your embedded Looker content.


## 4. Consider user access issues
The user must be logged in to Looker to view your embedded content. The iframe will show a 401 error page if the user is not logged in.
### User login options
Your user can log in to Looker in one of two ways:
#### 1. Log in to Looker beforehand
Your user must log in to Looker on the same browser before they can view the embedded content.
#### 2. Enable an optional embed Looker login screen
Add `allow_login_screen=true` to your embed content URL parameters to present a Looker login screen in the iframe if the user is not signed in. Our example embed content URL becomes: `https://instance_name.looker.com/embed/dashboards/4?Timeframe=14+day&allow_login_screen=true`
Keep in mind two caveats:
  * You must disable the Same-Origin Protections for Looker Login Pages setting to enable the Looker login screen in the iframe embed.
  * If your Looker instance authenticates users using single sign-on (SSO) with an identity provider, your identity provider may block the login screen within your iframe. You will need to use option 1 if this happens.


### User browser cookie policy
Looker uses cookies for user authentication and session storage. Your user's browser must enable third-party cookies if your user accesses your Looker instance embed content URL's hostname is under a different domain from your host application.
Some browsers, such as Firefox and Safari, default to a cookie policy that blocks third-party cookies. If the user's browser cannot allow third-party cookies, you can add a custom domain to your Looker instance so your host application and embed content URL's hostname Looker instance reside under the same domain.
## 5. Interact with your iframe
Get started with Looker embedding iframe post messaging.
## Next steps
Get started with signed embedding using our Embed SDK and check out examples of what you can do with Looker embedding.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


