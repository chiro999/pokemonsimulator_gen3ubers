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
  return pokemon.stats.attack * modifier

def defense_stat(pokemon:Pokemon, crit:bool, terrain:str) -> float:
    '''
    Returns modified defense stat.
    '''
    modifier = dex.boosts[pokemon.boosts['def']]
    if crit and modifier > 1:
        modifier = 1
    return pokemon.stats.defense * modifier


def spattack_stat(pokemon:Pokemon, crit:bool, weather:str) -> float:
    '''
    Returns modified special attack stat.
    '''
    modifier = dex.boosts[pokemon.boosts['spa']]
    if crit and modifier < 1:
        modifier = 1
    if pokemon.item == 'choicespecs':
        modifier = 1.5
    return pokemon.stats.specialattack * modifier
