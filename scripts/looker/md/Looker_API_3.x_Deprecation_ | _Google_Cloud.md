# Looker API 3.x Deprecation  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/api-3x-deprecation

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * API 3.x will be disabled in August 2023
  * Who should read this?
  * What do I need to do?
  * API 4.0 Migration Details
    * Changing your code to point to the new API
    * API 3.x Endpoint Replacements
    * API 4.0 Breaking ID Field Types
  * Disabling/Enabling API 3.x via Legacy Feature Toggle




Was this helpful?
Send feedback 
#  Looker API 3.x Deprecation
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * API 3.x will be disabled in August 2023
  * Who should read this?
  * What do I need to do?
  * API 4.0 Migration Details
    * Changing your code to point to the new API
    * API 3.x Endpoint Replacements
    * API 4.0 Breaking ID Field Types
  * Disabling/Enabling API 3.x via Legacy Feature Toggle


### API 3.x will be disabled in August 2023
Previously, we had communicated that this change would happen in the July 2023 release. Based on customer feedback, we've moved this deadline back to August 2023 to help make this transition smoother. Close this dialog for further details.
Close
Following our API 4.0 GA release in Looker 22.4, we announced the deprecation of our 3.1 API, in addition to our already deprecated 3.0 API.
As of our deprecation announcement in June 2022, both the 3.1 API and the 3.0 API, referred to as 3.x, are in deprecated status. The 3.x API versions will be disabled starting with the release of Looker version 23.14 in August 2023.
**This upgrade will be rolled out to Looker-hosted instances during maintenance hours between August 14 and August 24.** As a result, **all Looker-hosted instances** must upgrade their applications to use 4.0 API endpoints instead of 3.x API endpoints before August 14, 2023. Any functionality relying on 3.x endpoints will cease to work after this change.
If your instance is self-hosted, you must upgrade your applications before upgrading your Looker instance to version 23.14 or later.
The 4.0 API fully covers the functionality offered by the deprecated APIs, and we expect the upgrade from 3.x to 4.0 to be straightforward for most customers.
Customers who are not able to successfully migrate to API 4.0 should contact Looker Support.
## Timeline
  * Pre-2022: API 3.0 is in deprecated status, 3.1 is in stable status, and 4.0 is in beta status
  * March 2022: API 4.0 enters stable status and is generally available in Looker 22.4
  * June 2022: API 3.1 deprecation is announced
  * August 2023: API 3.x will be turned off in Looker


## Who should read this?
This document is for you if you use the Looker API through Looker-supported SDKs, Community-supported SDKs, or the API itself. Continue reading to learn about breaking changes that may affect your application and learn
## What do I need to do?
You'll need to make the following changes to your code. These are described in further detail later on this page.
  * Change your code to point to the new API.
  * Identify usage of removed endpoints and replace those references with the API 4.0 equivalent.
  * Update ID values that were previously expressed as numbers to be expressed as strings.


## API 4.0 Migration Details
### Changing your code to point to the new API
When making API calls directly via command line or programs like Postman, you'll need to adjust the URL you're using to make the request.
```
### API 3.1 ###
GET https://myinstance.looker.com/api/3.1/users/5877

### API 4.0 ###
GET https://myinstance.looker.com/api/4.0/users/5877

```

If you're using one of our SDKs, you'll need to make sure that you're initializing the correct version of the SDK. Here's a basic example of how the beginning of a Python script might look using our SDK in both versions:
```
### API 3.1 ###
importlooker_sdk
sdk = looker_sdk.init31()

### API 4.0 ###
importlooker_sdk
sdk = looker_sdk.init40()

```

Once you've made the change to the 4.0 API, it's time to test your code and look out for the following changes.
### API 3.x Endpoint Replacements
In order to keep terminology consistent between the Looker API and Looker UI, API 4.0 replaces a few deprecated API 3.x endpoints with equivalent or improved endpoints, listed below:
#### "Space" endpoints have been renamed. Use synonymous "Folder" endpoints instead.
  * Review folder feature documentation.
  * Refer to the list of folder API endpoints.


#### Python SDK Example
```
    #####################
    ##### API 3 #########
    #####################

    # Create Folder in Shared Folders
    response = sdk.create_space(
      body=mdls.CreateSpace(
        name="My New Folder",
        parent_id="1"
      )
    )

    # Get Folder info by ID
    response = sdk.space(space_id="555")

    # Change name of existing Folder
    response = sdk.update_space(
      space_id="555",
      body=mdls.UpdateSpace(
        name="My Updated Folder"
      )
    )

    #####################
    ##### API 4 #########
    #####################

    # Create Folder in Shared Folders
    response = sdk.create_folder(
      body=mdls.CreateFolder(
        name="My New Folder",
        parent_id="1"
      )
    )

    # Get Folder info by ID
    response = sdk.folder(folder_id="555")

    # Change name of existing Folder
    response = sdk.update_folder(
      space_id="555",
      body=mdls.UpdateFolder(
        name="My Updated Folder"
      )
    )
    
```

