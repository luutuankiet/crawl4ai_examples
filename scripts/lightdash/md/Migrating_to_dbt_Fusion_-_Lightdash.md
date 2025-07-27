# Migrating to dbt Fusion - Lightdash

**Source:** https://docs.lightdash.com/dbt-guides/dbt-fusion-migration

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Migrating to dbt Fusion
  * Guide to package-lock.yml in dbt


  * Migrate to dbt 1.10


  * Migrate to dbt Fusion


On this page
  * What is dbt Fusion?
  * Recommended Migration Process
  * Step 1: Upgrade to dbt 1.10 and Fix Warnings
  * Step 2: Migrate to Fusion (only required for dbt Core users)
  * For dbt Core Users:


##  What is dbt Fusion?
dbt Fusion is a complete rewrite of the dbt engine built in Rust that offers dramatically faster performance, native SQL understanding, and real-time validation. While your familiar SQL and YAML syntax stays the same, the engine underneath is fundamentally more powerful and efficient. dbt Fusion replaces dbt Core and will be used under the hood in dbt Cloud. For more details, see the official dbt Fusion overview. Unlike dbt 1.10 which is an incremental update, Fusion represents a fundamental architectural change. While it maintains compatibility with the dbt language and syntax, existing projects must first resolve all deprecation warnings before migration, as Fusion enforces stricter validation than dbt Core. It is therefore necessary to first upgrade to dbt 1.10, and resolve and validation warnings before upgrading to dbt Fusion.
Important: dbt Fusion is still in beta, which means some dbt functionality is not supported at present. Please review the dbt Fusion supported features and current limitations documentation before proceeding with this migration.
##  Recommended Migration Process
###  Step 1: Upgrade to dbt 1.10 and Fix Warnings
  1. Upgrade your dbt environment to version 1.10 or later (see dbt instructions here).
  2. Use Lightdash’s MetaMove CLI to automatically migrate `meta` and `tags` from top-level properties to `config` blocks.
  3. Run your dbt project and address any other deprecation warnings before proceeding. Note you can also use dbt-autofix to automatically resolve many deprecation warnings.


###  Step 2: Migrate to Fusion (only required for dbt Core users)
Once all deprecation warnings are resolved, dbt Core users will need to follow the steps below to migrate to the dbt Fusion engine. dbt Cloud users, however, can wait for automatic rollout - dbt Labs will handle the dbt Fusion migration automatically.
####  For dbt Core Users:
  1. Check that you meet the dbt Fusion migration prerequisites
  2. Install the dbt Fusion engine following the installation guide
  3. Run your project with dbt Fusion to identify any compatibility issues.


Migrate to dbt 1.10
Assistant
Responses are generated using AI and may contain mistakes.


