import random
import textwrap

# Function SHOW: prepends an empty line and number [#], wraps, and prints each listed option.
def options(raw_option_list):
  
  list_counter = 1
  print("") # Skip line.
  for x in raw_option_list:
    numbered_option = ("(" + str(list_counter) +  ") " + str(x) + "\n") # Number.
    wrap(numbered_option) # Wrap & Print.
    list_counter += 1

# Function PROMPT: prompts user input, and returns that choice from list as string.
def prompt(option_list):
  error_list = ["Please enter a valid input.", "Please pick the number of the choice you would like to make.", "ANY choice will do, really. Pick one. By number, please."]
  insult_list = ["Seriously, what's your problem?", "Are you well?", "Knock it off.", "Okay, you're really starting to bother me.", "Don't you have anything better to do than test the developer's forethought?", "...", "Really?", "See, this is what's wrong with *your generation*"]
  insult_counter = 0
  
  while True:
  # IF the input is valid, print it back out and return the choice text.  
    prompt_input = input("\nMake your choice... ") # Get input at least once.
    if prompt_input.isdigit():                  # IF it's an int... 
      prompt_int = int(prompt_input)          # Store that int!
      if prompt_int <= len(option_list):              # AND IF that int <= number of options...
        prompt_chosen = option_list[prompt_int - 1]   # Get option text.
        print("\nYou chose:")
        wrap(prompt_chosen)               # Wrap and Print chosen option text.
        print("")
        return prompt_chosen                           # RETURN chosen option text.

  # ELSE it's not an option, or not an integer. Throw error and repeat.
    if insult_counter < len(error_list):              # IF there are more errors to print...
      print("")
      wrap(error_list[insult_counter])  # Print errors.
    else:
      print("\n")
      wrap(random.choice(insult_list))  # ELSE, print random insults.
    insult_counter += 1                               # Tally one insult.

# Function JOB
def job(job, variations_list):
  if job == 1:
    return variations_list[0]
  elif job == 2:
    return variations_list[1]    
  elif job == 3:
    return variations_list[2]

# Function WRAP
def wrap(text):
  print(textwrap.fill(text, width=42))