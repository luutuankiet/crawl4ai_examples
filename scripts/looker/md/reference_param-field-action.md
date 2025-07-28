# action  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/param-field-action

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Definition
    * Passing user attributes to the receiving server using user_attribute_param
    * Passing values to the receiving server using param
    * Specifying form behavior using form_url or form_param
    * Using a data action without a form
    * Server responses
  * Consider using the Looker Action Hub




Was this helpful?
Send feedback 
#  action
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Definition
    * Passing user attributes to the receiving server using user_attribute_param
    * Passing values to the receiving server using param
    * Specifying form behavior using form_url or form_param
    * Using a data action without a form
    * Server responses
  * Consider using the Looker Action Hub


## Usage
```
view: view_name {
  dimension: field_name {
    action:  {
      label: "Label to Appear in Action Menu"
      url: "https://example.com/posts"
      icon_url: "https://looker.com/favicon.ico"
      form_url: "https://example.com/ping/{{ value }}/form.json"
      param: {
        name: "name string"
        value: "value string"
      }
      form_param: {
        name:  "name string"
        type: textarea | string | select
        label:  "possibly-localized-string"
        option: {
          name:  "name string"
          label:  "possibly-localized-string"
        }
        required:  yes | no
        description:  "possibly-localized-string"
        default:  "string"
      }
      user_attribute_param: {
        user_attribute: user_attribute_name
        name: "name_for_json_payload"
      }
    }
  }
}

```

Hierarchy `action` |  Possible Field Types Dimension, MeasureDefault Value NoneAccepts Various parametersSpecial Rules
  * The `form_url`'s URL must be accessible to the Looker server and use HTTPS with a valid certificate
  * The `icon_url`'s URL must be accessible to the user's browser

  
---|---  
## Definition
The `action` parameter creates a data action that lets users perform field-level tasks in other tools, directly from Looker. For example, the action can cause an email to be sent, set values in other applications, or perform any other action that you can configure a receiving server to do. The receiving server must be able to accept a JSON POST.
You can define an `action` for a dimension or measure. You can access the action by selecting its field when you're on an Explore page, a Look, or a dashboard.
When defining an `action`, you specify the chosen behavior using the following parameters:
Parameter | Description  
---|---  
`label` | A string that specifies the name of the action as it will appear to users in the Action menu.  
`url` | A string that specifies the URL to process the action. If a **URL Allowlist for Data Actions** is specified, you must add this `url` value to the allowlist. Only URLs that match the allowlist pattern are allowed for any data action. If there are no existing entries, all URLs are allowed for data actions.  
`icon_url` | A string that specifies a URL that contains an image file to make it easier for users to understand, at a glance, where this link will direct them. The `icon_url` value must be accessible to the user's browser.  
`form_url` | A string that specifies a URL that will return a form to present to users; the form must be presented in a JSON format as described in the Specifying form behavior using `form_url` or `form_param` section on this page. The `form_url` must be accessible to the Looker server and use HTTPS with a valid certificate.  
`param` | Passes a value to the receiving server.  
`form_param` | Adds a form input that will be displayed for this action.  
`user_attribute_param` | Passes a user attribute to the receiving server. You must add the data action's `url` value to the **URL Allowlist for Data Actions** if you are using a `user_attribute_param` for your data action.  
Similar to a data action, you can also use a field-level action available from the Looker Action Hub to send data from a specific cell. See the Consider using the Looker Action Hub section on this page for more information about this option.
### Passing user attributes to the receiving server using `user_attribute_param`
You can send user attributes to the receiving server by using the `user_attribute_param` parameter. Within each `user_attribute_param` you'll specify the following subparameters:
Parameter | Type | Description  
---|---|---  
`user_attribute` | Looker ID | The name of the user attribute in Looker  
`name` | String | The name of the attribute as you want it to appear in the JSON payload  
### Passing values to the receiving server using `param`
You can send arbitrary data in your JSON payload by using the `param` parameter. Within each `param` you'll specify the following subparameters:
Parameter | Type | Description  
---|---|---  
`name` | String | Name of a parameter to pass to the receiving server  
`value` | String | Value of a parameter to pass to the receiving server  
> Do not pass sensitive data or private information, such as user credentials, in the `param` parameter. Instead, configure user credentials as a user attribute in the Admin settings, and pass this information in the `user_attribute_param` parameter.
### Specifying form behavior using `form_url` or `form_param`
You can create a form for Looker users to interact with, and then submit their form input in your JSON payload. If you display a form, it will appear as an overlay on the page (Explore, Look, or dashboard) where the action was triggered. You can do this with either the `form_url` or the `form_param` parameter.
If you want your action hub server to define the form layout, use the `form_url` parameter. The `form_url` should contain a URL that returns a JSON representation of the form as described later on this page.
If you want to define the form layout directly in the LookML, use the `form_param` parameter.
#### Form options
In both cases, the possible options that you can use to define the form are:
Option | Type | Description  
---|---|---  
`name` | String | The name of the value as it will appear in your JSON payload  
`type` | Input Type | The type of form field that will be displayed to the user:
  * `select` - displays a drop-down list
  * `string` - displays a single line input field
  * `textarea` - displays a multi-line text input box

  
