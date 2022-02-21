
import pyinputplus as pp
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    r = pp.inputYesNo(prompt)
    if r == 'no':
        break
print('Thank you. Have a nice day.')
