# Formatting your fields - Lightdash

**Source:** https://docs.lightdash.com/guides/formatting-your-fields

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Guides
Formatting your fields
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
    * Interacting with your dashboards
    * Using the Slack integration
    * Scheduled deliveries
    * Chart Version History
    * Formatting your fields
    * How to promote content
    * Table calculation SQL templates
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment


##### Contact


On this page
  * Formatting your fields in your .yml files
  * The metrics and dimensions reference docs
  * Hiding fields
  * Grouping fields in the sidebar
  * Adding custom descriptions
  * Renaming fields
  * Rounding dimensions
  * Rounding metrics
  * Compacting big numbers
  * Compact dimensions
  * Compact metrics
  * Add units to your values
  * Add units to dimensions
  * Add units to metrics
  * Formatting your fields in the Lightdash UI
  * Formatting metrics
  * Formatting table calculations


##  Formatting your fields in your .yml files
Sometimes the format of things in your dbt project is different to how you want it to look in Lightdash. That’s okay! We’ve built a bunch of features to help you to format the fields in your dbt project so that the data in your Lightdash project looks exactly like you want it to 🥸
###  The metrics and dimensions reference docs
We’re going to go through formatting your fields in more detail below, but you can see a list of these configurations and all of the other properties you can customize for your fields in the dimensions reference doc and metrics reference doc.
###  Hiding fields
Sometimes, we have a bunch of columns in our YAML files that we might not want to include in Lightdash. For example, columns with PII data, or the same date data, but at different levels of date granularity. It’s easy to hide columns from Lightdash. All you need to do is add two words to your column: `hidden: true`. In your dbt YAML file, it’ll look something like this:
Copy
Ask AI
```
models:
name: users
    columns:
name: first_name
        meta:
          dimension:
            hidden: true

```

The same thing goes for metrics:
Copy
Ask AI
```
models:
name: users
    columns:
name: first_name
        meta:
          metrics:
            count_unique_first_names:
              type: count_distinct
              hidden: true

```

By default, all of your dimensions and metrics have been set to `hidden: false`.
###  Grouping fields in the sidebar
You can group related metrics and dimensions together using the model meta `group_details` block in combination with the `groups` property in your .yaml files. You can as well add descriptions to your groups using the property `description` that will be displayed when hovering over the group label.
**Max grouping levels.** There is a max of 2 levels of grouping in the sidebar.
For example you might want to group the percentile metrics into two sub categories one being for over 40 percentiles and the other for under 40 percentiles. You can do this by adding the `group` property to your metrics like so:
Copy
Ask AI
```
models:
name: events
    meta:
      group_details:
        events:
          label: Events
          description: Event-related fields.
        percentile:
          label: Percentiles
          description: Grouping of percentiles

          label: Percentiles under 40
          description: Grouping of percentiles under 40
        over:
          label: Percentiles over 40
          description: Grouping percentiles over 40
    columns:
name: event_id
        description: ''
        meta:
          dimension:
            type: number
            groups: ['events']
          metrics:
            percentile_25:
              type: percentile
              percentile: 25
              groups: ['percentile', 'sub']
            percentile_50:
              type: percentile
              percentile: 50
              groups: ['percentile', 'over']
            percentile_75:
              type: percentile
              percentile: 75
              groups: ['percentile', 'over']

```

You can use groups across metrics and dimensions. In the sidebar, your metrics will get grouped together under your label in the `metrics` section, and your dimensions will get grouped together under your label in the `dimensions` section.
###  Adding custom descriptions
####  Dimensions
By default, Lightdash pulls in the descriptions you’ve included for your dimensions. But, you can override the description you see in Lightdash using the `description` property.
Copy
Ask AI
```
models:
name: users
    columns:
name: user_id
        description: "Id generated by the Lightdash API on user's first login. On legacy systems, SHA64. On new systems since 2012, FARM_FINGERPRINT()"
        meta:
          dimension:
            description: 'Unique identifier for a user'

```

You can see the descriptions of your dimensions when you hover over the fields in Lightdash.
####  Metrics
If you don’t add a custom description for your metric, Lightdash will show a description for you in the app, by default. To override this default description, you can use the `description` property.
Copy
Ask AI
```
models:
name: users
    columns:
name: user_id
        description: "Id generated by the Lightdash API on user's first login. On legacy systems, SHA64. On new systems since 2012, FARM_FINGERPRINT()"
        meta:
          metrics:
            count_unique_users:
              type: count_distinct
              description: 'Count the unique number of user IDs'

```

Check out this doc to see all of the other properties you can customize for metrics.
###  Renaming fields
Sometimes, the labels we use for the fields in our dbt project aren’t very user friendly. We might want to change these in Lightdash, and we can! To change the name you’ll see for your field in Lightdash, you just use the `label` property. So, if I had a field `user_id_sha64`, I could relabel it to `User ID`.
Copy
Ask AI
```
models:
name: users
    columns:
name: user_id_sha64
        meta:
          dimension:
            label: 'User ID'

```

