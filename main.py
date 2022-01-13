from validation import Documentation
import stdnum
from stdnum import iban
#iban = IE69aibK93104787324084


iban_eg = "IE69aibK93104787324084"

ppsn_eg = "1021305ja"

doc = Documentation.verify_docs(iban_eg)

print(doc)

#form = iban.is_valid(iban_eg,check_country=True)
#print(form)