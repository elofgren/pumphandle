def NetDrop(url, filename):
    '''Simple function to check for existence of data file and download file
    from internet source if not otherwise present'''
    from requests import get
    import os
    fullname = os.path.join(os.getcwd(), filename)
    if os.path.isfile(fullname):
        existswarn = raw_input("File already exists. Overwrite (Y/N)? ")
        existswarn = existswarn.lower()

        while existswarn not in ['y', 'n']:
            print "Invalid input, please try again."
            existswarn = raw_input("File already exists. Overwrite (Y/N)? ")
            existswarn = existswarn.lower()

        if existswarn == "y":
            netfile = get(url, verify=False)
            f = open(fullname, 'w')
            f.write(netfile.content)
            f.close()

        elif existswarn == "n":
            print "Download canceled"

    else:
        netfile = get(url, verify=False)
        f = open(fullname, 'w')
        f.write(netfile.content)
        f.close()
    return()