Same thing goes for metrics!
Relabelling a metric will not break any saved charts that use the old metric name. Instead, your saved charts will just use the new metric name in their results tables.
Copy
Ask AI
```
models:
name: users
    columns:
name: user_id_sha64
        meta:
          metrics:
            count_unique_user_ids:
              type: count_distinct
              label: 'Total users'

```

Check out this doc to see all of the other properties you can customize for dimensions, and this one for all of the other properties you can customize for your metrics.
###  Rounding
Rounding your metrics is easy to do using the `format` property in your YAML file. Here’s an example of how different rounding will affect your numbers: Original number | Format value | How it will appear in Lightdash  
---|---|---  
121.854 | ’0.00’ | 121.85  
121.854 | ’0.0’ | 121.9  
121.854 | ’0’ | 123  
####  Rounding dimensions
Like this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          dimension:
            format: '0.00'

```

####  Rounding metrics
Like this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          metrics:
            total_revenue:
              type: sum
              format: '0.00'

```

Check out this doc to see all of the other properties you can customize for metrics.
###  Compacting big numbers
Here’s an example of how different compacting will affect your numbers: Original number | Format value | How it will appear in Lightdash  
---|---|---  
1000000000 | ’0’ | 1000000000  
1000000000 | ’0,” K“‘ | 1000000K  
1000000000 | ’0,,” M“‘ | 1000M  
####  Compact dimensions
Like this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          dimension:
            format: '0," K"'

```

As an example, this option will compact the number value from 1,500 to 1.50K. Check out this doc to see all the other compact values. to see all the other formatting options.
####  Compact metrics
Like this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          metrics:
            total_revenue:
              type: sum
              format: '0.00,,," B"'

```

As an example, this option will compact the number value from 1,500,000,000 to 1.50B. Check out this doc to see all the other formatting options.
###  Add units to your values
Some columns need a special format to convey what units they’re in. For example, if you’re a global company, and you have a `revenue` field. Is that in GBP? USD? In Lightdash, you can use the `format` label to add units to your fields. Here’s an example of how different formats will affect your values: Original value | Format value | How it will appear in Lightdash  
---|---|---  
121.854 | ’[$£]#,##0.00’ | £121.85  
121.854 | ’$#,##0.00’ | $121.90  
####  Add units to dimensions
You can add a `format` to your dimensions this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          dimension:
            format: '[$£]#,##0.00'

```

To see which format types are available for dimensions, check the reference docs here.. Check out this doc to see all of the other properties you can customize for dimensions.
####  Add units to metrics
You can add a `format` to your metrics this:
Copy
Ask AI
```
models:
name: sales
    columns:
name: revenue
        meta:
          metrics:
            total_revenue:
              type: sum
              format: '[$£]#,##0.00'

```

To see which format types are available for metrics, check the reference docs here.Check out this doc to see all of the other properties you can customize for metrics.
##  Formatting your fields in the Lightdash UI
You can also format your fields in the Lightdash UI. This is useful if you want to format your fields quickly without having to change your YAML files. Currently you can format 2 types of fields in the Lightdash UI:
  * Custom metrics (reference)
  * Table calculations (reference)


###  Formatting metrics
Metrics formatting is currently only available for numeric metric types.
You can adjust the formatting of your pre-defined metrics from the results table. You can customize the formatting of your custom metrics when you create them, and later on from the results table. These are the formatting options available:
  * `percent`: Formats your metric as a percentage, with the following options:
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
  * `currency`: Formats your metric as a currency
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
    * `currency` symbol, e.g. from `$` to `£`
    * `compact` value to compact your metric to a certain unit, e.g. from `1,000,000` to `1M`
  * `number`: Formats your metric as a number
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
    * `compact` value to compact your metric to a certain unit, e.g. from `1,000,000` to `1M`
    * `prefix` value to add a prefix to your metric, e.g. `+` or `-`
    * `suffix` value to add a suffix to your metric, e.g. `%`


###  Formatting table calculations
On the results table, you can add a table calculation by clicking on the button on the right hand side of the section. Once you’ve created your table calculation, you can format it by clicking on the `Format` tab: You can then choose from the following formatting types:
  * `percent`: Formats your metric as a percentage, with the following options:
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
  * `currency`: Formats your metric as a currency
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
    * `currency` symbol, e.g. from `$` to `£`
    * `compact` value to compact your metric to a certain unit, e.g. from `1,000,000` to `1M`
  * `number`: Formats your metric as a number
    * `round` value to your metric to round it to a certain number of decimal places
    * `separator`, e.g. from `.` to `,`
    * `compact` value to compact your metric to a certain unit, e.g. from `1,000,000` to `1M`
    * `prefix` value to add a prefix to your metric, e.g. `+` or `-`
    * `suffix` value to add a suffix to your metric, e.g. `%`


Chart Version HistoryHow to promote content
Assistant
Responses are generated using AI and may contain mistakes.


