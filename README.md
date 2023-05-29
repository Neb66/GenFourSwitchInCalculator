# GenFourSwitchInCalculator
Program that calculates the ranking that the AI will use when switching in Pokemon against the user

This program calculates the order in which the Gen 4 AI will attempt to switch in, based on the Pokemon you used to faint its most recent one.

Please watch Drxx's video on this before using as it explains it much more detail than I am able to: 

https://www.youtube.com/watch?v=Szxw5sC06G4&t=2s

Essentially this code is based on the google doc in the description of the video, it assumes all of the AI's Pokemon have a Super-Effective hit on you and rank each of them in the order that the AI will pick.

This program also takes the glitch that places 2x quad effective mons in the between 1.5x Effective mons and 2x mons by rendering any 8x effective pokemon as 1.75x effective. AFAIK, it is impossible for any combo to also equal 1.75 so this should accurately represent the order in which all of these mons will be sent in.

I wrote this largely by screaming at ChatGPT until it learned what a quad effective type matchup was. Its refusal to understand what I actually meant by dual type matchups melted most of my brain cells and by then I had to take writing the code (of which I have little to no experience, other than GCSE Computer Science) into my own hands. As such it is not capable of doing the more complex task of identifying every exception to the rule or combining Phase 1 and Phase 2 of the switch-in.

However, given the much more complex nature of deciding switch-ins (compared with Gen 3 at least), it does most of the heavy lifitng in terms of not only calculating type matchups in the exact same (flawed) way that the Platinum AI does, but it also lets you name each of the inputted Pokemon so you can clearly see them in the list.

Instructions:
*IMPORTANT* ALWAYS CAPITALISE THE FIRST LETTER OF EACH TYPE YOU ENTER OR THE CODE WILL ASSUME THE TYPE IS WRONG (Correct example: Rock, Electric - Incorrect example: rock, electric)
1) Enter the typing of your current pokemon, (if it only has one type then enter this and hit enter again when asked for the second typing).
2) Enter the name of the one of the AI's Pokemon
3) Enter the types as above
4) The program will output the name of the pokemon along with its current rank and overall effectiveness (according to the AI)
5) Hit y to continue and repeat steps 2-4 until all Pokemon have been entered
6) Press n or any other key to quit the program, this will reset the ranking so you can use it again.

Be aware that this is version 0.1.0 and currently remains untested. Further updates will come soon.
