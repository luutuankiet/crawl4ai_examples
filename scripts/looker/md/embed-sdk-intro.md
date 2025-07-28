# Introduction to the Embed SDK  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/embed-sdk-intro

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting up the Looker Embed SDK
    * Installing the Embed SDK
    * Constructing the embedded content
    * Connecting to the embedded content
  * Signed URL auth endpoint
    * Signed URL advanced auth configuration




Was this helpful?
Send feedback 
#  Introduction to the Embed SDK
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting up the Looker Embed SDK
    * Installing the Embed SDK
    * Constructing the embedded content
    * Connecting to the embedded content
  * Signed URL auth endpoint
    * Signed URL advanced auth configuration


Looker's Embed SDK is a library of functions that you can add to the code of your browser-based web application to manage embedded dashboards, Looks, reports, and Explores in your web app.
The Embed SDK facilitates embedding in the following ways:
  * Providing the encapsulation of the embedded content without the need to manually create HTML elements.
  * Providing point-to-point communication so that there's no cross-frame communication. The Embed SDK handles cross-domain message passing between your host web page and your embedded Looker content, making use of a dedicated message channel.


Without the Embed SDK, you can invoke or respond to events in embedded Looker content by using JavaScript events such as `dashboard:run:start` or `page:changed`, which are described on the Embedded JavaScript events documentation page. Developers who embed Looker content with JavaScript events must create the HTML elements to house the embedded content and rely on window broadcast events for communications between the web app and the embedded content.
Note that the Looker Embed SDK is different from the Looker API and the Looker API SDK:
  * The Looker Embed SDK lives in the client-side code of your web application and manages the Looker embed context and content. (The Embed SDK does not provide access to the Looker API.)
  * The Looker API lives on the server with your Looker instance and executes commands on the Looker server.
  * Looker API client SDKs reside in the code of non-browser applications to provide access to Looker API functions.


Be aware that Looker does not control the order in which browsers dispatch events to web applications. This means that the order of events is not guaranteed across browsers or platforms. Be sure to write your JavaScript appropriately to account for the event handling of different browsers.
## Quick example
In this example, a dashboard with an ID of `11` is created inside a DOM element with the ID `embed_container`. The `dashboard:run:start` and `dashboard:run:complete` events are used to update the state of the embedding window's UI, and a button with an ID of `run` is scripted to send a `dashboard:run` message to the dashboard.
```
getEmbedSDK().init('looker.example.com','/auth')

constsetupConnection=(connection)=>{
document.querySelector('#run').addEventListener('click',()=>{
connection.asDashboardConnection().run()
})
}

try{
connection=awaitgetEmbedSDK()
.createDashboardWithId('11')
.appendTo('#embed_container')
.on('dashboard:run:start',()=>updateStatus('Running'))
.on('dashboard:run:complete',()=>updateStatus('Done'))
.build()
.connect()
setupConnection(connection)
}catch(error){
console.error('An unexpected error occurred',error)
}

```

A more complete example is described on the Embed SDK demo documentation page.
## Setting up the Looker Embed SDK
The Looker Embed SDK uses a fluent interface pattern. Once you install the Embed SDK, you then construct the embedded content and connect to the embedded content. The hosting application may interact with the embedded content once the connection is established.
### Installing the Embed SDK
You can get Looker's Embed SDK library through the node package manager (NPM) at https://www.npmjs.com/package/@looker/embed-sdk. However, if you want to see the sample code or the demo, you should instead use the Looker Embed SDK repository.
To install the Looker Embed SDK using the Looker Embed SDK repository, follow these steps:
  1. Install Node.js, if you don't already have it.
  2. Download or clone the `/looker-open-source/embed-sdk` repository.
  3. In a terminal window, navigate to the `/embed-sdk` directory and run these commands:

```
npminstall
npmstart

```

### Constructing the embedded content
First, initialize the SDK with the address of the Looker server and the endpoint of the embedding application server that will create a signed Looker embedded login URL. These servers are used by all the embedded content. For private embedding, omit the signing endpoint.
```
getEmbedSDK().init('looker.example.com','/auth')

```

Then the embedded content is built using a series of steps to define its parameters. Some of these parameters are optional, and some are mandatory.
The process starts with creating the builder either with a dashboard `id` or with a `url` that refers to a dashboard (created by the process that is described on the Signed embedding documentation page).
```
getEmbedSDK().createDashboardWithId('id')

```

or
```
getEmbedSDK().createDashboardWithUrl('url')

```

