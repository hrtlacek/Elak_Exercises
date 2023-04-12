bad = ["NO!", 'computer sys no', 'i cannot do that dave', 'i believe in you', 'sorry for these idiotic messages. Anyway. Not correct!']
good = ["yay, correct!", 'congrats!', 'Perfect!', 'Bravo! Correct!']

import numpy as np

def getMsg(success):
    if success:
        msg = np.random.choice(good)
    else:
        msg = np.random.choice(bad)
    print(msg)
        