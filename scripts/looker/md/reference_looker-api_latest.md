# Looker API Reference  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Looker Application API Methods
  * Looker Application API Types
  * Looker (Google Cloud core) Admin API




Was this helpful?
Send feedback 
#  Looker API Reference
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Looker Application API Methods
  * Looker Application API Types
  * Looker (Google Cloud core) Admin API


Version 4.0.25.10 (latest) 
Looker's API provides access to the vast majority of Looker functionality over a convenient JSON-oriented REST API. For an introduction on our API see our getting started guide.
This API reference provides details on methods/endpoints exposed via the API, as well as type definitions that define the request and response structures.
## Looker Application API Methods
Alert
  * Update select fields on an alert


ApiAuth


Artifact
  * Get namespaces and counts
  * Get an artifact value
  * Get one or more artifacts
  * Delete one or more artifacts
  * Create or update artifacts


Auth
  * Create Signed Embed Url
  * Get Embed URL Validation
  * Create Acquire cookieless embed session
  * Delete cookieless embed session
  * Generate tokens for cookieless embed session
  * Get LDAP Configuration
  * Update LDAP Configuration
  * Register Mobile Device
  * Update Mobile Device Registration
  * Deregister Mobile Device
  * Get All OAuth Client Apps
  * Get OAuth Client App
  * Delete OAuth Client App
  * Activate OAuth App User
  * Deactivate OAuth App User
  * Get OIDC Configuration
  * Update OIDC Configuration
  * Get OIDC Test Configuration
  * Delete OIDC Test Configuration
  * Create OIDC Test Configuration
  * Update Password Config
  * Get SAML Configuration
  * Update SAML Configuration
  * Get SAML Test Configuration
  * Delete SAML Test Configuration
  * Create SAML Test Configuration
  * Update Session Config
  * Get Support Access Allowlist Users
  * Add Support Access Allowlist Users
  * Delete Support Access Allowlist Entry
  * Enable Support Access
  * Disable Support Access
  * Support Access Status
  * Get All User Login Lockouts
  * Search User Login Lockouts
  * Delete User Login Lockout


Board
  * Get All Board sections


ColorCollection
  * Get all Color Collections
  * Create ColorCollection
  * Get all Custom Color Collections
  * Get all Standard Color Collections
  * Set Default Color Collection
  * Get Default Color Collection
  * Get Color Collection by ID
  * Update Custom Color collection
  * Delete ColorCollection


Config
  * Get Custom Welcome Email
  * Update Custom Welcome Email Content
  * Send a test welcome email to the currently logged in user with the supplied content 
  * Deliver digest email contents
  * Public Egress IP Addresses
  * Get Internal Help Resources Content
  * Update internal help resources content
  * Get Internal Help Resources
  * Update internal help resources configuration
  * Get All Legacy Features
  * Update Legacy Feature
  * Get an API specification
  * Get Private label configuration
  * Update Private label configuration


Connection
  * Delete Connection Override
  * Test Connection Configuration
  * Get All Dialect Infos
  * Get All External OAuth Applications
  * Create External OAuth Application
  * Update External OAuth Application
  * Create Create OAuth user state.


Content
  * Search Favorite Contents
  * Delete Favorite Content
  * Create Favorite Content
  * Get All Content Metadatas
  * Update Content Metadata
  * Create Content Metadata Access
  * Get All Content Metadata Accesses
  * Update Content Metadata Access
  * Delete Content Metadata Access
  * Search Content Summaries
  * Get Content Thumbnail


Dashboard
  * Import LookML Dashboard
  * Sync LookML Dashboard
  * Get Aggregate Table LookML for a dashboard
  * Import Dashboard from LookML
  * Create Dashboard from LookML
  * Search Dashboard Elements
  * Delete DashboardElement
  * Update DashboardElement
  * Get All DashboardElements
  * Create DashboardElement
  * Delete Dashboard Filter
  * Update Dashboard Filter
  * Get All Dashboard Filters
  * Create Dashboard Filter
  * Get DashboardLayoutComponent
  * Update DashboardLayoutComponent
  * Get All DashboardLayoutComponents
  * Delete DashboardLayout
  * Update DashboardLayout
  * Get All DashboardLayouts
  * Create DashboardLayout


DataAction
  * Fetch Remote Data Action Form


Datagroup


