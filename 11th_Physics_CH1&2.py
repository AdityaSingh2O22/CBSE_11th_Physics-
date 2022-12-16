# [I CREATED  PROGRAM IN PYTHON OF PHYSICS OF CHAPTER 1& 2]
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:30:20 2019
@author: ADITYA SINGH
"""
chapter=int(input("Enter Chapter 1 OR 2 for calculations:"))
#Program for calculating the physics calculation of chapter 1
if chapter==1:
   import math
   print("1.Electrostatic force of repulsion(Vaccum)")
   print("2.Electrostatic force of repulsion(Medium)")
   print("3.Superposition of Electric Forces || THIS OPTOIN ISN'T WORKING PROPERLY WE SHALL TRY TO FIX IT SOON,CHOOSE ANOTHER OPTION !!")
   print("4.Electric Field due to point Charges")
   print("5.Dipole Moment")
   print("6.Dipole Field at axial point")
   print("7.Dipole Field at Equatorial point")
   print("8.Torque")
   print("9.Electric Flux")
   print("10.Flux Density")
   print("11.Electric Field of a long straight wire with uniform charge density LEMDA")
   print("12.Electric Filed of infinite plane sheet of uniform surface charge density SIGMA")
   choose=int(input("Enter your choice:"))
   if choose==1:
      print("1.Electrostatic force of repulsion(Vaccum)")
      z=int(input("IF you have a single charge then(Press 1) or have two charges(Press 2)"))
      if z==1:
           q1=float(input("Enter the Charge:"))
           r1=float(input("Enter the distance or radius:"))
           e=(9*10**9)*q1/r1**2
           print("Electrostatic Force of Repulsion(Vaccum) due to single charge:",e)
      elif z==2:
          q1=float(input("Enter the 1st Charge:"))
          q2=float(input("Enter the 2nd Charge:"))
          r1=float(input("Enter the distance between the two charges:"))
          f1=(9*10**9)*q1*q2/r1**2
          print("Electrostatic force of repulsion in Vaccum:",f1)
      if z not in range(2):
         print("Please enter given number !!")    
   elif choose==2:
         print("Electrostatic force of repulsion(Medium)")
         z=int(input("IF you have a single charge then(Press 1) or have two charges(Press 2)"))
         if z==1:
            q1=float(input("Enter the Charge:"))
            r1=float(input("Enter the distance or radius:"))
            e=(9*10**9)*q1/r1**2
            print("Electrostatic Force of Repulsion(Vaccum) due to single charge:",e)
         elif z==2:
            q1=float(input("Enter the 1st Charge:"))
            q2=float(input("Enter the 2nd Charge:"))
            r=float(input("Enter the distance between the two charges:"))
            medium=float(input("Enter the Medium:"))
            f2=(9*10**9)*q1*q2/r**2*medium
            print("Electrostatic force of repulsion in Medium:",f2)
         if z not in range(2):
            print("Please enter given number !!")   
   elif choose==3:
         print("This option not working correctly,try another")
   elif choose==4:
       print("4.Electric Field due to point charges")
       z=int(input("IF you have a single charge then(Press 1) or have two charges(Press 2)"))
       if z==1:
           q1=float(input("Enter the Charge:"))
           r1=float(input("Enter the distance or radius:"))
           e=(9*10**9)*q1/r1**2
           print("Electric Field due to a single point charge:",e)
       elif z==2:
           Q=float(input("Enetr the 1st charge:"))
           q=float(input("Enter the 2n charge:"))
           r=float(input("Enter the distance between the charges:"))
           E=(9*10**9)*Q*q/r**2
           print("Electric Field due to two point charges:",E)
       elif z not in range(2):
          print("Please enter given number !!")   
   elif choose==5:
       print("Dipole Moment")
       q=float(input("Enter the charge:"))
       a=float(input("Enter the distance between thre charges:"))
       p=q*a
       print("Dipole Moment:",p)
   elif choose==6:
       print("Dipole Field at axial point")
       r=float(input("Enter the distance from the Center of the Dipole:"))
       a=float(input("Enter the distance between the two charges OR Length od the Dipole:"))
       y=input("Does you want to calculate the Dipole Moment(Press 1 for calculating|| Press 2 if you have Dipole Moment:")
       if y==1:
          q=float(input("Enter the charge:"))
          a=float(input("Enter the distance between the charges:"))
          p=q*a
          E=(9*10**9)*(2*p*r)/(r**2-a**2)**2
          print("Dipole Filed at axial point:",E)
       elif y==2:
          p=float(input("Enter the Dipole Moment:"))
          E=(9*10**9)*(2*p*r)/(r**2-a**2)**2
          print("Dipole Filed at axial point:",E)
       if y not in range(2):
          print("Please enter given number !!")   
   elif choose==7:
       print("Dipole Field at Equatorial point")
       r=float(input("Enter the distance form the center of the Dipole:"))
       a=float(input("Enter the Length of the Dipole:"))
       y=input("Does you want to calculate the Dipole Moment(Press 1 for calculating|| Press 2 if you have Dipole Moment):")
       if y==1:
          q=float(input("Enter the charge:"))
          a=float(input("Enter the distance between the charges:"))
          p=q*a
          E=(9*10**9)*(p/(r**2+a**2)**3/2)
       elif y==2:
          p=float(input("Enter the Dipole Moment:"))
          E=(9*10**9)*(p/(r**2+a**2)**3/2)
          print("Dipole Filed at Equatoroal point:",E)
       if y not in range(2):
          print("Please enter given number !!")   
   elif choose==8:
       print("Torque")
       y=input("Does you want to calculate the Dipole Moment(Press 1 for calculating|| Press 2 if you have Dipole Moment):")
       if y==1:
          q=float(input("Enter the charge:"))
          a=float(input("Enter the distance between the charges:"))
          p=q*a
       elif y==2:
          e=input("Does you want to calculate the Electric Field(Press 1 for calculating|| Press 2 if you have Dipole Moment & Electric Field):")
          if e==1:
              Q=float(input("Enetr the 1st charge:"))
              q=float(input("Enter the 2n charge:"))
              r=float(input("Enter the distance between the charges:"))
              E=(9*10**9)*Q*q/r**2
          elif e==2:
              p=float(input("Enter the Dipole Moment:"))
              E=float(input("Enter the Electric Field:"))
              angle=float(input("Enter the Angle:"))
              t=p*E*math.sin(angle)
              print("Torque:",t)
       if y not in range(2):
          print("Please enter given number !!")       
          if e not in range(2):
             print("Please enter given number !!")    
   elif choose==9:
       print("Electric Flux")
       y=input("Does you want to calculate the Electric Field(Press 1 for calculating|| Press 2 if you have Electric Field ):")
       z=int(input("IF you have a single charge then(Press 1) or have two charges(Press 2):"))
       if y==1:
           if z==1:
              q1=float(input("Enter the Charge:"))
              r1=float(input("Enter the distance or radius:"))
              e=(9*10**9)*q1/r1**2
              print("Electric Field due to single charge:",e)
           elif z==2:
              Q=float(input("Enetr the 1st charge:"))
              q=float(input("Enter the 2n charge:"))
              r=float(input("Enter the distance between the charges:"))
              E=(9*10**9)*Q*q/r**2
              angle=float(input("Enter the angle:"))
              S=float(input("Enter the Surface Area:"))
              flux=E*S*math.cos(angle)
              print("Electric Flux:",flux)
           elif z not in range(2):
             print("Please enter given number !!")   
       elif y==2:
           E=float(input("Enter the Electric Field:"))
           angle=float(input("Enter the angle:"))
           S=float(input("Enter the Surface Area:"))
           flux=E*S*math.cos(angle)
           print("Electric Flux:",flux)
       elif y not in range(2):
          print("Please enter given number !!")    
   elif choose==10:
       print("Flux Density")
       y=float(input("Does you want to calculate the Electric Flux(Press 1 for calculating|| Press 2 if you have Electric Flux:"))
       if y==1:
           E=float(input("Enter the Electric Field:"))
           angle=float(input("Enter the angle:"))
           S=float(input("Enter the Surface Area:"))
           flux=E*S*math.cos(angle)
           print("Electric Flux:",flux)
       elif y==2:
           flux=float(input("Enter the Electric Flux:"))
           S=float(input("Enter the Surface Area:"))
           fluxdensity=flux/S
           print("Flux Density:",fluxdensity)
       if y not in range(2):
          print("Please enter given number !!")    
   elif choose==11:
       print("Electric Field of a long straight wire with uniform charge density LEMDA")
       lcdensity=float(input("Enter the Linear Charge Density:"))
       r=float(input("Enter the length of the Wire:"))
       E=lcdensity/(2*3.14*8.82*10**-12*r)
       print("Electric Field of a long straight wire with uniform charge density LEMDA:",E)
   elif choose==12:
       print("Electric Filed of infinite plane sheet of uniform surface charge density SIGMA")
       scdensity=float(input("Enter the Surface Charge Density:"))
       E=scdensity/(2*8.82*10**-12)
       print("Electric Filed of infinite plane sheet of uniform surface charge density SIGMA:",E)
   elif choose not in range(12):
      print("Choose from given options !!")    
   print("Thanks for using our program for calculating your PHYSICS Chapter 1st problems")
   print("Developer:-  ADITYA SINGH")
elif chapter==2:    
# physics calculations of chapter 2
   print("                         [  ELECTROSTATIC POTENTIAL AND CAPACITANCE   ]         ")
   print("1.Potential Difference")
   print("2.Electric Potential due to point Charge")
   print("3.Electric Potential due to Dipole")
   print("4.Electric Field between two parallel conductors")
   print("5.Electric Potential Enery")
   print("6.Potential Energy of Electric Dipole in uniform electric field")
   print("7.Capacitance of Spherical conductor")
   print("8.Capacitance")
   print("9.Capacitance of Parallel plate capacitor")
   print("10.Potential Difference between two plates")
   print("11.Capacitance of Spherical capacitor")
   print("12.Capacitance of Cylinderical capacitor")
   print("13.Capacitors in Series")
   print("14.Capacitors in Parallel")
   print("15.Energy stored in Capacitor")
   print("16.Energy Stored per unit volume OR Energy Density of Electric Field of capacitor")
   print("17.Electric Field between capacitors plates")
   print("18.Capacitor filled with Dielectric of dielectric constan K")
   print("19.Capacitance with Conducting Slab of thickness T(NOT WORKING)")
   print("20.Capacitance of Spherical capacitor filled with Dielectric")
   print("21.Cylindrical capacitor filled with Dielectric")
   print("22.Effect of dielectric with battery disconnected from the capacitor")
   print("23.Effect if dielectric with battery connected across the capacitor")
   import math
   choose=int(input("Enter your choice:"))
   if choose==1:
       print("Potential Difference")
       work=float(input("Enter the Work Done:"))
       q=float(input("Enter the Charge:"))
       p=work/q
       print("Potential Difference:",p)
   elif choose==2:
       print("Electric Potential due to point Charge")
       q=float(input("Enter the Charge:"))
       r=float(input("Enter the distance:"))
       v=9*10**9*(q/r)
       print("Electric Potential due to point charge:",v)
   elif choose==3:
       print("Electric Potential due to Dipole")
       y=float(int("Press 1 for calculating the MOMENTUM or Press 2 if you have MOMENTUM:"))
       if y==1:
           q=float(input("Enter the Charge:"))
           a=float(input("Enter the length of the Dipole:"))
           p=q*a
           print("Momentum:",p)
           angle=float(input("Enter the Angle:"))
           r=float(input("Enter the Distance:"))
           v=9*10**9*(p*math.cos(angle)/r**2)
           print("Electric Potential due to Dipole:",v)
       elif y==2:
           p=float(input("Enter the Momentum:"))
           angle=float(input("Enter the Angle:"))
           r=float(input("Enter the Distance:"))
           v=9*10**9*(p*math.cos(angle)/r**2)
           print("Electric Potential due to Dipole:",v)
       elif y not in range(2):
           print("Please enter the given number !!")    
   elif choose==4:
       print("Electric Field between two parallel conductors")
       y=float(int("Press 1 for calculating the Electric Potential or Press 2 if you have Electric Potential:"))
       if y==1:
          p=float(input("Enter the Momentum:"))
          angle=float(input("Enter the Angle:"))
          r=float(input("Enter the Distance:"))
          v=9*10**9*(p*math.cos(angle)/r**2)
          print("Electric Potential:",v)
       elif y==2:
          v=float(input("Enter the Electric Potential:"))
          d=float(input("Enter the Distance:"))
          e=v/d
          print("Electric Field between two parallel conductors",e)
       elif y not in range(2):
           print("Please enter the given number !!")   
   elif choose==5:
       print("Electric Potential Energy")
       Q=float(input("Enter the 1st Charge:"))
       q=float(input("Enter the 2nd Charge:"))
       r=float(input("Enter the distance from 1st Charge -- 2nd Charge:"))
       u=9*10**9*(Q*q/r)
       print("Electric Potential Enery:",u)
   elif choose==6:
       print("Potential Energy of Electric Dipole in uniform electric field")    
       y=float(input("Press 1 for calculating the Electric Field or Press 2 if you have Electric Field:"))
       if y==1:
           charge=float(input("Press 1 if you have Single Charge or Press 2 if you have Double Charge:"))
           if charge==1:
               q=float(input("Enter the Single charge:"))
               r=float(input("Enter the distance:"))
               e=9*10**9*(q/r**2)
               print("Electric Field:",e)
               z=float(input("Press 1 for Calculating the MOMENTUM OR Press 2 if you have MOMENTUM:"))
               if z==1:
                   Q=float(input("Enter the Charge:"))
                   a=float(input("Enter the length of the Dipole:"))
                   p=Q*a
                   print("Momentum:",p)
                   angle1=float(input("Enter the Angle 1st:"))
                   angle2=float(input("Enter the Angle 2nd:"))
                   u=-p*e*(math.cos(angle2)-math.cos(angle1))
                   print("Potential Energy of Electric Dipole in uniform electric field:",u)
               elif z==2:
                   m=float(input("Enter the Momentum:"))
                   angle1=float(input("Enter the Angle 1st:"))
                   angle2=float(input("Enter the Angle 2nd:"))
                   u=-p*e*(math.cos(angle2)-math.cos(angle1))
                   print("Potential Energy of Electric Dipole in uniform electric field:",u)
               elif z not in range(2):
                  print("Please enter the given number !!")    
           elif charge==2:
              Q=float(input("Enter the 1st charge:"))
              q=float(input("Enter the 2nd charge:"))
              e=9*10**9*(Q*q/r**2)
              print("Electric Field:",e)
              z=float(input("Press 1 for Calculating the MOMENTUM OR Press 2 if you have MOMENTUM:"))
              if z==1:
                   Q=float(input("Enter the Charge:"))
                   a=float(input("Enter the length of the Dipole:"))
                   p=Q*a
                   print("Momentum:",p)
                   angle1=float(input("Enter the Angle 1st:"))
                   angle2=float(input("Enter the Angle 2nd:"))
                   u=-p*e*(math.cos(angle2)-math.cos(angle1))
                   print("Potential Energy of Electric Dipole in uniform electric field:",u)
              elif z==2:
                   m=float(input("Enter the Momentum:"))
                   angle1=float(input("Enter the Angle 1st:"))
                   angle2=float(input("Enter the Angle 2nd:"))
                   u=-p*e*(math.cos(angle2)-math.cos(angle1))
                   print("Potential Energy of Electric Dipole in uniform electric field:",u)
              elif z not in range(2):
                  print("Please enter the given number !!")
           elif charge not in range(2):
              print("Please enter the given number !!")
       elif y not in range(2):
           print("Please enter the given number !!")       
       elif y==2:
           E=float(input("Enter the Electric Field:"))
           y=float(input("Enter 1 for calculating MOMENTUM OR Enter 2 if you have MOMENTUM:"))        
           if y==1:
                Q=float(input("Enter the Charge:"))
                a=float(input("Enter the length of the Dipole:"))
                p=Q*a
                print("Momentum:",p)
                angle1=float(input("Enter the Angle 1st:"))
                angle2=float(input("Enter the Angle 2nd:"))
                u=-p*e*(math.cos(angle2)-math.cos(angle1))
                print("Potential Energy of Electric Dipole in uniform electric field:",u)
           elif y==2:
               m=float(input("Enter the Momentum:"))
               angle1=float(input("Enter the Angle 1st:"))
               angle2=float(input("Enter the Angle 2nd:"))
               u=-p*e*(math.cos(angle2)-math.cos(angle1))
               print("Potential Energy of Electric Dipole in uniform electric field:",u)
           elif y not in range(2):
              print("Please enter the given number !!")
       elif y not in range(2):
           print("Please enter the given number !!")    
   elif choose==7:
       print("Capacitance of Spherical conductor")
       r=float(input("Enter the Radius of the Sphere:"))
       c=4*3.14*8.82*10**-12*r
       print("Capacitance of Spherical conductor:",c)
   elif choose==8:
       print("Capacitance")
       q=float(input("Enter the Charge:"))
       y=float(input("Enter 1 for calculating Potential Difference OR Enter 2 if you have Potential Difference:"))    
       if y==1:
           work=float(input("Enter the Work Done:"))
           q=float(input("Enter the Charge:"))
           p=work/q
           print("Potential Difference:",p)
           c=q/p
           print("Capacitance:",c)
       elif y==2:
           v=float(input("Enter the Potential Difference:"))
           q=float(input("Enter the Charge:"))
           c=q/v      
           print("Capacitance:",c)
       elif y not in range(2):
          print("Please enter the given number !!")    
   elif choose==9:
       print("Capacitance of Parallel plate capacitor")
       a=float(input("Enter the Area:"))
       d=float(input("Enter the distnace between the plates of the capacitor:"))
       c=8.82*10**-12*a/d
       print("Capacitance of Parallel plate capacitor:",c)            
   elif choose==10:
       print("Potential Difference between two plates")
       Q=float(input("Enter the 1st Charge:"))
       q=float(input("Enter the 2nd Charge:"))
       y=float(input("Press 1 for calculating the Capacitance OR Press 2 if you have Capacitance:"))
       if y==1:
           work=float(input("Enter the Work Done:"))
           q=float(input("Enter the Charge:"))
           p=work/q
           print("Potential Difference:",p)
           c=q/p
           print("Capacitance:",c)
           v=q-Q/2*c
           print("Potential Difference between two plates:",v)
       elif y==2:
           c=float(input("Enter the Capacitance:"))
           v=q-Q/2*c
           print("Potential Difference between two plates:",v)
       elif y not in range(2):
           print("Please enter the given number !!")    
   elif choose==11:
       print("Capacitance of Spherical capacitor")
       a=float(input("Enter the Radius of the inner sphere:"))
       b=float(input("Enter the Radius of the Outer sphere:"))
       c=9*10**9*(a*b/b-a)
       print("Capacitance of Spherical capacitor:",c)
   elif choose==12:
       print("Capacitance of Cylinderical capacitor")
       L=float(input("Enter the Length of the Capacitor:"))
       a=float(input("Enter the Radius of the inner cylinder:"))            
       b=float(input("Enter the Radius of the Outer Co-axial cylinder:"))        
       c=L/2.303*(math.log10*b/a)        
       print("Capacitance of Cylinderical capacitor:",c)
   elif choose==13:
       print("Capacitors in Series")
       print("NOTE:-- ONLY 5 CAPACITORS ARE SUPPORTED AT ONCE")
       y=float(input("Enter total number of Capacitors in Series:"))
       if y==1:
           c1=float(input)("Enter a Capacitor:")
           C=1/c1
           print("Capacitors in Series:",1/C)
       elif y==2:
           c1=float(input("Enter the 1st Capacitance:"))
           c2=float(input("Enter the 2nd Capacitance:"))
           C=1/c1+1/c2
           print("Capacitors in Series:",1/C) 
       elif y==3:
           c1=float(input("Enter the 1st Capacitance:"))
           c2=float(input("Enter the 2nd Capacitance:"))
           c3=float(input("Enter the 3rd Capacitance:"))
           C=1/c1+1/c2+1/c3
           print("Capacitors in Series:",1/C)
       elif y==4:
           c1=float(input("Enter the 1st Capacitance:"))
           c2=float(input("Enter the 2nd Capacitance:"))
           c3=float(input("Enter the 3rd Capacitance:"))
           c4=float(input("Enter the 4th Capacitance:"))
           C=1/c1+1/c2+1/c3+1/c4
           print("Capacitors in Series:",1/C)
       elif y==5:
           c1=float(input("Enter the 1st Capacitance:"))
           c2=float(input("Enter the 2nd Capacitance:"))
           c3=float(input("Enter the 3rd Capacitance:"))
           c4=float(input("Enter the 4th Capacitance:"))
           c5=float(input("Enter the 5th Capacitance:"))
           C=1/c1+1/c2+1/c3+1/c4+1/c5
           print("Capacitors in Series:",1/C)
       elif y not in range(5):
           print("ONLY 5 CAPACITORS ARE SUPPORTED AT ONCE!!")
   elif choose==14:
       print("Capacitors in Parallel")
       print("NOTE:-- ONLY 5 CAPACITORS ARE SUPPORTED AT ONCE")
       print("IN CASE IF YOU HAVE LESS THEN 5 CAPACITORS THEN ENTER 0 IN REAMAINING CAPACITORS")
       c1=float(input("Enter the 1st Capacitance:"))
       c2=float(input("Enter the 2nd Capacitance:"))
       c3=float(input("Enter the 3rd Capacitance:"))
       c4=float(input("Enter the 4th Capacitance:"))
       c5=float(input("Enter the 5th Capacitance:"))
       C=c1+c2+c3+c4+c5
       print("capacitors in Parallel:",C)          
   elif choose==15:
       print("Energy stored in Capacitor")
       z=float(input("Press 1 for calculating the Capacitance OR Press 2 if you have Capacitance:"))
       if z==1:
          y=float(input("Enter 1 for calculating Potential Difference OR Enter 2 if you have Potential Difference:"))    
       if y==1:
           work=float(input("Enter the Work Done:"))
           q=float(input("Enter the Charge:"))
           p=work/q
           print("Potential Difference:",p)
           c=q/p
           print("Capacitance:",c)
           u=1/2*c*p**2
           print("Energy stored in Capacitor:",u)
       elif y==2:
           v=float(input("Enter the Potential Difference:"))
           q=float(input("Enter the Charge:"))
           c=q/v      
           print("Capacitance:",c) 
           u=1/2*c*v**2
           print("Energy stored in Capacitor:",u)
       if z and y not in range(2):
           print("Please enter the given number !!")
   elif choose==16:
       print("Energy Stored per unit volume OR Energy Density of Electric Field of capacitor")
       y=float(input("Press 1 for calculating the Electric Field OR Press 2 if you have Electric Field:"))
       if y==1:
           Q=float(input("Enter the 1st Charge:"))
           q=float(input("Enter the 2nd Charge:"))
           r=float(input("Enter the distance or Radius:"))
           E=9*10**9*(Q*q/r**2)
           print("Electric Field:",E)
           u=1/2*8.82*10**-12*E**2
           print("Energy Stored per unit volume OR Energy Density of Electric Field of capacitor:",u)
       elif y==2:
           E=float(input("Enter the Electric Field:"))
           u=1/2*8.82*10**-12*E**2
           print("Energy Stored per unit volume OR Energy Density of Electric Field of capacitor:",u)
       elif y not in range(2):
           print("Please enter the given number !!")    
   elif choose==17:
       print("Electric Field between capacitors plates")
       SIGMA=float(input("Enter the Surface Charge Density:"))
       E=SIGMA/8.82*10**-12
       print("Electric Field between capacitors plates:",E)
   elif choose==18:
       print("Capacitor filled with Dielectric of dielectric constan K")
       y=float(input("Press 1 if you have Capacitance of parallel plates OR if you don't have Capacitance of parallel plates Press 2:"))
       if y==1:
           k=float(input("Enter the Dielectric Constant 'K':"))
           c=float(input("Enter the Capacitance of the parallel plates:"))
           C=k*c
           print("Capacitor filled with Dielectric of dielectric constan K:",C)
       else:
           if y==2:
              a=float(input("Enter the Area between the two capacitors:"))
              k=float(input("Enter the Dielectric Constant 'K':"))
              d=float(input("Enter distance between the Capacitors:"))
              C=8.82*10**-12*k*a/d
              print("Capacitor filled with Dielectric of dielectric constan K:",C)
           elif y not in range(2):
              print("Please enter the given number !!")       
   elif choose==19:
       print("Capacitance with Conducting Slab of thickness T")
       a=float(input("Enter the Area between the two plates of the Capacitor:"))
       d=float(input("Enter the distance between the two plates of the Capacitors:"))
       k=float(input("Enter the Dielectric constant 'K':"))
       t=float(input("Enter the Thickness of the conducting slab:"))
       C=8.82*10**-12*a/(d-t(1-1/k))
       print("Capacitance with Conducting Slab of thickness T:",C)
   elif choose==20:
       print("Capacitance of Spherical capacitor filled with Dielectric")
       k=float(input("Enter the Dielectric constant 'K':"))
       a=float(input("Enter the Radius of the inner sphere:"))
       b=float(input("Enter the Radius of the Outer sphere:"))
       C=4*3.14*8.82*10**-12*k*(a*b/b-a)
       print("Capacitance of Spherical capacitor filled with Dielectric:",C)
   elif choose==21:
       print("Cylindrical capacitor filled with Dielectric")
       l=float(input("Enter the Length of the Capacitor:"))
       k=float(input("Enter the Dielectric constant 'K':"))    
       a=float(input("Enter the Radius of the inner sphere:"))
       b=float(input("Enter the Radius of the Outer sphere:"))
       C=2*3.14*8.82*10**-12*k*l*(2.303*math.log10*b/a)
       print("Cylindrical capacitor filled with Dielectric:",C)
   elif choose==22:
       print("Effect of dielectric with battery disconnected from the capacitor")
       print("1.V=v/K")
       print("2.E=e/K")
       print("3.C=Kc")
       print("4.U=u/K")
       select=float(input("Enter the given number form the above:"))
       if select==1:
           v=float(input("Enter the original Potential Difference:"))
           k=float(input("Enter the Dielectric constant 'K':"))
           V=v/k
           print("Effect of dielectric with battery disconnected from the capacitor:",V)
       elif select==2:
           e=float(input("Enter the ORiginal Electric Field:"))
           k=float(input("Enter the Dielectric constant:"))
           E=e/k
           print("Effect of dielectric with battery disconnected from the capacitor:",E)
       elif select==3:
           k=float(input("Enter the Dielectric constant:"))
           c=float(input("Enter the Original Capacitance:"))
           C=c*k
           print("Effect of dielectric with battery disconnected from the capacitor:",C)
       elif select==4:
           u=float(input("Enter the Original Electric Potential Energy:"))
           k=float(input("Enter the Dielectric constant:"))
           U=u/k
           print("Effect of dielectric with battery disconnected from the capacitor:",U)
       elif select not in range(4):
            print("Please enter the given number !!")
   elif choose==23:
       print("Effect if dielectric with battery connected across the capacitor")
       print("1.Q=kq")
       print("2.C=kc")
       print("3.U=ku")
       select=float(input("Enter the number given above:"))
       if select==1:
           k=float(input("Enter the Original Dielectric constant:"))
           q=float(input("ENter the Original Charge:"))
           Q=k*q
           print("Effect if dielectric with battery connected across the capacitor:",Q)
       elif select==2:
           k=float(input("Enter the Original Dielectric constant:"))
           c=float(input("Enter the Original Capacitance:"))
           C=c*k
           print("Effect if dielectric with battery connected across the capacitor:",C)
       elif select==3:
           k=float(input("Enter the Original Dielectric constant:"))
           u=float(input("Enter the Original Electric Potential Energy:"))
           U=k*u
           print("Effect if dielectric with battery connected across the capacitor:",U)
       elif select not in range(3):
           print("Please enter the given number !!")
   if choose not in range(23):
      print("Please choose given option !!")
   print("Developer :-- ADITYA SINGH")
   print("Thanks for using our Software for calculting your Physics problems of Chapter 2")        
elif chapter not in range(2):
    print("Please select Chapter 1 OR 2 !!")
