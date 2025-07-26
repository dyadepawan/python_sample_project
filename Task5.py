def factorail(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * factorail(n-1)
    
sample_number= 5
result = factorail(sample_number)

print(f"The factorial of {sample_number} is :{result}")

