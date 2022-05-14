# Welcome to the RSS Wimbledon 2022 Prediction Competition!

A big thank you to Smartodds (https://www.smartodds.co.uk/) for sponsoring the competition 

## Rules

1. The goal of the competition is to make probabilistic predictions of the outcome of matches from Wimbledon 2022
2. Entrants are free to use any data they wish, _provided it is publicly available_. This includes data scraped from public websites
3. The exact entry list is not known until the eve of the tournament. Instead, predictions are to be made for _every possible_ singles match between the top 100 female and male tennis players in the world (as of 14th May 2022).  
5. Submissions must be made before 10am on Monday 27th June (the first day of the tournament)
6. Code and data (or links to the data if the data sets are large) used to generate the predictions must be included in a submission so that the judging panel can reproduce the results
7. Participants are free to enter either as individuals or as teams
8. Entrants may update their predictions at any point before the start of the tournament by submitting a new entry but only the most recent submission will be scored
9. The two entries with the best log-score ([see Scoring below](#scoring)) will win a prize ([see Prizes below](#prizes)) along with a third entry chosen by the judging panel based on the methodology used

## Scoring

* Entries will be scored according to the log-score
* Each match will receive the score:
```
-(log(p_player1_win)*I(player1_win) + log(p_player2_win)*I(player2_win))
```
where  `I(.)` is the indicator function and e.g. `p_player1_win` is the entrant's estimate of the probability that Player 1 wins the match
* The individual log-scores for all matches that actually take place during Wimbledon 2022 will be summed to provide an overall score for the entry
* In the event of retirements, if any point has been scored in the match, the match will be deemed to have taken place and the retiree will be deemed the loser. 
* The lower the score, the better (note the minus signs!)

## Prizes

* All winners will be invited to present their work at the 2022 RSS conference with reasonable expenses paid 
* All winners will receive an appropriately tacky trophy!

## Making a Submission

* An example submission file can be found here: [submission-template.csv](submission-template.csv)
* Entrants should email a zip file to statisticsinsport@rss.org.uk that contains the submission file along with the code and data used to generate it
* If the zip file exceeds 10 megabytes then please do not submit the data but instead clearly comment the code with what data was used and where it can be obtained from. If the submission relies on scraped data and this is too large to be included then the scraping code must be included instead
* When making a submission please indicate whether entering as a team or individual and your name or team name and team members' names as appropriate

## Questions?

Any questions can be emailed to statisticsinsport@rss.org.uk or asked by creating a GitHub issue

## Suggested Resources

### Tennis Data

http://www.tennis-data.co.uk/data.php provides match results and betting odds across a wide variety of matches.

### Jeff Sackman's tennis data

A wide variety of match level and point by point data can be found on Jeff Sackmann's github https://github.com/JeffSackmann 

### World rankings

The WTA and ATP tour websites list the current world rankings, the ranking points attained to date and the competitions through which these have been accrued. 

https://www.wtatennis.com/rankings/singles

https://www.atptour.com/en/rankings/singles


