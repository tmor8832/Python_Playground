import random 

def conceal(word): #function to replace answer with asterixes
  length = len(word)
  concealed = '*' * length
  return concealed
 
def listToString(list):  #convert list to string
    string = ""    
    for ele in list:  
        string += ele     
    return string  
        
def check_guess(letter,lives_remaining,hidden): # function to check if the letter is in the answer
  j=0
  found = 0
  answer_list = list(answer) #create lists of strings
  hidden_list = list(hidden)

  while(j<len(answer_list)): # run for length of list
    if letter == answer_list[j]: #check if the guessed letter matches answer character
      hidden_list[j] = letter
      j+=1
      found = 1 
    else:
      j+=1
  if(found == 0): #if not found remove a life
    lives_remaining -= 1
  
  hidden = listToString(hidden_list) #convert back to string
  return (hidden,lives_remaining)

document_string = open('word_list.txt', 'r').read() #read in the text file
word_list = document_string.split() #split the string in to individual words
answer = random.choice(word_list) # randomly select a word and store as variable answer

hidden = conceal(answer) # call function to conceal answer
lives_remaining = 7 #set up with 7 lives
while(lives_remaining != 0): #run until out of lives
  user_txt = input('Please enter your next guess: ' + hidden + '\n') #get user input
  hidden, lives_remaining = check_guess(user_txt,lives_remaining,hidden) #call function
  if(hidden == answer): # when matching enter this loop
    print(answer+ '\ncongratulations you win')
    break #end
  if(lives_remaining == 0): # after 7 unsuccessful guesses
    print('you lose') 
