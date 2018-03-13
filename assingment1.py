#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 01:22:06 2018

@author:Sezin Gümüş 150113841
"""

import sys
def main():
 k = int(input("enter a k-mer number:")) #k-mer input
 n = int(input("enter a frequent:")) #number of occurance at least in given genome,frequent
 
 
 """
 In this part , validity of k-mer and frequent will be checked .
 If these inputs are not valid , user will need to re-enter these inputs until they become valid. 
 """ 
 if check_input_validity(k,n) is False:
     while (check_input_validity(k,n) is False):
         print("You entered invalid input , please enter new values")
         k = int(input("enter a k-mer number:"))
         n = int(input("enter a frequent:")) 
         
 
 s = input("Enter an input file:") #An input file or directory of an input file
 genome = open(s, 'r').read()  #our genome string we are going to process
 genome = genome.upper()  #if strings are lower case , we will make them upper case
 
 
 """
 #This method finds most occurance k-mers , 
 reverse compliments and
 number of occurance of reverse compliments in a given genome string.
 """
 
 most_occurance_kmer(genome,k,n) 
 
 
 
 
def most_occurance_kmer(s,k,n):
 
 substr_array = [] # it will keep the most occured k-mer in a given genome string 
 file = open("genome_result.txt","w") #The output of this funnction will be written in this file
 for i in range(0,len(s)-k): #It prevents substrings to go out of the genome string length
    substr= s[i:i+k] #substring to search
    c = s.count(substr)  #number of occurance of k-mers
    if c >= n: #if counter is equal and greather than entered frequence ,  # it will show the k-mers
        substr_array.append([substr,c])       
 substr_array = remove_duplicates(substr_array) #Removed duplicate elements
 
 print ("") 

 print ("%d-mers:" % (k))
 file.write("%d-mers: \r\n" % (k))
 
 for i in range (0,len(substr_array)):
     print (substr_array[i][0])  # desired k-mers are written
     file.write("%s \r\n" % (substr_array[i][0]))
   
 print ("----------------------------------------------------")
 file.write("----------------------------------------------------\r\n")
 
 for i in range (0,len(substr_array)):
     rs = reverse(substr_array[i][0])  #Reverse compliments of k-mers
     count = s.count(rs)  #number of reverse compliments
     print ("Reverse compliment: %s appearing %d times" % (rs,count))
     file.write("Reverse compliment: %s appearing %d times\r\n" % (rs,count))
     
 file.close()    
 #This method finds reverse compliment of the k-mer
def reverse (seq):
    seq = seq[::-1]
    compliment = ''
    for nucleotide in seq:
        if nucleotide == 'A':
            compliment += 'T'
        elif nucleotide == 'T':
            compliment += 'A'
        elif nucleotide == 'C':
            compliment += 'G'
        elif nucleotide == 'G':
            compliment += 'C'
    return compliment

 """
 In this method ,if k-mer less than 9 and greater than 0 , 
 and n is equal or greater than 2 returns true 
 
 """ 

def check_input_validity (k,n):
    if k <= 9 and k > 0 and n >= 2:
           return True
    else:
        return False
#This methods removes dublicates of thearray that holds most occuance k-mers
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        t = tuple(value)
        if t not in seen:
            output.append(value)
            seen.add(t)
    return output
          

  
if __name__== "__main__":
  main()
  