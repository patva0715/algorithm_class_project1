# Project 1 - Algorith Implementation
- Patrick Valera - pvalera@csu.fullerton.edu 
- Jimmie Gilmer III - JGilmer@csu.fullerton.edu

## Instructions to run the program
1. Write user inputs in the input.txt file.
2. Run Project1_starter.py. The script will read 10 sets of inputs from the input.txt file.
3. View the output of the algorithm in the output.txt file.

## Notes
- Input.txt file already contains 10 sets of inputs that can be edited for testing purposes.
- To avoid missing txt file error when running the script, run the following command from the root folder.
<pre>
python3 Project1_starter.py
or
python Project1_starter.py
</pre>

## Format for the input
- First line reads the number of members
- Second line read the minimum minutes required
- Rest of the reads will be the busy schedule and available time of each member
- [00:00] is used to indicate that a member doesnt have a busy schedule
## Example
<pre>
2                                  # 2 members
30                                 # 30 minutes minimum
[07:00,08:30],[12:00,13:00]        # Member 1's busy scheule
[08:00,12:00]                      # Member 1's login-logout interval
[07:00,08:30],[12:00,13:00]        # Member 2's busy scheule
[13:00,20:00]                      # Member 2's login-logout interval
</pre>
<pre>
2                                  # 2 members
30                                 # 30 minutes minimum
[00:00]                            # Member 1 Empty busy schedule
[08:00,12:00]                      # Member 1's login-logout interval
[00:00]                            # Member 2 Empty busy schedule
[13:00,20:00]                      # Member 2's login-logout interval
</pre>


