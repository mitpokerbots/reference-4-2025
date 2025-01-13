# PARAMETERS TO CONTROL THE BEHAVIOR OF THE GAME ENGINE
# DO NOT REMOVE OR RENAME THIS FILE
PLAYER_1_NAME = "A"
PLAYER_1_PATH = "./python_pot_odds"
# NO TRAILING SLASHES ARE ALLOWED IN PATHS
PLAYER_2_NAME = "B"
PLAYER_2_PATH = "./python_skeleton"  # Change this to './player_chatbot' to interact with your own bot!
# GAME PROGRESS IS RECORDED HERE
GAME_LOG_FILENAME = "gamelog"
# PLAYER_LOG_SIZE_LIMIT IS IN BYTES
PLAYER_LOG_SIZE_LIMIT = 524288
# STARTING_GAME_CLOCK AND TIMEOUTS ARE IN SECONDS
ENFORCE_GAME_CLOCK = True
STARTING_GAME_CLOCK = 60.0
BUILD_TIMEOUT = 10.0
CONNECT_TIMEOUT = 10.0
# THE GAME VARIANT FIXES THE PARAMETERS BELOW
# CHANGE ONLY FOR TRAINING OR EXPERIMENTATION
NUM_ROUNDS = 1000
STARTING_STACK = 400
BIG_BLIND = 2
SMALL_BLIND = 1

# Hyperparameters for Bounty Holdem
ROUNDS_PER_BOUNTY = 25  # unlikely to change
BOUNTY_RATIO = 1.5  # subject to change, ratio as a multiplier of pot
BOUNTY_CONSTANT = 10

PLAYER_TIMEOUT = 120
