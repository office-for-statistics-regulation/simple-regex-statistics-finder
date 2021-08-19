import re

def remove_unwanted_values(text):
    text = re.sub('(\d{2}|\d{1})\s(January|February|March|April|May|June|July|August|September|October|'
                  'November|December)\s\d{4}', '', text) # removes 01 January 2021 dates
    text = re.sub('(\d{2}|\d{1})\s(January|February|March|April|May|June|July|August|September|October|'
                  'November|December)', '', text) # removes 01 January dates
    text = re.sub('2019|2020|2021|2020', '', text) # removes years 2019-2020
    text = re.sub('stage\s(\d{2}|\d{1})', '', text) # stage 3 or stage 34 text
    text = re.sub('(covid19|covid-19|COVID 19)', '', text) # removes covid terms
    text = re.sub('(\d{2}|\d{1})\s(month|months)', '', text) # removes values like 12 months or 1 month
    text = re.sub('(\d{2}|\d{1})\s(year|years)', '', text) # removes values like 3 years or 1 year
    text = re.sub('(\d{3}|\d{2}|\d{1})(nd|st|rd|th)', '', text) # removes 1st, 22nd, 104th etc
    text = re.sub('category\s(\d{2}|\d{1})', '', text) # removes category 3 or catergory 12 text
    text = re.sub('No.\s(\d{3}|\d{2}|\d{1})', '', text) # removes No. 3, No. 56 or No. 765 text
    text = re.sub('Vol.\s(\d{3}|\d{2}|\d{1})', '', text) # removes Vol. 3, Vol. 56 or Vol. 765 text
    text = re.sub('c.(\d{3}|\d{2}|\d{1})', '', text) # removes c.3, c.56 or c.765 text
    text = re.sub('halfterm', '', text) # removes halfterm
    text = re.sub('(\d{2}|\d{1}).\d{2}(am|pm)', '', text) # removes 6.32am or 12.45pm text
    text = re.sub('Ayes\s(\d{3}|\d{2}|\d{1})', '', text) # removes Ayes 3, Ayes 45 or Ayes 352 text
    text = re.sub('Noes\s(\d{3}|\d{2}|\d{1})', '', text) # removes Noes 3, Noes 45 or Noes 352 text
    return text

def find_statistics(text):
    if len(re.findall(
        '(\d+|£|$|hundred|hundreds|thousand|thousands|million|millions|billion|billions|%|percent|quarter|half)',
            remove_unwanted_values(text))) > 1:
        return True
    return False