#### cURL Example
```
####################
#### API 3 #########
####################

Get    curl -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" https://myinstance.looker.com/api/3.1/spaces/555

Change    curl -X PATCH https://myinstance.looker.com/api/3.1/spaces/555 -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" -H "Content-Type: application/json" -d "{\"name\": \"My Updated Space\"}"

####################
#### API 4 #########
####################

Get    curl -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" https://myinstance.looker.com/api/4.0/folders/555

Change    curl -X PATCH https://myinstance.looker.com/api/4.0/folders/555 -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" -H "Content-Type: application/json" -d "{\"name\": \"My Updated Space\"}"

```

#### "Homepage" endpoints have been removed. Use expanded functionality "board" endpoints instead.
  * Review board feature documentation.
  * Refer to the list of board API endpoints.


#### Python SDK Example
```
    #####################
    ##### API 3 #########
    #####################

    # Get Board info by ID
    response = sdk.homepage(homepage_id=1348)

    # Update displayed title of Board item
    response = sdk.update_homepage_item(
      homepage_item_id=86,
      body=mdls.WriteHomepageItem(
        custom_title="Volume 3"
      )
    )

    #####################
    ##### API 4 #########
    #####################

    # Get Board info by ID
    response = sdk.board(board_id=1348)

    # Update displayed title of Board item
    response = sdk.update_board_item(
      board_item_id=86,
      body=mdls.WriteBoardItem(
        custom_title="Volume 3"
      )
    )
    
```

#### cURL Example
```
####################
#### API 3 #########
####################

Get    curl -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" https://myinstance.looker.com/api/3.1/homepages/1348

Update    curl -X PATCH https://myinstance.looker.com/api/3.1/homepage_items/86 -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" -H "Content-Type: application/json" -d "{\"custom_title\": \"Volume 3\"}"

####################
#### API 4 #########
####################

Get    curl -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" https://myinstance.looker.com/api/4.0/boards/1348

Update    curl -X PATCH https://myinstance.looker.com/api/4.0/boards/86 -H "Authorization: token Tg7gjGZD7B8c3k7g6XtmbcyYrQgMrXpjkR25dQ2G" -H "Content-Type: application/json" -d "{\"custom_title\": \"Volume 3\"}"

```

### API 4.0 Breaking ID Field Types
API 4.0 has updated types for some ID fields from numbers to strings. Use our API reference diff tool to determine which ID fields have changed between 3.1 and 4.0. Use up-to-date (23.0+) Looker-supported language SDKs to ensure your applications are type correct during and after migration. Most community-supported language SDKs, including Kotlin, Swift, R, C# and Go, already work with the updated types as well.
Developers who are using custom libraries should search their code for references to these fields to ensure that they are appropriately handled.
## API 4.0 Diff
In addition to the guidelines listed on this documentation page, the Looker API Explorer provides a full listing of all differences between the 3.x APIs and 4.0 API.
## Disabling/Enabling API 3.x via Legacy Feature Toggle
**For Looker-hosted customers using Looker 23.6, 23.8, 23.10, and 23.12** , Admins currently have the ability to disable all calls to API 3 endpoints. This will allow you to test on your instance to ensure no integrated services or applications break ahead of the August 14 deadline. To do so, you can toggle on "Deny API 3.x requests" in the Legacy Features Admin panel.
**Self-hosted customers using Looker 23.6, 23.8, 23.10, and 23.12** can execute the following shell command before starting Looker to add an environment variable which will make the "Deny API 3.x requests" toggle visible (Note: After executing the command, you'll still have to switch the toggle in the Legacy Features panel in the Looker UI in order to stop API 3 calls.):
```
export FF_DENY_API3=true

```

## FAQ
**I'm unsure if there are API 3.x calls being made on my instance. How can I find this information?**
As of Looker 23.8, the Source column in the Admin > Queries panel now correctly displays the API version (v3 or v4) for queries that are initiated from the Looker API. This will not include information about Admin or Developer tasks such as creating users or LookML development/Git tasks.
Our internal reporting service has more detailed information on API requests, including those used to complete Admin and LookML Development tasks. Customers with instances following the recommended networking configuration can reach out to Looker Support to request an export of this data.
**I host my own instance. Do I need to upgrade by August 14, 2023?**
If your instance is self-hosted, you'll need to make the changes before you upgrade to the August 2023 release (version 23.14) or any subsequent release. We recommend you start doing this work as soon as possible, so that you are able to stay on a supported release for the best experience with Looker.
**My instance is Looker-hosted, but on the ESR program. Do I need to upgrade by August 14, 2023?**
You'll need to make the changes before your instance is upgraded to the August 2023 release (version 23.14) or any subsequent release. We recommend you start doing this work as soon as possible, so that you are not pressed for time when your instance is slated to receive that upgrade.
**I've read over the documentation but I'm still having issues or am unsure how to proceed.**
Customers who are not able to successfully migrate to API 4.0 should contact Looker Support.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


