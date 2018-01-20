import string, random, hashlib

#challengeString = 'thisIsAchallengeHAHAHAstring12345789'
#print('challenge string = %s'%challengeString)

def generateAttempt(challengeString, challengeSize=100):
    st = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(challengeSize))
    attempt = st + challengeString
    return attempt

def start(challengeString):
    gotit = False
    while gotit == False:
        attempt = generateAttempt(challengeString)
        hashed = hashlib.sha256(attempt.encode()).hexdigest()
        if hashed.startswith('0000'):
            print('answer = %s'%hashed)
            print('string used = %s'%attempt)
            gotit = True
    return attempt


