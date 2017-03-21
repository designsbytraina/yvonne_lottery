import random

#########################
# Main

def main():
  print """
888        888   888                           
888        888   888                           
888        888   888                           
888 .d88b. 888888888888 .d88b. 888d888888  888 
888d88""88b888   888   d8P  Y8b888P"  888  888 
888888  888888   888   88888888888    888  888 
888Y88..88PY88b. Y88b. Y8b.    888    Y88b 888 
888 "Y88P"  "Y888 "Y888 "Y8888 888     "Y88888 
                                           888 
                                      Y8b d88P 
                                       "Y88P"
  """
  print "Time to Play the lotto"

  #Initialise an empty list that will be used to store the 6 lucky numbers!
  user_nums = []

  # Initialised counting variable
  num_remaining = 6

  while len(user_nums) < 6:
    num = raw_input("Choose your numbers (" + str(num_remaining) + " remaining): ")
    user_nums.append(num)
    # Decrimenting counter
    # num_remaining = num_remaining - 1
    num_remaining -= 1

    # Concatenating items in the list to a string, separated by commas
    print ", ".join(user_nums)

  # Empty list to hold pretty numbers as strings
  printable_user_nums = []
  for item in user_nums:
    printable_user_nums.append(str(item))
  printable_user_nums = ", ".join(printable_user_nums)

  printable_user_nums = ", ".join(user_nums)
  print "Your six lottery numbers are\n > " + printable_user_nums + " <"

  # Call to helper function => get_lotto_nums() => to get computer's lotto nums
  lotto_nums = get_lotto_nums()

  # Empty list to hold pretty numbers as strings
  printable_lotto_nums = []
  for item in lotto_nums:
    printable_lotto_nums.append(str(item))
  printable_lotto_nums = ", ".join(printable_lotto_nums)

  print "The winning lottery numbers are\n > " + printable_lotto_nums + " <"

  # Call to helper function => get_matches() => to get matching nums
  num_matches = get_matches(user_nums, lotto_nums)

  # Print some message to the user about their success
  # Comparing the number of matches we had to show specifica messages for success, failure, etc.
  if num_matches < 4 and num_matches > 1:
    message = "Better luck next time!"
  elif num_matches < 6 and num_matches >= 4:
    message = "You were so close! Keep trying and trust your gut."
  elif num_matches == 6:
    message = "Wow! You must be reading the machine's mind!"
  else:
    message = "You were not even close!"

  print "You have made %d matching lottery numbers."%(num_matches)
  print message

#########################
# Helper Functions

def get_lotto_nums():
  """Helper function to get computer generated lotteru numbers."""

  lotto_num_list = []

  for i in range (0,6):
    number = random.randint(1,51)

    #Check if this number has already been picked and ...
    while number in lotto_num_list:
      # ... if it has, pick a new number instead 
      number = random.randint(1,51)
    
    #Now that we have a unique number, let's append it to our list.
    lotto_num_list.append(number)

  #Return the list
  return lotto_num_list

def get_matches(user_nums, computer_nums):
  """Helper function to get number of matching numbers between both lists"""
    
  # Remove duplicates from lists
  set1 = set(user_nums)
  set2 = set(computer_nums)

  # Match contains all items comon to raw_input and lotto_num
  set3 = set1.intersection(set2)

  # Return number of matching items
  return len(set3)

#########################
# Needed to make program run

if __name__ == '__main__':
  # Calling main() when the program runs
  main()
  # pass

