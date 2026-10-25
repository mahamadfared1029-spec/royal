# Clash Royale Visual Agent Knowledge Pack v1.0

Verified deck: Goblin Barrel, Goblins (4 units), Valkyrie, Cannon, Dart Goblin, Goblin Gang, Princess, Wall Breakers. Average 2.875 elixir.

Contents:
- deck_verified.json: observed cards, cost, levels, broad targeting.
- counter_matrix.csv: 43 enemy threats and heuristic responses. Not deterministic guaranteed counters.
- matchup_playbooks.json: 5 matchup archetypes.
- strategy_rules.json: constraints, example scoring, play phases, positioning.
- agent_system_prompt.txt: system instructions for visual agent.
- decision_engine.py: starter legality gate and action ranking; not a complete screen controller.
- evaluation_template.csv: metrics for controlled testing.

INTEGRATION: map visual observations into {hand,own_elixir,urgent_air_threat,observation_confidence}. Use screen-to-tile calibration for deployment. Log outcomes. Validate all card mechanics against current official patch notes before asserting precise damage/interaction breakpoints.

LIMITATIONS: no live API dataset downloaded, no empirical match tests run, no guaranteed win rate, no verified evolution/hero-slot state, no pixel-coordinate calibration. Training and control interface require details of your existing agent.
