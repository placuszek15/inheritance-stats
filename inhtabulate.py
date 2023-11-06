import os
from collections import defaultdict, Counter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--folder",required=True,help="Folder containing inheritance replays, without path separators")
args = parser.parse_args()
folder = args.folder
global_state = defaultdict(Counter)
for file in os.listdir(f"{folder}"):
	with open(f"./{folder}/"+file,encoding="utf-8") as f:
		local_state = set()
		local_state_2 = set()
		for line in f.readlines():
			if "|switch|" in line:
				l = line.split("|")
				#print(f"player {l[2].split(': ')[0]} has pokemon {l[3].split(',')[0]} with nickname {l[2].split(': ')[1]}")
				local_state.add(
					(l[2].split(': ')[0],l[3].split(',')[0],l[2].split(': ')[1])
				)
			if "-start" in line and "[silent]" in line:
				for elem in local_state:
					player, species,nickname = elem
					_,typeofmes,player_shown,mind,silent = line.split("|")
					#print(player_shown,mind,silent)
					if nickname in player_shown and nickname in player_shown:
						local_state_2.add((species,mind))

		for body, mind in local_state_2:
			global_state[body].update([mind])
kv_pairs = sorted(list(global_state.items()),key=lambda x: x[1].total(),reverse=True) 

for key,ctr in kv_pairs:
	print("+-------------------------------------------+")
	print(f"| {key.ljust(23)}Total: {ctr.total():>2}   Usage: |")
	print("+-------------------------------------------+")
	for key,amount in iter(ctr.most_common()):
		print(f"| {key.ljust(34)}{100*amount/ctr.total():6.2f}% |")
	print("+-------------------------------------------+")