`label` | String | The label for the input as it will appear to users  
`description` | String | A description for the field that will appear to users  
`required` | Boolean | Specifies whether the form option must be provided by the user before the form is submitted  
`default` | String | The starting value of the form field, if any  
`option` | String | If you choose a `type` of `select`, define the select options here  
If you set the `type` to `select`, you then specify items in the drop-down list using `option`. Each `option` includes the following details:
Option | Type | Description  
---|---|---  
`name` | String | Name of the form value as it will appear in your JSON payload  
`label` | String | The label for the option as it will appear to users (optional)  
### Using a data action without a form
If you don't include a `form_url` or `form_param` parameter in your `action` definition, the data action won't include a form. In that case, the action sends a request when a user selects that action from the **Actions** menu.
After an action without a form is selected, the **Actions** menu displays icons to the left of the action to indicate its state:
  * A loading icon appears, which shows that the action is executing. 
  * A check mark appears, which shows that the action has executed. 
  * A circled _i_ appears, which indicates that the action failed. 


If no icon appears to the left of an action, the action was not triggered.
### Server responses
A successful HTTP response will be considered a successful action.
The server can also pass a few options back to Looker regarding the success of the action. If the webhook request responds with JSON, Looker looks for a special `looker` key in the response. Everything else is ignored. For example, in:
```
{
  "my_apps_business_logic": "something",
  "looker": {
    "success": true,
    "refresh_query": true
  }
}

```

Here `success` defaults to `true` and setting `success` to `false` will indicate in Looker that the request has failed. Also, `refresh_query` defaults to `false` and setting it to `true` will rerun the current Looker query, skipping the cache.
You can also respond with validation errors for any form parameters that were passed along:
```
{
  "looker": {
    "success": false,
    "validation_errors": {
      "body": "Body must be more than 10 characters long."
    }
  }
}

```

Here `validation_errors` defaults to `{}`. This should be a JSON object where the keys are the names of the form parameters and the value is a string representing an error message for that parameter.
#### Examples
If you use the `form_url` parameter (with Liquid syntax in this example) all the options must be returned in a JSON object. For example:
```
dimension: foo {
  action: {
    label: "Send a Thing"
    url: "https://example.com/ping/\{{ value \}}"
    form_url: "https://example.com/ping/\{{ value \}}/form.json"
  }
}

```

The server should return a JSON representation of a form that matches the LookML:
```
[
  {
    "name": "title",
    "type": "select",
    "label": "desired label name",
    "description": "description text",
    "required": true,
    "default": "value string",
    "options": [
      {
        "name": "name string"
        "label": "desired label name"
      },
      {
        "name": "name string"
        "label": "desired label name"
      }
    ]
  },
  {
    "name": "title",
    "type": "textarea",
    "label": "desired label name",
    "description": "description text",
    "required": true,
    "default": "value string",
  }
]

```

If you use the `form_param` parameter, the options are used as LookML parameters. For example:
```
form_param: {
  name: "title"
  type: select
  label: "desired label name"
  option: {
    name: "name string"
    label: "desired label name"
  }
  required: yes
  description: "description text"
  default: "value string"
}

```

## Consider using the Looker Action Hub
The `action` parameter is a good choice if you don't already have a server that is set up to receive your action requests or if you want to implement a use case that has limited reusability. However, as an alternative, you may want to consider using the field-level actions that are available from the Looker Action Hub. (Make sure that your instance fulfills these Looker Action Hub requirements.)
In addition to the existing Looker Action Hub integrations, you may also create your own custom action by following the instructions on the Action hub documentation page.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


