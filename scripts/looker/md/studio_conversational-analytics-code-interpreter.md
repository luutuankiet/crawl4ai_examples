# Conversational Analytics Code Interpreter  |  Looker Studio  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Enable the Code Interpreter
    * Enable the Code Interpreter in Looker Studio
    * Enable the Code Interpreter in Looker (original)
    * Enable the Code Interpreter in Looker (Google Cloud core)
  * Known limitations
    * Supported Python libraries
  * Suggested questions




Was this helpful?
Send feedback 
#  Conversational Analytics Code Interpreter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Release Notes 
  * On this page
  * Before you begin
  * Enable the Code Interpreter
    * Enable the Code Interpreter in Looker Studio
    * Enable the Code Interpreter in Looker (original)
    * Enable the Code Interpreter in Looker (Google Cloud core)
  * Known limitations
    * Supported Python libraries
  * Suggested questions


The Code Interpreter in Conversational Analytics translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. The Code Interpreter is available for Conversational Analytics in Looker Studio as part of a Looker Studio Pro subscription, in Looker (original), and in Looker (Google Cloud core).
In contrast to standard SQL-powered BI experiences, the Code Interpreter supports a wide variety of data analytics—from basic computations and charting to more advanced tasks like time series forecasting. The Code Interpreter enhances Conversational Analytics by enabling users to perform these types of advanced analysis, which otherwise would typically require specialized knowledge of advanced coding or statistical methods.
Learn how and when Gemini for Google Cloud uses your data.
## Before you begin
To use the Code Interpreter, you must meet the requirements for using Conversational Analytics in Looker Studio or in Looker:
  * To use the Code Interpreter with a Looker (original) instance, your instance must be on Looker 25.8 or later.
  * To use the Code Interpreter with a Looker (Google Cloud core) instance, your instance must be on Looker 25.10 or later.
  * To use the Code Interpreter in Looker Studio, you must be a user under a Looker Studio Pro subscription.


## Enable the Code Interpreter
This section describes how to enable the Code Interpreter in the following platforms:
  * Looker Studio
  * Looker (original)
  * Looker (Google Cloud core)


### Enable the Code Interpreter in Looker Studio
To enable the Code Interpreter for your conversations, follow these steps:
  1. In the left navigation panel within Conversational Analytics, click the **Advanced analytics** toggle to enable the Code Interpreter.
  2. With the Code Interpreter enabled, you can use Conversational Analytics as usual to start conversations and ask questions of your data. The Code Interpreter uses the engine that powers Gemini chat to translate your queries into Python code and execute that code.


### Enable the Code Interpreter in Looker (original)
In the Looker (original) instance, a Looker admin must follow these steps to enable the Code Interpreter and make it available to Gemini in Looker users:
  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Under **Gemini in Looker enablement** , turn on the **Enable Gemini in Looker** setting.
  3. Select **Enable Trusted Tester Features**. When this setting is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. **This setting must be enabled to allow users to access Gemini during the pre-GA preview.**
  4. Optionally, select **Enable Trusted Tester Data Use**. When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms. This setting can be enabled only when the **Enable Trusted Tester Features** setting is enabled. This setting is enabled automatically when the **Enable Trusted Tester Features** setting is enabled.
  5. Select **Enable Code Interpreter**. When this setting is enabled, users can access the Code Interpreter in Conversational Analytics. This setting can be enabled only when the **Enable Trusted Tester Features** setting is also enabled. The Enable Code Interpreter setting was enabled by default for Looker (original) instances that met the following criteria: 
     * A Looker admin turned on the **Enable Gemini in Looker** and **Enable Trusted Tester Features** settings on your Looker (original) instance before you updated your instance to Looker 25.8.
     * A Looker admin updated your instance to Looker 25.8 on the first day of release deployments.


A Looker admin must grant the `gemini_in_looker` permission to users before they can use the Code Interpreter.
### Enable the Code Interpreter in Looker (Google Cloud core)
In the Looker (Google Cloud core) instance, a Looker admin must follow these steps to enable the Code Interpreter and make it available to Gemini in Looker users:
  1. Navigate to the **Admin** panel > **Platform** section > **Gemini in Looker** page.
  2. Enable **Code Interpreter**.


The Code Interpreter is disabled by default, even when **Gemini in Looker** is enabled in the Looker (Google Cloud core) instance settings in the Google Cloud console.
A Looker admin must grant the `gemini_in_looker` permission to users before they can use the Code Interpreter.
## Known limitations
  * The Code Interpreter uses Python to solve problems. Since Python is more flexible than structured query languages, Code Interpreter responses might have more variability than responses from the core Conversational Analytics experience.
  * For Looker data, Conversational Analytics can return a maximum of 5,000 rows per query.
  * The Code Interpreter supports these Python libraries. To request support for additional Python libraries, send an email to conversational-analytics-feedback@google.com.
  * The following visualization chart types are not supported in Code Interpreter responses: 
    * Maps


For information about additional limitations, see the documentation on known limitations in Conversational Analytics.
### Supported Python libraries
#### Show supported Python libraries
The Code Interpreter supports the following Python libraries:
  * `altair`
  * `attrs`
  * `chess`
  * `contourpy`
  * `cycler`
  * `entrypoints`
  * `fonttools`
  * `fpdf`
  * `geopandas`
  * `imageio`
  * `jinja2`
  * `joblib`
  * `jsonschema`
  * `jsonschema-specifications`
  * `kiwisolver`
  * `lxml`
  * `markupsafe`
  * `matplotlib`
  * `mpmath`
  * `numexpr`
  * `numpy`
  * `opencv-python`
  * `openpyxl`
  * `packaging`
  * `pandas`
  * `patsy`
  * `pdfminer-six`
  * `pillow`
  * `plotly`
  * `protobuf`
  * `pylatex`
  * `pyparsing`
  * `PyPDF2`
  * `python-dateutil`
  * `python-docx`
  * `python-pptx`
  * `pytz`
  * `referencing`
  * `reportlab`
  * `rpds-py`
  * `scikit-image`
  * `scikit-learn`
  * `scipy`
  * `seaborn`
  * `six`
  * `statsmodels`
  * `striprtf`
  * `sympy`
  * `tabulate`
  * `tensorflow`
  * `threadpoolctl`
  * `toolz`
  * `torch`
  * `tzdata`
  * `xlrd`


## Suggested questions
When you enable the Code Interpreter, Python's advanced analytic capabilities enable Conversational Analytics to answer a wider range of questions, in addition to the standard types of supported questions. For example:
  * Can you explain the key drivers for sales based on my data?
  * What is the lifetime value for each of my customer segments, taking into account the average purchase frequency and the average order value?
  * How do sales this year compare to sales last year?
  * Identify outliers in my sales data to help identify products or regions that are performing particularly well or particularly poorly.
  * Perform a cohort analysis to understand customer retention.
  * Are my highest margin products also the most popular products? Use this answer to provide a suggestion on how to optimize my product mix.
  * What is the compound annual growth rate (CAGR) for sales by product category for the last 3 years?
  * Show the CAGR as a bar chart with product category on the x-axis and CAGR on the y-axis.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


