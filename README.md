# GenFourSwitchInCalculator
This program calculates the order in which the Gen 4 AI will attempt to switch in, based on the Pokemon you used to faint its most recent one.

Please watch Drxx's video on this before using as it explains it much more detail than I am able to: 

https://www.youtube.com/watch?v=Szxw5sC06G4&t=2s

Essentially this code is based on the google doc in the description of the video, it assumes all of the AI's Pokemon have a Super-Effective hit on you and rank each of them in the order that the AI will pick.

This program also takes the glitch that places 2x quad effective mons in the between 1.5x Effective mons and 2x mons by rendering any 8x effective pokemon as 1.75x effective. AFAIK, it is impossible for any combo to also equal 1.75 so this should accurately represent the order in which all of these mons will be sent in.

I wrote this largely by screaming at ChatGPT until it learned what a quad effective type matchup was. Its refusal to understand what I actually meant by dual type matchups melted most of my brain cells and by then I had to take writing the code (of which I have little to no experience, other than GCSE Computer Science) into my own hands. As such it is not capable of doing the more complex task of identifying every exception to the rule or combining Phase 1 and Phase 2 of the switch-in.

However, given the much more complex nature of deciding switch-ins (compared with Gen 3 at least), it does most of the heavy lifitng in terms of not only calculating type matchups in the exact same (flawed) way that the Platinum AI does, but it also lets you name each of the inputted Pokemon so you can clearly see them in the list.

v0.2.0 Patch notes
- Switched to GUI-based interface
- Added drop-down bars to select types
- Added buttons to calculate and clear results

INSTRUCTIONS
1) Enter the type of your current Pokemon (If it is dual type you can either put the same type in each drop-down bar or select the blank option at the end of the type 2 drop down)
2) Enter a name for one of the AI's pokemon and then input the types
3) Hit calculate
4) Repeat step 2-3 until the entire party has been done
5) The Pokemon at the top of the list will be the next one switched in
6) Hit clear to reset at any time 

I'm super proud of what I've managed to cobble together in a second night's work, I'm a lone developer with very little experience coding but I've tested this out a couple of times indepently and it has been accurate so far! I'm looking forward to improving it so that it can calculate each phase of the switch-in process. Please contact with me any feedback through my GitHub!
