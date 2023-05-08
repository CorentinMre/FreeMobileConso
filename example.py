

from FreeMobileConso import FreeMobileConso


client = FreeMobileConso(
                        "identifiant",
                        "password"
                        )


conso = client.getConso()


print(conso)