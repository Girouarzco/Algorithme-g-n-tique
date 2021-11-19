#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:47:09 2021

@author: mariusgirouard
"""
import math
import random
import time
def Lecture_fichier():
    
    donnees = {}
    with open ('temperature_sample.csv','r') as f:
        for ligne in f.readlines()[1:]:
            ligne = ligne.strip().split(';')
            donnees[float(ligne[0])] = float(ligne[1])
    return donnees


def  Fonction(i, a, b, c):
    f=0
    for n in range(0,c+1):
        f += (a**n)*math.cos((b**n)*math.pi*i)
    return f
class Individu:
    def __init__(self):
        self.a = random.random()
        self.b = random.randint(0,21)
        self.c = random.randint(0,21)
        self.error = self.Fitness()
        
    def Fitness(self):   #calcul l'erreur
        self.error = 0
        for m in donnees.keys() :
            f = Fonction(m,self.a,self.b,self.c)
            self.error += abs(f - donnees[m])
        return self.error
def population(taille):
    pop = []
    for i in range(taille):
        pop.append(Individu())
    return pop
def tripop(pop):
    population = sorted(pop,key = lambda Individu : Individu.error)
    return population
def select(population):
    selectedliste = tripop(population)
    listepop = []
    for i in range(int(len(population)/2)):
        listepop.append(selectedliste[i])
    for i in range(int(len(population)/10)):
        listepop.append(selectedliste[len(selectedliste)-i-1])
    return listepop

def erreurfaible(population):
    individu = population[0]
    for i in range(len(population)):
        if (population[i].error < individu.error):
            individu = population[i]
    return individu
            
def Operateurdecroisement(individu1,individu2):
    variable = random.randint(0,3)
    if(variable == 0):
        temp = individu1.a
        individu1.a = individu2.a
        individu2.a = temp
    if(variable == 1):
        temp = individu1.b
        individu1.b = individu2.b
        individu2.b = temp
    if(variable == 2):
        temp = individu1.c
        individu1.c = individu2.c
        individu2.c = temp

if __name__ == '__main__' :
    donnees = Lecture_fichier()
    print(donnees)
    taille = int(input("taille de population?"))
    t1 = time.time()
    population = population(taille)
    newpopulation = select(population)
    for i in range(0,len(newpopulation)-1, 2):
        Operateurdecroisement(newpopulation[i],newpopulation[i+1])
    print("erreur : ",erreurfaible(population).error)
    print("individu : ",erreurfaible(population).a,erreurfaible(population).b,erreurfaible(population).c)
    t2 = time.time()
    print("temps : ",t2-t1)
    
    
