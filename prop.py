import random, math

def tally(members=151):
    ayes = random.random()
    nays = 1 - ayes
    turnout = random.random()
    virt_ayes = random.random()
    virt_nays = 1 - virt_ayes
    def_pass = ayes > nays
    virt_pass = (ayes + virt_ayes*turnout) > (nays + virt_nays*turnout)
    print("Result\nAyes: {0}\nNays: {1}\nResults: {2}\n\nAdd Virts\nAyes: {3}\nNays: {4}\nResults: {5}".format(
        math.floor(ayes*members),
        math.floor(nays*members),
        def_pass,
        math.floor((ayes+turnout*virt_ayes)*members),
        math.floor((nays+turnout*virt_nays)*members),
        virt_pass,
    ))