# Periodic Table Information Finder
from pyscript import display, document


def elementchecker(e):
    document.getElementById('output').innerHTML = '' # No multiple outputs

    elementsymbol = document.getElementById('element_symbol').value # Assigning each value
    Hy = {
        'Symbol':'H',
        'Element':'Hydrogen',
        'Atomic Number': 1,
        'Atomic Mass': 1.008
    }
    Ca = {
        'Symbol':'C',
        'Element':'Carbon',
        'Atomic Number': 6,
        'Atomic Mass': 12.011
    }
    Ni = {
        'Symbol':'N',
        'Element':'Nitrogen',
        'Atomic Number': 7,
        'Atomic Mass': 14.007
    }
    Ox = {
        'Symbol':'O',
        'Element':'Oxygen',
        'Atomic Number': 8,
        'Atomic Mass': 16
    }
    Ph = {
        'Symbol':'P',
        'Element':'Phosphorus',
        'Atomic Number': 15,
        'Atomic Mass': 30.974
    }
    Su = {
        'Symbol':'S',
        'Element':'Sulfur',
        'Atomic Number':16,
        'Atomic Mass': 32.06
    }
    Se = {
        'Symbol':'Se',
        'Element':'Selenium',
        'Atomic Number': 34,
        'Atomic Mass': 78.971
    }
    Fl = {
        'Symbol':'F',
        'Element':'Flourine',
        'Atomic Number':9,
        'Atomic Mass': 18.998
    }
    Cl = {
        'Symbol':'Cl',
        'Element':'Chlorine',
        'Atomic Number': 17,
        'Atomic Mass': 35.45
    }
    Br = {
        'Symbol':'Br',
        'Element':'Bromine',
        'Atomic Number':35,
        'Atomic Mass':79.904
    }
    Io = {
        'Symbol':'I',
        'Element':'Iodine',
        'Atomic Number':53,
        'Atomic Mass': 126.904
    }
    As = {
        'Symbol':'At',
        'Element':'Astatine',
        'Atomic Number':85,
        'Atomic Mass': 210
    }
    Te = {
        'Symbol':'Ts',
        'Element':'Tennessine',
        'Atomic Number':117,
        'Atomic Mass': 294
    }
    He = {
        'Symbol':'He',
        'Element':'Helium',
        'Atomic Number':2,
        'Atomic Mass': 4.003
    }
    Ne = {
        'Symbol':'Ne',
        'Element':'Neon',
        'Atomic Number':10,
        'Atomic Mass': 20.18
    }
    Ar = {
        'Symbol':'Ar',
        'Element':'Argon',
        'Atomic Number':18,
        'Atomic Mass': 39.95
    }
    Kr = {
        'Symbol':'Kr',
        'Element':'Krypton',
        'Atomic Number':36,
        'Atomic Mass': 83.8
    }
    Xe = {
        'Symbol':'Xe',
        'Element':'Xenon',
        'Atomic Number':54,
        'Atomic Mass': 131.29
    }
    Rn = {
        'Symbol':'Rn',
        'Element':'Radon',
        'Atomic Number':86,
        'Atomic Mass': 222
    }

    elements = { # Connects the Elements to its respective names
        'H': Hy,
        'C': Ca,
        'N': Ni,
        'O': Ox,
        'P': Ph,
        'S': Su,
        'Se': Se,
        'F': Fl,
        'Cl': Cl,
        'Br': Br,
        'I': Io,
        'At': As,
        'Ts': Te,
        'He': He,
        'Ne': Ne,
        'Ar': Ar,
        'Kr': Kr,
        'Xe': Xe,
        'Rn': Rn
    }

    element = elements.get(elementsymbol, {
        'Symbol': 'N/A',
        'Element': 'Element not found',
        'Atomic Number': 'N/A',
        'Atomic Mass': 'N/A'
    }) # Shows this if the element inputted is not in the list

    display(element, target='output')
