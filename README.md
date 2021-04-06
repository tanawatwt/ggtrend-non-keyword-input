# ggtrend
This script would pull googletrend data from API with Pytrend library. Main function to pull all data for selected category with defined time range

You can pull trending keyword from google trend API with Pytrends. Here is docs : https://pypi.org/project/pytrends/

FYI: Some code copied from stackoverflow 👍 , github => its disappeared from my notion wtf????!!

As my job need to pull all trend data from all category of googletrend with no keyword input for marketing team.

You can see all google trend category in "all google trend category.xlsx" in this repo (1,427 categories). Yes, google interface is hiding some categories.

But because of API data request limitation, we can not pull all category in one time. 

I need to select only interested categories, Lets say I would select only category that shown up on the interface.

Then I would put all selected category in "cat1.xlsx" file in this repo.

And run the script "ggtrend_api_main.py" => this script would transform all excel input to json, prepare setting for Pytrends. Create request. Get Josn and transform to excel file.

You will get result in "result.xlsx"