DerivedTable
  * Get Derived Table graph for model
  * Get subgraph of derived table and dependencies
  * Start a PDT materialization
  * Check status of a PDT materialization
  * Stop a PDT materialization


Folder
  * Search Folder Children
  * Get Folder Dashboards


Group
  * Search Groups with Roles
  * Search Groups with Hierarchy
  * Get All Groups in Group
  * Add a Group to Group
  * Get All Users in Group
  * Remove a User from Group
  * Deletes a Group from Group
  * Set User Attribute Group Value
  * Delete User Attribute Group Value


Homepage
  * Get All Primary homepage sections


Integration
  * Get All Integration Hubs
  * Create Integration Hub
  * Update Integration Hub
  * Delete Integration Hub
  * Accept Integration Hub Legal Agreement
  * Fetch Remote Integration Form


Look


LookmlModel
  * Get All LookML Models
  * Get LookML Model Explore


Metadata
  * Model field name suggestions
  * List accessible databases to this connection
  * Metadata features supported by this connection
  * Get schemas for a connection
  * Get tables for a connection
  * Get columns for a connection
  * Search a connection for columns
  * Estimate costs for a connection


Project
  * Fetch Continuous Integration run
  * Create a Continuous Integration run
  * Get Active Git Branch
  * Checkout New Git Branch
  * Update Project Git Branch
  * Deploy Remote Branch or Ref to Production
  * Cached Project Validation Results
  * Get Project Workspace
  * Get All Project Files
  * Get All Git Connection Tests
  * Run Git Connection Test
  * Create Repository Credential
  * Delete Repository Credential
  * Get All Repository Credentials


Query
  * Get Multiple Async Query Results
  * Get Async Query Info
  * Get Async Query Results
  * Run Url Encoded Query
  * Get All Running Queries
  * Create SQL Runner Query
  * Get SQL Runner Query
  * Run SQL Runner Query


RenderTask
  * Create Look Render Task
  * Create Query Render Task
  * Create Dashboard Render Task
  * Create Dashboard Element Render Task


Report


Role
  * Search Permission Sets
  * Delete Permission Set
  * Update Permission Set
  * Get All Permission Sets
  * Create Permission Set
  * Search Roles with User Count


ScheduledPlan
  * Scheduled Plans for Space
  * Get All Scheduled Plans
  * Run Scheduled Plan Once
  * Search Scheduled Plans
  * Scheduled Plans for Look
  * Scheduled Plans for Dashboard
  * Scheduled Plans for LookML Dashboard
  * Run Scheduled Plan Once by Id


Session


SqlInterfaceQuery
  * Get SQL Interface Query Metadata
  * Run SQL Interface Query
  * Create SQL Interface Query


Theme


User
  * Search CredentialsEmail
  * Get User by Credential Id
  * Get Email/Password Credential
  * Create Email/Password Credential
  * Update Email/Password Credential
  * Delete Email/Password Credential
  * Get Two-Factor Credential
  * Create Two-Factor Credential
  * Delete Two-Factor Credential
  * Delete LDAP Credential
  * Get Google Auth Credential
  * Delete Google Auth Credential
  * Get Saml Auth Credential
  * Delete Saml Auth Credential
  * Get OIDC Auth Credential
  * Delete OIDC Auth Credential
  * Delete API Credential
  * Get All API Credentials
  * Create API Credential
  * Get Embedding Credential
  * Delete Embedding Credential
  * Get All Embedding Credentials
  * Get Looker OpenId Credential
  * Delete Looker OpenId Credential
  * Get Web Login Session
  * Delete Web Login Session
  * Get All Web Login Sessions
  * Create Password Reset Token
  * Get User Attribute Values
  * Set User Attribute User Value
  * Delete User Attribute User Value
  * Send Password Reset Token
  * Create an embed user from an external user ID


UserAttribute
  * Get All User Attributes
  * Get User Attribute Group Values
  * Set User Attribute Group Values


Workspace


## Looker Application API Types
Common
  * ValidationErrorDetail


Alert
  * AlertAppliedDashboardFilter


ApiAuth


Artifact


Auth
  * EmbedCookielessSessionAcquire
  * EmbedCookielessSessionAcquireResponse
  * EmbedCookielessSessionGenerateTokens
  * EmbedCookielessSessionGenerateTokensResponse
  * LDAPConfigTestResult
  * LDAPUserAttributeRead
  * LDAPUserAttributeWrite
  * OIDCUserAttributeRead
  * OIDCUserAttributeWrite
  * SamlMetadataParseResult
  * SamlUserAttributeRead
  * SamlUserAttributeWrite
  * SupportAccessAllowlistEntry
  * SupportAccessAddEntries


