# Maximizing code reusability with DRY LookML: Defining reusable measures for complex calculations  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/dry-cookbook-3

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Example: Breaking a complex calculation into intermediate measures




Was this helpful?
Send feedback 
#  Maximizing code reusability with DRY LookML: Defining reusable measures for complex calculations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Example: Breaking a complex calculation into intermediate measures


When you're defining complex calculations in LookML, it can be helpful to break them down into intermediate steps that involve simpler calculations. By creating intermediate measures, you make your calculations more readable, easier to maintain, and less error-prone, since you only need to ensure that each intermediate calculation is correct in one place.
This page provides an example of how you can make your calculations in LookML more readable and maintainable by defining intermediate measures to break complex calculations into smaller, more manageable steps.
## Ingredients
  * The LookML `measure` parameter
  * The `sql` parameter of a measure
  * A measure of `type: sum`
  * A measure of `type: number`
  * The LookML `hidden` parameter (for fields)


## Prerequisites
  * A configured LookML model
  * Permissions to develop LookML


## Example: Breaking a complex calculation into intermediate measures
Suppose you have a company that sells products online, and you want to define measures to calculate total profit and shareholder dividends. One way to do this would be to define two measures: a `total_profit` measure and a `shareholder_dividends` measure, as follows:
```

measure: total_profit {
  type: number
  sql: SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost}) ;;
}

measure: shareholder_dividends
  description: "We give shareholders 60% of our total profits."
  type: number
  sql: 0.6 * (SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost})) ;;


```

In this example, the calculation `SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost})` is reused in the `sql` parameter for both measures. If you need to update the definition of this calculation, such as to correct an error, you would have to update the calculation manually for both measures.
You can make these measure definitions easier to maintain by reusing the `total_profit` measure within the calculation in the `shareholder_dividends` measure:
```

measure: total_profit {
  type: number
  sql: SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost}) ;;
}

measure: shareholder_dividends
  description: "We give shareholders 60% of our total profits."
  type: number
  sql: 0.6 * ${total_profit} ;;


```

You may want to break the calculation in `total_profit` into even simpler measures that can be reused in other calculations. For example, you can create measures of `type: sum` called `total_sales`, `total_revenue`, `total_cost`, and `total_salary`:
```

measure: total_sales {
  hidden: yes
  type: sum
  sql: ${orders.sale_price} ;;
}

measure: total_revenue {
  hidden: yes
  type: number
  sql: ${total_sales} ;;
}

measure: total_cost {
  hidden: yes
  type: sum
  sql: ${products.cost} ;;
}

measure: total_salary {
  hidden: yes
  type: sum
  sql: ${employees.salary} ;;
}


```

You can then reuse the intermediate fields you have defined as follows:
```

measure: total_expenses {
  type: number
  sql: ${total_cost} + ${total_salary} ;;
}

measure: total_profit {
  type: number
  sql: ${total_revenue} - ${total_expenses} ;;
}

measure: shareholder_dividends {
  description: "We give shareholders 60% of our total profits."
  type: number
  sql: 0.6 * ${total_profit} ;;
}


```

Although you have defined more measures, these intermediate measures can be reused within other calculations, and it will be easier correct a mistake or make any changes to calculations that are used in multiple measures.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


