# LeetCode 249 - Group Shifted Strings

## Problem

Given an array of strings, group strings that belong to the same shifting sequence.

A string belongs to the same group if every character can be shifted by the same number of positions to obtain another string.

## Example

**Input:**

```text
["abc","bcd","acef","xyz","az","ba","a","z"]
```

**Output:**

```text
[["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]
```

## Approach

For each string, calculate the difference between every pair of consecutive characters.

The differences are taken modulo 26 so that shifts from `z` to `a` are handled correctly.

Strings with the same difference pattern belong to the same group.

## Algorithm

1. Create a dictionary to store groups.
2. For each string, calculate the difference between consecutive characters.
3. Use the difference pattern as the key.
4. Add the string to the corresponding group.
5. Return all groups.

## Complexity

* Time Complexity: **O(n × m)**, where `n` is the number of strings and `m` is the maximum string length.
* Space Complexity: **O(n × m)** for storing the groups.

## Language

Python

## LeetCode

Problem 249 - Group Shifted Strings

## Author

**T.Nandhini**
