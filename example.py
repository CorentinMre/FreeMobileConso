

import FreeMobileConso


client = FreeMobileConso.Client(
                        "<identifiant>",
                        "<password>"
                        )


conso = client.getConso()


print(conso)