Board


ColorCollection


Config
  * InternalHelpResourcesContent
  * InternalHelpResources
  * MarketplaceAutomation
  * WhitelabelConfiguration
  * PrivatelabelConfiguration


Connection
  * CreateOAuthApplicationUserStateRequest
  * CreateOAuthApplicationUserStateResponse
  * DBConnectionOverride
  * DBConnectionTestResult
  * DialectDriverNamesVersion
  * ExternalOauthApplication


Content
  * ContentMetaGroupUser
  * ContentValidatorError
  * ContentValidationFolder
  * ContentValidationLook
  * ContentValidationDashboard
  * ContentValidationDashboardElement
  * ContentValidationError
  * ContentValidationDashboardFilter
  * ContentValidationScheduledPlan
  * ContentValidationAlert
  * ContentValidationLookMLDashboard
  * ContentValidationLookMLDashboardElement


Dashboard
  * DashboardAggregateTableLookml
  * CreateDashboardFilter
  * DashboardLayoutComponent
  * ResultMakerFilterablesListen
  * ResultMakerFilterables
  * ResultMakerWithIdVisConfigAndDynamicFields


DataAction
  * DataActionFormSelectOption


Datagroup


DerivedTable


Folder
  * DashboardLayoutComponent
  * ResultMakerFilterablesListen
  * ResultMakerFilterables
  * ResultMakerWithIdVisConfigAndDynamicFields


Group
  * CredentialsLookerOpenid
  * GroupIdForGroupInclusion
  * GroupIdForGroupUserInclusion
  * UserAttributeGroupValue


Homepage


Integration
  * DataActionFormSelectOption
  * IntegrationRequiredField
  * IntegrationTestResult


Look


LookmlModel
  * LookmlModelNavExplore
  * LookmlModelExploreSupportedMeasureType
  * LookmlModelExploreAccessFilter
  * LookmlModelExploreConditionallyFilter
  * LookmlModelExploreAlwaysFilter
  * LookmlModelExploreAlias
  * LookmlModelExploreSet
  * LookmlModelExploreError
  * LookmlModelExploreFieldset
  * LookmlModelExploreField
  * LookmlModelExploreFieldEnumeration
  * LookmlModelExploreFieldTimeInterval
  * LookmlModelExploreFieldSqlCase
  * LookmlModelExploreFieldMeasureFilters
  * LookmlModelExploreFieldPeriodOverPeriodParams
  * LookmlModelExploreFieldMapLayer
  * LookmlModelExploreJoins


Metadata
  * ModelFieldSuggestions
  * ModelNamedValueFormats


Project
  * GitConnectionTestResult
  * LocalizationSettings
  * AssertValidatorResult
  * AssertValidatorTestedExplore
  * ContentValidatorResult
  * ContentValidatorTestedExplore
  * LookMLValidatorResult
  * LookMLValidatorErrorItem
  * SqlValidatorTestedExplore
  * ProjectValidationCache
  * RepositoryCredential


Query
  * MergeQuerySourceQuery


RenderTask
  * CreateDashboardRenderTask


Report


Role
  * CredentialsLookerOpenid


ScheduledPlan
  * ScheduledPlanDestination


Session


SqlInterfaceQuery
  * JsonBiBigQueryMetadata
  * SqlInterfaceQueryCreate
  * SqlInterfaceQueryMetadata


Theme


User
  * CreateEmbedUserRequest
  * CreateCredentialsApi3
  * CredentialsEmailSearch
  * CredentialsLookerOpenid
  * UserAttributeWithValue


UserAttribute
  * UserAttributeGroupValue


Workspace


Uncategorized
  * AssertValidatorTestSuccess
  * AssertValidatorErrorItem
  * AssertValidatorTestError
  * ContentValidatorErrorItem
  * ContentValidatorContentError
  * LookMLValidatorError
  * SqlValidatorErrorItem


## Looker (Google Cloud core) Admin API
## Versions
The latest version of the API is 4.0.25.10. You are currently viewing the docs for the latest version. 
Documents are also available for prior supported versions:


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