You can then add additional attributes to the builder to complete your setup.
For example, you can specify where in your web page to insert the Looker embed UI. The following call places the Looker embed UI inside an HTML element with an ID value of `dashboard`:
```
.appendTo('#dashboard')

```

Add event handlers:
```
.on('dashboard:run:start',
()=>updateStatus('Running')
)
.on('dashboard:run:complete',
()=>updateStatus('Done')
)

```

Create an embedded client by calling the build method:
```
.build()

```

### Connecting to the embedded content
Once the client is built, call `connect` to create the iframe. The connect process creates the `src` attribute that is used for the actual iframe. The way that the `src` value is generated is based on how the embed SDK is initialized:
  1. Signed: The endpoint that is specified by the second argument of the `init` call is called. The endpoint is expected to return a signed embed login URL.
  2. Cookieless: The endpoint or the function that is specified by the second argument of the `initCookieless` call is called. The endpoint or function is expected to return cookieless tokens, specifically the authentication and navigation tokens. The tokens are appended to the embed login URL.
  3. Private: The embed connection is private if the second argument of the `init` call is not provided. In this case, the URL is derived from the builder and decorated with the parameters that are required for Looker embed. For private embed, it is expected that the user is already logged in to Looker _or_ that the embedding URL includes the `allow_login_screen=true` parameter.


`connect` returns a `Promise` that resolves to the connection interface for the embedded iframe.
```
.connect()
.then((connection)=>{
// Save the connection
})
.catch(console.error)

```

### Interacting
Embed SDK 2.0.0 returns a unified connection that supports interacting with all Looker content types. The embedding application can determine what kind of content is being displayed and interact accordingly.
```
if(connection.getPageType()==='dashboards'){
connection.asDashboardConnection().run()
}else(connection.getPageType()==='looks'){
connection.asLookConnection().run()
}else(connection.getPageType()==='explore'){
connection.asExploreConnection().run()
}

```

The iframe does not need to be recreated when different content needs to be loaded. Instead, the connection methods `loadDashboard`, `loadLook`, `loadExplore`, or `loadUrl` can be used. The `loadDashboard`, `loadLook`, and `loadExplore` methods accept an `id`. The `loadUrl` method accepts an embed `URL`, and this method can be used to specify additional parameters (such as filters).
```
connection.loadDashboard('42')
// OR
connection.loadUrl('/embed/dashboards/42?state=california')

```

If it is necessary to create a new iframe, the Embed SDK won't call the signing or acquire session endpoints again. Instead it will construct iframe `src` directly from the builder. Should it be necessary to create a new embed session, the Embed SDK will need to be reinitialized in the following way:
```
getEmbedSDK(newLookerEmbedExSDK()).init('looker.example.com','/auth')

```

## Signed URL auth endpoint
This section does not apply to cookieless embed. See Cookieless embedding for details.
To use the Embed SDK, you must supply a backend service that handles signing of the embed URL. This service is called by the Embed SDK to generate a signed URL that is unique to the requesting user. The backend process can either generate the signed embed URL itself by using an embed secret, or the backend process can generate the URL by calling the Looker Create Signed Embed URL API. Manual URL generation and signing avoids calling the Looker API, which decreases latency. Calling the Looker API requires less code and is easier to maintain.
A JavaScript example of a helper method that generates a signed URL, `createSignedUrl()`, can be found in server/utils/auth_utils.ts. It is used in the following way:
```
import{createSignedUrl}from'./utils/auth_utils'

app.get('/looker_auth',function(req,res){
// It is assumed that the request is authorized
constsrc=req.query.src
consthost='looker.example.com'
constsecret=...// Embed secret from Looker Server Embed Admin page
constuser=...// Embedded user definition
consturl=createSignedUrl(src,user,host,secret)
res.json({url})
})

```

See the python example in the repository.
### Signed URL advanced auth configuration
This section does not apply to cookieless embed. See Cookieless embedding for details.
You can configure the auth endpoint to allow custom request headers and CORS support by passing an options object to the `init` method.
```
getEmbedSDK().init('looker.example.com',{
url:'https://api.acme.com/looker/auth',
headers:[{name:'Foo Header',value:'Foo'}],
params:[{name:'foo',value:'bar'}],
withCredentials:true,// Needed for CORS requests to Auth endpoint include Http Only cookie headers
})

```

## Troubleshooting
The Embed SDK is built on top of chatty. Chatty uses debug for logging. You can enable logging in a browser console with this command:
```
localStorage.debug='looker:chatty:*'
```none

Note that both the parent window and the embedded content have separate local storage, so you can enable logging on one, the other, or both. You can disable logging with this command:

```javascript
localStorage.debug=''

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


