# Exploratory Data Analysis Using StackOverflow Survey Data

## **Introduction**
Every year the website StackOverflow.com sends out a survey to the web developers that use their site.  This is always a large dataset and interesting to explore. There is traditionally a synopsis and visual of the findings but I thought I would take a crack at it.

## **Questions**
I went into this analysis with a few questions on the forefront.
1. What Countries are being represented?
2. What is the Gender breakdown of Respondents?
3. What programming languages are most common?
4. How popular is python overall?
5. What is the Work location distribution for Respondents?
6. How varied are the salaries versus experience?

## **Process**
I used Python Jupyter Notebook to load the data in csv format.  I then set out to systematically address all questions presented initially to gain some insigths from this survey data.  Using Pandas, I created a dataframe and made the display more user-friendly.  After formatting the data, I went back and created some visuals using seaborn and matplotlib.

<img src= "https://github.com/BrianHarrisCodes/Project/blob/main/Portfolio_Projects/2_Survey_EDA/images/age_bar.png">


## **Data Source**

The data was located here: https://insights.stackoverflow.com/survey/

## **Conclusion**

Most of the respondents for the Survey were in the United States. I was curious as to how popular the Python coding language was and it was in the top five. There was a fairly even distribution between hybrid and remote work location. Much less were reporting in-person employment, but that is more common with developers. Some errors did present themselves when examining the compensation data in the survey.  I'm not sure if any limits were set but I did see several entries where it stated that the developers were receiving millions in US converted Currency. That would seem to be a topic to follow-up with the administrators responsible for the survey.


## **Acknowledgements**
Stackoverflow for making a robust survey dataset with minimal null value issues.


##### © Brian Harris 2023
