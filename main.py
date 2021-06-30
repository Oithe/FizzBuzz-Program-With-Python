class FizzBuzz_Solution:

    def __init__(self, starting_range, end_range):
        self.starting_range = starting_range
        self.end_range = end_range

    def fizzBuzz(self):
        for i in range(self.starting_range, self.end_range+1):
            if i == 0:
                continue
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
                continue
            if i % 3 == 0 and i % 5 != 0:
                print("Fizz")
                continue
            if i%3 != 0 and i%5 == 0:
                print("Buzz")
                continue
            else:
                print(i)

starting_range = input("Initial Number ")
end_range = input("End Number ")
p1 = FizzBuzz_Solution(int(starting_range), int(end_range))
p1.fizzBuzz()