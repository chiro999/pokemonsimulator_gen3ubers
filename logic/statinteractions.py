'''
handling changes in
attack
defense
sp_attack
sp_defense
speed
accuracy

fainting
damage
status
remove_status
raise_stat
'''

def attack_stat(pokemon:Pokemon, weather:str, crit:bool=False) -> float:
    '''
    Returns modified attack stat.
    Uses weather and abilities to derive final value.
    '''
    modifier = dex.boosts[pokemon.boosts['atk']]
    if crit and modifier < 1:
        modifier = 1
    if pokemon.ability == 'hugepower' or pokemon.ability == 'purepower':
        modifier *= 2
    if pokemon.ability == 'hustle':
        modifier *= 1.5
    if pokemon.item == 'choiceband':
        modifier = 1.5
    if pokemon.species == 'pikachu' and pokemon.item == 'lightball':
        modifier = 2
    if pokemon.species in {'cubone', 'marowak'} and pokemon.item == 'thickclub':
        modifier = 2
