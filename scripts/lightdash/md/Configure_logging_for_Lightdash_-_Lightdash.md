# Configure logging for Lightdash - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-logging-for-lightdash

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure logging for Lightdash
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
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
    * Standalone scheduler worker
    * Environment variables
    * Resource recommendations
    * Secure Lightdash with HTTPS


##### Contact


By default Lightdash logs to the console in a human readable format. You can configure the logging behaviour, such as logging to a file or using a JSON format, by using the following environment variables: Variable | Description | Required? | Default  
---|---|---|---  
`LIGHTDASH_LOG_LEVEL` | The minimum level of log messages to display | `INFO`  
`LIGHTDASH_LOG_FORMAT` | The format of log messages | `pretty`  
`LIGHTDASH_LOG_OUTPUTS` | The outputs to send log messages to | `console`  
`LIGHTDASH_LOG_CONSOLE_LEVEL` | The minimum level of log messages to display on the console | `LIGHTDASH_LOG_LEVEL`  
`LIGHTDASH_LOG_CONSOLE_FORMAT` | The format of log messages on the console | `LIGHTDASH_LOG_FORMAT`  
`LIGHTDASH_LOG_FILE_LEVEL` | The minimum level of log messages to write to the log file | `LIGHTDASH_LOG_LEVEL`  
`LIGHTDASH_LOG_FILE_FORMAT` | The format of log messages in the log file | `LIGHTDASH_LOG_FORMAT`  
`LIGHTDASH_LOG_FILE_PATH` | The path to the log file | `./logs/all.log`  
External storagePrometheus metrics
Assistant
Responses are generated using AI and may contain mistakes.


