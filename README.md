# Deal or No Deal? Classification of Outcomes for Sales Deals
Random Forest Model to Classify Sales Deals Outcomes

This project uses IBM data for various sales deal and their characteristics to classify the outcome of sales. This resulted in a Flask app (instructions below)

## Target Question
How can we help sales representatives prioritize deals?


## Notebooks
01 Data Acquistion
02 Preprocessing & EDA
03 Modeling
04 Data Visualization


## Run

### Install 
* Pandas
* Numpy
* Matplotlib
* Jupyter Notebook
* Flask

### Run

## Data 
[IBM Sales Data](https://www.ibm.com/communities/analytics/watson-analytics-blog/sales-win-loss-sample-dataset/)

### Target
Sales Outcome - Won or Loss

### Features

| ID |  Name | Description | Type|
|-----------|---------|--------------|------|
| oppID | Opportunity Number | A unique generated number assigned to the opportunity | Categorical|
| subGroup	|Supplies SubGroup	|Reporting supplies subgroup. Values are: Batteries & Accessories, Car Electronics, Exterior Accessories, Garage & Car Care, Interior Accessories, Motorcycle Parts, Performance Parts, Replacement Parts, Shelters & RV, Tires & Wheels, Towing & Hitches	| Categorical | 
|mainGroup|Supplies Group|Reporting supplies group Values are: Car Accessories, Car Electronics, Performance & Non-auto, Tires & Wheels	| Categorical |
|region	|Region	|Name of the Region. Values could be : Mid-Atlantic, Midwest, Northeast, Northwest, Pacific, Southeast, Southwest	| Categorical |
|route	|Route to Market|The opportunities’ route to market: Fields Sales, Other, Reseller, Telecoverage, Telesales	| Categorical|
|daysinstage|Elapsed Days In Sales Stage|The number of days between the change in sales stages. The counter is reset for each new sales stage| Numerical |
|oppOutcome	|Opportunity Results|A closed opportunity is won or loss.| Categorical|
|stageChanges|Sales Stage Change Count	|Actually a count of number of times an opportunity changes sales stages (back and forwards)| Numerical |
|daysToClose|Total Days Identified Through Closing	|Total days the opportunity has spent in Sales Stages from Identified/Validating to Gained Agreement/closing | Numerical |
|daysToQual	|Total Days Identified Through Qualified|Total days the opportunity has spent in Siebel Stages from Identified/Validating to Qualified/Gaining Agreement	|Numerical |
|oppValue|Opportunity Amount (USD)|Sum of line item revenue estimates by sales representative in American currency	| Numerical |
|sizeByRev	|Client Size by Revenue	Client|size based on annual revenue: 1: < $1M, 2: [$1M, $10M], 3: [$10M, $50M], 4: [$50M, $100M], 5: ≥ $100M| Categorical |
| sizeByEE	|Client Size by Employee Count |1: < 1, 2: [1K, 5K], 3: [5K, 10K], 4: [10K, 30K] , 5: ≥ 30K| Categorical |
|pastSale|Revenue From Client Past Two Years	|Revenue identified from this client in past two years: 0: 0, 1, [1, 50K), 2: [50K, 400K), 3: [400K, 1.5M), 4: ≥ 1.5M	| Categorical |
|Competitor	|Competitor Type	|An indicator if a competitor has been identified Values: Known, Unknown, None	| Categorical |
|ratioIDtoT	|Ratio Days Identified To Total Days|Ratio of total days the opportunity has spent in sales stage: Identifiedover total days in sales process	| Numerical |
|ratioValtoT|Ratio Days Validating To Total Days	|Ratio of total days the opportunity has spent in sales stage: Validating over total days in sales process	| Numerical |
|ratioQualtoT|Ratio Days Qualified To Total Days	Ratio	|total days the opportunity has been spent in sales stage: Qualified/Gaining Agreement over total days in sales process	| Numerical |
|dealsizeCat	|Deal Size by Category	|Categorical grouping of the opportunity amount (OpportunityAmountUSD): 1: < 10K, 2: [$10K, 25K], 3: [$25K, $50K], 4: [$50K, $100K], 5: [$100K, $250K], 6: [$250K, $500K], 7: ≥ $500K	|Categorical|













