import subprocess

def metadata(player=''):
	try:
		music_player = subprocess.run('playerctl --player=%s status --format "{{ uc(status) }}"' % (player),shell=True,stdout=subprocess.PIPE, text=True).stdout
		if(music_player == ''):
			return 'No player start'

		track = subprocess.run('playerctl --player=%s metadata --format "{{ duration(position) }} ^ {{ title }} ^ {{ artist }} ^ {{status}}"' % (player),shell=True,stdout=subprocess.PIPE, text=True).stdout.split('^')
		
		if track[3].strip() != "Playing":
			if track[3].strip() == "Stopped":
				metadata = f'Track Stopped - 📻 {track[1].strip()+" -" if track[1].strip() else "Track unknow -"} {track[2].strip() if track[2].strip() else "Artist unknow"}'
			else:
				metadata = f'Track Paused - 📻 {track[1].strip()+" -" if track[1].strip() else "Track unknow -"} {track[2].strip() if track[2].strip() else "Artist unknow"}'
		else:
			metadata = f'📻 {track[1].strip()+" -" if track[1].strip() else "Track unknow -"} {track[2].strip() if track[2].strip() else "Artist unknow"}'
		return metadata

	except:
		return 'Not found player'