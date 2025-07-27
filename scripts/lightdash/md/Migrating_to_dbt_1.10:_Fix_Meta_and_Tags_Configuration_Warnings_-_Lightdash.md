# Migrating to dbt 1.10: Fix Meta and Tags Configuration Warnings - Lightdash

**Source:** https://docs.lightdash.com/dbt-guides/dbt-1.10-migration

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Migrating to dbt 1.10: Fix Meta and Tags Configuration Warnings
  * Guide to package-lock.yml in dbt


  * Migrate to dbt 1.10


  * Migrate to dbt Fusion


On this page
  * What Changed in dbt 1.10?
  * Why This Change Matters
  * Automated Migration with MetaMove
  * Safe Migration Process
  * Advanced Options
  * What MetaMove Handles
  * Manual Migration (If Needed)
  * Model-Level Changes
  * Column-Level Changes
  * Source-Level Changes
  * Other dbt 1.10 Changes to Consider
  * Handling Warnings During Migration
  * Testing Your Migration
  * Best Practices
  * Troubleshooting Common Issues
  * ”Config block already exists” Errors
  * Unexpected YAML Structure
  * Performance with Large Projects


When you upgrade to dbt 1.10, you’ll likely encounter deprecation warnings that look like this:
Copy
Ask AI
```
Warning: while parsing model config: Ignore unexpected key "meta"
Warning: while parsing model config: Ignore unexpected key "tags"

```

These warnings indicate that dbt is changing how `meta` and `tags` should be structured in your YAML files. Instead of manually updating potentially hundreds of files, you can use MetaMove - a CLI tool specifically designed to automate this migration.
##  What Changed in dbt 1.10?
Starting in dbt 1.10, you will receive deprecation warnings for dbt code that will become invalid in the future, including custom inputs like unrecognized resource properties and configurations. Some properties are moving to configs, including `meta` and `tags`. The key change affects how you define `meta` and `tags` properties across your dbt project: **Before (dbt < 1.10):**
Copy
Ask AI
```
models:
name: my_model
    meta:
      owner: "Data Team"
      priority: "high"
    tags: ["core", "customer"]
    columns:
name: id
        meta:
          is_primary_key: true
        tags: ["identifier"]

```

**After (dbt 1.10+):**
Copy
Ask AI
```
models:
name: my_model
    config:
      meta:
        owner: "Data Team"
        priority: "high"
      tags: ["core", "customer"]
    columns:
name: id
        config:
          meta:
            is_primary_key: true
          tags: ["identifier"]

```

##  Why This Change Matters
Previously, dbt allowed you to configure inputs largely unconstrained. Without a set of strictly defined inputs, it becomes challenging to validate your project’s configuration, creating unintended issues such as silently ignoring misspelled properties and configurations. This change provides several benefits:
  * **Better Validation** : dbt can now catch misspelled properties and configurations
  * **Consistent Structure** : All custom attributes must be nested under the `meta` config
  * **Future-Proofing** : Prevents conflicts when dbt introduces new reserved properties


##  Automated Migration with MetaMove
Rather than manually updating your YAML files, use MetaMove - a CLI tool built specifically for this migration. MetaMove automatically transforms your files while preserving comments and formatting.
###  Installation
Install MetaMove using pipx (recommended):
Copy
Ask AI
```
pip install pipx  # if you don't have it
pipx install metamove

```

###  Basic Usage
Transform a single YAML file:
Copy
Ask AI
```
metamove models/my_model.yml

```

Transform multiple files:
Copy
Ask AI
```
metamove models/* seeds/* snapshots/*

```

Transform all YAML files in your dbt project:
Copy
Ask AI
```
metamove models/**/* seeds/**/* snapshots/**/*

```

###  Safe Migration Process
MetaMove follows a safe-by-default approach:
  1. **Test First** : By default, transformed files are saved to a `transformed` directory:
Copy
Ask AI
```
metamove models/*  # saves to ./transformed/

```

  2. **Review Changes** : Compare the original and transformed files to ensure accuracy.
  3. **Apply In-Place** : Once confident, transform files in place:
Copy
Ask AI
```
metamove models/* -i

```



###  Advanced Options
Specify a custom output directory:
Copy
Ask AI
```
metamove models/* -o my_transformed_models

```

The tool automatically processes only `.yml` and `.yaml` files, so wildcards work safely:
Copy
Ask AI
```
# Transform specific model directories
metamove models/marts/* models/staging/*
# Transform all nested directories
metamove models/**/*

```

##  What MetaMove Handles
MetaMove intelligently processes:
  * **Nested Structures** : `meta` and `tags` at any nesting level, including inside `columns`
  * **Existing Config Blocks** : Merges new values into existing `config` sections
  * **All YAML Types** : Dictionaries, lists, and scalar values
  * **Formatting Preservation** : Maintains your comments and whitespace
  * **Complex Cases** : Handles edge cases following dbt precedence rules


