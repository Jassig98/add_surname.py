# Author: Jasmine Singh
# Github username: Jassig98
# Date: November 1, 2022
# Description: Program that takes list of first names and returns only the names that start with K and add surname Kardashian

def add_surname(first_names_list):
    full_list= [name+ 'Kardashian' for name in first_names_list if name [0] == 'K']
    return full_list

