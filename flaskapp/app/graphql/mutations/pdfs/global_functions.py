

def isCNSvalid(cns:int) -> bool:
    """verify if the CNS is valid
    code by: philippeoz

    Args:
        cns (int): cns number that will be validated
    """
    cns = ''.join(filter(str.isdigit, str(cns)))
    
    if len(cns) != 15:
        return False
    
    return sum(
        [int(cns[i]) * (15 - i) for i in range(15)]
    ) % 11 == 0



if __name__ == "__main__":
    cns = 138490784180008
    cns = str(cns)
    cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]

    print(cns)