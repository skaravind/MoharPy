import string, random, hashlib

def generateAttempt(challengeString, challengeSize=100):
    st = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(challengeSize))
    attempt = st + challengeString
    return attempt

def start(challengeString):
    got_it = False
    while got_it == False:
        attempt = generateAttempt(challengeString)
        hashed = hashlib.sha256(attempt.encode()).hexdigest()
        if hashed.startswith('0000'):
            print('answer = %s'%hashed)
            print('string used = %s'%attempt)
            got_it = True
    return attempt