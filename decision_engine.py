from dataclasses import dataclass

DECK = {"Goblin Barrel":3,"Goblins":2,"Valkyrie":4,"Cannon":3,"Dart Goblin":3,"Goblin Gang":3,"Princess":3,"Wall Breakers":2}
AIR = {"Dart Goblin","Princess","Goblin Gang"}

def validate_action(action, state):
    card=action.get("card")
    if card is None: return action.get("type")=="wait"
    if card not in DECK or card not in state.get("hand",[]): return False
    if state.get("own_elixir",-1)<DECK[card]: return False
    if state.get("urgent_air_threat",False) and action.get("purpose")=="direct_air_defense" and card not in AIR: return False
    if state.get("observation_confidence",0)<0.65 and action.get("type")=="attack": return False
    return True

def rank_actions(candidates, state):
    valid=[a for a in candidates if validate_action(a,state)]
    return sorted(valid,key=lambda a: (100*a.get("prevents_lethal",0)+4*a.get("damage_prevented",0)+2*a.get("damage_dealt",0)+1.5*a.get("elixir_advantage",0)-3*a.get("risk",0)-2*a.get("uncertainty",0)),reverse=True)
