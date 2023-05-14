

import FreeMobileConso


client = FreeMobileConso.Client(
                        "<identifiant>",
                        "<password>"
                        )


conso = client.consommation()

################################################################################

print("Acount name: " + conso.nameAcount)
print("Identifier: " + conso.identifier)
print("Number: " + conso.number)
print("Date: " + conso.date)
print("Total excluding package: " + conso.totalExcludingPackage)

################################################################################
print("\n\n\nLocal: ")

print("Internet consumption in my country: " + conso.local.internet.conso)
print("Internet plan mobile in my country: " + conso.local.internet.total)
print("Internet Remaining plan in my country: " + conso.local.internet.remaining)
print("Excluding package in my country (Internet): " + conso.local.internet.excludingPackage)
print("Carbon footprint in my country: " + conso.local.internet.carbonFootprint)
print("\n")
print("Call consumption in my country: " + conso.local.call.conso)
print("Call plan mobile in my country: " + conso.local.call.total)
print("Call plan in my country: " + conso.local.call.callToMyCountry)
print("Call plan International: " + conso.local.call.callToInternational)
print("Excluding package in my country (Call): " + conso.local.call.excludingPackage)
print("\n")
print("SMS consumption in my country: " + conso.local.sms.conso)
print("SMS plan mobile in my country: " + conso.local.sms.total)
print("Max nb os SMS in my plan in my country: " + conso.local.sms.maxNbSMS)
print("Nb of SMS in my country: " + conso.local.sms.nbSMS)
print("Excluding package in my country (SMS): " + conso.local.sms.excludingPackage)
print("\n")
print("MMS consumption in my country: " + conso.local.mms.conso)
print("MMS plan mobile in my country: " + conso.local.mms.total)
print("Max nb os MMS in my plan in my country: " + conso.local.mms.maxNbMMS)
print("Nb of MMS in my country: " + conso.local.mms.nbMMS)
print("Excluding package in my country (MMS): " + conso.local.mms.excludingPackage)

################################################################################
print("\n\n\nRoaming: ")

print("Internet consumption not in my country: " + conso.roaming.internet.conso)
print("Internet plan mobile not in my country: " + conso.roaming.internet.total)
print("Internet Remaining plan not in my country: " + conso.roaming.internet.remaining)
print("Excluding package not in my country (Internet): " + conso.roaming.internet.excludingPackage)
print("\n")
print("Call consumption not in my country: " + conso.roaming.call.conso)
print("Call plan mobile not in my country: " + conso.roaming.call.total)
print("Call plan in my not country: " + conso.roaming.call.callToMyCountry)
print("Call plan International: " + conso.roaming.call.callToInternational)
print("Excluding package not in my country (Call): " + conso.roaming.call.excludingPackage)
print("\n")
print("SMS consumption not in my country: " + conso.roaming.sms.conso)
print("SMS plan mobile not in my country: " + conso.roaming.sms.total)
print("Max nb os SMS not in my plan in my country: " + conso.roaming.sms.maxNbSMS)
print("Nb of SMS not in my country: " + conso.roaming.sms.nbSMS)
print("Excluding package not in my country (SMS): " + conso.roaming.sms.excludingPackage)
print("\n")
print("MMS consumption not in my country: " + conso.roaming.mms.conso)
print("MMS plan mobile not in my country: " + conso.roaming.mms.total)
print("Max nb os MMS not in my plan in my country: " + conso.roaming.mms.maxNbMMS)
print("Nb of MMS not in my country: " + conso.roaming.mms.nbMMS)
print("Excluding package not in my country (MMS): " + conso.roaming.mms.excludingPackage)