#write a program that requests the user to write a tweet
#tweet length criteria
    #20 characters

#if tweet length is greater than 20 then program prints
    #tweet exceeds allowed length of 20 characters
#if tweet length is <= 20 then the program prints
    #tweet posted

tweet_input=input("Write a tweet: ")
min_chr=2
max_chr=20

if len(tweet_input)>max_chr:#cover al number greater than max
   print("tweet exceeds %d chr" %max_chr)
elif len(tweet_input)>=min_chr and len(tweet_input)<=max_chr:#(min-max)
   print("tweet posted!")
else:#cover below min
   print("Tweet must include at least %d chr" %min_chr)









