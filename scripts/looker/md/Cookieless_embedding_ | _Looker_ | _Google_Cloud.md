# Cookieless embedding  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/cookieless-embed

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * How does cookieless embedding work?
    * Creating a Looker embed iframe
    * Generating new tokens
  * Implementing Looker cookieless embed
    * Configuring the Looker instance
    * Application client implementation
    * Application server implementation
    * Running the Looker cookieless embed example




Was this helpful?
Send feedback 
#  Cookieless embedding
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * How does cookieless embedding work?
    * Creating a Looker embed iframe
    * Generating new tokens
  * Implementing Looker cookieless embed
    * Configuring the Looker instance
    * Application client implementation
    * Application server implementation
    * Running the Looker cookieless embed example


When Looker is embedded in an iframe using signed embedding, some browsers default to a cookie policy that blocks third-party cookies. Third-party cookies are rejected when the embedded iframe is loaded from a domain that is different from the domain that loads the embedding application. You can generally work around this limitation by requesting and using a vanity domain. However, vanity domains can't be used in some scenarios. It is for these scenarios that Looker cookieless embedding can be used.
## How does cookieless embedding work?
When third-party cookies are not blocked, a session cookie is created when a user initially logs in to Looker. This cookie is sent with every user request, and the Looker server uses it to establish the identity of the user who initiated the request. When cookies are blocked, the cookie is not sent with a request, so the Looker server can't identify the user who is associated with the request.
To solve this problem, Looker cookieless embed associates tokens with each request that can be used to recreate the user session in the Looker server. It is the responsibility of the embedding application to get these tokens and make them available to the Looker instance that is running in the embedded iframe. The process of obtaining and providing these tokens is described in the rest of this document.
To use either API, the embedding application must be able to authenticate into the Looker API with admin privileges. The embed domain must also either be listed in the **Embed Domain Allowlist**, or, if using Looker 23.8 or later, the embed domain can be included when the cookieless session is acquired.
### Creating a Looker embed iframe
The following sequence diagram illustrates the creation of an embed iframe. Multiple iframes may be generated either simultaneously or at some point in the future. When implemented correctly, the iframe will automatically join the session that is created by the first iframe. The Looker Embed SDK simplifies this process by automatically joining the existing session.
  1. The user performs an action in the embedding application that results in the creation of a Looker iframe.
  2. The embedding application client acquires a Looker session. The Looker Embed SDK can be used to initiate this session, but an endpoint URL or a callback function must be provided. If a callback function is used, it will call the embedding application server to acquire the Looker embed session. Otherwise, the Embed SDK will call the provided endpoint URL.
  3. The embedding application server uses the Looker API to acquire an embed session. This API call is similar to the Looker signed embed signing process, as it accepts the embed user definition as input. If a Looker embed session already exists for the calling user, the associated session reference token should be included in the call. This will be explained in greater detail in the Acquire session section of this document.
  4. The acquire embed session endpoint processing is similar to the signed `/login/embed/(signed url)` endpoint, in that it expects the Looker embed user definition as the body of the request, rather than in the URL. The acquire embed session endpoint process validates, and then creates or updates, the embed user. It also can accept an existing session reference token. This is important as it allows multiple Looker embedded iframes to share the same session. The embed user won't be updated if a session reference token is provided and the session has not expired. This supports the use case where one iframe is created using a signed embed URL and other iframes are created without a signed embed URL. In this case, the iframes without signed embed URLs will inherit the cookie from the first session.
  5. The Looker API call returns four tokens, each with a time to live (TTL): 
     * Authorization token (TTL = 30 seconds)
     * Navigation token (TTL = 10 minutes)
     * API token (TTL = 10 minutes)
     * Session reference token (TTL = remaining lifetime of the session)
  6. The embedding application server must keep track of the data that is returned by the Looker data and associate it with both the calling user and the user agent of the calling user's browser. Suggestions for how to do this are provided in the Generate tokens section of this document. This call will return the authorization token, a navigation token, and an API token, along with _all_ the associated TTLs. The session reference token should be secured and not exposed in the calling browser.
  7. Once the tokens have been returned to the browser, a Looker embed login URL must be constructed. The Looker Embed SDK will construct the embed login URL automatically. To use the `windows.postMessage` API to construct the embed login URL, see the Using the Looker `windows.postMessage` API section of this document for examples.