##  Manual Migration (If Needed)
If you prefer to migrate manually or need to understand the changes, here are the key transformations:
###  Model-Level Changes
**Before:**
Copy
Ask AI
```
models:
name: customer_metrics
    description: "Customer analytics model"
    meta:
      owner: "analytics_team"
      sla: "daily"
    tags: ["core", "customer", "metrics"]

```

**After:**
Copy
Ask AI
```
models:
name: customer_metrics
    description: "Customer analytics model"
    config:
      meta:
        owner: "analytics_team"
        sla: "daily"
      tags: ["core", "customer", "metrics"]

```

###  Column-Level Changes
**Before:**
Copy
Ask AI
```
models:
name: customers
    columns:
name: customer_id
        description: "Unique customer identifier"
        meta:
          is_primary_key: true
          data_type: "uuid"
        tags: ["pii", "identifier"]

```

**After:**
Copy
Ask AI
```
models:
name: customers
    columns:
name: customer_id
        description: "Unique customer identifier"
        config:
          meta:
            is_primary_key: true
            data_type: "uuid"
          tags: ["pii", "identifier"]

```

###  Source-Level Changes
**Before:**
Copy
Ask AI
```
sources:
name: raw_data
    schema: staging
    meta:
      loader: "fivetran"
      freshness_sla: "1 hour"
    tags: ["external", "raw"]
    tables:
name: users
        meta:
          row_count: 50000
        tags: ["pii"]

```

**After:**
Copy
Ask AI
```
sources:
name: raw_data
    schema: staging
    config:
      meta:
        loader: "fivetran"
        freshness_sla: "1 hour"
      tags: ["external", "raw"]
    tables:
name: users
        config:
          meta:
            row_count: 50000
          tags: ["pii"]

```

##  Other dbt 1.10 Changes to Consider
While migrating `meta` and `tags`, be aware of other properties moving to configs:
  * `freshness` (for sources)
  * `docs`
  * `group`
  * `access`

These properties should now be set under the `config` block following the same pattern as `meta` and `tags`.
##  Handling Warnings During Migration
If you’re using `--warn-error` flags that promote warnings to errors, you may need to adjust your configuration during migration:
Copy
Ask AI
```
# In dbt_project.yml
flags:
  warn_error_options:
    warn: ["Deprecations"# Keep deprecation warnings as warnings
    error: ["other_warning_types"# Promote other warnings to errors

```

This allows you to continue working while addressing deprecation warnings gradually.
##  Testing Your Migration
After migrating your files:
  1. **Run dbt parse** : Ensure your project parses without errors:
Copy
Ask AI
```
dbt parse

```

  2. **Check for Warnings** : Run a simple command to verify warnings are resolved:
Copy
Ask AI
```
dbt compile --select my_model

```

  3. **Run Tests** : Execute your test suite to ensure functionality is preserved:
Copy
Ask AI
```
dbt test

```



##  Best Practices
  * **Backup First** : Always backup your project before running any migration tool
  * **Test in Development** : Run the migration in a development branch first
  * **Review Changes** : Use git diff to review all changes before committing
  * **Migrate Incrementally** : For large projects, consider migrating one directory at a time
  * **Update CI/CD** : Ensure your deployment processes work with the new structure


##  Troubleshooting Common Issues
###  ”Config block already exists” Errors
If you have existing `config` blocks, MetaMove will merge the new properties. However, if you encounter conflicts:
  1. Review the specific file causing issues
  2. Manually resolve conflicts between existing and new config properties
  3. Re-run MetaMove on the corrected file


###  Unexpected YAML Structure
If your YAML files have unusual structures that MetaMove doesn’t handle:
  1. Note the problematic files in the tool output
  2. Manually migrate these files using the patterns shown above
  3. Use MetaMove for the remaining standard files


###  Performance with Large Projects
For projects with hundreds of YAML files:
  1. Run MetaMove on subdirectories rather than the entire project at once
  2. Use the `-o` flag to organize transformed files by directory
  3. Process files in batches to make review manageable


##  Conclusion
Migrating to dbt 1.10’s new `meta` and `tags` structure is essential for maintaining a robust, future-proof dbt project. MetaMove makes this migration straightforward by automating the tedious work while preserving your careful formatting and comments. The goal is to enable you to work with more safety, feedback, and confidence going forward. By moving `meta` and `tags` under `config` blocks, dbt can provide better validation and prevent the subtle issues that arise from misspelled properties or unintended conflicts. Start your migration today:
Copy
Ask AI
```
pipx install metamove
metamove models/* --help

```

For more information about dbt 1.10 changes and package management best practices, check out the official dbt upgrade guide and explore MetaMove on GitHub for advanced usage and contributing opportunities.
Guide to package-lock.yml in dbtMigrate to dbt Fusion
Assistant
Responses are generated using AI and may contain mistakes.


