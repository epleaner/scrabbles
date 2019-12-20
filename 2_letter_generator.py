import string
d = {letter: [[],[]] for letter in string.ascii_lowercase}
all_2_letters = ['aa','ab','ad','ae','ag','ah','ai','al','am','an','ar','as','at','aw','ax','ay','ba','be','bi','bo','by','da','de','do','ed','ef','eh','el','em','en','er','es','et','ew','ex','fa','fe','gi','go','ha','he','hi','hm','ho','id','if','in','is','it','jo','ka','ki','la','li','lo','ma','me','mi','mm','mo','mu','my','na','ne','no','nu','od','oe','of','oh','oi','ok','om','on','op','or','os','ow','ox','oy','pa','pe','pi','po','qi','re','sh','si','so','ta','te','ti','to','uh','um','un','up','us','ut','we','wo','xi','xu','ya','ye','yo','za']
for word in all_2_letters:
    [first,last] = word
    d[first][1].append(last)
    d[last][0].append(first)

letters = d.keys()
letters.sort()
for letter in letters:
    print("{: >20} {:.>20} {:.>20}".format(string.join(d[letter][0], ''),letter, string.join(d[letter][1], '')))