The login URL does not contain the signed embed user detail. It contains the target URI, including the navigation token, and the authorization token as a query parameter. The authorization token must be used within 30 seconds and can be used only once. If additional iframes are required, an embed session must be acquired again. However, if the session reference token is provided, the authorization token will be associated with the same session.
  8. The Looker embed login endpoint determines if the login is for cookieless embed, which is denoted by the presence of the authorization token. If the authorization token is valid, it checks the following:
     * The associated session is still valid.
     * The associated embed user is still valid.
     * The browser user agent that is associated with the request matches the browser agent that is associated with the session.
  9. If the checks from the previous step pass, the request is redirected using the target URI that is contained in the URL. This is the same process as for the Looker signed embed login.
  10. This request is the redirect to launch the Looker dashboard. This request will have the navigation token as a parameter.
  11. Before the endpoint is executed, the Looker server looks for the navigation token in the request. If the server finds the token, it checks for the following:
     * The associated session is still valid.
     * The browser user agent that is associated with the request matches the browser agent that is associated with the session.
If valid, the session is restored for the request and the dashboard request runs.
  12. The HTML to load the dashboard is returned to the iframe.
  13. The Looker UI that is running in the iframe determines that the dashboard HTML is a cookieless embed response. At that point, the Looker UI sends a message to the embedding application to request the tokens that were retrieved in step 6. The UI then waits until it receives the tokens. If the tokens don't arrive, a message is displayed.
  14. The embedding application sends the tokens to the Looker embedded iframe.
  15. When the tokens are received, the Looker UI that is running in the iframe starts the process to render the request object. During this process, the UI will make API calls to the Looker server. The API token that was received in step 15 is automatically injected as a header into all API requests.
  16. Before any endpoint is executed, the Looker server looks for the API token in the request. If the server finds the token, the server checks for the following:
     * The associated session is still valid.
     * The browser user agent that is associated with the request matches the browser agent that is associated with the session.
If the session is valid, it is restored for the request, and the API request runs.
  17. Dashboard data is returned.
  18. The dashboard is rendered.
  19. The user has control over the dashboard.


### Generating new tokens
The following sequence diagram illustrates the generation of new tokens.
  1. The Looker UI that is running in the embedded iframe monitors the TTL of the embed tokens.
  2. When the tokens approach expiration, the Looker UI sends a refresh token message to the embedding application client.
  3. The embedding application client then requests new tokens from an endpoint that is implemented in the embedding application server. The Looker Embed SDK will request new tokens automatically, but the endpoint URL or a callback function must be provided. If the callback function is used, it will call the embedding application server to generate new tokens. Otherwise, the Embed SDK will call the provided endpoint URL.
  4. The embedding application finds the `session_reference_token` that is associated with the embed session. The example that is provided in the Looker Embed SDK Git repository uses session cookies, but a distributed server-side cache, Redis for example, can also be used.
  5. The embedding application server calls the Looker server with a request to generate tokens. This request also requires recent API and navigation tokens in addition to the user agent of the browser that initiated the request.
  6. The Looker server validates the user agent, the session reference token, the navigation token, and the API token. If the request is valid, new tokens are generated.
  7. The tokens are returned to the calling embedding application server.
  8. The embedding application server strips the session reference token from the response and returns the remaining response to the embedding application client.
  9. The embedding application client sends the newly generated tokens to the Looker UI. The Looker Embed SDK will do this automatically. Embedding application clients that use the `windows.postMessage` API will be responsible for sending the tokens. Once the Looker UI receives the tokens, they will be used in subsequent API calls and page navigations.


