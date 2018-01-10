def analyze_file(filename):
    try:
        infile = open(filename, "r")

        counts = 26 * [0] # create and initialize counts
        for line in infile:
            countLetters(line.lower(), counts)
        infile.close()

        # show histogram
        histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File","File " + filename + " does not exist")
# count each letter in the string
# note: counts is a list, we update this list in-place
# (making counts a dict is a more explicit solution)
def countLetters(line, counts):
     for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1