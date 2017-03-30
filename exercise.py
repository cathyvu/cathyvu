def showErrorMessage(user, error, numberOfStars):
    print "*" * numberOfStars
    print user
    print error
    print "*" * numberOfStars
    print "Its {2} so {0} is a angry {1}".format(user, "cat", error)


showErrorMessage("Garfield", "Mondays", 4)