## Implementing Looker cookieless embed
Looker cookieless embed can be implemented by using either the Looker Embed SDK or the `windows.postMessage` API. You can use the Looker Embed SDK method, but an example showing how to use the `windows.postMessage` API is also available. Detailed explanations of both implementations can be found in the Looker Embed SDK README file. The Embed SDK git repository also contains working implementations.
### Configuring the Looker instance
Cookieless embedding has commonality with Looker signed embedding. To use cookieless embedding, an admin must enable **Embed SSO Authentication**. However, unlike Looker signed embedding, cookieless embedding does not use the **Embed Secret** setting. Cookieless embedding uses a JSON Web Token (JWT) in the form of an **Embed JWT Secret** setting, which can be set or reset on the **Embed** page in the **Platform** section of the **Admin** menu.
Setting the JWT secret is _not_ required, since the very first attempt to create a cookieless embed session will create the JWT. Avoid resetting this token, as doing so will invalidate all active cookieless embed sessions.
Unlike the embed secret, the embed JWT secret is never exposed, as it is only used internally in the Looker server.
### Application client implementation
This section includes examples of how to implement cookieless embedding in the application client and contains the following subsections:
  * Installing and updating the Looker Embed SDK
  * Using the Looker Embed SDK
  * Using the Looker `windows.postMessage` API


#### Installing or updating the Looker Embed SDK
The following Looker SDK versions are required to use cookieless embedding:
```
@looker/embed-sdk=2.0.0
@looker/sdk=22.16.0

```

#### Using the Looker Embed SDK
A new initialization method has been added to the Embed SDK to initiate the cookieless session. This method accepts either two URL strings or two callback functions. The URL strings should reference endpoints in the embedding application server. Implementation details of these endpoints on the application server are covered in the Application server implementation section of this document.
```
getEmbedSDK().initCookieless(
runtimeConfig.lookerHost,
'/acquire-embed-session',
'/generate-embed-tokens'
)

```

The following example shows how callbacks are used. Callbacks should only be used when it is necessary for the embedding client application to know the status of the Looker embedding session. You can also use the `session:status` event, making it unnecessary to use callbacks with the Embed SDK.
```
constacquireEmbedSessionCallback=
async():Promise<LookerEmbedCookielessSessionData>=>{
constresp=awaitfetch('/acquire-embed-session')
if(!resp.ok){
console.error('acquire-embed-session failed',{resp})
thrownewError(
`acquire-embed-session failed: ${resp.status}${resp.statusText}`
)
}
return(awaitresp.json())asLookerEmbedCookielessSessionData
}

constgenerateEmbedTokensCallback=
async({api_token,navigation_token}):Promise<LookerEmbedCookielessSessionData>=>{
constresp=awaitfetch('/generate-embed-tokens',{
method:'PUT',
headers:{'content-type':'application/json'},
body:JSON.stringify({api_token,navigation_token}),
})
if(!resp.ok){
console.error('generate-embed-tokens failed',{resp})
thrownewError(
`generate-embed-tokens failed: ${resp.status}${resp.statusText}`
)
}
return(awaitresp.json())asLookerEmbedCookielessSessionData
}

getEmbedSDK().initCookieless(
runtimeConfig.lookerHost,
acquireEmbedSessionCallback,
generateEmbedTokensCallback
)

```

#### Using the Looker `windows.postMessage` API
You can view a detailed example of using the `windows.postMessage` API in the `message_example.ts` and `message_utils.ts` files in the Embed SDK Git repository. Highlights of the example are detailed here.
The following example demonstrates how to build the URL for the iframe. The callback function is identical to the `acquireEmbedSessionCallback` example seen previously.
```
privateasyncgetCookielessLoginUrl():Promise<string>{
const{authentication_token,navigation_token}=
awaitthis.embedEnvironment.acquireSession()
consturl=this.embedUrl.startsWith('/embed')
?this.embedUrl
:`/embed${this.embedUrl}`
constembedUrl=newURL(url,this.frameOrigin)
if(!embedUrl.searchParams.has('embed_domain')){
embedUrl.searchParams.set('embed_domain',window.location.origin)
}
embedUrl.searchParams.set('embed_navigation_token',navigation_token)
consttargetUri=encodeURIComponent(
`${embedUrl.pathname}${embedUrl.search}${embedUrl.hash}`
)
return`${embedUrl.origin}/login/embed/${targetUri}?embed_authentication_token=${authentication_token}`
}

```

