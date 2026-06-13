"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining

def preparation_time_in_minutes(layers):
    """Calculate preparation time in minutes."""
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate total elapsed cooking time."""
    return preparation_time_in_minutes(layers) + elapsed_bake_time
