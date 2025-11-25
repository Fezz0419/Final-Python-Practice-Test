# Final-Python-Practice-Test
📌 Questions Overview & Requirements
## Question 1: get_date_of_birth(id_number: str)

    Extract the date of birth from a South African ID number.

### Formula / Structure of SA ID Number:
        YYMMDDSSSSCAZ

            YY → Year

            MM → Month

            DD → Day

### Required Output Format:
    DD/MM/YY

## Question 2: get_gender(id_number)

    Determine the gender from the ID number.

### Formula:
    Extract digits 7–10 (the sequence number):
    sequence = int(id_number[6:10])

### Rule:

        If sequence < 5000 → Female

        If sequence ≥ 5000 → Male

## Question 3: get_shape()

    Prompt the user to enter a shape name.

### Requirements:

    Input cannot be empty

    Must match a valid shape, such as: "circle", "square", "triangle", "rectangle", "pentagon"

    Return the validated shape

## Question 4: draw_triangle_multiplication(n: int)

    Draw a multiplication triangle up to n.

### Formula:
    For row i, the values are:
        i * 1, i * 2, i * 3, ... , i * i
        
### Example (n = 5):
        1
        2 4
        3 6 9
        4 8 12 16
        5 10 15 20 25

## Question 5: draw_pyramid(n: int)

    Draw a pyramid of stars with height n.

### Formula:
    For row i (starting from 1):

        Number of stars: 2*i - 1

        Number of leading spaces: n - i

### Example (n = 4):
   *
  ***
 *****
*******

## Question 6: fibonacci(n: int)

    Return the nth Fibonacci number using recursion.

### Fibonacci Formula:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)

## Question 7: fizz_buzz(n: int)

    Return different outputs depending on divisibility.

### Rules:

    If n % 3 == 0 → "Fizz"

    If n % 5 == 0 → "Buzz"

    If divisible by both:
        n % 3 == 0 and n % 5 == 0 → "FizzBuzz"
    
    Otherwise return n

## Question 8: is_prime(n: int)
    Determine if a number is prime.

### Prime Number Definition:
    A number is prime if:
        n > 1 AND it has no divisors other than 1 and n.

### Efficient Formula Check:
    Check divisibility from 2 to √n:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0 → Not prime

## Question 9: factorial(n: int)

Return the factorial of n using recursion.

### Factorial Formula:
    0! = 1
    n! = n × (n - 1)!  

### Example:
    5! = 5 × 4 × 3 × 2 × 1 = 120

## Question 10: prime_triangle(n: int)

Draw a triangle of prime numbers up to n rows.

### Formula / Logic:

    Generate primes in ascending order

    Row i contains i prime numbers

### Example (n = 5):
2
3 5
7 11 13
17 19 23 29
31 37 41 43 47

## Question 11: pascal_triangle(n: int)

Draw Pascal’s Triangle up to n rows.

### Pascal’s Triangle Formula:
Each element is a binomial coefficient:
    C(n, k) = n! / (k! (n - k)!)

Or recursively:
    pascal[i][0] = 1
    pascal[i][i] = 1
    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

### Example (n = 5):
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
