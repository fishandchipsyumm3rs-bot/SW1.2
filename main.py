from pyscript import document, display

def search(event):
    countries = document.getElementById("countries")
    countries_value = str(countries.value)

    display(f'{countries.value}', target = 'country_data', append = False)
