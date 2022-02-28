# Exercises week 4

This week, we will especially look into data wrangling using pandas. Additionally, use explorative data anlaysis and visualization techniques to understand the data!


We will work with data on housing prizes in Amsterdam, the so-called WOZ-waarde.

## 0. The input data
Take a look at `wozwaarde.csv` and try to understand it. 

For your understanding, Amsterdam is administatively divided into 7 "stadsdelen" (~ city parts), which -- for statitistical purposes -- are consisting of multiple "wijken" (~ residential areas) each. A "wijk", in turn, consists of multiple "buurten" (~ neighbourhoods), but we do not have any data on these in this specific exercise. Also, note that the "WOZ-waarde" is the estimated value (for tax purposes) of a house (or appartment).


- Take a look at `wozwaarde.csv`. Can you see any problems with the data? What do you think what the codes consisting of letters and numbers mean? Are they consistent?

- Now take a look at `wozwaarde-clean.csv`. Can you see the differences? What did we clean up? (For reference, we included `clean.py`, the script that we wrote to do this. You are not expected to do this yourself now, even though you probably could transform `wozwaarde.csv` to `wozwaarde-clean.py` with the skills you have learned so far as well.)


## 1. From wide to long

- You may have realized that `wozwaarde-clean.csv` is in wide format. Transform it to long!


## 2. Analyze the data!

Make a report in form of a Jupyter Notebook:
- Use Markdown cells to format and interpret what you are doing and finding.
- Use descriptive statistics.
- Use visualizations.

You will find useful examples here: https://github.com/uvacw/teaching-bdaca/blob/main/modules/basics/visualization.ipynb


## 3. Bonus exercise

If you have time left and want an extra challenge, try to implement the necessary cleanup steps from step 0 yourself, so that your analysis can work directly on `wozwaarde.csv` instead of having to rely on our pre-cleaned `wozwaarde-clean.csv`.
