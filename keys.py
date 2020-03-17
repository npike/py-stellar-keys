#!/usr/bin/env python -x -u

import sys
from mnemonic import Mnemonic

from stellar_sdk import Keypair
from stellar_sdk import Account

def main():
    phrase = sys.argv[1]
    print("Words: " + sys.argv[1])
    
    seed = Mnemonic.to_seed(phrase)[:32]

    keypair = Keypair.from_raw_ed25519_seed(seed)

    stellarPublicAddress = keypair.public_key
    stellarPrivateSecret = keypair.secret

    print("public: " + stellarPublicAddress)
    print("private: " + stellarPrivateSecret)

if __name__ == "__main__":
    main()