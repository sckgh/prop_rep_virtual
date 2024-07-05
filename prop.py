import random, math
def num_to_perc(num):
    return "{:.2%}".format(num)

def tally(members=151, ayes = random.random()):
    nays = 1 - ayes
    turnout = random.random()
    virt_ayes = random.random()
    virt_nays = 1 - virt_ayes
    def_pass = ayes > nays
    virt_pass = (ayes + virt_ayes*turnout) > (nays + virt_nays*turnout)
    print("--------\nResult\nAyes: {0}\nNays: {1}\nResults: {2}\n\nAdd Virts\nTurnout: {6}\nAyes: {3}\nNays: {4}\nVirtual Seats: {7}\nResults: {5}\n------\n".format(
        (num_to_perc(ayes),math.floor(ayes*members)),
        (num_to_perc(nays),math.floor(nays*members)),
        def_pass,
        (num_to_perc(virt_ayes),math.floor((ayes+turnout*virt_ayes)*members)),
        (num_to_perc(virt_nays),math.floor((nays+turnout*virt_nays)*members)),
        virt_pass,
        num_to_perc(turnout),
        math.floor((turnout*virt_ayes)*members)+math.floor((turnout*virt_nays)*members),
    ))
    return ayes, nays, turnout, virt_ayes, virt_nays, def_pass, virt_pass

def main():
    for i in range(50):
        tally(ayes=0.45)
        
if __name__ == "__main__":
    main()