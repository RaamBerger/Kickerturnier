"""
Created on Thu May 15 17:26:55 2025

@author: Raam
"""
import tools as t

#generierung Listen, der Teilnehmer*innen und Spiele
player, games = t.list_players_games()

#ausgabe Teilnehmer*innen, aller Spiele
print("Die Teilnehmer*innen des Turniers sind:")
for i in  range(len(player)):
    print(player[i][0])

print("Dies sind alle Speile:")
for i in  range(len(player)):
    print(games[i])

#auswahl der Punkte
while True:
    antwort = input("Möchtest du die Punkte für jedes Spiel einzelnd angeben? (y/n)")
    if antwort.lower() == "y":
        player = t.single_points(player, games)
            
        break
    
    if antwort.lower() == "n":
        player = t.combined_points(player)
        
        break

player.sort(reverse = True, key=lambda x: x[1])

for i in range(len(player)):
    print(f"{i + 1}. {player[i][0]} ({player[i][1]})")
