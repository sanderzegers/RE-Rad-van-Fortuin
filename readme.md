# Reverse Engineering: Rad van Fortuin

## What's this?

Rad van Fortuin is a 90's TV game show and freeware DOS Game from the Netherlands based on the wheel of fortune format.
My main goal was to extract the sound effects of this DOS Game, since I was not able to find the files online.
Along the process I also discovered some other interesting files and functionalities.
The Rad van Fortuin game was created by Eric Zijlstra (E-Z Productions).

# Tools used

- IDA 5.0 Freeware
- 010 Editor
- Dosbox with Debugger Support (https://www.vogons.org/viewtopic.php?t=7323)

# Game Files

| Filename | Contains | Description |
| :------- | :------- | -------: |
| RVF.EXE | Code, Graphics, some Sound effects | The main Game executable. Dos 16-Bit real mode. Contains also some parts of the sound effects and all graphics |
| RVF.DOC | Readme| General information about the game, like Authors, System requirement, Explanation how to play the game |
| RVF.DTA | Solution words | All the words used in the game. Slightly obfuscated |
| RVF.CFG | Player names | The amount of players and playernames when last game was started. No other configuration is stored |
| RVF.SCR | Highscores | Highscore |
| RVF.SND | Sound files | Additional sound files, headers obfuscated |


# Sound Files

All sound files ares stored in the Creative Voice format (https://de.wikipedia.org/wiki/VOC_(Audiocodec))
9 out of 38 audio files are stored in the EXE File. All other files are in the RVF.SND.
To hide the existence of VOC files the Author apparently decided to obfuscate the VOC header.
By definition every VOC file starts with 'Creative Voice File'. This has been modified to a random value.

I've created an '010 Editor' script (RVF-VOC-Exctract.1sc) which searches for parts of the VOC header which are not obfuscated.
It will then fix the header and exports the file. The script works both on the .EXE and .SND file.
VLC Player is able to play VOC files natively.

| Filename | Text| Play WAV |
| :-- | :-- | :-- |
|exesound001.voc|Het is goed goed goed!| ![test](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound001.wav)
|exesound002.voc|(draai rad), je komt op.. |![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound002.wav)
|exesound003.voc|Oh daar gaat de sirene, alle medeklinkers zijn op|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound003.wav)
|exesound004.voc|*buzzer*|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound004.wav)
|exesound005.voc|Goed - ja - ga maar verder|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound005.wav)
|exesound006.voc|Wat ga je doen?|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound006.wav)
|exesound007.voc|*pling*|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound007.wav)
|exesound008.voc|Nee - helaas niet|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound008.wav)
|exesound009.voc|Nee - het is aardig geprobeert, maar hij zit er niet in|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound009.wav)
|rvfsound001.voc|*buzzer* - is al gezegd|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound001.wav)
|rvfsound002.voc|Nee moet je draaien|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound002.wav)
|rvfsound003.voc|Nee je moet een medeklinker doen want je hebt al gedraait|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound003.wav)
|rvfsound004.voc|Je mag een klinker kopen ja|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound004.wav)
|rvfsound005.voc|We gaan luisteren, we gaan luisteren|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound005.wav)
|rvfsound006.voc|Je hebt geen geld genoeg om een klinker te kopen|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound006.wav)
|rvfsound007.voc|Bankroet!|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound007.wav)
|rvfsound008.voc|*Superronde Countdown*|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound008.wav)
|rvfsound009.voc|*bankroet buzzer*|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound009.wav)
|rvfsound010.voc|*fluitje* één verliesbeurt|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound010.wav)
|rvfsound011.voc|50 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound011.wav)
|rvfsound012.voc|150 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound012.wav)
|rvfsound013.voc|200 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound013.wav)
|rvfsound014.voc|300|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound014.wav)
|rvfsound015.voc|350 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound015.wav)
|rvfsound016.voc|400 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound016.wav)
|rvfsound017.voc|450|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound017.wav)
|rvfsound018.voc|550 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound018.wav)
|rvfsound019.voc|600 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound019.wav)
|rvfsound020.voc|700|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound020.wav)
|rvfsound021.voc|750 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound021.wav)
|rvfsound022.voc|800 gulden|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound022.wav)
|rvfsound023.voc|1000 gulden - mooi bedrag|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound023.wav)
|rvfsound024.voc|kort woord - moeilijk hè mensen|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound024.wav)
|rvfsound025.voc|een ding|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound025.wav)
|rvfsound026.voc|eten en drinken|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound026.wav)
|rvfsound027.voc|een gebeurtenis|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound027.wav)
|rvfsound028.voc|een gezegde|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound028.wav)
|rvfsound029.voc|kretolgie|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound029.wav)

# Config file

This config file only contains the amount of player and playernames which were used during the last game.
Settings from the settings menu are not stored and must be re-set after each application launch.

010-Editor template: rvf.cfg.bt 

File format:

Header:
````
short counter; //incremented after every change
short player_count; // amount of players 
````

Player entry:
````
byte length_username;
uchar username; //this value is slightly obfuscated
````

# Word database

The word Database is actually not using any Database format. It's just a simple list, where every entry has a fixed length of 59 Chars.
Each entry starts with the word length and the following word is obfuscated with the same method as used in the RVF.CFG file.
You can use the 010-Editor Template (rvf.dta.bt), or check out the full list here: wordlist.txt
I have not found out yet how the categories (een ding, eten en drinken, etc) are mapped to the word. This must be in the game code.

# Additional sources

- DOS Game demonstration: https://www.youtube.com/watch?v=ue_EcGxPxv8
- Play Online: https://www.playdosgames.com/online/rad-van-fortuin/
- Original TV Show: https://www.youtube.com/watch?v=6REHeaD1kLk


# Todo

- [ ] How does category to word mapping work?
- [ ] Find the randomization code which sets next wheel turn
- [ ] Highscore format (RVA.SCR)
- [ ] Find and extract graphics
- [ ] Create sound effect player in Assembly for DOS
