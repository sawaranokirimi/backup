#coding: utf-8
import numpy as np


def Q2_1(n1, n2):
    return np.cos(2.0*np.pi*n1/2)
def Q2_2(n1, n2):
    return np.cos(2.0*np.pi*n2/2)
def Q2_3(n1, n2):
    return np.cos(2*np.pi*(n1/2.0+n2/2.0))

def Q3_1(n1, n2):
    return np.cos(2*np.pi*(n1/3.0))
def Q3_2(n1, n2):
    return np.sin(2*np.pi*(n1/3.0))
def Q3_3(n1, n2):
    return np.cos(2*np.pi*(n2/3.0))
def Q3_4(n1, n2):
    return np.sin(2*np.pi*(n2/3.0))
def Q3_5(n1, n2):
    return np.cos(2*np.pi*(n1/3.0+n2/3.0))
def Q3_6(n1, n2):
    return np.sin(2*np.pi*(n1/3.0+n2/3.0))
def Q3_7(n1, n2):
    return np.cos(2*np.pi*(n1/3.0-n2/3.0))
def Q3_8(n1, n2):
    return np.sin(2*np.pi*(n1/3.0-n2/3.0))

def Q6_1(n1, n2):
    return np.cos(2*np.pi*(n1/6.0))
def Q6_2(n1, n2):
    return np.sin(2*np.pi*(n1/6.0))
def Q6_3(n1, n2):
    return np.cos(2*np.pi*(n2/6.0))
def Q6_4(n1, n2):
    return np.sin(2*np.pi*(n2/6.0))
def Q6_5(n1, n2):
    return np.cos(2*np.pi*(n1/6.0+n2/6.0))
def Q6_6(n1, n2):
    return np.sin(2*np.pi*(n1/6.0+n2/6.0))
def Q6_7(n1, n2):
    return np.cos(2*np.pi*(n1/6.0-n2/6.0))
def Q6_8(n1, n2):
    return np.sin(2*np.pi*(n1/6.0-n2/6.0))

def Q2and3_1(n1, n2):
    return np.cos(2*np.pi*(n1/2.0+n2/3.0))
def Q2and3_2(n1, n2):
    return np.sin(2*np.pi*(n1/2.0+n2/3.0))
def Q2and3_3(n1, n2):
    return np.cos(2*np.pi*(n1/3.0+n2/2.0))
def Q2and3_4(n1, n2):
    return np.cos(2*np.pi*(n1/3.0+n2/2.0))

def Q2and6_1(n1, n2):
    return np.cos(2*np.pi*(n1/2.0+n2/6.0))
def Q2and6_2(n1, n2):
    return np.sin(2*np.pi*(n1/2.0+n2/6.0))
def Q2and6_3(n1, n2):
    return np.cos(2*np.pi*(n1/6.0+n2/2.0))
def Q2and6_4(n1, n2):
    return np.cos(2*np.pi*(n1/6.0+n2/2.0))

def Q3and6_1(n1, n2):
    return np.cos(2*np.pi*(n1/3.0+n2/6.0))
def Q3and6_2(n1, n2):
    return np.sin(2*np.pi*(n1/3.0+n2/6.0))
def Q3and6_3(n1, n2):
    return np.cos(2*np.pi*(n1/6.0+n2/3.0))
def Q3and6_4(n1, n2):
    return np.sin(2*np.pi*(n1/6.0+n2/3.0))
def Q3and6_5(n1, n2):
    return np.cos(2*np.pi*(n1/6.0-n2/3.0))
def Q3and6_6(n1, n2):
    return np.sin(2*np.pi*(n1/6.0-n2/3.0))
def Q3and6_7(n1, n2):
    return np.cos(2*np.pi*(n1/3.0-n2/6.0))
def Q3and6_8(n1, n2):
    return np.sin(2*np.pi*(n1/3.0-n2/6.0))
