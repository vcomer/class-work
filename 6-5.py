str = 'X-DSPAM-Confidence: 0.8475'
expos = str.find(':')
portion = str[expos+2:]
function = float(portion)
print(function)