The following example demonstrates how to listen for token requests, generate new tokens, and send them to Looker. The callback function is identical to the previous `generateEmbedTokensCallback` example.
```
this.on(
'session:tokens:request',
this.sessionTokensRequestHandler.bind(this)
)

privateconnected=false

privateasyncsessionTokensRequestHandler(_data:any){
constcontentWindow=this.getContentWindow()
if(contentWindow){
if(!this.connected){
// When not connected the newly acquired tokens can be used.
constsessionTokens=this.embedEnvironment.applicationTokens
if(sessionTokens){
this.connected=true
this.send('session:tokens',this.embedEnvironment.applicationTokens)
}
}else{
// If connected, the embedded Looker application has decided that
// it needs new tokens. Generate new tokens.
constsessionTokens=awaitthis.embedEnvironment.generateTokens()
this.send('session:tokens',sessionTokens)
}
}
}

send(messageType:string,data:any={}){
constcontentWindow=this.getContentWindow()
if(contentWindow){
constmessage:any={
type:messageType,
...data,
}
contentWindow.postMessage(JSON.stringify(message),this.frameOrigin)
}
returnthis
}

```

### Application server implementation
This section includes examples of how to implement cookieless embedding in the application server and contains the following subsections:
  * Basic implementation
  * Acquire session
  * Generate tokens
  * Implementation considerations


#### Basic implementation
The embedding application is required to implement two server-side endpoints that will invoke Looker endpoints. This is to ensure that the session reference token remains secure. These are the endpoints:
  1. Acquire session — If a session reference token already exists and is still active, requests for a session will join the existing session. Acquire session is called when an iframe is created.
  2. Generate tokens — Looker triggers calls to this endpoint periodically.


#### Acquire session
This example in TypeScript uses the session to save or restore the session reference token. The endpoint does not have to be implemented in TypeScript.
```
app.get(
'/acquire-embed-session',
asyncfunction(req:Request,res:Response){
try{
constcurrent_session_reference_token=
req.sessionreq.session.session_reference_token
constresponse=awaitacquireEmbedSession(
req.headers['user-agent']!,
user,
current_session_reference_token
)
const{
authentication_token,
authentication_token_ttl,
navigation_token,
navigation_token_ttl,
session_reference_token,
session_reference_token_ttl,
api_token,
api_token_ttl,
}=response
req.session!.session_reference_token=session_reference_token
res.json({
api_token,
api_token_ttl,
authentication_token,
authentication_token_ttl,
navigation_token,
navigation_token_ttl,
session_reference_token_ttl,
})
}catch(err:any){
res.status(400).send({message:err.message})
}
}
)

asyncfunctionacquireEmbedSession(
userAgent:string,
user:LookerEmbedUser,
session_reference_token:string
){
awaitacquireLookerSession()
try{
constrequest={
...user,
session_reference_token:session_reference_token,
}
constsdk=newLooker40SDK(lookerSession)
constresponse=awaitsdk.ok(
sdk.acquire_embed_cookieless_session(request,{
headers:{
'User-Agent':userAgent,
},
})
)
returnresponse
}catch(error){
console.error('embed session acquire failed',{error})
throwerror
}
}

```

