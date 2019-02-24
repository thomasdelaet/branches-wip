# Branches-WIP

Simple scripts that create visibility on how much work is in-progress based on open branches

Moving to a faster release cadance requires product owners to define features in smaller increments, otherwise yor faster release cadance is not effective.

By measuring how long branches have been open with work that is not integrated into the mainline branch, we can create good visibility on the above and do some naming and shaming ;-).

# Example usage.

```bash
#change into directory where repositories are checked out
cd repositories

./branch-status.sh | ./processing.py > branches.csv
```
Then load the CSV file in a spreadsheet, apply some formatting and coloring. Example [here](https://docs.google.com/spreadsheets/d/1CnlPvMi3wuVGSaMKqeIgIB1DmF4_BinAkKo3fwEbhLk/edit?usp=sharing)

# branch-status.sh

This script needs to be configured with two variables:
* What is the name of your mainline branch? (dev variable)
* What is the list of repositories to process? (REPOSITORIES variable). Currently we assume that all repositories are git and checked out in the directory from which the script is run.

For every branch that is not merged into the mainline, the script outputs:
* The data of the first commit in this branch that deviates from mainline. This is a good proxy for how old this branch is
* The author of the last commit in this branch that deviates from mainline. This is a good proxy to know who to hold accountable.

# processing.py

This script enriches the output from branch-status as follows:

* It converts the date to a format of "how many days is this open" 
* It uses the email of author and a statically configured dictionary (which you'll need to adapt) to map this branch to a team and a PO (or map to "Unknown")
* It sorts the list with branches open the longest at the top.

