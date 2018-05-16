# Chess Visualization Project

This repo hosts the Final Project for the Data Visualization course from the Master's in Data Science at USF. Due to the large size of the pgn file, we neede to store it in [Google Drive](https://drive.google.com/file/d/1cbPOdqe6QRi8fLIDinbIybAc3C1pACiw/view). 

## Authors:
* Danai Avgerinou - [LinkedIn](https://www.linkedin.com/in/danai-avgerinou/)
* Jake Toffler - [LinkedIn](https://www.linkedin.com/in/jake-toffler/)

## GitHub Page:
https://dsavg.github.io/Chess_Visualization_Project/

## Motivation:
Our motivation for working with chess data stems from our mutual interest in the game of chess. Chess is one of the most strategic games, so we wanted to explore what kinds of insights we could extract from that data and maybe improve our skills from those findings. 

Elite chess players are not only highly skilled at recognizing patterns but also memorize openings and positions so during a match they can use previously played games as a reference point to help understand which moves may be more optimal in that situation. So, our goal is to build a tool that players of all levels can use to play out different games and scenarios to see how a given move effects their empirical odds of winning.

## Project Objectives:
The primary objective of this visualization is to create a tool that a chess player of any level can use to improve. This visualization can be used for two different functions:
- Users are able to click their way through a game move-by-move and at each move see how often certain moves were made in games identical up to that point and how the odds of winning change with each move. 
- Players can use this as a tool to study openings and their variations. 

## Data
Free Internet Chess Server [FICS](https://www.ficsgames.org/download.html) is one of the largest chess servers that provides data from online chess matches. The files are in portable game notation (PGN) format, and data since 1999 is available there.

## Data Processing
In our initial research, we found a useful library in Python called [chess](http://python-chess.readthedocs.io/en/latest/).  PGN files are highly structured, containing tags for each game describing things such as who the players are and which color they are playing, their Elo rankings, how many moves the game had, and the result, among others.  Following the tags are the moves of that game.  This format repeats for each game in the file.

The chess library helped us with parsing the PGN file and get information about the chess games, such us the move sequence and the chess board for each move. So, we buid [Chess_data_parser.py](https://github.com/dsavg/Chess_Visualization_Project/blob/master/Chess_data_parser.py) which takes as an input any file from FICS and turns it into a json file, which is the input for all our visualizations.

## References:
- https://ebemunk.com/chess-dataviz/
- https://github.com/jbkunst/d3-chessboard
- https://github.com/jgoodall/d3-colorlegend
