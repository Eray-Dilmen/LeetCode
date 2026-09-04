> 📌 **Guide:** This directory serves as a Concept Map for the **Bit Manipulation** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0136-Single Number`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Bit Manipulation Pattern?

* **Definition:** An algorithmic technique that operates directly on the binary representations of numbers (0s and 1s) using bitwise operators: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Left Shift (`<<`), and Right Shift (`>>`).
* **The Core Superpower:** Extreme speed and memory efficiency. Bitwise operations are executed directly by the CPU at the hardware level, making them faster than arithmetic operations. They allow you to compress boolean arrays or Hash Sets into a single integer (a Bitmask), reducing space complexity from `O(n)` to strict `O(1)`.

---

## Core Variations & Algorithmic Strategies

Bit manipulation relies heavily on a few mathematical properties of binary logic.

### 1. XOR Magic (Exclusive OR)
* **Algorithm:** The XOR operator (`^`) returns `1` if the bits are different, and `0` if they are the same. It has two crucial properties: `a ^ a = 0` (a number XORed with itself cancels out) and `a ^ 0 = a`. By XORing a sequence of numbers, all duplicate numbers will cancel each other out, leaving only the unique number.
* **When to use it:** Finding missing numbers, finding the single element in an array where every other element appears twice, or swapping variables without a temporary variable.
* **Repository Examples:**
  * [0136-Single Number](./0136-Single%20Number)
  * [0268-Missing Number](./0268-Missing%20Number)

### 2. Brian Kernighan's Algorithm
* **Algorithm:** The expression `n & (n - 1)` always flips the lowest set bit (the rightmost `1`) of `n` to `0`. If you put this in a `while n > 0:` loop and count how many times it runs before `n` becomes `0`, you efficiently count the number of `1`s in the binary representation.
* **When to use it:** Counting set bits (Hamming Weight) or checking if a number is a power of 2 (a power of 2 has exactly one `1` bit, so `n & (n - 1) == 0`).
* **Repository Examples:**
  * [0191-Number of 1 Bits](./0191-Number%20of%201%20Bits)
  * [0231-Power of Two](./0231-Power%20of%20Two)

### 3. Bitmasking (Sets as Integers)
* **Algorithm:** Instead of using a Hash Set or a boolean array of size 26 to track lowercase alphabet characters, use a single 32-bit integer. You can "add" a character to the set by setting its corresponding bit to 1: `mask |= (1 << char_index)`. You can check if it exists using AND: `(mask & (1 << char_index)) != 0`. 
* **When to use it:** When solving subset problems, state tracking in Dynamic Programming (Bitmask DP), or heavily optimizing space when dealing with small, fixed-size domains (like the alphabet).
* **Repository Examples:**
  * [0078-Subsets](./0078-Subsets) (Bitmask approach)
  * [3133-Minimum Array End](./3133-Minimum%20Array%20End)

### 4. Shifting (Fast Multiplication / Division)
* **Algorithm:** Left shifting a number by 1 (`x << 1`) multiplies it by 2. Right shifting by 1 (`x >> 1`) divides it by 2 (integer division). You can extract bits one by one by continuously right-shifting a number and checking `n & 1` (which tells you if the last bit is a 1 or 0).
* **When to use it:** Reversing bits, calculating quotients without the division operator, or parsing binary strings.
* **Repository Examples:**
  * [0190-Reverse Bits](./0190-Reverse%20Bits)
  * [0338-Counting Bits](./0338-Counting%20Bits)

---

## 💡 Professional Details & Edge Cases

* **Operator Precedence:** Bitwise operators have very low precedence in almost all programming languages (lower than `==` or `!=`). Always wrap your bitwise operations in parentheses. Writing `if mask & 1 == 0:` evaluates as `mask & (1 == 0)`, which is `mask & 0`, breaking your logic. Always write `if (mask & 1) == 0:`.
* **Python's Infinite Integers:** Unlike Java or C++ where integers are strictly 32-bit (and overflow or flip signs), Python integers have arbitrary precision and do not automatically overflow. When doing problems that rely on 32-bit signed integer behavior (like reversing bits or dealing with negative binary numbers), you must manually mask the result with `0xFFFFFFFF` to simulate 32-bit bounds.
* **Readability Trade-off:** While bit manipulation is incredibly fast, it is notoriously hard to read. In a professional codebase, you should only use Bitmasking or XOR tricks if performance is a strict bottleneck. Otherwise, a standard Hash Set or boolean array is vastly preferred for maintainability.