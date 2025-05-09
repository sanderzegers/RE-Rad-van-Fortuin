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


# EXE File

RVF is written in Turbo Pascal 7.0. The binary executable is a 16-bit real mode dos file.
The Soundblaster CT-Driver is linked statically. 

I included the IDA database (RVF.idb). A lot of the function and variables are named. But this is still work in progress. 
You can open the file in IDA 5.0 Freeware.


# Sound Files

All the sound files ares stored in the creative voice format (https://en.wikipedia.org/wiki/Creative_Voice_file)
9 out of 38 voice files are stored in the EXE File, the other voices files are in the RVF.SND file.
To hide the existence of VOC files the author apparently decided to obfuscate the VOC header.
By definition every VOC file starts with 'Creative Voice File'. This has been modified to a random value.

The sounds are played by using the CT-Voice driver, which is statically linked in the exe file.

I've created an '010 Editor' script (RVF-VOC-Exctract.1sc) which is able to located the obfuscated VOC files.
The scripts fixes the VOC header and exports the files. The script works on both the .EXE and .SND file.
VLC Player is able to play VOC files natively.

See following list with all VOC files converted to WAV

| Filename | Text| Play WAV |
| :-- | :-- | :-- |
|exesound001.voc|Het is goed goed goed!| ![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/exesound001.wav)
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
|rvfsound024.voc|kort woord - moeilijk he mensen|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound024.wav)
|rvfsound025.voc|een ding|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound025.wav)
|rvfsound026.voc|eten en drinken|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound026.wav)
|rvfsound027.voc|een gebeurtenis|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound027.wav)
|rvfsound028.voc|een gezegde|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound028.wav)
|rvfsound029.voc|kretolgie|![play](https://github.com/sanderzegers/RE-Rad-van-Fortuin/raw/main/WAV/rvfsound029.wav)

# Config file

The config file only contains two settings, which are stored when launching a new game: The amount of players and each player name.
Settings from the settings menu are not stored and must be re-set after each application start.

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

The obfuscation method is quite simple. See this code example:
````
for (i=0;i<length_username;i++)
        result[i]=(username[i]-i)/2;
````

# Word database

The word database is just a simple list, in which every entry has a fixed length of 59 Chars.
Each entry starts with the word length and the actual word. This is the standard Pascal sting format. 
The words are obfuscated with the same method as used in the RVF.CFG file.
The category ID for each entry is stored at byte 58.

Category IDs:

| ID | Category|
| :-- | :-- |
|0x01|FLORA_FAUNA|
|0x02|ETEN_DRINKEN|
|0x03|GEBEURTENIS|
|0x04|DING|
|0x05|INSTELLING|
|0x06|PERSONEN|
|0x07|GEZEGDE|
|0x08|GEOGRAFIE|
|0x09|AKTIVITEIT|
|0x0a|BIOLOGIE|
|0x0b|TITEL|
|0x0c|BEROEP|
|0x0d|KRETOLOGIE|

You can use the 010-Editor Template (rvf.dta.bt) to view the DB entries, or check out the full extracted list here: ![wordlist.txt](https://github.com/sanderzegers/RE-Rad-van-Fortuin/blob/main/wordlist.txt)

Note that the letter frequencies in the word list closely match the standard Dutch letter frequency, so sticking to the common letters is a valid strategy for winning the game.

![Letter Frequency](https://raw.githubusercontent.com/sanderzegers/RE-Rad-van-Fortuin/refs/heads/main/letter_frequency.png)


# Wheel and Randomization

RVF uses the standard pascal 7.0 runtime library pseudo random number generator.
The initial seed is created from the local system time. The next seeds are generated by multipliying the previous seed by 0x8088405 and adding 1.
For every request to the Random function it will update the seed.

Every round the wheel will turn between 38 and 56 fields.

By reading the current seed, it's possible to predict all future wheel values.
This works best in speaker mode. In Soundblaster mode, if you guess a letter which is not in the solution, the random function will be ran an additional time.
This makes the prediction incorrect again.

# Additional sources

- DOS Game demonstration: https://www.youtube.com/watch?v=ue_EcGxPxv8
- Play Online: https://www.playdosgames.com/online/rad-van-fortuin/
- Original TV Show: https://www.youtube.com/watch?v=6REHeaD1kLk


# Todo

- [ ] Highscore format (RVA.SCR)
- [ ] Find and extract graphics
- [ ] Create sound effect player in Assembly for DOS
