import pickle

player_data = {
'player-position' : 'N23 E45',
'pockets' : [ 'keys', 'pocket knife', 'polished stone' ],
'backpack' : [ 'rope', 'hammer', 'apple' ],
'money' : 158.50
}

save_file = open('player.dat', 'wb')
pickle.dump(player_data, save_file)
save_file.close()
