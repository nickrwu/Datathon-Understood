# DSC @ NYU 2020 Datathon
*In Association with Understood.org*

https://dsc-nyu.github.io/datathon/

## Datathon Primary Directive:
**Tasks:**
* Build an automated tool to create and populate a dataset of companies that have potential to partner with Understood.org.
* Build logic for Understood.org to score how closely each company aligns with their mission statement.
* Your approach should be built with latency in mind although the way you score how each company aligns with Understood is up to you.

Examples of companies who align with Understood's mission statement: 
* National Center for Learning Disabilities
Examples of companies who do not align with Understood's mission statement:
* Exxon Mobile


**Scoring:**
How many useful entities (rows) and features (columns) can you bring to the dataset?
Is the information usable in the long term? Can it be refreshed as it gets outdated?
Latency of your model
Can you identify for-profit and non-profit entities that are aligned with Understood.org's mission?
Can you identify how close each company is to Understood's mission


## Our Top Ranked Companies:
1. Connection Fund, Inc.
2. Essex County
3. Arc Facilities Inc
4. The Urban Assembly, Inc.
5. Amityville Cemetery Association
6. Cedar Grove Cemetery Association
7. Cedar Lawn Cemetery Association
8. Boy Scouts of America
9. Edith and Carl Marks Jewish Community House of Bensonhurst Inc
10. Friends Academy 
11. The Packer Collegiate Institute

## Our Feature Importance:
1. Total Revenue (37%)
2. Total Assets (22%)
3. Number of Employees (12.5%)
4. Others (29.5%)


## Our Summary: 
* During the data collection process, we found a dataset of 3002 non-profit organizations from GuideStar and scraped the mission statements using the links provided by the GuideStar
* We cleaned the 3002 data and sorted out the “Total Asset”, “Total Revenue” and “Employee” columns without any null values inside it
* Utilized Decision Trees to compute feature importance
* To set the partner criteria, we tested on the 20 organizations that Understood already is partnered with and parsed the most frequently appeared words in their mission statements
* We also calculated their median value of the total asset, total revenue, and employee. We then vectorize the three criterias and generate a center
* We calculate the distance of the potential companies with the center and find out the top-ten closest companies
* We also plot all the potential companies in a 3-d graph

Team: LNECH

Thank you to Kyle Ma, Esther Wu, Lucy Wu, and Christian Zhao.

