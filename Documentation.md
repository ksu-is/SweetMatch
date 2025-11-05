## Sprint 1 Notes

When cloning the forked code to my computer, it took a while sense the original fork had a file named "project roadmap." I finally realized the reason my computer couldn't copy it was because of the punctuation. 

Running the code, I encountered some problems. There was a list of emotions, but only some of the emotions in the code actually worked. Emotions like "bored", "stressed", or "angry" would output that the code didn't have any recommendations for my mood. Emotions like "happy", "excited", and "romantic" worked though. 
The original Mood Movie code is mostly static since it outputs a full list of recommendations for the emotions that do work.
There is overlapping logic in the code: two separate data structures (emotion_to_genre + genre_to_movies vs. movies_by_mood) and two separate functions essentially do the same task, which can be confusing and limits flexibility.

For SweetMatch, I plan to implement a dynamic loop system for user interaction:
The user inputs their mood/emotion and flavor preference.
The program provides a random dessert recommendation.
If the user doesn’t like the recommendation, it will give up to two additional options.
After three suggestions, the program will ask if the user wants to try a different flavor.
If the user chooses a new flavor (same emotion), the program outputs a new set of dessert suggestions.
If the user does not want to try a new flavor, they can quit the program.
This approach will make the code interactive and user-friendly, unlike the static original code, while also eliminating duplicate logic and centralizing the recommendation process.