Starting in Looker 23.8, the embed domain can be included when the cookieless session is acquired. This is an alternative to adding the embed domain using the Looker **Admin > Embed** panel. Looker saves the embed domain in the Looker internal database, so it won't be shown on the **Admin > Embed** panel. Instead, the embed domain is associated with the cookieless session and exists for the duration of the session only. Review the security best practices if you decide to take advantage of this feature.
#### Generate tokens
This example in TypeScript uses the session to save or restore the session reference token. The endpoint does not have to be implemented in TypeScript.
It is important that you know how to handle 400 responses, which occur when tokens are invalid. Although a 400 response being returned shouldn't happen, if it does, it is best practice to terminate the Looker embed session. You can terminate the Looker embed session by either destroying the embed iframe or by setting the `session_reference_token_ttl` value to zero in the `session:tokens` message. If you set the `session_reference_token_ttl` value to zero, the Looker iframe displays a session expired dialog.
A 400 response is not returned when the embed session expires. If the embed session has expired, a 200 response is returned with the `session_reference_token_ttl` value set to zero.
```
app.put(
'/generate-embed-tokens',
asyncfunction(req:Request,res:Response){
try{
constsession_reference_token=req.session!.session_reference_token
const{api_token,navigation_token}=req.bodyasany
consttokens=awaitgenerateEmbedTokens(
req.headers['user-agent']!,
session_reference_token,
api_token,
navigation_token
)
res.json(tokens)
}catch(err:any){
res.status(400).send({message:err.message})
}
}
)
}
asyncfunctiongenerateEmbedTokens(
userAgent:string,
session_reference_token:string,
api_token:string,
navigation_token:string
){
if(!session_reference_token){
console.error('embed session generate tokens failed')
// missing session reference  treat as expired session
return{
session_reference_token_ttl:0,
}
}
awaitacquireLookerSession()
try{
constsdk=newLooker40SDK(lookerSession)
constresponse=awaitsdk.ok(
sdk.generate_tokens_for_cookieless_session(
{
api_token,
navigation_token,
session_reference_token:session_reference_token||'',
},
{
headers:{
'User-Agent':userAgent,
},
}
)
)
return{
api_token:response.api_token,
api_token_ttl:response.api_token_ttl,
navigation_token:response.navigation_token,
navigation_token_ttl:response.navigation_token_ttl,
session_reference_token_ttl:response.session_reference_token_ttl,
}
}catch(error:any){
if(error.message?.includes('Invalid input tokens provided')){
// The Looker UI does not know how to handle bad
// tokens. This shouldn't happen but if it does expire the
// session. If the token is bad there is not much that that
// the Looker UI can do.
return{
session_reference_token_ttl:0,
}
}
console.error('embed session generate tokens failed',{error})
throwerror
}

```

#### Implementation considerations
The embedding application must keep track of the session reference token and must keep it secure. This token should be associated with the embedded application user. The embedding application token can be stored in one of the following ways:
  * In the embedded application user's session
  * In a server-side cache that is available across a clustered environment
  * In a database table that is associated with the user


If the session is stored as a cookie, the cookie should be encrypted. The example in the embed SDK repository uses a session cookie to store the session reference token.
When the Looker embed session expires, a dialog will be displayed in the embedded iframe. At this point, the user won't be able to do anything in the embedded instance. When this occurs, the `session:status` events will be generated, allowing the embedding application to detect the current state of the embedded Looker application and take some kind of action.
An embedding application can detect if the embed session has expired by checking if the `session_reference_token_ttl` value that is returned by the `generate_tokens` endpoint is zero. If the value is zero, then the embed session has expired. Consider using a callback function for generating tokens when the cookieless embed is initializing. The callback function can then determine if the embed session has expired and will destroy the embedded iframe as an alternative to using the default embedded session expired dialog.
### Running the Looker cookieless embed example
The embed SDK repository contains a node express server and client written in TypeScript that implements an embed application. The examples shown previously are taken from this implementation. The following assumes that your Looker instance has been configured to use cookieless embed as described earlier.
You can run the server as follows:
  1. Clone the Embed SDK repository — `git clone git@github.com:looker-open-source/embed-sdk.git`
  2. Change the directory — `cd embed-sdk`
  3. Install the dependencies — `npm install`
  4. Configure the server, as shown in the Configure the server section of this document.
  5. Run the server — `npm run server`


#### Configure the server
Create a `.env` file in the root of the cloned repository (this is included in `.gitignore`).
The format is as follows:
```
LOOKER_WEB_URL=your-looker-instance-url.com
LOOKER_API_URL=https://your-looker-instance-url.com
LOOKER_DEMO_HOST=localhost
LOOKER_DEMO_PORT=8080
LOOKER_EMBED_SECRET=embed-secret-from-embed-admin-page
LOOKER_CLIENT_ID=client-id-from-user-admin-page
LOOKER_CLIENT_SECRET=client-secret-from-user-admin-page
LOOKER_DASHBOARD_ID=id-of-dashboard
LOOKER_LOOK_ID=id-of-look
LOOKER_EXPLORE_ID=id-of-explore
LOOKER_EXTENSION_ID=id-of-extension
LOOKER_VERIFY_SSL=true
LOOKER_REPORT_ID=id-of-report
LOOKER_QUERY_VISUALIZATION_ID=id-of-query-visualization

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


