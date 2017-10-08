podstawowy = {'υ': 'y', 'λ': 'l', 'ᾶ': 'a', 'έ': 'e', 'Α': 'a', 'ύ': 'y', 'σ': 's', 'ἠ': 'e', 'ἀ': 'a', 'Τ': 't',
 'ι': 'i', 'ῇ': 'e', 'ὄ': 'o', 'π': 'p', 'ᾔ': 'e', 'ξ': 'ks', 'ἐ': 'e', 'Γ': 'g', 'ὴ': 'e', 'ᾐ': 'e',
 'ᾷ': 'a', 'δ': 'd', 'ἶ': 'i', 'τ': 't', 'ω': 'o', 'ἂ': 'a', 'ῶ': 'o', 'ῴ': 'o', 'Ν': 'n', 'ἦ': 'e',
 'Ζ': 'dz', 'ή': 'e', 'Λ': 'l', 'Ἀ': 'a', 'ς': 's', 'ψ': 'ps', 'χ': ('h', 'ch', 'kh'), 'ᾳ': 'a', 'ῆ': 'e',
 'Μ': 'm', 'ῖ': 'i', 'ῳ': 'o', 'Ι': 'i', 'ὸ': 'o', 'ῷ': 'o', 'ῦ': 'u', 'ἤ': 'e', 'Χ': ('h', 'ch', 'kh'), 'κ': 'k',
 'γ': 'g', 'ί': 'i', 'ἔ': 'e', 'Φ': ('f', 'ph'), 'μ': 'm', 'ἰ': 'i', 'Ε': 'e', 'φ': ('f', 'ph'), 'ὶ': 'i', 'ἄ':
     'a', 'ε': 'e', 'α': 'a', 'ώ': 'o', 'ᾠ': 'o', 'Κ': 'k', 'Θ': 'th', 'ὤ': 'o', 'ὐ': 'y', 'η': 'e', 'ὀ': 'o', 'ἱ': 'i',
 'ά': 'a', 'ῃ': 'e', 'ρ': 'r', 'ο': 'o', 'ὺ': 'y', 'ὼ': 'o', 'β': 'b', 'θ': 'th', 'ᾤ': 'o', 'ὲ': 'e',
 'ό': 'o', 'Σ': 's', 'ζ': 'dz', 'ὰ': 'a', 'ῥ': ('r', 'rh'), 'ὡ': 'o', 'ν': 'n'}

przydechy = {'ἑ': 'he', 'ὃ': 'ho', 'ἡ': 'he', 'ὁ': 'ho', 'ὕ': 'hy', 'ἅ': 'ha', 'ἕ': 'he', 'ἣ': 'he',
             'ὧ': 'ho', 'ὅ': 'ho', 'ὑ': 'he', 'ἥ': 'he', 'ᾗ': 'he', 'ἃ': 'ha', 'ὥ': 'ho', 'ὗ': 'hy',
             'ἵ': 'hi', 'ἧ': 'he', 'ἷ': 'hi'}

def dicmaker(file):
    #txt file should contain pairs of letters (words) in every line divided by comma
    # file is a name of a txt file which has to be in the same category and inserted as a str
    file = open(file, 'r')

    newdic = {}
    for line in file.readlines():
        if len(line) > 1:
            newdic[line.split()[0]] = line.split()[1]

    return newdic

dyftongi = dicmaker('dyft')
