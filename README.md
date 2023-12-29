# Skyjo study project

The goal of this project is to study the best strategy to win in the game named 'Skyjo', for that we are going to remake the game in python and build strategy to make them play together. You can participate to the project by helping us to find new strategy and run them on your own computer. <br/>
At this time the game is not finished and the way to write strategy is not set so the project is at his beginning. <br/>

## Installation

### Linux
You need python 3<br/>
If you don't have python installed &rarr;
```sudo apt-get install python3```<br/>
Clone the repo &rarr;
```git clone https://github.com/Alexander7474/skydjo-startegy-study.git```<br/>
And its done!!<br/>

### Windows
You need python interpreter(last version is better)<br/>
After that you can download the repo from github and use it<br/>
Done!!<br/>

## Strategy

### Human
Located in ```humanStrat.py```, State: finished.<br/>
The game is played by human and the program ask to the person who play what to do at each turn.<br/>
Natural algorithm:<br/>
```
if condition:   
   ask the player
```

### Only Low card
Located in ```...```, State: not created.<br/>
Always choose card under a certain value, no focus on column
```
if visible card in pile value is under x:
    if card in grid over visible card value:
        switch it
    else:
        switch visible card with invisible card in grid
else:
    take invisble card in pile
    if card value is under x:
        if card in grid is over card value:
            switch it
        else:
            switch visible card with invisible card in grid
    else:
        put it in visible pile
        return random card in grid
    
```