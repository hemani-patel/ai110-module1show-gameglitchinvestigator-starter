# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first opened the streamlit demo the game looked like a number guessing game with multiple difficulty levels. The first time I ran it, the game was on Normal difficulty and i saw on the edge the range was from 1-100 and I had 8 attempts. When i guessed a number I could only use the submit guess button not enter to submit my answer. When I submitted my answer if it was not the correct number then I would get a hint popup to help me get to the right number but it seemed to be flawed. I also noticed a developer debug info dropdown menue with lots of information that would help me but if i was trying to play the game fairly it would be counterintuitive to see the answer. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  One bug I notices was that the hint popups that I saw were backwards (target number is 86 when i type 99 it says go Higher (should say go lower), vice versa for lower number guessed). Another bug i encountered was the new game button dosen't work, i had to reload the page manually to play a new game. Also, it will say I am out of attempts at the bottom of the page but in reality at the top it will show I still have 1 attempt left so it ends the game 1 attempt early. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used claude and chatGPT on this project. One correct suggestion from the AI was to move the check_guess function from app.py into logic_utils.py and fix the high/low hint bug. The AI pointed out that when a guess was higher than the secret number, the game incorrectly told the player to go higher instead of lower, and vice versa. I implemented this change and checked it by playing the game and making guesses above and below the secret number. One incorrect suggestion from the AI was that the attempt counter bug was only caused by setting attempts to 1 instead of 0. While changing the initialization helped, it didnt  fix the issue fully. I tested the game and noticed that empty guesses were still decrementing the number of attempts. After more debugging, I realized the problem was that the code incremented the attempts before checking if the input was valid. I fixed this by moving the increment so it only happens after a valid guess with the help of chatGPT, and then played the game to confirm this change was correct.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that the bug was really fixed when I played the agme and the code matched what I believed the code was supposedt to logically do. I did not trust the AI suggestion automatically or asssume the bug would be gone after the agent changed the code. One test I ran manually was for the high/low I made sure the code logically followed if the guess < target then we need to say go higher and if the guess > target then we need to say go lower and I tested higher and lower numbers in the game when I played to make sure the output was correct. Yes after each fix I made the Agent create tests in pytest to make sure that the code was correct and I looked at the tests it wrote and made sure they made sense and then ran them. I asked the agent immidiately after it fixed the code to make the tests so that it knew exactly what to test for and made sure to ask for edge cases as well. 


## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

I did not notice when I first played the game that the number would change so I did not make any changes in the code so that the secret number stayed stable. However, after realizing that I went back and tried to find this error and come up with some ideas as to why this may have happened and what I could do to solve it. I believe that the secret number kept changing becuase Streamlit reruns the code from top to bottom any time we intereact with the page. if the secre number is created in the code without getting stored then it will change each rerun. To make sure that the secret doesnt change thorughout the game I would store it in st.session_state and only make sure to create it once if it didnt exist already. I used logic like if "secret" not in st.session_state: before assigning a random number made sure the secret stayed the same until the player started a new game.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future labs is testing fixes rught after making changes. In this project I learned that even small bugs (like off-by-one errors or swapped messages) can be caught quickly by writing a simple test or manually reproducing the bug in the game. Running pytest and checking the behavior in the Streamlit app helped me make sure that my fixes worked. One thing I would do differently next time when working with AI on a coding task is check the AI’s fizes more carefully before assuming they are correct. Some suggestions were helpful, but others only solved part of the problem. This project changed the way I think about AI-generated code because I realized that AI can be a helpful assistant for brainstorming fixes and writing tests, but it is not always correct and still needs human debugging and checks.
