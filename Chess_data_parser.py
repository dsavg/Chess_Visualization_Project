# importing the needed libraries
import chess.pgn
import chess
import json
import sys

pgn_file = sys.argv[1]


def dict_maker(chess_dict, game):
    """
    Inputs:
        chess_dict - A dictionary with or without games already entered
        move_list - A list of mvoes for a single chess game
    Output:
        chess_dict - A dictionary with the single game added
    """
    result = game[0]
    move_list = game[1]
    board_list = game[2]
    # Given the starting dictionary, get to the first move
    spot = chess_dict['openings']['children']
    for move in move_list:

        new_dict = {'board': board_list[move_list.index(move)], 'san': move, 'count': 1, 'children': [],
                    'white_points': result}  # Create a dictionary in case this path is new
        # If games have followed the path up to this move, check to see if this move has been played
        if len(spot) > 0:
            for i in range(len(spot)):
                if spot[i]['san'] == move:
                    spot[i]['count'] += 1  # If it has, add one to the count
                    spot[i]['white_points'] += result  # Update the number of points white has scored
                    spot = spot[i]['children']  # And update the current location
                    break
                elif i + 1 == len(spot):
                    spot.append(new_dict)  # If it has not, add the dictionary from above
                    spot = spot[-1]['children']  # And update the current location
        else:
            spot.append(new_dict)  # If no game has followed this path, add the dictionary from above
            spot = spot[0]['children']  # And update the current location
    return chess_dict


def game_selector(pgn_file, number_games, elo_rating=1000, depth=10):
    all_games = []
    for i in range(number_games):
        first_game = chess.pgn.read_game(pgn_file)  # reads the first 10 games, one at the time
        board = chess.Board()  # creates the chess board object
        # moves = first_game.main_line()  # main line is the game's information
        node = first_game

        if (int(first_game.headers["WhiteElo"]) > elo_rating) and \
                (int(first_game.headers["BlackElo"]) > elo_rating) and \
                (int(first_game.headers["PlyCount"]) > 10):
            # we want to make sure that the players are experts

            outcome = first_game.headers["Result"]
            if outcome[0:2] == "1-":
                result = 1
            elif outcome[0:2] == "0-":
                result = 0
            else:
                result = 0.5
            moves_list = []
            board_list = []
            j = 0
            while node.variations:  # now we are looping within the games

                if j > depth:  # we don't want the depth of the sunburst graph to be greater then a certain depth

                    break

                else:
                    next_node = node.variation(0)

                    # this is the next square each time and we need to save that as the 'san' each time
                    chess_move = node.board().san(next_node.move)
                    moves_list.append(chess_move)

                    # this puts to the board the next move of the player
                    board.push_san(node.board().san(next_node.move))
                    node = next_node

                    # if we are going to need it for later, it is the piece that moved each time
                    board.piece_at(next_node.move.to_square)
                    board_list.append(str(board.fen()))

                    if (board.is_game_over() == True) or (board.is_checkmate() == True):
                        # even though the depth is pretty small, we need to account for games that end before
                        break

                    j += 1
        game = [result, moves_list, board_list]
        all_games.append(game)

    return all_games


if __name__ == "__main__":
    chess_dict = {'openings': {'san': 'start', 'children': []}}
    pgn = open(pgn_file)
    chess_games = game_selector(pgn, number_games=2000)

    for chess_game in chess_games:
        dict_maker(chess_dict, chess_game)

    with open('./data.json', 'w') as outfile:
        json.dump(chess_dict, outfile)
