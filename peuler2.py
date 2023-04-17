fibo = [1, 2] #Let's initialize the fibo variable (first 2 values)
#Using list comprenssion, we add the i position of fibo with the i-1 position
#We append the result to fibo
[fibo.append(fibo[i] + fibo[i-1]) for i in range(1, 32) if fibo[i] + fibo[i-1] <= 4000000] #We do this in a 1 to n range()
euler = [euler + i for i in fibo if i%2 == 0] # We add all the even numbers in fibo
print(euler)
