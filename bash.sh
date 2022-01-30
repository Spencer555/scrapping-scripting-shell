#! /bin/bash

# this is  comment 

# echo Hello World!
# #echo is print 

# #variables is uppercase by convention 

# NAME="SPENCER LEWIS"

# # print variables
# echo ${NAME}


# #to accept input 

# read -p "Enter your Age" AGE 
# echo "you are ${AGE} years old"


# #conditionals 
# if [ "$NAME" == "SPENCER LEWIS" ]
# then 
#   echo "this is your name"
# elif [ "$NAME" == "df" ]
# then 
#   echo "you dont exist"

# else
#   echo "this is not your name"
# fi


#comparisms

# -eq means equal 
# -ne not equal 
# -gt greater than 
# -ge greater or equal to 
# -lt less than 
# -le less or equal to 


# #file conditions 
# FILE="test.txt"
# if [ -f "${FILE}" ]
# then 
#   echo "file exits"
# else 
#   echo "file does not exist"


# -d file   true if the file is a directory
# -d file   true if file exists 
# -f file   true if the provided string is a file 
# -g file   true if the group id is set on a file 
# -r file   true if file is readable 
# -s file   true if the file has a non zero size 
# -u  true if the user id is set on the file 
# -w true if the file is writeable 
# -x true if the file is an executable



# #case statement like switch in js
# read -p "Are you 21 or over? Y/N" ANSWER
# case "$ANSWER" in 
#    [yY] | [yY][eE][sS])
#    echo "You are an Adult"
#    ;;
#    [nN] | [nN][oO])
#    echo "You are not and adult"
#    ;;
#  *)
#  echo "this is like the default in js  please enter y/yes or n/no"
#  ;;
# esac

#to close case spell it backwards and | is or the []things in are the ans for lower or uppr case y or Y or yes Yes and for no 
#if the option entered is not valid the default runs



# #loops
# #for loops
# NAMES="brad keviin alice mark"

# for NAME in $NAMES 
#  do 
#    echo "hello $NAME"
# done



# # for loop to remanme files 
# FILES=$(ls *.txt) #list all files with extention .txt
# NEW="new"

# for FILE in $FILES
#  do 
#    echo "Renaming  $FILE to new-$FIlE"
#    mv $FILE $NEW-$FILE
# done



# #while llop to read through a file line by line 
# LINE=1 # start at line one

# while read -r CURRENT_LINE #the current line
#   do 
#    echo "$LINE: $CURRENT_LINE"
# done < "./new-1.txt"

#function
# function sayHello(){
#     echo "Hello World"
# }

# #running the function 
# sayHello

#function with parameters


# function greet(){
#     echo "Hello World $1 and $2"
# }

# #running the function 
# greet "Brad" "21"


# #create folder and write to a file
# mkdir hello
# touch "hello/world.txt"
# echo "Hello World" >> "hello/world.txt"
# echo "Created hello/world.txt"



# # a const 
# declare -r NUM1=5
# num2=5 

# #arith operations
# num3=$((NUM1+ num2))
# echo ${num3}


#set operation to variable 
# arith opeators 
# + ADD
# - SUBTRACT 
# * MULTIPLY
# / DIVIDE 
# % MODULUS 
# ** EXPONENT

# echo "5 + 4 $num4"

# U CAN USE THE I += 2 CAN USE THE SANE FOR OTHER OPERATORS

# let rs = 54 #a local variable

# ++ is incremental -- decremental

#using python in script 
# num8=2
# num10=2
# num9=(python -c "print $num8 + $num10")

# local variable 
# local name="popo"


# another if 
# if ((1 == 1)) then 
#    echo "another method"

# fi


# if (( ((1 == 1)) && ((1 == 1)) ));
#  then 
#    echo "another method"
# fi

# # || or 

# pat= "^[0-9]{8}$"

# #comparing to regex
# if [[ $date =~ $pat ]]; then
#  echo "$date is valid"


#  #to make item not display on screen 

#  read -sp "Enter the name"Name

# echo $Name

#to get values through index
# test="jkdfsjf fj dskfjds jdskfjsdkf dsffkflsdljf dslfjs dkf sfl"
# echo "${test:0:10}"
#get first  zero to ten characters
# can also use for array

#u can also use contine break in function

#untill loop
# until [1 == 1]; do 
#  echo "runs till the condition is true"

# done


#arrays 

fav_nums=(3.124 13.12 43.12 .43424)

echo "${fav_nums[0]}"
#get a specific index 


fav_nums[2] =2.343
#change value


fav_nums+=(3 5)
#add more numbers to array


unset '$fav_num[1]'
#delete item from array