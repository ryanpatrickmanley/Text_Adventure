import random

# Function SHOW: howing numbered options in a list, given a list.
def show(options_list):
  list_counter = 1
  print("\n")
  for x in options_list:
    print("[" + str(list_counter) +  "] " + str(x) + "\n")
    list_counter += 1

# Function PROMPT: prompts user input, and returns that choice from list as string.
def prompt(option_list):
  error_list = ["Please enter a valid input.", "Please pick the number of the choice you would like to make.", "ANY choice will do, really. Pick one. By number, please."]
  insult_list = ["Seriously, what's your problem?", "Are you well?", "Knock it off.", "Okay, you're really starting to bother me.", "Don't you have anything better to do than test the developer's forethought?", "...", "Really?", "See, this is what's wrong with *your generation*"]
  insult_counter = 0
  # TESTIN' GIT.
  while True:
  # IF the input is valid, print it back out and return the choice text.  
    prompt_input = input("Make your choice: ") # Get input at least once.
    if prompt_input.isdigit():               # IF it's an int... 
      prompt_number = int(prompt_input) - 1    # Get that int!
      if prompt_number <= len(option_list):    # And IF that int <= number of options...
        prompt_chosen = option_list[prompt_number]   # Get option text.
        print("\n" + prompt_chosen + "\n")           # Print chosen option text.
        return prompt_chosen                         # RETURN chosen option text.

  # ELSE it's not an option, or not an integer. Throw error and repeat.
    if insult_counter < len(error_list): # IF there are more errors to print...
      print("\n" + error_list[insult_counter] + "\n") # Print errors.
    else:
      print("\n" + random.choice(insult_list) + "\n") # Then, print random insults
    insult_counter += 1                               # Tally one insult

# Function JOB
def job(job, variations_list):
  if job == 1:
    return variations_list[0]
  elif job == 2:
    return variations_list[1]    
  elif job == 3:
    return variations_list[2]