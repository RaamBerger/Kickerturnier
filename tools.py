"""
Created on Thu May 15 17:15:00 2025

@author: Raam
"""
def list_players_games():
    """
    
    Returns
    -------
    Liste = [[str, int], ...]
    Eine Liste, die für jeden Player eine Liste mit dem Namen als ersten
    und dem Punktstand als zweiten eintrag besitzt.

    """
    print("Name, player. Falls fertig n")
    
    player = []
    while True:
        name = input()
        
        if name.lower() == "n":
            break
        
        player.append([name, int(0)])
    
    games = []
    for i in range(len(player)):
        player1 = player[i][0] 
        player2 = player[(i + 1) % len(player)][0]
        player3 = player[(i + 2) % len(player)][0]
        player4 = player[(i + 4) % len(player)][0]
        games.append(f"Spiel {i + 1}\n"
              f"Team 1: {player1}, {player2}\n"
              f"Team 1: {player3}, {player4}\n")

    return player, games

def single_points(player: list, games: list):
    """
    

    Parameters
    ----------
    player : list
        DESCRIPTION.
    games : list
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for i in range(len(player)):
        print("das nächste Spiel ist:\n"
              f"{games[i]}")
        
        punkte1 = int(input("Wie viele Tore hat Team 1 geschossen? "))
        punkte2 = int(input("Wie viele Tore hat Team 2 geschossen? "))
        
        
        player[i][1] += punkte1 - punkte2 
        player[(i + 1) % len(player)][1] += punkte1 - punkte2
        player[(i + 2) % len(player)][1] += punkte2 - punkte1
        player[(i + 4) % len(player)][1] += punkte2 - punkte1
        
    return player

def combined_points(player: list):
    """
    

    Parameters
    ----------
    player : list
        DESCRIPTION.

    Returns
    -------
    player : TYPE
        DESCRIPTION.

    """
    punkte = list(input("Gib die Punkte in folgender Form an:\n"
                   "Punte Team 1 - Punkte 2, von Spiel 1"
                   ", Punte Team 1 - Punkte 2, von Spiel 2\n"
                   "ohne ein Leerzeichen, Komma oder irgendwas zwischen den einzelnen Zahlen."
                   "\n"))
    
    for i in range(len(player)):
        player[i][1] += int(punkte[i])
        player[(i + 1) % len(player)][1] += int(punkte[i])
        player[(i + 2) % len(player)][1] += - int(punkte[i])
        player[(i + 4) % len(player)][1] += - int(punkte[i])
    
    return player
