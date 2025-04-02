import random
my_favourite_number =362
choice = ["Head","Tail"]
#adding to te list
choice.append("Body")
choice.extend(["Head","Tail","Body"])
print(choice[2 ])
print(choice)
#changing something in the list
choice[1] = "Lait"
print(choice)    
person_to_pay_the_bill = ["Eliud", "Kalia","Yena","Peace","Mutua", "Sunguti", "Mutua", "Naliaka"]
print(random.choice(person_to_pay_the_bill))
random_geusses = random.randint(0,7)
print(person_to_pay_the_bill[random_geusses])
#indexerror
# print(person_to_pay_the_bill[8])
# dirty_dozen = ["Strawberries","Spinach","Kale, collard & mustard greens","Grapes","Peaches","Pears","Nectarines","Apples"]
Fruits= ["Strawberries","Grapes","Peaches","Apples","Pears"]
Vegetables = ["Spinac", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [Fruits,Vegetables]
print(dirty_dozen)
# states_of_America = [States_of_america:
# {Delawear 7, 1787},
# { Pennsylvania	December 12, 1787,},
# {New Jersey	December 18, 1787},
# { Georgia	January 2, 1788},
# { Connecticut	January 9, 1788}
#  {Massachusetts	February 6, 1788}
# 7. {Maryland	April 28, 1788}
# 8. South Carolina	May 23, 1788
# 9. New Hampshire	June 21, 1788
# 10. Virginia	June 25, 1788
# 11. New York	July 26, 1788
# 12. North Carolina	November 21, 1789
# 13. Rhode Island	May 29, 1790
# 14. Vermont	March 4, 1791
# 15. Kentucky	June 1, 1792
# 16. Tennessee	June 1, 1796
# 17. Ohio	March 1, 1803
# 18. Louisiana	April 30, 1812
# 19. Indiana	December 11, 1816
# 20. Mississippi	December 10, 1817
# 21. Illinois	December 3, 1818
# 22. Alabama	December 14, 1819
# 23. Maine	March 15, 1820
# 24. Missouri	August 10, 1821
# 25. Arkansas	June 15, 1836
# 26. Michigan	January 26, 1837
# 27. Florida	March 3, 1845
# 28. Texas	December 29, 1845
# 29. Iowa	December 28, 1846
# 30. Wisconsin	May 29, 1848
# 31. California	September 9, 1850
# 32. Minnesota	May 11, 1858
# 33. Oregon	February 14, 1859
# 34. Kansas	January 29, 1861
# 35. West Virginia	June 20, 1863
# 36. Nevada	October 31, 1864
# 37. Nebraska	March 1, 1867
# 38. Colorado	August 1, 1876
# 39. North Dakota	November 2, 1889
# 40. South Dakota	November 2, 1889
# 41. Montana	November 8, 1889
# 42. Washington	November 11, 1889
# 43. Idaho	July 3, 1890
# 44. Wyoming	July 10, 1890
# 45. {Utah	January 4, 1896},
# 46. {Oklahoma	November 16, 1907}
# 47. {New Mexico	January 6, 1912}
# 48. {Arizona	February 14, 1912}
# 49. {Alaska	January 3, 1959}
# 50. {Hawaii	August 21, 1959}]

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""