## simple regex statistics finder

A super simple regex (regular expressions) function called `statistics_finder.py` that looks for statistics in text. It also removes numbers which aren't statistics (dates for example). This was designed for parsing parliment speech text.

### What it looks for
- Absolute values comprising one moe more digits (e.g. 1, 100, 10000000)
- Uses of £, $ and % symbols
- Uses of words such as hundred(s), thousand(s), million(s), billion(s), percent, half and quarter

### What it ignores
- Dates in 01 January 2021 or 01 January format
- The years between 2019 and 2021
- covid19, covid 19 or covid-19
- values followed by months or years
- time values in am and pm format
- values that are preceeded by the words stage, category, No. Vol., c. Ayes or Noes
- certain words like halfterm

### Examples

Actual statistics highlighted in bold we would want to look for. Text comprises many other values that we want to ignore.


#### Absolute values

text = 'On 4 June during the covid19 pandemic OSR released stage 3 of their findings from the last 12 months. The team met for 92nd on the 1st of this month (01 July 2021); **675000 bananas** were eaten after reading category 2 No. 8 Vol. 686 c.23 of the report. Many were absent due to halfterm but at 6.44pm the vote was in, it was Ayes 524 to Noes 64. The report will now be published on 12 December 2021 following completion of stage 16. Thank you.'

find_statistics(text)

`Out: TRUE`

#### Uses of numerical words

text = 'On 4 June during the covid19 pandemic OSR released stage 3 of their findings from the last 12 months. The team met for 92nd on the 1st of this month (01 July 2021); **thousands of bananas** were eaten after reading category 2 No. 8 Vol. 686 c.23 of the report. Many were absent due to halfterm but at 6.44pm the vote was in, it was Ayes 524 to Noes 64. The report will now be published on 12 December 2021 following completion of stage 16. Thank you.'

find_statistics(text)

`Out: TRUE`

#### Uses of symbols

text = 'On 4 June during the covid19 pandemic OSR released stage 3 of their findings from the last 12 months. The team met for 92nd on the 1st of this month (01 July 2021); **54% of bananas** were eaten after reading category 2 No. 8 Vol. 686 c.23 of the report. Many were absent due to halfterm but at 6.44pm the vote was in, it was Ayes 524 to Noes 64. The report will now be published on 12 December 2021 following completion of stage 16. Thank you.'

find_statistics(text)

`Out: TRUE`

#### No relevant statistics

text = 'On 4 June during the covid19 pandemic OSR released stage 3 of their findings from the last 12 months. The team met for 92nd on the 1st of this month (01 July 2021);  everyone ate after reading category 2 No. 8 Vol. 686 c.23 of the report. Many were absent due to halfterm but at 6.44pm the vote was in, it was Ayes 524 to Noes 64. The report will now be published on 12 December 2021 following completion of stage 16. Thank you.'

find_statistics(text)

`Out: FALSE`
