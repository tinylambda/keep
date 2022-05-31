import os


print("Loaded {} from {}".format(__name__, __file__[len(os.getcwd()) + 1 :]))
